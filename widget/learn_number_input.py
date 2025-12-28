import streamlit as st


number_input = st.number_input(
    label='Enter a number',
    min_value=0,
    max_value=100,
    value=50,
    step=1,
    help='Use this widget to input a number',
    label_visibility='visible'
)

sidebar_number_input = st.sidebar.number_input(
    label='Number Input in sidebar',
    min_value=5,
    max_value=100,
    value=30,
    step=5,
    label_visibility='visible'
)

st.write(sidebar_number_input)
