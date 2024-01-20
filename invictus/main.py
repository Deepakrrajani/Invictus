# from sqlalchemy import create_engine, Column, Integer, String
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import Session
from datetime import date
import json
#from sqlalchemy.engine import URL
from fastapi import FastAPI ,Form,Request
from fastapi.responses import JSONResponse
from typing import List
import uvicorn
from pydantic import BaseModel
from typing import Optional
import joblib
import pandas as pd
model=joblib.load('Classify1.joblib')
app=FastAPI()
# url = URL.create(
#     drivername="mysql",
#     username="root",
#     password="Deepak",
#     host="192.168.10.122",
#     database="user",
#     port=3306
# )

# Define the SQLAlchemy declarative base
# Base = declarative_base()
# class user(Base):
#     __tablename__ = 'user'
#     user_id = Column(Integer, primary_key=True)
#     username = Column(String(50), nullable=False)
#     password = Column(String(10), nullable=False)



# Define the Product model



# Create an SQLite database in memory for demonstration purposes
# engine = create_engine(url)
@app.post('/classify')
def classify(request:Request,med:int=Form(...),fed:int=Form(...),ss:int=Form(...),fs:int=Form(...)):


    data=[[med,fed,ss,fs]]
    columns = ['Medu', 'Fedu', 'schoolsup', 'famsup']

# Create a DataFrame
    df = pd.DataFrame(data, columns=columns)

    pred=model.predict(data)
    if pred==[0]:
        p='Student is not underprivileged'
    else :
        p='Student is underpreviliged'
    ot=json.dumps(p)
    return JSONResponse(content=ot)
   

                







if __name__ == "__main__":
   uvicorn.run("main:app", host="127.0.0.1", port=8221, reload=True)
