from flask import Flask, request
 
app = Flask(__name__)     

@app.route('/')           
def run():                
    return 'hello world'  

@app.route('/hi')
def hi():
    return 'hi page'

@app.route('/hello')
def hello():
    return 'hello page'

@app.route('/shutdown')
def shutdown():
    shutdown_server()
    return 'Server shutting down.'

def shutdown_server(): # 해당 포트 종료시 사용
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()   

if __name__ == "__main__":
    app.run() 
