
from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route('/')
def main():
	return render_template('index.html')

@app.route('/facebook')
def facebook():
	return redirect('http://facebook.com')

if __name__ == "__main__":
	app.run(debug= True)