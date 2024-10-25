import streamlit as st
import smtplib
from email.mime.text import MIMEText
import csv

# Email configuration
EMAIL_ADDRESS = 'meermiro299@gmail.com'  # Replace with your email
EMAIL_PASSWORD = 'tlkt ejed oftf imze'  # Replace with your email password

# Define acceptance criteria
ACCEPTANCE_CRITERIA = {
    "english_level": "3",
    "python_level": "3",
    "experience": "5+ years"
}

# Course name
COURSE_NAME = "Course"  # Replace with your actual course name

# Function to send email
def send_email(to_email, applicant_name, accepted):
    subject = "Application Status"
    if accepted:
        body = f"Dear {applicant_name},\n\nWe are delighted to inform you that your application for our {COURSE} has been accepted! We are excited to have you join us.\nYou will be hearing from us soon with more details about the course."
    else:
        body = f"Dear {applicant_name},\n\nThank you for your interest in our course.\nWe appreciate you taking the time to apply.\nUnfortunately, due to limited enrollment or other factors, we are unable to offer you a place in this particular course at this time.\nWe understand that this may be disappointing, and we apologize for any inconvenience.\nPlease know that we will keep your application on file and will inform you of any future opportunities or similar courses that may be of interest to you."

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = to_email

    # Send email
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:  # Replace with your SMTP server
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)

# Streamlit app
st.title("Personal Information Form")

with st.form(key='application_form'):
    name = st.text_input("Name")
    dob = st.date_input("Date of Birth")
    mobile = st.text_input("Mobile Number")
    email = st.text_input("Email")
    english_level = st.selectbox("Level of English Language", [1, 2, 3])
    python_level = st.selectbox("Level of Python", [1, 2, 3])
    experience = st.selectbox("Experience", ["less than a year", "2-4 years", "5+ years"])

    submit_button = st.form_submit_button("Submit")

    if submit_button:
        # Save data to a CSV file
        with open('applications.csv', 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([name, dob, mobile, email, english_level, python_level, experience])

        # Determine if accepted or declined
        if (english_level == ACCEPTANCE_CRITERIA["english_level"] and 
            python_level == ACCEPTANCE_CRITERIA["python_level"] and 
            experience == ACCEPTANCE_CRITERIA["experience"]):
            send_email(email, name, accepted=True)
        else:
            send_email(email, name, accepted=False)

        # Clear the form fields after submission
        st.experimental_rerun()
