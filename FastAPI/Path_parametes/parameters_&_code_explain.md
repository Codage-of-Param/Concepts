# 🔎 **Parameters**:

- Adding route `view_patient()`, We pass patient_id in it and load data after that check the patient_id is in the database or not, if yes then so it else return message

- Visit `/docs` endpoint after `view_patient()`, It automatically adds new routes in docs file.

- In `/docs` file you see all routes and in `/patients/{patient_id}` :

<img width="1308" height="415" alt="Screenshot 2026-01-28 190650" src="https://github.com/user-attachments/assets/71268065-ac72-4c23-80b1-6099d00b1b8b" />

- if clients are seeing through the docs then he/she can't understand the which values put in the textfield, and of which type?

- we can **add description and example** and many more from `Path()` function.

## **`Path()` function:**

- `Path()` function in FastAPI is used to provide **metadata, validations, rules, and documentation** hints for path parameters in your API endpoints.

- like **title, description, example, ge(greater then equal), gt, le, lt, Min_length, Max_length, regex**

    - **Library** : 

        ```python
        from fastapi import Path
        ``` 

- Add `Path()` function in argument 

- for `/docs` endpoint 

## 🔎 **`HTTPException`**:

- It is a special built-in exception in FastAPI used to **return custom HTTP error respones** when something goes wrong in your API. 

- Instead of placing a normal json message or crashing the server, you gracefully **raise the error** with:

- a proper HTTP status code (like 404, 403, 400, etc)

- a custom error message

- (optional) extra header message

    - **Library** : 
    
        ```python
        from fastapi import HTTPException
        ```
- you can raise the error

## 🔎 **`Query()` parameter**:

- It is a optional key value pairs appended to the end of the URL used to **past additional data** to the server in an HTTP request.

- They are typically employed for **operations like filtering, sorting, pagination, searching without altering the endpoint path itself**.

- `?` is the state of the query parameters.

- Each parameters is the `key=value` pair

- Multiple parameters are separated by `&` 

    - **Example**: 
    
        - `/patients?city=Rajkot&sort_by=age`
    
        - In our case `city=Rajkot` is an query parameter for **filtering**
    
        - `sort_by=age` is an query parameter for **sorting**

- `Query()` is an utility function provided by FastAPI to **declare, validate and document the query parameters** in your API endpoints.

- It allows you to:

    1. Set **default values**

    2. Enforce **validation rules**
    
    3. Add meta data like **Description, example, title**
