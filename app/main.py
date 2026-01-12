import uvicorn
from fastapi import FastAPI
from .api import router as api_router
app = FastAPI(title="PARSER-API")
app.include_router(api_router)
@app.get("/")
def root():
    return {"status":"ok"}
if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000)
