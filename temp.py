import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle

vectorization = TfidfVectorizer()
df_manual=pd.DataFrame()
df_manual['title']=''
df_manual['text']=''
df_manual['subject']=''
df_manual['date']=''
df_manual['Label']=''

loaded_model = pickle.load(open('trained_model.sav', 'rb'))

def manual_testing(news):
    testing_news = {"text":[news]}
    new_def_test = pd.DataFrame(testing_news)
    new_def_test["text"] = new_def_test["text"].apply(reuters_removal)

    new_def_test["text"] = new_def_test["text"].apply(stemmer)
    new_x_test = new_def_test["text"]
    new_xv_test = vectorization.transform(new_x_test)
    prediction= loaded_model.predict(new_xv_test)
    return prediction[0]
manual_testing(df_manual.loc[12,'text'])

sample_text = "As we have become accustomed to, when Arsenal are in need, up steps No. 7 and Bukayo Saka tore apart Southamption at the Emirates, much to the delight of Mikel Arteta."
print("Predicted category:", manual_testing(sample_text))