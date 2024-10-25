import pandas as pd
import streamlit as st
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import base64

# Initialize an empty DataFrame to store applications
applications_df = pd.DataFrame(columns=["Name", "DOB", "Mobile", "Email", "English_Level", "Python_Level", "Experience"])

def send_email(recipient, name, accepted):
    # Email configuration
    sender_email = "meermiro299@gmail.com"
    sender_password = "tlkt ejed oftf imze"
    subject = "Application Status"

    if accepted:
        body = f"Dear {name},\n\nWe are delighted to inform you that your application for our course has been accepted! We are excited to have you join us.\nYou will be hearing from us soon with more details about the course."
    else:
        body = f"Dear {name},\n\nThank you for your interest in our Course.\nUnfortunately, due to limited enrollment or other factors, we are unable to offer you a place in this particular course at this time."

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, recipient, msg.as_string())
        print(f"Email sent successfully to {recipient}")
    except Exception as e:
        print(f"Error sending email: {e}")

# Streamlit form code
with st.form("application_form"):
    name = st.text_input("Name")
    dob = st.date_input("Date of Birth")
    mobile = st.text_input("Mobile Number")
    email = st.text_input("Email")
    english_level = st.selectbox("Level of English language", [1, 2, 3])
    python_level = st.selectbox("Level of Python", [1, 2, 3])
    experience = st.selectbox("Experience", ["less than a year", "2-4 years", "5+ years"])
    
    submitted = st.form_submit_button("Submit")

    if submitted:
        # Determine acceptance criteria
        accepted = (english_level == 3 and python_level == 3 and experience == "5+ years")
        
        # Send the email
        send_email(email, name, accepted)
        
        # Store submission in DataFrame
        new_application = {
            "Name": name,
            "DOB": dob,
            "Mobile": mobile,
            "Email": email,
            "English_Level": english_level,
            "Python_Level": python_level,
            "Experience": experience,
        }
        applications_df.loc[len(applications_df)] = new_application  # Append new row
        
        # Create a download button for the CSV file
        csv = applications_df.to_csv(index=False)
        b64 = base64.b64encode(csv.encode()).decode()  # Convert to base64
        linko = f'<a href="data:file/csv;base64,{b64}" download="applications.csv">Download applications.csv</a>'
        st.markdown(linko, unsafe_allow_html=True)
