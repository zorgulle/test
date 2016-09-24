from flask import Flask

app = Flask(__name__)

def reply(msg=None):
    return msg


@app.route('/')
def index():
    return "Index"

if __name__ == '__main__':
    app.run()
