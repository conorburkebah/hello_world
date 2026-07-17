# Hello World FastAPI (uv)

Simple FastAPI app managed with `uv`.

## Run

```bash
uv run uvicorn main:app --reload --port 8010
```

Then open http://127.0.0.1:8010

## Endpoints

- `GET /` -> `{"message": "Hello, World!"}`
- `GET /docs` -> Swagger UI
