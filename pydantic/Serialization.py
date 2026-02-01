# Exporting model in JSON and dictionary format
'''
Export in Dictionary format: 

    obj_name.model_dump() it export in "dict" dtype
    
Export in JSON format: 

    obj_name.model_dump_json() it export in "str" dtype
    
- 2 parameters include and exclude you can choose which parameters are export and which are not

- `exclude_unset = True` -> If you don't set value in dictionary then it doesnot include in exported model
'''

from pydantic import BaseModel, model_validator
from typing import List, Dict

class patients(BaseModel):
    
    name: str
    age: int
    email: str
    weight: float 
    married: bool = False
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
    print('Inserted\n\n')
     
 
patients_info = {
        'name': 'Amit', 
        'age':89, 
        'weight': 77.2, 
        'email': 'abc@gmail.com',
        # 'married' : True , # remove for exclude_unset for results
        'allergies': ['pollen', 'dust'], 
        'contact_details': {'mail': 'abc@gmail.com', 'emergency': '123232'} 
    } 
patient1 = patients(**patients_info) # It's a pydantic object -> First it checks the type

insert_patient_data(patient1)

exported_model = patient1.model_dump()
print("Exported in dict format : \n",exported_model)
print(type(exported_model), "\n")

exported_model2 = patient1.model_dump_json()
print("Exported in josn format : \n",exported_model2)
print(type(exported_model2), "\n")

##### include and exclude

exported_model3 = patient1.model_dump(include=['name', 'contact_details']) # It exports only name and age
print("Exported in dict format : \n",exported_model3)
print(type(exported_model3), "\n")

exported_model4 = patient1.model_dump(exclude=['gender', 'email']) # It removes gender & mail from patients
print("Exported in dict format : \n",exported_model4)
print(type(exported_model4), "\n")

exported_model5 = patient1.model_dump(exclude={'contact_details': 'emergency'}) # It removes emergency
print("Exported in dict format : \n",exported_model5)
print(type(exported_model5), "\n")

exported_model6 = patient1.model_dump(exclude_unset=True)
print("Exported in dict format : \n",exported_model6)
print(type(exported_model6), "\n")