import streamlit as st
import smtplib
from email.mime.text import MIMEText
import csv

# Email configuration
EMAIL_ADDRESS = 'meermiro299@gmail.com'
EMAIL_PASSWORD = 'Meer2025meer'  # Change this as soon as possible!

# Define acceptance criteria
ACCEPTANCE_CRITERIA = {
    "english_level": "3",
    "python_level": "3",
    "experience": "5+ years"
}

# Function to send email
# Function to send email
def send_email(to_email, applicant_name, accepted):
    subject = "Application Status"
    if accepted:
        body = f"Dear {applicant_name},\n\nWe are delighted to inform you that your application for our course has been accepted!"
    else:
        body = f"Dear {applicant_name},\n\nThank you for your interest in our course. Unfortunately, we cannot offer you a place at this time."

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
            st.success(f"Thank you, {name}! Your application has been accepted. An email has been sent.")
        else:
            send_email(email, name, accepted=False)
            st.warning(f"Thank you, {name}. Unfortunately, your application has been declined. An email has been sent.")
