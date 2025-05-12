from fastapi import FastAPI
from pydantic import BaseModel
from app.extractor import hybrid_extract

# Load city list
with open("data/citilist.txt") as f:
    cities = [line.strip() for line in f]

app = FastAPI()

# Define request body schema
class FlightRequest(BaseModel):
    text: str

@app.post("/extract")
async def extract_flight_info(request: FlightRequest):
    result = hybrid_extract(request.text)
    return result


import uvicorn

if __name__ == "__main__":
    uvicorn.run("api.main:app", host="0.0.0.0", port=8000)
