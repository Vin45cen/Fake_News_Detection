import streamlit as st

def main():
    st.title("Fake News Detector")
    text = st.text_input("Input Text Here: ")
    text_button = st.button("Submit")

if __name__ == '__main__':
    main()