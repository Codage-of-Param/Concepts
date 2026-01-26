# **📌 Python Virtual Environments**

#### **Topics**: Virtual Environments in Python — what they are, how to create/use them

---

## **1️⃣ What Is a Virtual Environment?**

- **Definition**:
  - A virtual environment is a self-contained directory that contains a Python interpreter and its own set of packages. It isolates project-specific dependencies from the global Python installation.

    _OR_

  - Virtual environments (venv) are essential for managing Python projects because they create isolated environments that **prevent dependency conflicts** between projects.

- **Why use it?**:

  ✔️ **Avoid** **dependency conflicts between projects** (e.g., one project needs Django 4.x and another needs Django 3.x).

  ✔️ Keep global Python clean and stable.

  ✔️ Makes your projects **repeatable and shareable.**


## **2️⃣ How to Create a Virtual Environment**

- Step-by-Step

  1. Open your terminal or command prompt.

  2. Navigate to your project folder.

  3. Run the command:
 
      - Windows:
        ```bash
        python -m venv env
        ```

     - Mac/Linux:
       ```bash
       python3 -m venv env
       ```
       
  - (“env” is the name of the virtual environment folder — you can name it anything.)

## **3️⃣ Activate & Deactivate the Environment**

### 1. Activate:
- Windows:
  ```bash
  env\Scripts\activate
  ```

  _OR_

  ```bash
  env\Scripts\activate.bat
  ```

- Mac/Linux:
  ```bash
  source env/bin/activate
  ```
- here 'env' is your enivornment name

- After activation, your terminal prompt shows the environment name **at prefix**(e.g., (env)).

### 2. Deactivate:

- Windows/Mac/Linux:
  ```bash
  deactivate
  ```

- This returns you to in system python

## **4️⃣ Install and Manage Packages**

```bash
pip install package_name
```

- Check installed libraries

  ```bash
  pip list
  ```

## **5️⃣ Saving Dependencies (Requirements File)**  

- When collaborating or deploying, you should record all project packages:

- **Save dependencies**:
  ```bash
  pip freeze > requirements.txt
  ```

- **Install from List (on another machine)**:
  ```bash
  pip install -r requirements.txt
  ```
  - **-r** stands for **install from a file**

- **Why this matters:**
 
  ✔️ Makes your project reproducible.  

  ✔️ Ensures team members use the same packages and versions.

## 6️⃣ **Best Practices & Tips**:

✔️ Create a virtual environment **inside** your project folder.

✔️ Do *not* mix your project source code and venv folder.  

✔️ Exclude the venv folder in version control (like `.gitignore` in Git).

### Delete an old environment:

```bash
rm -r env 
```
- Where env is your environment name
