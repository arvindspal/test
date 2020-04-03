from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def home():
    #return render_template('index.html')
    return '<h1>hello ooooo </h1>'

if __name__ == '__main__':
	#app.run(debug=True)
    app.run(host='0.0.0.0', port=5000)
