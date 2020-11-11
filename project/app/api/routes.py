import pandas as pd 
from fastapi import APIRouter
import json


router = APIRouter()


def bridge_csv():
    df = pd.read_csv('app/api/finalv2.csv', delimiter= ';')
    return df 


DF = bridge_csv()


def hosp_csv():
    hs = pd.read_csv('app/api/Hospitals.csv')
    return hs 


HS = hosp_csv()


@router.get("/hospital-data/")
async def bridge_data():
    result = HS.to_json(orient="records")
    return json.loads(result)


@router.get("/bridge-data/")
async def bridge_data():
    result = DF.to_json(orient="records")
    return json.loads(result)
