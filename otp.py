from flask import Flask, render_template, request
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from random import randint


app = Flask(__name__)

otp = randint(100000, 999999)

def send_otp(email):
    sender_email = 'slayz9168@gmail.com'
    receiver_email = email
    password = 'hfcu cual pbge oaxl'

    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = 'Your OTP'

    message.attach(MIMEText(f'Your OTP is: {otp}', 'plain'))

    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/verify', methods=["POST"])
def verify():
    email = request.form['email']
    send_otp(email)
    return render_template('verify.html')

@app.route('/validate', methods=['POST'])
def validate():
    user_otp = request.form['otp']
    if otp == int(user_otp):
        return "<h3>Email verification successful</h3>"
    return "<h3>Please Try Again</h3>"

if __name__ == '__main__':
    app.run(debug=True)
