import semantic_checker_v2
from flask import Flask, render_template, request

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check', methods=['POST'])
def check():
    text = request.form.get('text', '').strip()
    problems = []

    # === 規則 1：關鍵詞粗略檢測 ===
    if "問題" in text:
        problems.append("偵測到關鍵字『問題』")
    if len(text) < 20:
        problems.append("內容過短，語義不充分")
    if "重複" in text:
        problems.append("偵測到重複詞語")
    if "矛盾" in text:
        problems.append("語句存在矛盾")

    # === 規則 2：基礎語義拆解（非常簡化版） ===
    subject = ""
    action = ""
    time = ""
    place = ""

    # 簡易判斷，真實場景建議用更強語言處理
    if "昨天" in text:
        time = "昨天"
    if "去看電影" in text:
        action = "去看電影"
    if "沒離開家" in text:
        action = "沒離開家"

    # === 規則 3：邏輯矛盾偵測 ===
    if time == "昨天" and "去看電影" in text and "沒離開家" in text:
        problems.append("語義矛盾：同時說『去看電影』與『沒離開家』")

    return render_template('check.html', result=problems, text=text)

if __name__ == '__main__':
    app.run(debug=True)
