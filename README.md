# FastAPI - The Complete Course

A comprehensive collection of FastAPI example projects demonstrating various features and implementation patterns. This repository contains multiple progressive projects from basic endpoints to full-featured applications with authentication, databases, and testing.

## 🚀 Quick Start

### Prerequisites
- Python 3.7+
- pip (Python package installer)

### Installation

1. **Clone the repository** (if not already done)
2. **Create and activate a virtual environment** (recommended)
   ```powershell
   # Windows PowerShell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   
   # If PowerShell execution policy blocks scripts, use Command Prompt:
   # .\.venv\Scripts\activate.bat
   ```

3. **Install dependencies**
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

## 📁 Project Structure

This repository contains multiple progressive FastAPI projects:

### Project 1 - Basic FastAPI
- **File**: `Project1/books.py`
- **App Instance**: `Project1.books.app`
- **Description**: Simple in-file endpoints demonstrating basic FastAPI functionality

**Run from Project1 folder:**
```bash
cd Project1
uvicorn books:app --reload
```

**Run from repository root:**
```bash
uvicorn Project1.books:app --reload
```

### Project 2 - Pydantic Models
- **File**: `Project2/books2.py`
- **App Instance**: `Project2.books2.app`
- **Description**: Demonstrates Pydantic models and data validation

**Run:**
```bash
uvicorn Project2.books2:app --reload
```

### Project 3 - Todo App (Basic)
- **File**: `Project3/TodoApp/main.py`
- **App Instance**: `Project3.TodoApp.main.app`
- **Description**: Basic todo application with SQLite database

**Run:**
```bash
uvicorn Project3.TodoApp.main:app --reload
```

### Project 3.5 - Todo App with Alembic
- **File**: `Project3.5/TodoApp/main.py`
- **App Instance**: `Project3.5.TodoApp.main.app`
- **Description**: Todo app with database migrations using Alembic

**Run:**
```bash
uvicorn Project3.5.TodoApp.main:app --reload
```

### Project 4 - Todo App with Authentication
- **File**: `Project4/TodoApp/main.py`
- **App Instance**: `Project4.TodoApp.main.app`
- **Description**: Todo app with user authentication and authorization

**Run:**
```bash
uvicorn Project4.TodoApp.main:app --reload
```

### Project 5 - Full-Featured Todo App
- **File**: `Project5/TodoApp/main.py`
- **App Instance**: `Project5.TodoApp.main.app`
- **Description**: Complete todo application with templates, static files, and comprehensive testing

**Run from Project5 folder:**
```bash
cd Project5
uvicorn TodoApp.main:app --reload
```

### 📝 Important Notes
- If you run uvicorn from the repository root, use the dotted import path shown above.
- If you run uvicorn from inside a project folder, you can use the module name only (e.g., `uvicorn books:app --reload` inside Project1).

## 🧪 Running Tests

Many projects include pytest tests. To run tests for a specific project:

```bash
# Example: Run tests for Project5
cd Project5/TodoApp
pytest -q

# Run with verbose output
pytest -v

# Run specific test file
pytest test/test_todos.py -v
```

## 📚 Additional Resources

### Helpful Files
- **Root launcher example**: `main.py`
- **Dependency list**: `requirements.txt`
- **Example endpoints**: `Project1/books.py`, `Project2/books2.py`

## 📖 FastAPI Documentation

Each project provides access to the built-in FastAPI documentation:

- **Interactive Swagger UI**: http://127.0.0.1:8000/docs
- **ReDoc**: http://127.0.0.1:8000/redoc
- **OpenAPI JSON**: http://127.0.0.1:8000/openapi.json

### Example Commands

Fetch OpenAPI spec with curl:
```bash
curl http://127.0.0.1:8000/openapi.json
```

Start Project 1 and access docs:
```bash
cd Project1
uvicorn books:app --reload
# Then open http://127.0.0.1:8000/docs
```

### Customizing Documentation

You can customize or disable built-in docs in your FastAPI app:

```python
from fastapi import FastAPI

app = FastAPI(
    title="My API",
    description="Short description",
    docs_url="/swagger",     # change swagger ui path, use None to disable
    redoc_url=None,          # disable ReDoc
    openapi_url="/api/openapi.json"  # change openapi json path
)
```

### Production Considerations

For production deployments:
- Consider disabling docs (`docs_url=None, redoc_url=None`)
- Serve documentation behind authentication or VPN
- Use environment variables to control doc availability

## 🤝 Contributing

Feel free to explore each project to understand different FastAPI patterns and implementations. Each project builds upon the previous one, demonstrating progressively more complex features.

---

**Quick Reference**: Start with Project 1 for basic concepts, then progress through each project to learn authentication, database integration, testing, and full-stack development with FastAPI.
