from fastapi import FastAPI, HTTPException

app = FastAPI()


@app.post("/calc/add")
async def add(x: float, y: float):
    return {"result": x + y}


@app.post("/calc/subtract")
async def subtract(x: float, y: float):
    return {"result": x - y}


@app.post("/calc/multiply")
async def multiply(x: float, y: float):
    return {"result": x * y}


@app.post("/calc/divide")
async def divide(x: float, y: float):
    if y == 0:
        raise HTTPException(status_code=400, detail="Cannot divide by zero")
    return {"result": x / y}
