from pydantic import BaseModel

class Address(BaseModel): # This address contains city, state, pin in address
    city: str
    state: str
    pincode: str

class patients(BaseModel):
    
    name: str
    age: int
    gender: str
    address: Address
    
     
 
Address_Dict = {
    'city': 'Rajkot',
    'state': 'Gujarat',
    'pincode': '360002'
} 

add1 = Address(**Address_Dict)

patients_dict = {
    'name': 'Amit',
    'age': 32,
    'gender': 'Male',
    'address': add1
}

patient1 = patients(**patients_dict)

print(patient1)
print(patient1.name)
print(patient1.age)
print(patient1.gender)
print(patient1.address)
print(patient1.address.pincode)

print(add1.city) # access particular item of address
