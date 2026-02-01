from pydantic import BaseModel, model_validator
from typing import List, Dict

class patients(BaseModel):
    
    name: str
    age: int
    email: str
    weight: float 
    married: bool 
    allergies: List[str]
    contact_details : Dict[str, str] 
    
    @model_validator(mode='after')
    def validation_emergency_contact(cls,model):
        if model.age>60 and 'emergency' not in model.contact_details:
            raise ValueError('Patients older than 60 must have emergency contacts')
        return model

def insert_patient_data(patient: patients):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    print('Inserted')
     
 
patients_info = {
        'name': 'Amit', 
        'age':89, 
        'weight': 77.2, 
        'email': 'abc@gmail.com',
        'married' : True ,
        'allergies': ['pollen', 'dust'], 
        'contact_details': {'mail': 'abc@gmail.com', 'emergency': '123232'} 
    } 
patient1 = patients(**patients_info) # It's a pydantic object -> First it checks the type

insert_patient_data(patient1)

