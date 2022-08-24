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

@app.get("/api/paycheck/")
def getAll():
    res = model_pay.getAll()
    return res if res else None

@app.post("/api/paycheck/")
async def register(item : InsertType):
    return model_pay.register(
        year = item.year,
        month = item.month,
        income1 = item.income1,
        income2 = item.income2
    )

@app.put("/api/paycheck/update")
async def update(item : InsertType):
    return model_pay.update(
        year = item.year,
        month = item.month,
        income1 = item.income1,
        income2 = item.income2
    )

@app.post("/api/paycheck/delete")
async def delete(item : InsertType):
    return model_pay.delete(
        year = item.year,
        month = item.month,
    )