from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    #return render_template('index.html')
    return '<h1>hello</h1>'
