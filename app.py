import streamlit as st
import smtplib
from email.mime.text import MIMEText

# Accessing environment variables (email and password) securely
EMAIL_ADDRESS = st.secrets["meermiro299@gmail.com"]
EMAIL_PASSWORD = st.secrets["tlkt ejed oftf imze"]

def send_email(subject, body, to_email):
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = to_email
    
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)

# Streamlit Form
st.title("Personal Information Form")

with st.form("applicant_form"):
    name = st.text_input("Name")
    email = st.text_input("Email")
    mobile = st.text_input("Mobile Number")
    dob = st.date_input("Date of Birth")
    
    english_level = st.selectbox("Level of English Language", [1, 2, 3], format_func=lambda x: ["Beginner", "Intermediate", "Advanced"][x-1])
    python_level = st.selectbox("Level of Python", [1, 2, 3], format_func=lambda x: ["Beginner", "Intermediate", "Advanced"][x-1])
    experience = st.selectbox("Experience", ["less than a year", "2-4 years", "5+ years"])
    
    submit = st.form_submit_button("Submit")

if submit:
    # Criteria for acceptance
    if english_level == 3 and python_level == 3 and experience == "5+ years":
        # Accepted email
        subject = "Congratulations on Your Acceptance!"
        body = f"Dear {name},\n\nWe are delighted to inform you that your application for our course has been accepted! We are excited to have you join us.\nYou will be hearing from us soon with more details about the course.\n\nBest regards,\n[Hakari Organization]"
    else:
        # Declined email
        subject = "Thank You for Your Application"
        body = f"Dear {name},\n\nThank you for your interest in our Course.\nWe appreciate you taking the time to apply.\nUnfortunately, due to limited enrollment or other factors, we are unable to offer you a place in this particular course at this time.\nWe understand that this may be disappointing, and we apologize for any inconvenience.\nPlease know that we will keep your application on file and will inform you of any future opportunities or similar courses that may be of interest to you.\n\nBest regards,\n[Hakari Organization]"
    
    # Send email without showing the result in the Streamlit app
    send_email(subject, body, email)
    st.success("Your form has been submitted successfully.")
