"dummy docstring"
import streamlit as st
import pandas as pd
from Backend import PDFtoDF_clean
from Backend import convert_pdf_to_csv
from Backend import notifs
from Backend import getCurrentTime
from Backend import getDay
from PIL import Image
import os
from twilio.rest import Client

#initializes twilio API with necessary API keys
account_sid = os.environ['AC1385351c76f52c0899c297a8be387a32']
auth_token = os.environ['955b53aec92b587c2c2bfbc466ecf80f']
client = Client(account_sid, auth_token)

image = Image.open('/Users/neeyad/Desktop/myproject/logo.png')
st.image(image, caption='Welcome to OnTime!')

st.write("OnTime provides students a means of planning out their day, including reminders for when to leave and what transportation to take in order to get to their classes on time.")


st.write("How to use: ")
st.write("Step 1: Go to Self Service and click the 'Registration and Records tab' ")
st.write("Step 2: Click the 'Enhanced Registration' button and click 'View Class Schedules'")
st.write("Step 3: Choose your schedule from the current semester, click the 'printer' icon on the right corner of the screen and save your schedule as a pdf")
st.write("Step 4: Upload your schedule below!")

#prompt to upload schedule to the app
uploaded_file = st.file_uploader('Choose your .pdf file', type="pdf")

#prompt to upload phone number to receive text notifs
phone_number = st.text_input('Enter your phone number',max_chars=12,help='Enter your phone number without spaces or dashes, including the area code. Ex: Use "+1" for a USA number.')

st.write("Now you will recieve text reminders to leave for your classes based on your location!")

if uploaded_file is not None:
    #filters PDF that the user uploads
    df = PDFtoDF_clean(uploaded_file)
    # gets tht time (militaryt ime)
    curr_time = getCurrentTime()
    time = str(curr_time)
    
    # gets the day 
    curr_day = getDay()
    day = str(curr_day)

    # dummy notif method
    str = notifs(df, day, time)
    str2 = notifs(df,'0', '10:40:00')


if phone_number is not None:
    message = client.messages \
                .create(
                     body = str2,
                     from_='+19135134529',
                     to = phone_number
                 )