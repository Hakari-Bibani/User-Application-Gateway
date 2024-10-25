import streamlit as st
import smtplib
from email.mime.text import MIMEText
import json
import requests
from datetime import datetime

# Email configuration
EMAIL_ADDRESS = 'meermiro299@gmail.com'
EMAIL_PASSWORD = 'tlkt ejed oftf imze' 
GITHUB_TOKEN = 'your-github-token'  # Replace with your GitHub token
GITHUB_REPO = 'Hakari-Bibani/User-Application-Gateway'  # Your repository
CSV_FILE = 'applications.csv'  # The name of the CSV file

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

# Function to save data to GitHub CSV
def save_to_github_csv(data):
    url = f'https://api.github.com/repos/{GITHUB_REPO}/contents/{CSV_FILE}'
    headers = {
        'Authorization': f'token {GITHUB_TOKEN}',
        'Accept': 'application/vnd.github.v3+json'
    }
    
    try:
        # Check if file exists
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        file_info = response.json()
        sha = file_info['sha']  # Get the SHA of the existing file for update
        
        # Prepare the content
        existing_content = requests.get(file_info['download_url']).text
        existing_content += data + "\n"  # Append new data
        content_encoded = existing_content.encode('utf-8')
        
        # Update the file
        update_data = {
            "message": "Update CSV with new application data",
            "content": content_encoded.decode('utf-8'),
            "sha": sha
        }
        requests.put(url, headers=headers, json=update_data)
        
    except requests.exceptions.HTTPError as err:
        if err.response.status_code == 404:  # If file doesn't exist, create it
            # Create a new file
            content_encoded = data.encode('utf-8')
            create_data = {
                "message": "Create CSV for application data",
                "content": content_encoded.decode('utf-8')
            }
            requests.put(url, headers=headers, json=create_data)
        else:
            st.error(f"Error updating file: {err}")

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
    english_level = st.selectbox("Level of English Language", [1, 2, 3], index=0 if not st.session_state.form_submitted else None)
    python_level = st.selectbox("Level of Python", [1, 2, 3], index=0 if not st.session_state.form_submitted else None)
    experience = st.selectbox("Experience", ["less than a year", "2-4 years", "5+ years"], index=0 if not st.session_state.form_submitted else None)

    submit_button = st.form_submit_button("Submit")

    if submit_button:
        # Prepare the data to save
        data_to_save = f"{name},{dob},{mobile},{email},{english_level},{python_level},{experience}"
        
        # Save data to GitHub CSV
        save_to_github_csv(data_to_save)

        # Determine if accepted or declined
        accepted = False  # Initialize accepted status

        # Check acceptance criteria
        if (english_level == 3 and 
            python_level == 3 and 
            experience == "5+ years"):
            accepted = True
        elif (english_level in [1, 2] or python_level in [1, 2]) and experience in ["less than a year", "2-4 years"]:
            accepted = False  # This condition leads to decline

        # Send email based on acceptance status
        send_email(email, name, accepted)

        # Update session state to indicate form submission
        st.session_state.form_submitted = True

        # Show success message (optional)
        st.success("Your application has been submitted successfully!")

# Reset form fields if already submitted
if st.session_state.form_submitted:
    st.session_state.form_submitted = False
