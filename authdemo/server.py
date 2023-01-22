from fastapi import FastAPI
from fastapi.responses import Response

app = FastAPI()

#uvicorn server:app --reload
@app.get("/")
def index_page():
	return Response("Hi user", media_type="text/html")