# Instruction

First of all, create venv, activate it, and do ```pip install -r requirements.txt```

1. WSGI 
```gunicorn wsgi_app:app```

2. ASGI
```uvicorn asgi_app:app --reload```

3. Starlette
```uvicorn starlette_app:app --reload```

4. FastAPI
```uvicorn fastapi_app:app --reload```