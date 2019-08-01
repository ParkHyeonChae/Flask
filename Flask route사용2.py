# 라우팅으로 변수 넘기기

from flask import Flask

app = Flask(__name__)

@app.route('/userID/<userID>')
def showUserID(userID):
    return 'UserID : ' +userID

if __name__ =='__main__':
    app.run()