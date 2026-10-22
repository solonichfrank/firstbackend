from fastapi import FastAPI

app = FastAPI()

@app.get('/health')
def hello_world():
    return {"message": "hello world"}

@app.get('/bio')
def bios():
    return {
        'name':'Solo Niko',
        'age':20,
    }
# command run fast api with uvicorn
# uvicorn App01.src.app.main:app --reload