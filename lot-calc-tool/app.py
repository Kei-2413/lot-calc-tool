from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# symbolの辞書
dollar_straghts = {
    "USD": "USDJPY",
    "EUR": "EURJPY",
    "GBP": "GBPJPY",
    "AUD": "AUDJPY",
    "NZD": "NZDJPY"
}

# APIからレートを取得
def real_time_rate(base_currency, target_currency):
    url = f"https://open.er-api.com/v6/latest/{base_currency}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        rate = data["rates"].get(target_currency)
        if rate:
            return rate
        else:
            print(f"{base_currency}->{target_currency} レート取得失敗！")
            return None
    else:
        print(f"APIリクエスト失敗: {response.status_code}")
        return None

@app.route('/', methods=['GET', 'POST'])
def form():
    LOT = None
    product_type = ''
    payment_currency = ''
    amount = ''
    pips = ''
    spread = ''
    real_time_rate_value = ''

    if request.method == 'POST':
        product_type = request.form['product_type']
        payment_currency = request.form['payment_currency']
        amount = float(request.form['amount'])
        pips = float(request.form['pips'])
        spread = float(request.form['spread'])
        pips_per_jpy = 0.01
        pips_per_dollar = 0.0001

        if product_type == "FX" and payment_currency == "JPY":
            LOT = amount / ((pips + spread) * pips_per_jpy * 100000)
            real_time_rate_value = "N/A"

        elif product_type == "FX" and payment_currency in dollar_straghts:
            # 例: USDJPY → base=USD, target=JPY
            symbol = dollar_straghts[payment_currency]
            base_currency = symbol[:3]
            target_currency = symbol[3:]
            rate = real_time_rate(base_currency, target_currency)
            real_time_rate_value = rate

            if rate:
                LOT = amount / ((pips + spread) * pips_per_dollar * rate * 100000)

        if product_type == "BTC" and payment_currency == "JPY":
            LOT = amount / (pips + spread)
            real_time_rate_value = "N/A"

        elif product_type == "BTC" and payment_currency == "USD":
            rate = real_time_rate("USD", "JPY")
            real_time_rate_value = rate
            if rate:
                LOT = amount / ((pips + spread) * 0.01 * rate)

        if product_type == "GOLD" and payment_currency == "USD":
            rate = real_time_rate("USD", "JPY")
            real_time_rate_value = rate
            if rate:
                LOT = amount / ((pips + spread) * 10 * rate)

    return render_template(
        'form.html',
        LOT=LOT,
        payment_currency=payment_currency,
        amount=amount,
        pips=pips,
        spread=spread,
        real_time_rate=real_time_rate_value
    )

if __name__ == '__main__':
    app.run(debug=True)
