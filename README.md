## important test !! 

This is a sample FastAPI application with multiple interconnected files demonstrating a structured approach to building a REST API.

## Project Structure

```
app/
├── api/                  # API routes
│   ├── routes/           # API endpoints
│   │   ├── auth.py       # Authentication endpoints
│   │   ├── items.py      # Item endpoints
│   │   └── users.py      # User endpoints
│   └── api.py            # API router
├── config/               # Configuration
│   └── settings.py       # Application settings
├── core/                 # Core functionality
│   ├── auth.py           # Authentication dependencies
│   └── security.py       # Security utilities
├── db/                   # Database
│   └── database.py       # Database connection
├── models/               # SQLAlchemy models
│   ├── item.py           # Item model
│   └── user.py           # User model
├── schemas/              # Pydantic schemas
│   ├── item.py           # Item schemas
│   ├── token.py          # Token schemas
│   └── user.py           # User schemas
├── services/             # Business logic
│   ├── item.py           # Item services
│   └── user.py           # User services
├── utils/                # Utilities
│   └── init_db.py        # Database initialization
└── main.py               # Application entry point
```

## Features

- User authentication with JWT tokens
- User management (CRUD operations)
- Item management (CRUD operations)
- Role-based access control
- SQLAlchemy ORM for database operations
- Pydantic schemas for request/response validation

## Installation

1. Clone the repository
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

## Running the Application

```
uvicorn app.main:app --reload
```

The API will be available at http://localhost:8000

## API Documentation

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Initial Users

The application comes with two predefined users:

1. Admin user:
   - Email: admin@example.com
   - Password: admin123

2. Regular user:
   - Email: user@example.com
   - Password: user123

To create these users, run:
```
python -m app.utils.init_db
