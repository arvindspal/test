from flask import Flask, request, jsonify, render_template
import test
app = Flask(__name__)


@app.route('/')
def home():
    #return render_template('index.html')
    return '<h1>hello ooooo </h1>'

@app.route("/predict")
def predict():
    test1 = test.Test()
    predictedvalue = test1.predict()
    return predictedvalue


if __name__ == '__main__':
	#app.run(debug=True)
    app.run(host='0.0.0.0', port=5000)
