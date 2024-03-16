from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return " aws cicd sevices sucessfully implemented "

if __name__ == '__main__':
    app.run() 

