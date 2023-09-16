from flask import Flask

app = Flask(__name__)

username = 'admin'

@app.route('/')
def hello():
    return 'Hello,' + username + '!'

if __name__ == '__main__':
    app.run()
