from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator
from typing import List, Dict, Optional, Annotated

class patients(BaseModel):
    
    # Step-1 : Define Schema
    name: Annotated[str, Field(max_length=100, description="Enter your name", example=['Param'])]
    age: int
    email: str
    weight: float = Field(gt=0, strict=True)
    married: bool = False # Default value is False, You can pass True/False or 1/0
    allergies: Optional[List[str]] = None 
    # You can't directly add lists for this , add module from typing import List after that you can make a list
    contact_details : Dict[str, str] #Type of key is string & value is string
    URLs : Optional[AnyUrl]
    
    @field_validator('email')
    @classmethod # Because it is a classmethod
    def email_validator(cls, value:str): # cls is class and value is email value pass by user
        
        valid = ['hdfc.com', 'icici.com', 'gmail.com'] 
        value = value.strip()
        domain_Name = value.split('@')[-1] # It splits value at @ and check the end part which is gmail.com or not 
        
        if domain_Name in valid:
            return value
        raise ValueError('Not a valid domain')# If domain_name let's say yahho.com than it returns the ValueError

    @field_validator('name')
    @classmethod
    def Upper_name(cls, value):
        return value.upper()
    
    @field_validator('age' ,mode='after') # There are 2 modes before and after by default is after, It you enter mode = after then basically converts dtype after that it goes in function and if mode = before then it does not convert dtype it directly passes the value from the variable with the same datatype 
    @classmethod
    def Validate_Age(cls, value):
        if 0<value<100:
            return value
        else:
            raise ValueError('Please, Enter valid value of age')

def insert_patient_data(patient: patients):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    print('Inserted')

def update_patient_data(patient: patients):
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    print('Updated')  
     
 
patients_info = {
        'name': 'Amit', 
        'age':'23', 
        'weight': 77.2, 
        'email': 'abc@gmail.com',
        'married' : True ,
        'allergies': ['pollen', 'dust'], 
        'contact_details': {'mail': 'abc@gmail.com'},
        'URLs': 'https://linkedin.com'
    } 
# If you write string in age variable then code gives error and if you write '23' then it auto converts in integer
# You can run optional part with removing from dictionary

patient1 = patients(**patients_info) # It's a pydantic object -> First it checks the type

insert_patient_data(patient1)
update_patient_data(patient1)

