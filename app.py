import streamlit as st
import smtplib
from email.mime.text import MIMEText
import csv
from datetime import datetime

# Email configuration
EMAIL_ADDRESS = 'meermiro299@gmail.com'
EMAIL_PASSWORD = 'tlkt ejed oftf imze'

# Define course name
COURSE_NAME = "Course"

# Function to send email
def send_email(to_email, applicant_name, accepted):
    subject = "Application Status"
    if accepted:
        body = f"Dear {applicant_name},\n\nWe are delighted to inform you that your application for our course has been accepted! We are excited to have you join us.\nYou will be hearing from us soon with more details about the course."
    else:
        body = f"Dear {applicant_name},\n\nThank you for your interest in our course.\nWe appreciate you taking the time to apply.\nUnfortunately, due to limited enrollment or other factors, we are unable to offer you a place in this particular course at this time.\nWe understand that this may be disappointing, and we apologize for any inconvenience.\nPlease know that we will keep your application on file and will inform you of any future opportunities or similar courses that may be of interest to you."

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = to_email

    # Send email
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)

# Streamlit app
st.title("Personal Information Form")

# Initialize session state to clear form
if 'form_submitted' not in st.session_state:
    st.session_state.form_submitted = False

with st.form(key='application_form'):
    name = st.text_input("Name", value="" if not st.session_state.form_submitted else "")
    
    # Adjust date of birth input to allow only 1970-2015
    min_date = datetime(1970, 1, 1)
    max_date = datetime(2015, 12, 31)
    dob = st.date_input("Date of Birth", value=None if not st.session_state.form_submitted else None, min_value=min_date, max_value=max_date)
    
    mobile = st.text_input("Mobile Number", value="" if not st.session_state.form_submitted else "")
    email = st.text_input("Email", value="" if not st.session_state.form_submitted else "")
   
