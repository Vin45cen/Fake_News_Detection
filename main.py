import streamlit as st
import pickle, string
from nltk.stem.porter import PorterStemmer
from nltk.tokenize import word_tokenize
from nltk.stem import SnowballStemmer, WordNetLemmatizer
from nltk.corpus import stopwords
import nltk

port_stemmer= PorterStemmer()
stop_words = set(stopwords.words('english'))
punc_list = set(string.punctuation)
stemmer = SnowballStemmer('english')
lemmatizer = WordNetLemmatizer()


with open('nlp_pipeline.pkl', 'rb') as file:
    model_pipeline = pickle.load(file)
    vc = model_pipeline['vectorizer']
    lgr = model_pipeline['model']

def preprocessing(text):
    text_list = word_tokenize(text.lower())
    text_list = [word for word in text_list if word not in stop_words]
    text_list = [word for word in text_list if word not in punc_list and word.isalpha()]
    text_list = [stemmer.stem(word) for word in text_list]
    text_list = [lemmatizer.lemmatize(word) for word in text_list]

    return ' '.join(text_list)

def predict(text):
    text = preprocessing(text) 
    text_transformed = vc.transform([text])
    prediction = lgr.predict(text_transformed)

    return prediction[0]

def main():
    
    st.title("Fake News Detector")
    input_text = st.text_area("Input Text Here: ")
    # text_button = st.button("Submit")
    # clear_button = st.button("Clear Text")
    if st.button("Predict"):
        if input_text:
            # Call the predict function with the user input
            prediction = predict(input_text)
            st.write(f"Prediction: {prediction}")
        else:
            st.write("Please enter some text to get a prediction.")

    # if st.button("Submit"):
    #     prediction = model_pipeline.predict([input_text])[0]
    #     print(prediction)
    #     if prediction == 0:
    #         st.write("Hasil Prediksi : Positive")
    #     elif prediction == 1:
    #         st.write("Hasil Prediksi : Negative")
        

if __name__ == '__main__':
    main()