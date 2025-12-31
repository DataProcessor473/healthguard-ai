from fastapi import FastAPI
import uvicorn

app = FastAPI(title="HealthGuard AI")

@app.get("/")
def home():
    return {"message": "HealthGuard AI Running!"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
