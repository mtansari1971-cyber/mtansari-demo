import streamlit as st
st.title("Welcome to the Streamlit App")
st.write("This is a simple Streamlit application.")

user_msg = st.text_input("Enter your message:")

if st.button("submit"):
    st.write(user_msg)