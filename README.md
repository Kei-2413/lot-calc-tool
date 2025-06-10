# ロット計算ツール（FX用）

Flaskで作った海外FXトレーダー向けのロット計算ツールです。  
通貨ペア、損切り幅、スプレッド、許容損失を入力すると、適正ロットを自動計算します。

## 💡 特徴
- Flask + HTML ベース
- スマホ対応UI（Bootstrapなど使用）
- JPY/USD/EURなどメジャーな決済通貨に対応している他、GOLDやビットコインのロット計算も可能
- 将来的にはリアルタイム為替レート対応も検討中

## ▶️ 起動方法

```bash
git clone https://github.com/あなたのユーザー名/lot-lacl-tool.git
cd lot-lacl-tool
python app.py

🛠 技術スタック
Python 3.x

Flask

HTML（Jinja2テンプレート）

Bootstrap（CSSフレームワーク）
