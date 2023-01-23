from fastapi import FastAPI, Form
from fastapi.responses import Response

app = FastAPI()

users = {
	"alex@gmail.com": {
		"name": "alex",
		"password": "qwerty",
		"balance": 10_000
	},
	"dmitry@gmail.com": {
		"name": "dima",
		"password": "123456",
		"balance": 17_000
	}
}


# uvicorn server:app --reload

@app.get("/")
def index_page():
	with open(r'/Users/alexalex/Desktop/practice_python/Pet/authdemo/sign-in-form/index.html', 'r') as file:
		login_page = file.read()
	return Response(login_page, media_type="text/html")


@app.post("/login")
def login_page(user_name: str = Form(...), password: str = Form(...)):
	user = users.get(user_name)
	if not user or user["password"] != password:
		return Response("Not found user", media_type="text/html")

	response = Response(
		f"Hi user, {user['name']}!, Balance: {user['balance']}", media_type="text/html"
	)
	response.set_cookie(key="username", value=user_name)
	return response
