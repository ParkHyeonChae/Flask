# form사용하여 여러가지 데이터를 다음페이지로 넘겨보기
# https://blog.naver.com/pk3152/221361470754 

from flask import Flask, render_template, request

app = Flask (__name__)

@app.route('/')
def formpage():
    return render_template('FormPage.html')

@app.route('/view', methods=['post'])
def view():
    userName = request.form['userName']
    userPw = request.form['userPw']
    userEmail = request.form['userEmail']

    return render_template('ViewData.html',userName=userName, userPw=userPw, userEmail=userEmail)

if __name__ == "__main__":
    app.run()
