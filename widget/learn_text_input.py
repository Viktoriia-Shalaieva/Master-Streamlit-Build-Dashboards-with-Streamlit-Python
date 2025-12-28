import streamlit as st


st.title("Streamlit Text Widgets Lesson")

# 1. Text Input: For single-line text entry
text_input = st.text_input(label="Enter the text",
                           placeholder="Type here...",
                           help='This is a single-line text input field.',
                           type='default', # default, password
                           max_chars=100,
                           key='text_input')

if text_input:
    st.write(f"You entered: {text_input}")

my_password = st.text_input(label='Banking Password',
                            type='password',
                            max_chars=10,
                            key='password1')

# 2. Text Area: For multi-line text entry
text_area = st.text_area(label='Enter the text',
                         placeholder="Write your text here...",
                         height=150,
                         help='This is a multi-line text area.',
                         max_chars=1000,
                         key='text_area1')

if text_area:
    st.write(f"You wrote: {text_area}")
    