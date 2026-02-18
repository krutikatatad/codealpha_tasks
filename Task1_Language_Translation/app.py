from flask import Flask, render_template, request
from googletrans import Translator

app = Flask(__name__)
translator = Translator()

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""

    if request.method == "POST":
        text = request.form.get("text", "")
        language = request.form.get("language", "en")

        if text:
            translated = translator.translate(text, dest=language)
            result = translated.text

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
