FastAPI: Local Development and Troubleshooting

To start a FastAPI application defined in `main.py`:

1.  **Verify `main.py` Structure:** Ensure your `main.py` includes the following structure:

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}
```

2.  **Run with Uvicorn:** Uvicorn is the recommended ASGI server.

    *   Install: `pip install uvicorn` (if not already installed).
    *   Execute: From the project directory (containing `main.py`), run `uvicorn main:app --reload`.
