# **Workflow of API**

![alt text](<Screenshot 2026-01-26 184921.png>)

```bash
A client sends data 
    ⬇️
The web server receives it 
    ⬇️
SGI passes it to API code 
    ⬇️
API processes it 
    ⬇️
response is sent back.
```

# **Step-by-Step Workflow**

### **1️⃣ Client Sends a Request**

- A client (browser, mobile app, Postman, etc.) sends an **HTTP POST request.**

- URL: `/predict`

- Data is sent in JSON format:

    ```json
    {
    "feature1": 5.2,
    "feature2": 3.1
    }
    ```

- Think of this as:

> “Here is some data. Please calculate something for me.”

### **2️⃣ Web Server Receives the Request**

- The **Web Server** (e.g., Uvicorn, Gunicorn) listens for incoming requests.

- It does _not_ process business logic.

- Its job is only:

    - Accept the request

    - Pass it forward correctly

- Analogy:

> The receptionist receives your form but doesn’t make decisions.

### **3️⃣ SGI Acts as a Bridge**

- ***SGI (Server Gateway Interface)*** connects the web server and API code.

- A generalized concept describing how web servers and Python applications communicate.

- The two main implementations are:

    1. **WSGI (Web Server Gateway Interface)**: 
        
        - A **synchronous** standard used by frameworks like **Flask and Django** (pre-3.0).<br>
        - It handles standard HTTP requests but lacks support for real-time features.<br>
        - **Synchronus means** jab tak ek request complete nahi hoti tab tak dusri request hold par rahegi<br>
        - Use production servers like **Gunicorn** or **uWSGI**.

    2. **ASGI (Asynchronous Server Gateway Interface)**: 
    
    - The modern successor to WSGI, supporting asynchronous operations, WebSockets, HTTP/2, and high concurrency.   <br>
    - Frameworks like **FastAPI and Django** 3.0+ use ASGI for real-time and scalable applications<br>
    - **Asynchronus means** we can send multiple request at same time<br>
    - Use production servers like **Uvicorn**.

![WSGI,ASGI](<Screenshot 2026-01-26 184958.png>)

- SGI converts the raw HTTP request into a structured format (API does know the http language that's why sgi converts in pyton language):

    - request.method → "POST"

    - request.url → "/predict"

    - request.json() → {"feature1": 5.2, "feature2": 3.1}

- Analogy:

> The receptionist translates your form into a format the manager understands.

### **4️⃣ API Code Processes the Data**

- The **API code**:

    - Reads input values (`feature1`, `feature2`)

    - Runs logic or a machine learning model

    - Computes a result

- Example result:

    ```python
    {
        "prediction": 8.3
    }
    ```

- Analogy:

> The manager analyzes the form and makes a decision.

### **5️⃣ Response Is Sent Back**

- API returns a JSON response with status:

    ```pgsql
    HTTP/1.1 200 OK
    Content-Type: application/json
    ```
- this travels ***back through*** **SGI → Web Server → Client**

- Analogy:

> The decision is sent back to you through the receptionist.

### **? Why This Design Is Important**

- **Separation of concerns**

    - Web server handles traffic

    - API handles logic

- **Scalable**

    - Multiple requests handled efficiently

- **Standardized**

    - Works the same for web apps, mobile apps, ML APIs