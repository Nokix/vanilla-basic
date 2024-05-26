from flask import Flask, jsonify, render_template
# from provided_translator import translate_to_eng
from sqlalchemy_translator import translate_to_eng

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('src/index.html')


@app.route('/translate/<pokemon_name>')
def translate(pokemon_name):
    result = jsonify({"name": translate_to_eng(pokemon_name).lower()})
    return result


if __name__ == '__main__':
    app.run(debug=True, port=5000)
