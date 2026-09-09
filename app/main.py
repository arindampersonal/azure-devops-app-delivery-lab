from fastapi import FastAPI

app = FastAPI(
    title="Azure DevOps Application Delivery Lab",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "message": "Hello from Azure DevOps!",
        "version": "1.0.0"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }