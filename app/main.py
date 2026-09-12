from fastapi import FastAPI

app = FastAPI(title="Academy Backend")


@app.get("/health")
def health_check():
    return {"status": "ok"}
