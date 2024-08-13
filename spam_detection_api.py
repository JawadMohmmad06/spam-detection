import pickle
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware



app=FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"], 
)

with open('pipeline.pkl', 'rb') as file:
    loaded_clf = pickle.load(file)
class Item(BaseModel):
    spam: str
@app.post("/spamornot/")
def spamornot(item:Item)->str:
    spam=[item.spam]
    return "spam" if loaded_clf.predict(spam)[0] else "not spam"

