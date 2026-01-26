# **FastAPI - Introduction**

![image.png](attachment:image.png)

## **1. What is an API? (Application Programming Interface)**

- **Definition**: 
    - A set of rules and protocols that allows different software applications to communicate with each other. 

- **Role**: 
    - Acts as a **bridge** between systems — takes a request from one application, processes it through another, and returns the response. 

- **Analogy**: 
    - Like a waiter in a restaurant — the client gives the order to the waiter (API), who communicates it to the kitchen (server) and delivers the result back to you. 

- **Purpose**:

    - Enables **integration** between systems.

    - Promotes **modularity** and reuse of components.

    - **Improves scalability** and **efficiency** of applications. 

## **2. How APIs Work?**

- **Client–Server Model:**

    - Client *sends* an *API request* to an endpoint (URL).

    - The server **processes** the request.

    - The server sends back a **response** (often in JSON).

- APIs communicate over standard web protocols such as **HTTP/HTTPS**.

## **3. Common API Concepts**

1. **Endpoint**

    - A specific URL which performs a defined action or delivers a defined response.

2. **Request and Response**

    - **Request**: Sent by client to ask for data or action.

    - **Response**: Sent back by server with the data or outcome.

3. **Types of API Communication**

    - _REST_ (Representational State Transfer) — most commonly used today

## **4. Why APIs Matter**

1. **Integration**: Connect diverse systems (mobile apps, web services, databases). 

2. **Modularity**: Let developers reuse components without rebuilding from scratch. 

3. **Scalability**: Backend functions can evolve independently. 

4. **Efficiency**: Automates data access and processes across systems.

![image.png](attachment:image.png)

## **5. Introduction to FastAPI**

1. What is ***FastAPI***?

    - A modern, high-performance ***Python framework*** to build APIs rapidly.

2. Key Features

    - _Speed_ : Built on top of Starlette and designed for high performance.

    - _Automatic Validation & Docs_ : Uses Python type hints and auto-generates docs (Swagger/OpenAPI).

    - _Asynchronous Support_ : Enables non-blocking operations for heavier workloads.

    - _Automatic Interactive Docs_ : API documentation available out of the box.

## **6. FastAPI Advantages for Machine Learning**

- Makes it **easier to deploy ML models as APIs**. 

- APIs can accept data, run predictions, and return results in production applications. 

- Enables **real-time model serving** and integration with frontends or other services.

![image.png](attachment:image.png)

## **7. Summary (Quick Points)**

1. API = Interface for software communication. 

2. FastAPI = High-performance Python framework for building APIs. 

3. FastAPI benefits include automatic docs, async support, data validation, and fast development cycle.