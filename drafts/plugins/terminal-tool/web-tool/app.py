from flask import Flask, render_template, request
from core.semantic_checker import check_gpt_content

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        user_input = request.form["user_input"]
        if check_gpt_content(user_input):
            result = "GPT 相關內容"
        else:
            result = "非 GPT 相關內容"
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)


