import streamlit as st
import csv
import pickle
import pandas as pd
from data_cleaner import DataCleaner, clean, change

st.title("Demo ia o'poil")

animals = []
with open('data/animals.csv', newline='') as animalFile:
    reader = csv.reader(animalFile, delimiter=' ', quotechar='|')
    for row in reader:
        animals.append(', '.join(row))

animal_selected = st.selectbox(
    'Specie : ',
    animals
)

symptoms = []
with open('data/symptoms.csv', newline='') as symptomsFile:
    reader = csv.reader(symptomsFile, delimiter=' ', quotechar='|')
    for row in reader:
        symptoms.append(' '.join(row))

symptoms_selected = st.multiselect(
    'Select symptoms (max5)',
    symptoms, max_selections=5
)

user_prediction = {"AnimalName" : animal_selected,
                   "symptoms1" : '',
                   "symptoms2" : '',
                   "symptoms3" : '',
                   "symptoms4" : '',
                   "symptoms5" : '',
                   }

for i, symptom in enumerate(symptoms_selected):
    cat = f"symptoms{i+1}"
    user_prediction[cat] = symptom

st.write(pd.DataFrame([user_prediction]))

model = pickle.load(open('models/opoil-pipelinev3.pkl', 'rb'))

prediction = model.predict(pd.DataFrame([user_prediction]))

st.write(prediction)
