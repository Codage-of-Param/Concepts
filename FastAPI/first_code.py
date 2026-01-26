from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def intro():
    return {"Messsage": "Welcome to FastAPI World!"}

@app.get('/about')
def about():
    return {"Message": "FastAPI is faster than Flask"}

'''
- How to run?

    - Make a venv
    - pip install uvicorn fasapi pydantic (If not installed)
    - uvicorn main:app --reload # run the code, put your file name inplace of main
        => we use --reload because if we change in code then it automatically reload it without refreshing on browser
'''