import streamlit as st
import pickle

def main():
    with open('nlp_pipeline.pkl', 'rb') as file:
        model_pipeline = pickle.load(file)

    st.title("Fake News Detector")
    input_text = st.text_area("Input Text Here: ")
    # text_button = st.button("Submit")
    # clear_button = st.button("Clear Text")

    if st.button("Submit"):
        prediction = model_pipeline.predict([input_text])[0]
        print(prediction)
        if prediction == 'True':
            st.write("Hasil Prediksi : Positive")
        elif prediction == 'Fake':
            st.write("Hasil Prediksi : Negative")
        

if __name__ == '__main__':
    main()