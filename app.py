from flask import Flask, request, jsonify, render_template
from test import Test

app = Flask(__name__)


@app.route('/')
def home():
    #return render_template('index.html')
    return '<h1>hello ooooo </h1>'

@app.route("/predict")
def predict():
    #test = Test()
    #predictedvalue = test.predict()
    return 10024


if __name__ == '__main__':
	#app.run(debug=True)
    app.run(host='0.0.0.0', port=5000)
