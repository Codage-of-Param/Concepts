from pydantic import BaseModel, computed_field
from typing import List, Dict

class patients(BaseModel):
    
    name: str
    age: int
    email: str
    weight: float 
    height: float
    married: bool 
    allergies: List[str]
    contact_details : Dict[str, str] 
    
    @computed_field
    @property
    def bmi(self) -> float: # we pass the instance of the class, This function name becomes your field name
        bmi = (self.weight / (self.height**2))
        return round(bmi, 2)

def insert_patient_data(patient: patients):
    print('Name ',patient.name)
    print('Age ',patient.age)
    print('Weight ',patient.weight)
    print('Height ',patient.height)
    print('BMI ',patient.bmi)
    print('Inserted')
     
 
patients_info = {
        'name': 'Amit', 
        'age':89, 
        'weight': 77.2, # in kg
        'height': 1.2, # in meters
        'email': 'abc@gmail.com',
        'married' : True ,
        'allergies': ['pollen', 'dust'], 
        'contact_details': {'mail': 'abc@gmail.com', 'emergency': '123232'} 
    } 
patient1 = patients(**patients_info) # It's a pydantic object -> First it checks the type

insert_patient_data(patient1)

