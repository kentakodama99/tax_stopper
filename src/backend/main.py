from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from sql import modelPay
from pydantic import BaseModel
model_pay = modelPay()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)


class InsertType(BaseModel):
    year : int
    month : int
    income1 : int = 0
    income2 : int = 0

@app.get("/paycheck/")
def getAll():
    return model_pay.getAll()

@app.post("/paycheck/")
async def register(item : InsertType):
    print(item)
    return model_pay.register(
        year = item.year,
        month = item.month,
        income1 = item.income1,
        income2 = item.income2
    )