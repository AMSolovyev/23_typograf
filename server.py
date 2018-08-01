import os

from flask import Flask, render_template, request, jsonify

from typograf import typografy_text

ENV_DEBUG = os.environ.get('DEBUG') == 'True'

app = Flask(__name__)


@app.route('/')
def form():
    return render_template('form.html')


@app.route('/typografy', methods=['POST'])
def typografy():
    typographed_text = typografy_text(request.form['text'])
    if typographed_text is None:
        typographed_text = ''
    return jsonify(text=typographed_text)


if __name__ == "__main__":
    app.run(debug=ENV_DEBUG)
