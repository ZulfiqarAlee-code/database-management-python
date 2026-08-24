# PostgreSQL Database Project with Python

A simple Python project for creating and inserting data into a **PostgreSQL database**. This project demonstrates how Python can be used to connect with PostgreSQL and perform basic database operations.

## 📁 Project Files

```text
python-database-manager/
│
├── create_database.py
├── insertdata.py
└── README.md
```

### `create_database.py`

This script connects to PostgreSQL and creates the required database/tables for the project.

### `insertdata.py`

This script connects to the PostgreSQL database and inserts data into the required tables.

## 🛠️ Technologies Used

* **Python**
* **PostgreSQL**
* **psycopg2** – Python PostgreSQL adapter
* **SQL**

## ⚙️ Requirements

Before running the project, make sure you have:

* Python 3.x installed
* PostgreSQL installed and running
* A PostgreSQL database/user configured
* `psycopg2` installed

Install the PostgreSQL Python library with:

```bash
pip install psycopg2-binary
```

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/python-database-manager.git
```

### 2. Navigate to the project directory

```bash
cd python-database-manager
```

### 3. Configure PostgreSQL

Update the PostgreSQL connection details in the Python files according to your local PostgreSQL setup.

For example:

```python
connection = psycopg2.connect(
    host="localhost",
    database="your_database",
    user="your_username",
    password="your_password"
)
```

> **Important:** Do not upload your real PostgreSQL password or other sensitive credentials to GitHub.

### 4. Create the database

Run:

```bash
python create_database.py
```

### 5. Insert the data

After the database and required tables have been created, run:

```bash
python insertdata.py
```

## 🔄 Project Workflow

```text
PostgreSQL
    │
    ▼
create_database.py
    │
    ▼
Database & Tables Created
    │
    ▼
insertdata.py
    │
    ▼
Data Inserted into PostgreSQL
```

## 🎯 Purpose

The purpose of this project is to practice:

* Connecting Python with PostgreSQL
* Creating databases and tables
* Executing SQL queries from Python
* Inserting data into PostgreSQL
* Working with database connections
* Understanding basic database automation

## 🔐 Security

Never commit database passwords, API keys, or other sensitive information to GitHub.

For a real project, consider using environment variables or a `.env` file for your PostgreSQL credentials.

## 👨‍💻 Author

**Your Name**

If you found this project useful, feel free to ⭐ the repository.
