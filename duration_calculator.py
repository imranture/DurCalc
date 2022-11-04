"""
A simple date/time duration calculator
"""

# Import libraries
import datetime as dt
import streamlit as st

# Use wide mode
st.set_page_config(layout = 'wide')

# Set title
st.write('# *Date/Time Duration* Calculator')
st.write('##### A very simple app to help you calculate days between dates:')

# Set columns
col1, col2 = st.columns(2)

# User enters start and end dates
start_date = col1.date_input('Start Date')
start_time = col2.time_input('Start Time')
start_datetime = dt.datetime.combine(start_date, start_time)

st.markdown('''---''')

# Set columns
col3, col4 = st.columns(2)

end_date = col3.date_input('End Date')
end_time = col4.time_input('End Time')
end_datetime = dt.datetime.combine(end_date, end_time)

st.markdown('''---''')

# Calculator
# delta = end_datetime - start_datetime
delta_date = end_date - start_date
# end_time = dt.datetime(2010,10,10,20,10,10).time()
# start_time = dt.datetime(2010,10,10,10,10,10).time()
# delta_time = end_time - start_time
delta_time = dt.datetime.combine(dt.date.today(), end_time) - dt.datetime.combine(dt.date.today(), start_time)



# Calculate button
if st.button('Calculate'):
	if delta_date.days > 1:
		st.write(f'#### {delta_date.days} days and {delta_time.seconds} seconds apart!', unsafe_allow_html = True)
	else:
		st.write(f'#### {delta_date.days} day and {delta_time.seconds} seconds apart!', unsafe_allow_html = True)
	# st.write(f'Equivalent to {round(delta.days / 365, 0)} years.')
	# st.write(f'Equivalent to {delta_time} hours.')
	# st.write(f'Equivalent to {delta.days * 24 * 60} minutes.')
	# st.write(f'Equivalent to {delta.days * 24 * 60 * 60} seconds.')