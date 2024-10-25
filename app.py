from flask import Flask, request, render_template, redirect, url_for
from flask_mail import Mail, Message
import csv

app = Flask(__name__)

# Configure Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.example.com'  # Replace with your mail server
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'your-email@example.com'  # Replace with your email
app.config['MAIL_PASSWORD'] = 'your-email-password'  # Replace with your email password
mail = Mail(app)

# Define acceptance criteria
ACCEPTANCE_CRITERIA = {
    "english_level": "3",
    "python_level": "3",
    "experience": "5+ years"
}

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    dob = request.form['dob']
    mobile = request.form['mobile']
    email = request.form['email']
    english_level = request.form['english_level']
    python_level = request.form['python_level']
    experience = request.form['experience']

    # Save data to a file
    with open('applications.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow([name, dob, mobile, email, english_level, python_level, experience])

    # Determine if the applicant is accepted or declined
    if english_level == ACCEPTANCE_CRITERIA["english_level"] and \
       python_level == ACCEPTANCE_CRITERIA["python_level"] and \
       experience == ACCEPTANCE_CRITERIA["experience"]:
        send_email(email, name, accepted=True)
    else:
        send_email(email, name, accepted=False)

    return redirect(url_for('index'))

def send_email(to_email, applicant_name, accepted):
    if accepted:
        subject = "Application Accepted!"
        body = f"Dear {applicant_name},\n\nWe are delighted to inform you that your application for our course has been accepted!"
    else:
        subject = "Application Status"
        body = f"Dear {applicant_name},\n\nThank you for your interest in our course. Unfortunately, we cannot offer you a place at this time."

    msg = Message(subject, sender=app.config['MAIL_USERNAME'], recipients=[to_email])
    msg.body = body
    mail.send(msg)

if __name__ == '__main__':
    app.run(debug=True)
