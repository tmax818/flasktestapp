from flask import Flask, render_template
from flask_mail import Mail, Message
app = Flask(__name__)
mail = Mail(app)


@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/mail')
def mail():
    msg = Message("Hello",
        sender="test",
        recipients=["tmax818@mac.com"])
  
    mail.send(msg)



if __name__ == '__main__':
    app.run()
