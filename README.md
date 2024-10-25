# User Application Gateway

## Overview

The User Application Gateway is a Streamlit application that collects user information through a form and sends personalized emails based on set criteria.
It combines form handling, logic-based evaluations, and automated email functionality to streamline the application process.

## Features

- User input form to collect personal information.
- Logic to evaluate applications based on language proficiency, Python skills, and experience.
- Automated email notifications to inform applicants about their application status.
- Data storage in a CSV file for record-keeping.

## Requirements

- Python 3.x
- Streamlit
- smtplib (comes with Python)
- Email account for sending emails 

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Hakari-Bibani/User-Application-Gateway.git

   2-Navigate to the project directory:

cd User-Application-Gateway

3- Install the required packages:pip install streamlit


4-Configure your email settings in the code
EMAIL_ADDRESS = 'your-email@example.com'  # Replace with your email
EMAIL_PASSWORD = 'your-email-password'  # Replace with your email password

5-Run the Streamlit application: streamlit run app.py


Code ExplanationL:

1-Importing Libraries

import streamlit as st
import smtplib
from email.mime.text import MIMEText
import csv
from datetime import datetime

2- Email Functionality:The send_email function handles the email sending process:

3-Streamlit App Structure: The main structure of the Streamlit app includes form creation, user input collection, evaluation of criteria, 
and sending emails based on the results

4. Logic for Acceptance Criteria

Conclusion
This project serves as a gateway for collecting user information and automating the email response process based on user qualifications.

For further inquiries or contributions, please feel free to contact me.


