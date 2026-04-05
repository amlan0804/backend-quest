from fastapi import FastAPI
from routes import router

app = FastAPI()
@app.get('/ping')
def ping():
    return {"status":"ok"}

@app.get('/')
def root():
    return {"message":"hello"}
#app.include_router(router)


@app.post("/echo")
def post_echo(data: dict):
    return data