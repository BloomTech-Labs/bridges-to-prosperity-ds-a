from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from app.api import predict, viz, database

app = FastAPI(
    title='Labs28-Bridges-TeamA',
    description='Redeployment test',
    version='0.1',
    docs_url='/',
)

app.include_router(predict.router)
app.include_router(viz.router)
app.include_router(database.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)


# @app.get("/predict")
# '''
# Any of the data can be used, but our guess is that Estimated Span, Height Differential 
# Between Banks, Created By, and Flag for Rejection are likely to be the most reliable predictors. 
# '''
# def predict():
#     return

# @app.get(/hospital)
# def nearest_hospital(lat, long):
#     return name of hospital, distance, lat/long of hospital

# @app.get(/bridges)
# def bridges(lat, long):
#     return info


if __name__ == '__main__':
    uvicorn.run(app)
