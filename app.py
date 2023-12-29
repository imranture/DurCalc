"""
# DurCalc: Hassle-Free Calculation of Date and Time Durations
This app helps you calculate the duration between dates and/or times without any fuss.
"""

# Import libraries
import datetime as dt
import streamlit as st

# --- --- --- --- --- ---
# Section 1: App
# --- --- --- --- --- ---

# Use wide mode
# st.set_page_config(layout = 'wide')

# Set title
st.write(
    "## ***DurCalc***",
    "<span style = 'font-size: 0.7em; font-weight: normal'>: A Simple Date/Time Duration Calculator</span>",
    unsafe_allow_html=True,
)
st.write(
    "<span style = 'font-size: 1.1em; font-weight: normal'>This app helps you calculate duration between dates and/or times without any fuss.</span>",
    unsafe_allow_html=True,
)

# Set columns for firt row
col1, col2 = st.columns(2)

# User enters start date and time
start_date = col1.date_input("Start Date")
start_time = col2.time_input("Start Time")
start_datetime = dt.datetime.combine(start_date, start_time)

# Add a horizontal line
st.markdown("""---""")

# Set columns for second row
col3, col4 = st.columns(2)

# User enters end date and time
end_date = col3.date_input("End Date")
end_time = col4.time_input("End Time")
end_datetime = dt.datetime.combine(end_date, end_time)

# Add a horizontal line
st.markdown("""---""")

# Set columns for second row
col5, col6 = st.columns(2)

# --- --- --- --- --- ---
# Section 2: Calculator
# --- --- --- --- --- ---

# Add an option to whether include end date in calculation
include_end_date = col6.checkbox("Include the end date as well?")


# Function to convert seconds into hours, minutes, and seconds
def convert_seconds_to_hms(seconds):
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    seconds = int(seconds % 60)
    return hours, minutes, seconds


# Calculate button
if col5.button("Calculate"):
    # Error check for same day with end time earlier than start time
    if start_date == end_date and end_time < start_time:
        st.error("Error: End time cannot be earlier than start time on the same day.")
    else:
        # Calculate the number of days between dates
        delta_days = (end_date - start_date).days

        # Adjust for including the end date
        if include_end_date:
            delta_days += 1

        # Calculate the time difference
        delta_time = (
            dt.datetime.combine(dt.date.min, end_time)
            - dt.datetime.combine(dt.date.min, start_time)
        ).total_seconds()

        # If end time is earlier than start time and dates are different, adjust the delta_days and delta_time
        if end_date > start_date and delta_time < 0:
            delta_days -= 1
            delta_time += 24 * 3600  # Add 24 hours in seconds

        # Convert the total seconds to hours, minutes, and seconds
        hours, minutes, seconds = convert_seconds_to_hms(delta_time)

        # Display the result
        if delta_days >= 1:
            st.write(
                f"<span style='font-size: 1.5em; font-weight: normal'>{delta_days} days, {hours} hours, and {minutes} minutes apart.</span>",
                unsafe_allow_html=True,
            )
        else:
            st.write(
                f"<span style='font-size: 1.5em; font-weight: normal'>{hours} hours and {minutes} minutes apart.</span>",
                unsafe_allow_html=True,
            )
