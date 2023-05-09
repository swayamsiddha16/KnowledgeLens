from fastapi import FastAPI

app = FastAPI()


@app.get("/add/{num1}/{num2}")
async def add(num1: int, num2:int):
    return {"result" : num1+num2}


@app.get("/sub/{num1}/{num2}")
async def sub(num1: int, num2:int):
    return {"result" : num1-num2}


@app.get("/multiply/{num1}/{num2}")
async def add(num1: int, num2:int):
    return {"result" : num1*num2}

@app.get("/divide/{num1}/{num2}")
async def divide(num1: int, num2: int):
    try:
        result = num1 / num2
        return {"result": result}
    except ZeroDivisionError:
        return {"error": "division by zero"}



    


