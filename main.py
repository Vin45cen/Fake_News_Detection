import streamlit as st

def main():
    st.title("Fake News Detector")
    input_text = st.text_input("Input Text Here: ")
    text_button = st.button("Submit")
    clear_button = st.button("Clear Text")

    if st.button("Submit"):
        if input_text:
            pass
            # output = classify_text(input_text)
            # st.write(f"Prediction: {output}")
        else:
            st.write("Please enter text")

    if st.button("Clear Text"):
        # input_text = ""  # This will clear the input_text variable
        st.experimental_rerun()

if __name__ == '__main__':
    main()