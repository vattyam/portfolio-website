import streamlit as st

st.set_page_config(layout="wide")
col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png", width=600)

with col2:
    st.title("Sandeep Vattyam")
    content = """
     Hi, I am Sandeep Vattyam having over 13 years of IT experience 
     """
    st.info(content)