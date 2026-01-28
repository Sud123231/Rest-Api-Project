# Flask REST API – Course, Student & Enrollment Management

A simple **Flask RESTful API** that manages **Courses**, **Students**, and **Enrollments** using **Flask-RESTful** and **Flask-SQLAlchemy**. This project demonstrates core REST principles, CRUD operations, relational data handling, and proper HTTP status codes.

---

## 🚀 Features

* RESTful API design using Flask-RESTful
* CRUD operations for:

  * Courses
  * Students
  * Enrollments (Student–Course relationship)
* SQLite database using SQLAlchemy ORM
* CORS enabled for frontend integration
* Clear separation of resources
* JSON-based request and response handling

---

## 🛠 Tech Stack

* **Python** 3.x
* **Flask**
* **Flask-RESTful**
* **Flask-SQLAlchemy**
* **SQLite**
* **Flask-CORS**

---

## 📂 Project Structure

```
flask_restful/
│── app.py
│── requirements.txt
│── README.md
│── venv/          # ignored
│── instance/      # ignored
```

---

## ⚙️ Setup & Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/Sud123231/Rest-Api-Project.git
cd Rest-Api-Project
```

### 2️⃣ Create and activate virtual environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
# source venv/bin/activate  # Linux / macOS
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the application

```bash
python app.py
```

The server will start at:

```
http://127.0.0.1:5000/
```

---

## 🗄 Database

* Database: **SQLite**
* File: `api_database.sqlite3`
* Tables are automatically created on first run using:

  ```python
  db.create_all()
  ```

---

## 📘 API Documentation (OpenAPI)

This project follows the REST API design and request/response conventions described in the official MAD1 OpenAPI documentation:

🔗 **API Spec Reference:** https://onlinedegree.gitlab.io/mad1/week_six_openapi/

The endpoints, payload structure, and HTTP status codes in this project are aligned with this specification.

---

## 📌 API Endpoints

### 🔹 Course APIs

| Method | Endpoint                  | Description       |
| ------ | ------------------------- | ----------------- |
| GET    | `/api/course/<course_id>` | Get course by ID  |
| POST   | `/api/course`             | Create new course |
| PUT    | `/api/course/<course_id>` | Update course     |
| DELETE | `/api/course/<course_id>` | Delete course     |

#### Sample Request (POST)

```json
{
  "course_name": "Data Science",
  "course_code": "DS101",
  "course_description": "Intro to Data Science"
}
```

---

### 🔹 Student APIs

| Method | Endpoint                    | Description        |
| ------ | --------------------------- | ------------------ |
| GET    | `/api/student/<student_id>` | Get student by ID  |
| POST   | `/api/student`              | Create new student |
| PUT    | `/api/student/<student_id>` | Update student     |
| DELETE | `/api/student/<student_id>` | Delete student     |

#### Sample Request (POST)

```json
{
  "first_name": "John",
  "last_name": "Doe",
  "roll_number": "CS001"
}
```

---

### 🔹 Enrollment APIs

| Method | Endpoint                                       | Description                      |
| ------ | ---------------------------------------------- | -------------------------------- |
| GET    | `/api/student/<student_id>/course`             | Get all enrollments of a student |
| POST   | `/api/student/<student_id>/course`             | Enroll student into course       |
| DELETE | `/api/student/<student_id>/course/<course_id>` | Remove enrollment                |

#### Sample Request (POST)

```json
{
  "course_id": 1
}
```

---

## ❗ Error Handling

* `400` – Bad Request (missing or invalid fields)
* `404` – Resource not found
* `409` – Conflict (duplicate entries)
* Consistent JSON error responses

---

## 🧠 What This Project Demonstrates

* RESTful design principles
* Proper HTTP status codes
* One-to-many relationships using SQLAlchemy
* Clean API resource design
* Backend-ready structure for frontend integration

---
# Flask REST API – Course, Student & Enrollment Management

A simple **Flask RESTful API** that manages **Courses**, **Students**, and **Enrollments** using **Flask-RESTful** and **Flask-SQLAlchemy**. This project demonstrates core REST principles, CRUD operations, relational data handling, and proper HTTP status codes.

---

## 🚀 Features

* RESTful API design using Flask-RESTful
* CRUD operations for:

  * Courses
  * Students
  * Enrollments (Student–Course relationship)
* SQLite database using SQLAlchemy ORM
* CORS enabled for frontend integration
* Clear separation of resources
* JSON-based request and response handling

---

## 🛠 Tech Stack

* **Python** 3.x
* **Flask**
* **Flask-RESTful**
* **Flask-SQLAlchemy**
* **SQLite**
* **Flask-CORS**

---

## 📂 Project Structure

```
flask_restful/
│── app.py
│── requirements.txt
│── README.md
│── venv/          # ignored
│── instance/      # ignored
```

---

## ⚙️ Setup & Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/Sud123231/Rest-Api-Project.git
cd Rest-Api-Project
```

### 2️⃣ Create and activate virtual environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
# source venv/bin/activate  # Linux / macOS
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the application

```bash
python app.py
```

The server will start at:

```
http://127.0.0.1:5000/
```

---

## 🗄 Database

* Database: **SQLite**
* File: `api_database.sqlite3`
* Tables are automatically created on first run using:

  ```python
  db.create_all()
  ```

---

## 📘 API Documentation (OpenAPI)

This project follows the REST API design and request/response conventions described in the official MAD1 OpenAPI documentation:

🔗 **API Spec Reference:** [https://onlinedegree.gitlab.io/mad1/week_six_openapi/](https://onlinedegree.gitlab.io/mad1/week_six_openapi/)

The endpoints, payload structure, and HTTP status codes in this project are aligned with this specification.

---

## 📌 API Endpoints

### 🔹 Course APIs

| Method | Endpoint                  | Description       |
| ------ | ------------------------- | ----------------- |
| GET    | `/api/course/<course_id>` | Get course by ID  |
| POST   | `/api/course`             | Create new course |
| PUT    | `/api/course/<course_id>` | Update course     |
| DELETE | `/api/course/<course_id>` | Delete course     |

#### Sample Request (POST)

```json
{
  "course_name": "Data Science",
  "course_code": "DS101",
  "course_description": "Intro to Data Science"
}
```

---

### 🔹 Student APIs

| Method | Endpoint                    | Description        |
| ------ | --------------------------- | ------------------ |
| GET    | `/api/student/<student_id>` | Get student by ID  |
| POST   | `/api/student`              | Create new student |
| PUT    | `/api/student/<student_id>` | Update student     |
| DELETE | `/api/student/<student_id>` | Delete student     |

#### Sample Request (POST)

```json
{
  "first_name": "John",
  "last_name": "Doe",
  "roll_number": "CS001"
}
```

---

### 🔹 Enrollment APIs

| Method | Endpoint                                       | Description                      |
| ------ | ---------------------------------------------- | -------------------------------- |
| GET    | `/api/student/<student_id>/course`             | Get all enrollments of a student |
| POST   | `/api/student/<student_id>/course`             | Enroll student into course       |
| DELETE | `/api/student/<student_id>/course/<course_id>` | Remove enrollment                |

#### Sample Request (POST)

```json
{
  "course_id": 1
}
```

---

## ❗ Error Handling

* `400` – Bad Request (missing or invalid fields)
* `404` – Resource not found
* `409` – Conflict (duplicate entries)
* Consistent JSON error responses

---

## 🧠 What This Project Demonstrates

* RESTful design principles
* Proper HTTP status codes
* One-to-many relationships using SQLAlchemy
* Clean API resource design
* Backend-ready structure for frontend integration

---

## 👤 Author

**Sudhir**
IIT Madras BS – Data Science

---

## 📜 License

This project is for learning and demonstration purposes.

