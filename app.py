"""
# DurCalc: Hassle-Free Calculation of Date and Time Durations
This app helps you calculate the duration between dates and/or times without any fuss.
"""

# Import libraries
import datetime as dt
import pytz
import streamlit as st

# --- --- --- --- --- ---
# Section 1: Web App
# --- --- --- --- --- ---

# Set title
st.write(
    '## ***DurCalc***',
    "<span style = 'font-size: 0.7em; font-weight: normal'>: A Simple Date/Time Duration Calculator</span>",
    unsafe_allow_html=True,
)
st.write(
    "<span style = 'font-size: 1.1em; font-weight: normal'>This app helps you calculate duration between dates and/or times without any fuss.</span>",
    unsafe_allow_html=True,
)

# Set columns for first row
col1, col2, col3 = st.columns(3)

# User enters start date and time
start_date = col1.date_input('Start Date')
start_time = col2.time_input('Start Time')
start_datetime = dt.datetime.combine(start_date, start_time)

# Initialize session state for the start timezone if not already done
if 'start_timezone' not in st.session_state:
    st.session_state['start_timezone'] = 'UTC'

# Add a timezone selection box
start_timezone = col3.selectbox(
    'Start Timezone',
    pytz.all_timezones,
    index=pytz.all_timezones.index(st.session_state['start_timezone']),
)

# Adjust the start_datetime to include the timezone
start_tz = pytz.timezone(start_timezone)
start_datetime = dt.datetime.combine(start_date, start_time)
start_datetime = start_tz.localize(start_datetime)

# Add a horizontal line
st.markdown('---')

# Set columns for second row
col4, col5, col6 = st.columns(3)

# User enters end date and time
end_date = col4.date_input('End Date')
end_time = col5.time_input('End Time')
end_datetime = dt.datetime.combine(end_date, end_time)
end_datetime = start_datetime.astimezone(pytz.utc)

# Initialize session state for the end timezone if not already done
if 'end_timezone' not in st.session_state:
    st.session_state['end_timezone'] = 'UTC'

# Add a timezone selection box
end_timezone = col6.selectbox(
    'End Timezone',
    pytz.all_timezones,
    index=pytz.all_timezones.index(st.session_state['end_timezone']),
)

# Adjust the end_datetime to include the timezone
end_tz = pytz.timezone(end_timezone)
end_datetime = dt.datetime.combine(end_date, end_time)
end_datetime = end_tz.localize(end_datetime)
end_datetime = end_datetime.astimezone(pytz.utc)

# Add a horizontal line
st.markdown('---')

# Set columns for second row
col7, col8 = st.columns(2)

# --- --- --- --- --- ---
# Section 2: Calculator
# --- --- --- --- --- ---

# # Add an option to whether include end date in calculation
# include_end_date = col8.checkbox('Include the end date as well?')

# Function to convert seconds into hours, minutes, and seconds
def convert_seconds_to_hms(seconds):
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    seconds = int(seconds % 60)
    return hours, minutes, seconds

# Calculate button
if col7.button('Calculate'):
    # Selected timezones
    st.session_state['start_timezone'] = start_timezone
    st.session_state['end_timezone'] = end_timezone

    # Convert start and end datetime to UTC for comparison
    start_datetime_utc = start_datetime.astimezone(pytz.utc)
    end_datetime_utc = end_datetime.astimezone(pytz.utc)

    # Error check for same day with end time earlier than start time, considering timezones
    if end_datetime_utc.date() < start_datetime_utc.date() or \
        (start_datetime_utc.date() == end_datetime_utc.date() and end_datetime_utc.time() < start_datetime_utc.time()):
        st.error('Error: End date and time cannot be earlier than start date and time.')
    else:
        # Calculate the number of days between dates
        delta_days = (end_datetime_utc.date() - start_datetime_utc.date()).days

        # # Adjust for including the end date
        # if include_end_date:
        #     delta_days += 1

        # Calculate the time difference within a day
        delta_time = (end_datetime_utc - start_datetime_utc).seconds

        # Check if end time is on the next day compared to start time
        if end_datetime_utc.time() < start_datetime_utc.time():
            delta_days -= 1  # Subtract a day as it's already accounted in delta_time

        # Convert the total seconds to hours, minutes, and seconds
        hours, minutes, seconds = convert_seconds_to_hms(delta_time)

        # Display the result
        day_str = 'day' if delta_days == 1 else 'days'
        hour_str = 'hour' if hours == 1 else 'hours'
        minute_str = 'minute' if minutes == 1 else 'minutes'

        if delta_days >= 1:
            st.success(
                f"{delta_days} {day_str}, {hours} {hour_str}, and {minutes} {minute_str} apart."
            )
        else:
            st.success(
                f"{hours} {hour_str} and {minutes} {minute_str} apart."
            )
