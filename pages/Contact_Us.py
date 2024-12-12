import streamlit as st

st.header("Contact Me")

with st.form(key="email_form"):
    user_email = st.text_input("Your e-mail address")
    message = st.text_area("Message")
    button = st.form_submit_button("Submit")
    if button:
        print("Hello")
