"""
# DurCalc: A Simple Date/Time Duration Calculator
This app helps you calculate duration between dates and/or times without any fuss.
"""

# Import libraries
import datetime as dt
import streamlit as st

# Use wide mode
# st.set_page_config(layout = 'wide')

# Set title
st.write('## ***DurCalc***', "<span style = 'font-size: 0.7em; font-weight: normal'>: A Simple Date/Time Duration Calculator</span>", unsafe_allow_html = True)
st.write("<span style = 'font-size: 1.1em; font-weight: normal'>This app helps you calculate duration between dates and/or times without any fuss.</span>", unsafe_allow_html = True)

# Set columns for firt row
col1, col2 = st.columns(2)

# User enters start- date and time
start_date = col1.date_input('Start Date')
start_time = col2.time_input('Start Time')
start_datetime = dt.datetime.combine(start_date, start_time)

# Add a horizontal line
st.markdown('''---''')

# Set columns for second row
col3, col4 = st.columns(2)

# User enters end date and time
end_date = col3.date_input('End Date')
end_time = col4.time_input('End Time')
end_datetime = dt.datetime.combine(end_date, end_time)

# Add a horizontal line
st.markdown('''---''')

# Calculate the duration
delta_date = end_date - start_date
delta_time = dt.datetime.combine(dt.date.today(), end_time) - dt.datetime.combine(dt.date.today(), start_time)

# Calculate button
if st.button('Calculate'):
	if delta_date.days > 1:
		st.write(f"<span style = 'font-size: 1.5em; font-weight: normal'>{delta_date.days} days and {delta_time.seconds} seconds apart!</span>", unsafe_allow_html = True)
	else:
		st.write(f"<span style = 'font-size: 1.5em; font-weight: normal'>{delta_date.days} day and {delta_time.seconds} seconds apart!</span>", unsafe_allow_html = True)