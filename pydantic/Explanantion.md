# **Pydantic**

## Why?

- ***Problem 1*** is **Type validation.**

- ***Problem 2*** is **Data validation key.**

- All are steps of pydantic:

    1. Define **pydantic class** that represents **ideal schema** of the data.

        - This includes the expected fields, their types, and any validation constraints (e.g. `gt=0` for positive number)

    2. **Instantiate the model with raw input data**(usually JSON based)

        - Pydantic automatically **validate** the data and **coerce** it into correct pytho types(if possible)

        - If the data **does not meet** the models **requirements**, Pydantic raises **`ValidationError`.**

    3. **Pass the validated model object** to functions or use it throughout your code-base     

        - This ensures that every part of your program works with **clean**, **type-safe**, and **logically valid data.**

    ```bash
    pip install pydantic # Version - 2
    ```

# **Type validation**:

## **Make optional field**

- By default all fields are required but if you want to add optional then:-

- import : 

    ```python
    from typing import Optional
    ```

- Example :

    ```python
    car_color : Optional[str] = None # Give by default value too, It is mandatory
    ```

- If i don't write the car_color variable then it is also runnable because field is optional

- You can also add default vaulues on By default variables (e.g. `wheel_brand : str = 'CEAT'`, Now, if you don't add the wheel_brand values in the dictionary then it sets By default as 'CEAT')   

# **Data validation**:

- For **email**: 

    - download package:

    ```bash
    pip install pydantic[email]
    ```

    - import

    ```python
    from pydantic import EmailStr
    ```

- For **Any url**: 

    - import

    ```python
    from pydantic import AnyUrl
    ```

- For **Field : Any Buisness logic**: 

- Field library we can do Custom **data validation, Adding metadata, Adding a default values** 

    - import

    ```python
    from pydantic import Field
    ```

    - Example

    ```python
    height : float = Field(gt=0) # It means if value is now less than zero it throws error
    ```

- We can define range too

    - Example

    ```python
    height : float = Field(gt=0, le=7) # It means if value is now less than zero it throws error
    ```

- We can add constraints for strings too

- Example: let's say your name length should be <100 character then,

    ```python
    name : str = Field(max_length=100) # If you add more than 100 characters than it gives error, same for list
    ```

- **Through `Field` we can attach metadata (Like description)**

    - import

    ```python
    from typing import Annonated # Annonated[dtype, Field()]
    from pydantic import Field
    ```

    - Example

    ```python
    weight: Annonated[float, Field(default=None, description="YOur weight", examples=[45,60])]
    ```

- If you pass any number in string format than it automaitcally converts it into a particular type, but sometimes it is harmful so we can add validation through `strict=True` in Field.  

    - Example

    ```python
    weight: Annonated[float, Field(default=None, description="YOur weight", examples=[45,60], strict=True)]
    # If you pass 56.2 then it perfectly runs but if '56.2' then it doesn't
    ```

# **feild_validator**:

- It **only vaidate the single field**

    - import

    ```python
    from pydantic import field_validator
    ```

    - Example

    ```python
    @field_validator('email') # Add field_validator in which key you want to add
    @classmethod # It is applied in class method that's why we add class method
    def email_validator(cls, value:str): # cls is class and value is email value pass by user
        
        valid = ['gmail.com'] 
        value = value.strip()
        domain_Name = value.split('@')[-1] # It splits value at @ and check the end part which is gmail.com or not 
        
        if domain_Name not in valid:
            raise ValueError('Not a valid domain')# If domain_name let's say yahho.com than it returns the ValueError
        return value
    ```
- Through cls you can add many methods from one class (Multipurpose)

#### **mode**:

    ```python
    @field_validator('age' ,mode='after')  
    @classmethod
    def Validate_Age(cls, value):
        if 0<value<100:
            return value
        else:
            raise ValueError('Please, Enter valid value of age')

    ```

- There are **2 modes before and after** 

- by default is after 

- If you enter `mode = after` then basically **converts dtype**,then **after** that it **goes in function**. 

- If `mode = before` then it **does not convert dtype** it directly passes the value from the variable with the same datatype.

- Example: 

    - If i pass `age = '23'`in above code with **`mode = after`** then it runs becuase it **first converts it into an integer type**

    - If i pass `age = '23'`in above code with **`mode = before`** then it throws error because it directly **passes the string datatype value.**

# **model_validator**:

- It is used when you want to **validate the multiple variables**

- Same mode concept as **feild_validator**.

- We pass the whole **model** instead of any particular variable

```python
from pydantic import model_field

@model_validator(mode='after')
    def validation_emergency_contact(cls,model):
        if model.age>60 and 'emergency' not in model.contact_details:
            raise ValueError('Patients older than 60 must have emergency contacts')
        return model
```

- So according to code if patient data doeesn't have **emergency** key then it raises the error and if age is less than 60 and you don't have emergency key then it also runs it it applies only for >60

# **computed_validator**:

- It simply validate by calculating model variables , this feilds does nt provide by the user

- for example i want to add bmi of patients so user can't calculate 

    - Import: 

    ```python
    from pydantic import computed_field
    ```

    ```python
    @computed_field
    @property
    def bmi(self) -> float: # we pass the instance of the class, This function name becomes your field name
        bmi = (self.weight / (self.height**2))
        return round(bmi, 2)
    ```

-  bmi is calculated through weight and height

- This function name becomes your field name

```python
print(class_name.bmi)
```

# **nested_models**:

- **Benifits:**

    - Better organization of related data (e.g. vitals, address, insurance)

    - **Reusability**: Use vitals in multiple models (e.g. patients, MedicalRecord)

    - **Redability**: Easier for developers and API consumer to understand

    - **Validation**: Nested models are validated automatically no extra work needed

    - Check code: [nested_models.py](https://github.com/Codage-of-Param/Concepts/blob/main/pydantic/nested_models.py)

# **Export in JSON and Dictionary format**

- Export in **Dictionary format**: 

    - `obj_name.model_dump()` -> it export in "dict" dtype
    
- Export in **JSON format**: 

    - `obj_name.model_dump_json()` -> it export in "str" dtype
    
- **2 parameters include and exclude** you can choose which parameters are export and which are not

- `exclude_unset = True` -> If you don't set value in dictionary then it doesnot include in exported model
