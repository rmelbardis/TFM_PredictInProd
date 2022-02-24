from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import numpy as np
import pandas as pd
import joblib

from api.utils import convert_to_UTC
from TaxiFareModel import params

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

@app.get("/")
def index():
    return {"greeting": "Hello world"}

@app.get("/predict")
def predict(
    pickup_datetime,
    pickup_longitude,
    pickup_latitude,
    dropoff_longitude,
    dropoff_latitude,
    passenger_count):

    #create dataframe
    X_pred = pd.DataFrame()

    # objects
    X_pred['key'] = pd.Series('2021-06-11 17:00:00').astype(np.dtype('object'))
    X_pred["pickup_datetime"] = pd.Series(pickup_datetime).apply(convert_to_UTC)

    # floats
    coord_dict = {
        "pickup_longitude": pickup_longitude,
        "pickup_latitude": pickup_latitude,
        "dropoff_longitude": dropoff_longitude,
        "dropoff_latitude": dropoff_latitude
        }
    for k, v in coord_dict.items():
        X_pred[k] = pd.Series(v).astype(np.dtype('float64'))

    # integer
    X_pred["passenger_count"] = pd.Series(passenger_count).astype(np.dtype('int64'))

    pipeline = joblib.load(params.PATH_TO_LOCAL_MODEL)
    y_pred = pipeline.predict(X_pred)

    return {
        "fare": y_pred[0]
        }
