
from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route('/')
def main():
	return render_template('index.html')

@app.route('/sign_in')
def sign_in():
	return render_template('sign_in.html')

@app.route('/twitter')
def twitter():
	return redirect('https://twitter.com/')

@app.route('/facebook')
def facebook():
	return redirect('http://facebook.com')

@app.route('/github')
def github():
	return redirect('https://github.com')

if __name__ == "__main__":
	app.run(debug= True)