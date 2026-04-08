from fastapi import FastAPI
import time
app = FastAPI()

@app.get("/")
def read_root():
    return {
        "message": "Hello user, you have successfully deployed Ankit",
        "current_time": time.time()
    }