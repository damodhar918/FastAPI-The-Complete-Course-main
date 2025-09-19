Workspace: Collecting workspace informationFiltering to most relevant informationUse Uvicorn to run the FastAPI app defined in books.py (the ASGI app instance is `Project1.books.app`).

Install Uvicorn if needed:

````sh
# Install uvicorn
pip install uvicorn
````

Run from the Project1 directory (recommended, since the file is a plain module file):

````sh
# change to the folder containing books.py and run
cd Project1
uvicorn books:app --reload
````

Alternative (from workspace root) — only works if Python can import Project1 as a package (add __init__.py or set PYTHONPATH):

````sh
uvicorn Project1.books:app --reload


1) Create and activate a virtual environment (Windows)

````powershell
# Create venv in workspace root
python -m venv .venv

# PowerShell activate
.\.venv\Scripts\Activate.ps1

# If PowerShell blocks scripts, use cmd:
# .\.venv\Scripts\activate
````

2) Install FastAPI and Uvicorn

````sh
pip install --upgrade pip
pip install fastapi uvicorn[standard]
````

3) Create a requirements file (optional)

````text
fastapi
uvicorn[standard]
````

Or generate it from the active env:

````sh
pip freeze > requirements.txt
````

4) Run your app

From the workspace root (works if Project1 is importable):

````sh
uvicorn Project1.books:app --reload
````

Or change to the Project1 folder and run:

````sh
cd Project1
uvicorn books:app --reload
````

Workspace: Collecting workspace information```markdown
# FastAPI-The-Complete-Course — Workspace README

This repository contains multiple small FastAPI example projects. Quick reference below shows how to install dependencies and run each example.

## Requirements
Install dependencies listed in [requirements.txt](requirements.txt):

```sh
pip install -r requirements.txt
```

## Projects and how to run

- Project1 (simple in-file endpoints)
  - File: [Project1/books.py](Project1/books.py) — ASGI app instance: [`Project1.books.app`](Project1/books.py)
  - From the Project1 folder:
    ```sh
    cd Project1
    uvicorn books:app --reload
    ```
  - From repository root:
    ```sh
    uvicorn Project1.books:app --reload
    ```

- Project2 (Pydantic examples)
  - File: books2.py — ASGI app instance: `Project2.books2.app`
  - Run:
    ```sh
    uvicorn Project2.books2:app --reload
    ```

- Project3 / Project3.5 / Project4 / Project5 (Todo apps)
  - Project3 main: main.py — `Project3.TodoApp.main.app`
    ```sh
    uvicorn Project3.TodoApp.main:app --reload
    ```
  - Project3.5 main: main.py — `Project3.5.TodoApp.main.app`
    ```sh
    uvicorn Project3.5.TodoApp.main:app --reload
    ```
  - Project4 main: main.py — `Project4.TodoApp.main.app`
    ```sh
    uvicorn Project4.TodoApp.main:app --reload
    ```
  - Project5 main: main.py — `Project5.TodoApp.main.app`
    ```sh
    uvicorn Project5.TodoApp.main:app --reload
    ```

Notes:
- If you run uvicorn from the repository root, use the dotted import path shown above.
- If you run uvicorn from inside a project folder, you can use the module name only (e.g., `uvicorn books:app --reload` inside Project1).

## Running tests
Many projects include pytest tests (see e.g. test). Example:

```sh
# run from project folder
cd Project5/TodoApp
pytest -q
```

## Helpful files
- Root launcher example: main.py
- Dependency list: requirements.txt
- Example endpoints: books.py, books2.py

// ...existing code...

## FastAPI docs

- Interactive Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc
- OpenAPI JSON: http://127.0.0.1:8000/openapi.json

Example: fetch OpenAPI spec with curl
```sh
curl http://127.0.0.1:8000/openapi.json
```

Customize or disable built-in docs in your FastAPI app:
```python
# example: change or disable docs
from fastapi import FastAPI

app = FastAPI(
    title="My API",
    description="Short description",
    docs_url="/swagger",     # change swagger ui path, use None to disable
    redoc_url=None,          # disable ReDoc
    openapi_url="/api/openapi.json"  # change openapi json path
)
```

Protect docs (basic idea): require an auth dependency on a docs route or run docs only in dev. For production, disable or restrict docs and serve internal docs behind a VPN.

Open the docs after starting uvicorn:
```sh
# from Project1 folder
cd Project1
uvicorn books:app --reload
# then open http://127.0.0.1:8000/docs
```

If you want this README expanded with endpoint lists or screenshots of OpenAPI docs, tell me which project to document first.
