from flask import Flask, render_template
from flask_mail import Message
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/mail')
def mail():
    msg = Message("Hello",
        sender="from@example.com",
        recipients=["tmax818@mac.com"])



if __name__ == '__main__':
    app.run()
