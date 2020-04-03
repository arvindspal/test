from flask import Flask, request, jsonify, render_template
from test import Test

app = Flask(__name__)


@app.route('/')
def home():
    #return render_template('index.html')
    return '<h1>hello ooooo utyuiuytyu 123456 </h1>'

if __name__ == '__main__':
	#app.run(debug=True)
    app.run(host='0.0.0.0', port=5000)
