from fastapi import FastAPI, Path, HTTPException, Query
from fastapi.responses import JSONResponse
from pydantic import Field, computed_field
from typing import Annotated, Literal, Optional
import json
from pydantic import BaseModel

app = FastAPI()

# ==========================================PYDANTIC MODEL===============================================
class Patient(BaseModel):
    id: Annotated[str, Field(..., description="Patient ID : ", examples=['P001', 'P002'])]
    name: Annotated[str, Field(..., description="Name of the patient : ")]
    city: Annotated[str, Field(..., description="City where patient living : ")]
    age: Annotated[int, Field(..., description="Patient age : ", gt=0, lt=120)]
    gender: Annotated[Literal['Male','Female','Others'], Field(..., description="Gender of the patient : ")]
    height: Annotated[float, Field(..., description="Height of the patient (meters): ", gt=0)]
    weight: Annotated[float, Field(..., description="Weight of the patient (Kgs): ", gt=0)]


    @computed_field
    @property
    def bmi(self) -> float:
        bmi =  round(self.weight/(self.height**2),2)
        return bmi
    
    @computed_field
    @property
    def verdict(self) -> str:
        if self.bmi < 18.5: return 'Underweight'
        elif self.bmi < 30: return 'Normal'
        else: return 'Obese'
        
# ==========================================UTILITY FUNCTIONS===============================================   
def load_data():
    with open('patients.json', 'r') as f:
        data = json.load(f)

    return data

def save_data(data):
    with open('patients.json', 'w') as f:
        json.dump(data,f)
  
# ==========================================END POINTS===============================================       
@app.get("/")
def hello():
    return {'message':'Patient Management System API'}

@app.get('/about')
def about():
    return {'message': 'A fully functional API to manage your patient records'}


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

@app.post('/create')
def create_patient(patient : Patient): #patient is pydantic object
    
    # Load existing data
    data = load_data()
    
    # check if the patient already exists
    if patient.id in data:
        return HTTPException(status_code=400, detail="Already exist!")
    
    # Add new patient to the database so first convert in into dict format add it and after save in json format
    data[patient.id] = patient.model_dump(exclude=['id']) # exclude id because in our format id is a key of patients.json
    
    # Save into json format
    save_data(data)
    
    return JSONResponse(status_code=201, content = {'message': "Patient is added successfully"})

# ==========================================UPDATED PYDANTIC MODEL===============================================
class Patient_Updated(BaseModel):
    
    name: Annotated[Optional[str], Field( description="Name of the patient : ", default=None)]
    city: Annotated[Optional[str], Field( description="City where patient living : ", default=None)]
    age: Annotated[Optional[int], Field( description="Patient age : ", gt=0, lt=120, default=None)]
    gender: Annotated[Optional[Literal['Male','Female','Others']], Field( description="Gender of the patient : ", default=None)]
    height: Annotated[Optional[float], Field( description="Height of the patient (meters): ", gt=0, default=None)]
    weight: Annotated[Optional[float], Field( description="Weight of the patient (Kgs): ", gt=0, default=None)]
    
@app.put('/edit/{patient_id}')
def update_patient(patient_id: str, patient_update: Patient_Updated): # a new pydantic object
    
    data = load_data()
    
    if patient_id not in data:
        raise HTTPException(status_code=404, detail="Patient not found")
    
    # First extract existing patient info
    
    existing_patient_info = data[patient_id]
    
    updated_patient_info = patient_update.model_dump(exclude_unset=True) # For update the values, we first convert it into dict
    
    for key,values in updated_patient_info.items():
        existing_patient_info[key] = values # Change in existing field and iterate loop in updated field
        
    # Now existing info is in dictionary format converts in pydantic object but now verdict and bmi has changed because of changed value of weight 
    
    existing_patient_info['id'] = patient_id
    patient_pydantic_obj = Patient(**existing_patient_info) 
    # we make old pydantic object of new info because value chaged so computed field values also changed that's why we make it
    
    # Now converts this obj into dict format -> simply dump it
    patient_pydantic_obj.model_dump(exclude='id')
    
    # add this dict to data
    data[patient_id] = existing_patient_info
    
    # save the data
    save_data(data)
    
    return JSONResponse(status_code=200, content={'Messgae':'Message updated'})

@app.delete('/delete/{patient_id}')
def delete_patient(patient_id: str):
    
    data = load_data()
    
    if patient_id not in data:
        raise HTTPException(status_code=404, detail="Patient not found")
    
    del data[patient_id]
    
    return JSONResponse(status_code=200, content={'Messgae':'Patient Deleted Successfully'})
    