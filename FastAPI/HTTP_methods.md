# 📌 **HTTP Methods in FastAPI**

## 🚀 **Introduction**

FastAPI is a modern, **high-performance web framework** for building APIs with Python 3.7+ using standard **Python type hints**. One of its key strengths is clean and intuitive routing for different HTTP methods.

---

## 📍 **HTTP Methods Overview**

FastAPI supports all the common HTTP request methods:

| Method   | Purpose                      |
| -------- | ---------------------------- |
| `GET`    | Retrieve/read data           |
| `POST`   | Create new data              |
| `PUT`    | Update/replace existing data |
| `PATCH`  | Partially update data        |
| `DELETE` | Remove data                  |

---

## 🧠 **Setting Up FastAPI**

(DO in venv)

1. Install dependencies:

    ```bash
    pip install fastapi uvicorn
    ```

2. Create basic structure:

    ```python
    from fastapi import FastAPI
    app = FastAPI()
    ```

3. Run server:

    ```bash
    uvicorn main:app --reload
    ```

---

## 📌 **1. GET Method**

**Used to fetch or retrieve data from the server.**

```python
@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI!"}
```

**With path parameter:**

```python
@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}
```

## 📌 **JSON Validation & Pydantic**

FastAPI uses Pydantic models to validate request data:

* Required fields
* Data types enforcement
* Automatic error messages

---

## 📌 **Summary of HTTP Methods**

```plaintext
GET     → Read
POST    → Create
PUT     → Replace/Update
PATCH   → Partial Update
DELETE  → Delete
```

---

## 🧪 **Testing the API**

Use *Swagger UI* (interactive docs):

👉 Visit: `http://127.0.0.1:8000/docs`

FastAPI auto-generates documentation from routes and Pydantic schemas.

---