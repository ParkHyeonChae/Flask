# Flask 기초 정의

from flask import Flask # flask 모듈을 import하여 사용

app = Flask(__name__) # 현재 모듈에 app이란 이름의 flask 객체 생성

@app.route('/') # app이란 서버의 웹주소에 대한 동작 ('/'는 각 주소별 동작을 구성해주는 라우팅)

def hello_world():
    return 'hello world' # html페이지에 hello world 출력

if __name__ == "__main__":
    app.run()