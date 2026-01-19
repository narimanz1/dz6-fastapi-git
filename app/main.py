from fastapi import FastAPI

app = FastAPI(title="DZ6 FastAPI Mini API", version="1.0.0")


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/echo/{text}")
def echo(text: str):
    return {"echo": text}