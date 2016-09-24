from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

def process_translation(msg=None):
    return msg

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        msg = request.form['to_translate']
        translation = process_translation(msg=msg)
    else:
        translation = ''
    return render_template('index.html', translation=translation)

if __name__ == '__main__':
    app.run()
