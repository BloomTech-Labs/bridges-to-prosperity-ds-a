import logging
import random
import pickle

from fastapi import APIRouter
import pandas as pd
from pydantic import BaseModel, Field, validator

log = logging.getLogger(__name__)
router = APIRouter()

df = pd.read_csv('app/api/FinalCleanedData.csv', delimiter= ';')

class Item(BaseModel):
    """Use this data model to parse the request body JSON."""

    
    Project_Code: str = Field(..., example='1007387')

    # def to_df(self):
    #     """Convert pydantic object to pandas dataframe with 1 row."""
    #     return pd.DataFrame([dict(self)])

    # @validator('x1')
    # def x1_must_be_positive(cls, value):
    #     """Validate that x1 is a positive number."""
    #     assert value > 0, f'x1 == {value}, must be > 0'
    #     return value


@router.post('/predict')
async def predict(item: Item):
    """
    Make random baseline predictions for classification problem 🔮

    ### Request Body
    - Bridge Opportunity: Project Code

    ### Response
    - Prediction of wether the site will be Reviewed and Approved by a Senior Engineer for construction.
    """

    X_new = item.Project_Code
    mask = df['Bridge Opportunity: Project Code'] == X_new
    prediction = df[mask]
    indicator = prediction.iloc[0]['Good Site']
    if indicator == 1.0:
        return "Might be approved by a Senior Engineer"
    else:
        return "Likely to be rejected by Senior Engineer"
