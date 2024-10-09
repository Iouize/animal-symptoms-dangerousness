from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import pickle
from typing import Union
import streamlit as st

app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

model = pickle.load(open('models/opoilv4.pkl', 'rb'))


@app.get("/")
async def root(AnimalName: Union[str, None]="", Symptoms1:Union[str, None]="", Symptoms2:Union[str, None]="", Symptoms3:Union[str, None]="", Symptoms4:Union[str, None]="", Symptoms5:Union[str, None]=""):
    X_user = pd.DataFrame({
        "AnimalName" : [str(AnimalName)],
        "symptoms1" : [str(Symptoms1)],
        "symptoms2" : [str(Symptoms2)],
        "symptoms3" : [str(Symptoms3)],
        "symptoms4" : [str(Symptoms4)],
        "symptoms5" : [str(Symptoms5)],
    })
    st.write(X_user)
    pred = model.predict(X_user)
    return {"prediction" : pred[0]}
