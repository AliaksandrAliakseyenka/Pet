from fastapi import FastAPI, Form
from fastapi.responses import Response

app = FastAPI()


# uvicorn server:app --reload

@app.get("/")
def index_page():
	with open(r'/Users/alexalex/Desktop/practice_python/Pet/authdemo/sign-in-form/index.html', 'r') as file:
		login_page = file.read()
	return Response(login_page, media_type="text/html")


@app.post("/login")
def login_page(user_name: str = Form(...), password: str = Form(...)):
	return Response(f"Ваш Login: {user_name}, password: {password}", media_type="text/html")
