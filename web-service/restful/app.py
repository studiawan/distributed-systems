# Source: http://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"

if __name__ == '__main__':
    app.run(debug=True)
