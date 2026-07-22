from fastapi import FastAPI


app = FastAPI(title="Hello World API")


@app.get("/")
def read_root():
    return {"message": "Hello, World!"}


def main():
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=8026, reload=True)


if __name__ == "__main__":
    main()
