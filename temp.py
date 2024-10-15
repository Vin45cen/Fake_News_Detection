import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle



loaded_model = pickle.load(open('D:\github\Fake_News_Detection/trained_model.sav', 'rb'))
vectorizer = pickle.load(open('D:/github/Fake_News_Detection/tfidf_vectorizer.sav', 'rb'))

sample_text = "As we have become accustomed to, when Arsenal are in need, up steps No. 7 and Bukayo Saka tore apart Southamption at the Emirates, much to the delight of Mikel Arteta."

prediction = loaded_model.predict(sample_text)
print("Predicted category:", (prediction))