import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

import joblib
import os

df=pd.read_csv('data/intent.csv')

x=df["text"]
y=df["intent"]

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42,stratify=y)

vectorizer=TfidfVectorizer()
vector_x_train=vectorizer.fit_transform(x_train)
vector_y_test=vectorizer.transform(x_test)

model=LogisticRegression()
model.fit(vector_x_train,y_train)

accuracy=model.score(vector_y_test,y_test)

print("Accuracy: ",accuracy)

os.makedirs("model",exist_ok=True)
joblib.dump(model,"model/chatbot_model.pkl")
joblib.dump(vectorizer,"model/vectorizer.pkl")

print("Model trained successfully")