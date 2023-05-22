from fastapi import FastAPI

app = FastAPI()

@app.post("/add/{num1}/{num2}")
async def add(num1: int, num2: int):
    return {"result": num1 + num2}


@app.post("/sub/{num1}/{num2}")
async def add(num1: int, num2: int):
    return {"result": num1 - num2}
    

@app.post("/multiply/{num1}/{num2}")
async def add(num1: int, num2: int):
    return {"result": num1 * num2}
    
    
@app.post("/divide/{num1}/{num2}")
async def add(num1: int, num2: int):
    try:
        result = num1 / num2
        return {"result": result}
    except ZeroDivisionError:
        return   {"error": "division by zero"}
    
