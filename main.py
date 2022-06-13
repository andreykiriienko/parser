from flask import Flask
from parser import get_content

app = Flask(__name__)


@app.route('/')
def index():
    return get_content(url='https://usionline.com/vse-stati')


if __name__ == '__main__':
    app.run()
