# 🌍 Lot Calculation Tool for Forex & Crypto Traders

海外FXで損失額を一定に抑えるための「ロット計算ツール」をFlaskで開発しました。  
GOLD（XAUUSD）やビットコイン（BTCUSD）などにも対応し、リアルタイムの為替レートを使った計算が可能です。

ロット計算は、海外FXで損失許容額を超えないための必須技術ではありますが、自分自身がFXをやっているときには無料の便利ツールが無く、あったとしてもGOLDやビットコインに対応しているWebツールはほとんどありませんでした。

そこで、必要な機能だけに絞った実用的なツールを目指しました。

---

## できること

- 💹 為替 / GOLD / BTCなどに対応した**汎用ロット計算**
- 💸 損切り幅・許容損失から**適正ロットを自動計算**
- 🔄 API経由で**リアルタイムレートを取得**
- 📱 モバイルでも使いやすいシンプルUI（Bootstrap）
- 🌐 [WordPressブログにも埋め込み済み](https://your-blog-url.com)

---

## 使用技術

- **Flask**（バックエンド & ルーティング）
- **Jinja2**（テンプレートエンジン）
- **requests**（リアルタイムレート取得API用）
- **Bootstrap 5**（UI）
- **Render**（ホスティング）

---

## 🚀 Live Demo

👉 [アプリを使ってみる](https://your-render-url.onrender.com)

---

## 📌 Usage（使い方）

1. 決済通貨を選択（例：JPY）
2. 許容損失額を入力（円/ドルなど）
3. 損切りpipsとスプレッドを入力
4. 自動でロット数（10万通貨単位）が表示されます

---

## 🧑‍💻 Author

Kei/ [@Kei124](https://github.com/Keidai124)

---

