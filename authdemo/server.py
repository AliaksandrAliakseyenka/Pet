from typing import Optional

from fastapi import FastAPI, Form, Cookie
from fastapi.responses import Response

# Объект при помощи которого создаем приложение
app = FastAPI()
# База данных
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


# Запуск сервера
# uvicorn server:app --reload

@app.get("/")
def index_page(user_name: Optional[str] = Cookie(default=None)):  # По key user_name, берем данные из куки
	with open(r'/Users/alexalex/Desktop/practice_python/Pet/authdemo/sign-in-form/index.html', 'r') as file:
		login_page = file.read()

	if user_name:
		try:
			user = users[user_name]  # Проверим user
		except KeyError:
			response = Response(login_page, media_type="text/html")
			response.delete_cookie(key="user_name")  # Удалим куки
			return response

		return Response(f"Hi, {users[user_name]['name']}", media_type='text/html')
	return Response(login_page, media_type="text/html")


@app.post("/login")
def login_page(user_name: str = Form(...), password: str = Form(...)):
	user = users.get(user_name)
	if not user or user["password"] != password:
		return Response("Not found user", media_type="text/html")

	response = Response(
		f"Hi user, {user['name']}!, Balance: {user['balance']}", media_type="text/html"
	)
	# Установить set_cookie key user_name
	response.set_cookie(key="user_name", value=user_name)
	return response
