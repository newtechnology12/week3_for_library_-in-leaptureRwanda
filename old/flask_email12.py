from crypt import methods
from flask import Flask, render_template, request
from flask_mail import *

app = Flask(__name__)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'sentongoalbert12@gmail.com'
app.config['MAIL_PASSWORD'] = 'magufuri1992@@'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

@app.route("/")
def index():

  return render_template("sendemail.html")

@app.route('/send_message', methods=['GET','POST'])
def send_message():
  if request.method == 'POST':
    email = request.form['email']
    subject = request.form['subject']
    msg = request.form['message']

    message = Message(subject, sender="sentongoalbert12@gmail.com", recipients=[email])
    message.body = msg

    mail.send(message)
    success = 'Message sent'
    return render_template("result.html",success = success )

if __name__ == '__main__':
   app.run(debug = True)


