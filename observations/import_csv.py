# https://www.youtube.com/watch?v=f3q5aM9onnc
import pymongo
import pandas as pd
import json

client = pymongo.MongoClient("mongodb://localhost:27017")

df = pd.read_csv("climateData.csv")

df.head()

df.tail()

data = df.to_dict(orient="records")

db = client["eduClimateAnalysis"]

db.climateData_climatedata.insert_many(data)
