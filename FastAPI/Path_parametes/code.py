from fastapi import FastAPI, Path, HTTPException, Query
import json

app = FastAPI()

@app.get("/")
def hello():
    return {'message':'Patient Management System API'}

@app.get('/about')
def about():
    return {'message': 'A fully functional API to manage your patient records'}

def load_data():
    with open('patients.json', 'r') as f:
        data = json.load(f)

    return data

@app.get('/view') # Load data
def view():
    data = load_data()

    return data

@app.get('/patients/{patient_id}') # Access dynamic resources(values)
def view_patient(patient_id : str = Path(..., description='ID of the patient in DB', example="P001")): #... means patient_id is required
    data = load_data()
    
    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code=404,detail="Patient not found")

@app.get('/sort')
def sort_patients(sort_by: str = Query(..., description="Sort on the basis of height, weight and BMI", ),
                  order_is: str = Query('asc', description="sort in ascending or descending order")): #By default value is asc so if you don't write then it's also 'asc'
    
    sort_list = ['height', 'weight', 'bmi']
    
    if  sort_by not in sort_list:
        raise HTTPException(status_code=400, detail=f"Invalid fields , Select from {sort_list}") 
    
    if order_is not in ['asc', 'desc']:
        raise HTTPException(status_code=400, detail="Invalid order select between asc and desc")
    
    data = load_data()
    
    sort_order = True if order_is=='desc' else False
    
    sorted_data = sorted(data.values(), key= lambda x: x.get(sort_by, 0), reverse=sort_order)
    
    return sorted_data
