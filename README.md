# PostgreSQL Database Project with Python

A simple Python project for creating and inserting data into a **PostgreSQL database** using **SQLAlchemy** and **psycopg2**.

This project demonstrates how Python can connect to PostgreSQL, create database tables, and insert data.

## 📁 Project Files

```text
python-database-manager/
│
├── create_database.py
├── insertdata.py
└── README.md
```

### `create_database.py`

Creates the required tables and database structure using Python, SQLAlchemy, and PostgreSQL.

### `insertdata.py`

Inserts the required data into the PostgreSQL tables.

## 🛠️ Technologies Used

* Python
* PostgreSQL
* SQLAlchemy
* psycopg2
* SQL

## ⚙️ Installation

Make sure you have installed:

* Python 3.x
* PostgreSQL
* PowerShell
* pip

Install the required Python packages:

```powershell
pip install sqlalchemy psycopg2-binary
```

## 🔗 Database Configuration

The project uses the following PostgreSQL connection URL:

```python
DATABASE_URL = "postgresql+psycopg2://postgres:postgres@localhost:5432/urban_basket_python"
```

Connection details:

| Setting       | Value                 |
| ------------- | --------------------- |
| Database      | PostgreSQL            |
| Username      | `postgres`            |
| Password      | `postgres`            |
| Host          | `localhost`           |
| Port          | `5432`                |
| Database Name | `urban_basket_python` |

> **Note:** The connection string above is for local development. Do not use or commit real production passwords in a public GitHub repository.

## 🚀 How to Run the Project

Follow the steps below in order.

### Step 1: Create the PostgreSQL Database

First, open **PowerShell** and enter PostgreSQL's database mode.

For example:

```powershell
psql -U postgres
```

Enter your PostgreSQL password when prompted.

You should then see the PostgreSQL prompt:

```text
postgres=#
```

Create the database:

```sql
CREATE DATABASE urban_basket_python;
```

You can verify that the database was created with:

```sql
\l
```

After confirming the database exists, exit PostgreSQL:

```sql
\q
```

### Step 2: Return to the Main PowerShell

After exiting PostgreSQL database mode, you will return to your normal PowerShell.

Navigate to the project directory:

```powershell
cd path\to\python-database-manager
```

### Step 3: Create the Database Tables

Run the `create_database.py` file:

```powershell
python create_database.py
```

This script connects to the `urban_basket_python` PostgreSQL database using SQLAlchemy and creates the required tables.

### Step 4: Insert Data

After the tables have been created, run:

```powershell
python insertdata.py
```

This script inserts the required data into the PostgreSQL tables.

## 🔄 Project Workflow

```text
PowerShell
    │
    ▼
PostgreSQL Database Mode
    │
    ▼
CREATE DATABASE urban_basket_python;
    │
    ▼
Exit PostgreSQL (\q)
    │
    ▼
Main PowerShell
    │
    ▼
python create_database.py
    │
    ▼
Tables Created
    │
    ▼
python insertdata.py
    │
    ▼
Data Inserted
```

## 🎯 Project Purpose

This project was created to practice:

* Python and PostgreSQL integration
* SQLAlchemy
* psycopg2
* PostgreSQL database management
* Creating database tables
* Inserting data
* Running SQL/database operations from Python

## 🔐 Security

For learning purposes, the project uses a local PostgreSQL username and password in the connection string.

For a public or production project, it is recommended to use environment variables instead of storing database credentials directly in Python files.

## 👨‍💻 Author

**Zulfiqar Ali**

If you found this project useful, feel free to ⭐ the repository.
