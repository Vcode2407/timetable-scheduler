import streamlit as st
import requests
import pandas as pd
from datetime import datetime

st.set_page_config(layout="wide")
st.title('Timetable Scheduler')

# Add schedule form
st.header('Add Schedule')
with st.form(key='schedule_form'):
    course = st.text_input('Course Name')
    day = st.selectbox('Day', ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])
    time = st.time_input('Time')
    location = st.text_input('Location')
    submit = st.form_submit_button('Add Schedule')

if submit:
    response = requests.post('http://localhost:5000/api/schedule', json={
        'course': course,
        'day': day,
        'time': time.strftime('%H:%M'),
        'location': location
    })
    if response.status_code == 201:
        st.success('Schedule added!')
    else:
        st.error('Failed to add schedule')

# Display timetable
st.header('Timetable')
response = requests.get('http://localhost:5000/api/schedule')
if response.status_code == 200:
    schedules = response.json()
    if schedules:
        df = pd.DataFrame(schedules)
        st.dataframe(df)
    else:
        st.write('No schedules found.')

# Delete schedule
st.header('Delete Schedule')
course_to_delete = st.text_input('Course to Delete')
if st.button('Delete'):
    response = requests.delete(f'http://localhost:5000/api/schedule/{course_to_delete}')
    if response.status_code == 200:
        st.success('Schedule deleted!')
    else:
        st.error('Failed to delete schedule')

# Feedback section
st.header('Feedback')
feedback = st.text_area('Provide feedback to improve the UI')
if st.button('Submit Feedback'):
    st.success('Feedback submitted!')
