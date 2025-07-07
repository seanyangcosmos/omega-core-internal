from flask import Flask, render_template, request
from core.logic import process_text
from gpt_integration.gpt_helper import gpt_check

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check', methods=['POST'])
def check():
    text = request.form['text']
    
    # 本地邏輯初步判斷
    local_result = process_text(text)
    
    # 決定是否需要 GPT 輔助
    if local_result == "需要進一步語義檢測":
        gpt_result = gpt_check(text)
        final_result = f"GPT 語義判斷結果：{gpt_result}"
    else:
        final_result = f"本地邏輯判斷結果：{local_result}"
    
    return render_template('result.html', result=final_result)

if __name__ == '__main__':
    app.run(debug=True)


