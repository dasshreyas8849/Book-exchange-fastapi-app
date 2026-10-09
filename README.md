# 📚 Kitab Exchange API

A REST API for a simple **college book exchange platform**, built with **FastAPI**, **SQLModel**, and **SQLite**.

The API allows users to register, list books for sale, search available books, update book information, and mark books as sold. Protected operations use **API-key authentication through HTTP headers**.

## 🚀 Features

- 👤 User registration and listing
- 📚 Create and manage book listings
- 🔎 Search books by title or author
- 💰 Update book prices
- ✅ Mark books as sold
- 🔐 API-key based authentication
- 🗄️ SQLite database
- 📦 SQLModel ORM
- ⚡ FastAPI REST API
- 📖 Automatic interactive API documentation

## 🛠️ Tech Stack

- **Python**
- **FastAPI** — API framework
- **SQLModel** — ORM and data validation
- **SQLite** — Database
- **Uvicorn** — ASGI server

## 📁 Project Structure

```text
kitab-exchange/
│
├── main.py                 # FastAPI application entry point
├── auth.py                 # API-key authentication
├── database.py             # Database engine and session management
├── requirements.txt        # Python dependencies
├── .gitignore
│
├── models/
│   ├── __init__.py
│   ├── user.py             # User models
│   └── book.py             # Book models
│
└── routes/
    ├── __init__.py
    ├── users.py            # User endpoints
    └── books.py            # Book endpoints
```

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd kitab-exchange
```

### 2. Create a virtual environment

Windows:

```powershell
python -m venv venv
```

Activate it:

```powershell
venv\Scripts\activate
```

macOS/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

## ▶️ Running the API

Start the development server with:

```bash
uvicorn main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

### Interactive Documentation

FastAPI automatically provides Swagger UI:

```text
http://127.0.0.1:8000/docs
```

You can also access the ReDoc documentation at:

```text
http://127.0.0.1:8000/redoc
```

## 🔐 Authentication

Protected endpoints use an API key supplied through the `X-API-Key` HTTP header.

Example:

```http
X-API-Key: mysecretapikey
```

The API key is currently defined in `auth.py`:

```python
API_KEY = "mysecretapikey"
```

> ⚠️ For production use, the API key should **not** be hardcoded. Store it in an environment variable such as `.env`.

## 👤 User Endpoints

### Register a User

```http
POST /user/
```

Example request:

```json
{
  "name": "John Doe",
  "email": "john@example.com",
  "college": "VIT"
}
```

Requires the `X-API-Key` header.

### Get All Users

```http
GET /user/
```

Returns all registered users.

## 📚 Book Endpoints

### Create a Book

```http
POST /books/
```

Example:

```json
{
  "Title": "Database System Concepts",
  "Author": "Abraham Silberschatz",
  "price": 500,
  "user_id": 1
}
```

Requires authentication.

### Get Available Books

```http
GET /books/
```

Only books that have not been sold are returned.

### Search by Title

```http
GET /books/?Title=database
```

### Search by Author

```http
GET /books/?Author=Silberschatz
```

You can also combine filters:

```http
GET /books/?Title=database&Author=Silberschatz
```

### Update a Book

```http
PATCH /books/{book_id}
```

Example:

```json
{
  "price": 400
}
```

Requires authentication.

### Mark a Book as Sold

```http
PATCH /books/{book_id}/sold
```

Requires authentication.

## 🗄️ Database

The application uses **SQLite** with SQLModel.

The database connection is configured in `database.py`:

```python
DATABASE_URL = "sqlite:///./database.db"
```

Database tables are automatically created when the FastAPI application starts.

The main database relationships are:

```text
User
 │
 │ 1
 │
 │
 │ *
 ▼
Book
```

A user can own multiple books, while each book belongs to a user.

## 🔄 API Flow

A typical interaction looks like:

```text
Client
  │
  ▼
FastAPI
  │
  ├── Authentication
  │      └── X-API-Key
  │
  ├── Route
  │      ├── /user
  │      └── /books
  │
  ▼
SQLModel
  │
  ▼
SQLite
```

## 🔒 Security Note

This project currently uses a simple API-key authentication mechanism for learning purposes.

For a production application, authentication should be improved with features such as:

- Environment-based secrets
- Password hashing
- JWT authentication
- User-specific authorization
- Token expiration
- Role-based access control
- HTTPS
- Input validation and rate limiting

## 🧪 Testing the API

The easiest way to test the API is through the automatically generated Swagger UI:

```text
http://127.0.0.1:8000/docs
```

You can also use tools such as:

- Postman
- Insomnia
- curl
- HTTPie

## 📌 Future Improvements

Potential extensions include:

- 🔑 JWT authentication
- 👤 User login/logout
- 🔍 Advanced book search
- 🖼️ Book cover uploads
- 💬 Buyer/seller messaging
- ⭐ User ratings and reviews
- 🛒 Book purchase workflow
- 💳 Payment integration
- 🐳 Docker deployment
- ☁️ PostgreSQL for production
- 🧪 Automated tests with Pytest

## 📄 License

This project is intended for educational and personal development purposes.
