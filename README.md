\# 📝 Todo API with Authentication (FastAPI)



A RESTful \*\*Todo Management API\*\* built using \*\*FastAPI\*\*, \*\*SQLAlchemy\*\*, and \*\*MySQL\*\*, featuring \*\*JWT authentication\*\*, \*\*user-specific todos\*\*, \*\*pagination\*\*, \*\*search\*\*, and \*\*sorting\*\*.



This project is designed to help understand \*\*real-world backend development concepts\*\* and can be reused as a base for future projects.



---



\## 🚀 Features



\- 🔐 User Registration \& Login (JWT Authentication)

\- 🧑 User-specific Todos (Authorization)

\- ➕ Create Todo

\- 📄 Get Todos (Pagination, Search, Sorting)

\- ✏️ Update Todo

\- ❌ Delete Todo

\- 🗄️ MySQL Database using SQLAlchemy ORM

\- 📦 Clean project structure with routers \& schemas



---



\## 🛠️ Tech Stack



\- \*\*Backend Framework\*\*: FastAPI

\- \*\*Database\*\*: MySQL

\- \*\*ORM\*\*: SQLAlchemy

\- \*\*Authentication\*\*: JWT (JSON Web Tokens)

\- \*\*Password Hashing\*\*: Passlib (bcrypt)

\- \*\*Validation\*\*: Pydantic

\- \*\*Server\*\*: Uvicorn



---



\## 📁 Project Structure



todo\_api/

│

├── main.py # Application entry point

├── database.py # Database connection \& session

├── models.py # SQLAlchemy models

├── schemas.py # Pydantic schemas

├── auth.py # Password hashing \& JWT logic

├── dependencies.py # Auth dependency (get\_current\_user)

│

├── routers/

│ ├── user.py # Auth routes (register, login)

│ └── todo.py # Todo CRUD routes

│

├── venv/ # Virtual environment (ignored)

└── README.md





---



\## ⚙️ Setup Instructions



\### 1️⃣ Clone the Repository



```bash

git clone https://github.com/jaiprathap26/todo-api-fastapi.git

cd todo-api-fastapi



2️⃣ Create Virtual Environment



python -m venv venv



Activate it:



Windows



venv\\Scripts\\activate





Mac/Linux



source venv/bin/activate



3️⃣ Install Dependencies

pip install fastapi uvicorn sqlalchemy pymysql passlib\[bcrypt] python-jose pydantic slowapi



4️⃣ Configure Database



Make sure MySQL is running, then create database:



CREATE DATABASE todo\_api;



Update database.py:



DATABASE\_URL = "mysql+pymysql://root:root@localhost:3306/todo\_api"



5️⃣ Run the Application

uvicorn main:app --reload





Server will run at:



http://127.0.0.1:8000





📖 API Documentation (Swagger UI)



FastAPI automatically provides API docs:



👉 Swagger UI



http://127.0.0.1:8000/docs





👉 ReDoc



http://127.0.0.1:8000/redoc



🔐 Authentication Flow



Register



POST /register



Login



POST /login



Copy the returned JWT token



In Swagger → Click Authorize



Paste token as:



Bearer <your\_token\_here>



📌 API Endpoints

👤 Auth Routes

Method	Endpoint	Description

POST	/register	Register new user

POST	/login	Login user

POST	/refresh	Refresh JWT token

📝 Todo Routes (Protected)

Method	Endpoint	Description

POST	/todos	Create a todo

GET	/todos	Get todos (pagination, search, sort)

PUT	/todos/{id}	Update todo

DELETE	/todos/{id}	Delete todo

🔎 Query Parameters (GET /todos)

Parameter	Description

page	Page number

limit	Items per page

search	Search by title

sort	asc / desc



Example:



/todos?page=1\&limit=10\&search=test\&sort=asc



🔒 Security Notes



Passwords are hashed using bcrypt



JWT tokens are signed \& time-limited



Users can access only their own todos



🎯 Learning Outcomes



This project helps understand:



FastAPI architecture



SQLAlchemy ORM relationships



JWT authentication \& authorization



Dependency injection



Pagination \& filtering



Real-world API error handling 



⭐ Future Improvements



Environment variables (.env)



Role-based access control



Refresh token storage



Unit testing



Docker support




https://roadmap.sh/projects/todo-list-api

