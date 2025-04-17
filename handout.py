import streamlit as st

# Title of the app
st.title("My Streamlit App")

# Add a simple text input
user_input = st.text_input("Enter some text:")

# Display the input back to the user
st.write("You entered:", user_input)
