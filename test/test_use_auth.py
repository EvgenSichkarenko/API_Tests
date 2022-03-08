import requests
import pytest
import datetime

class TestUserAuth:
	exclude = [
		("no cookies"),
		("no token")
	]

	def setup(self):
		data = {
			"email" : "vinkotov@example.com",
			"password": "1234"
		}

		response1 = requests.post("https://playground.learnqa.ru/api/user/login", data=data)

		assert "auth_sid" in response1.cookies, "There is no auth_sid in cookies"
		assert "x-csrf-token" in response1.headers, "There is no token in header"
		assert "user_id" in response1.json(), "There is no user_id in json"

		self.auth_sid = response1.cookies.get("auth_sid")
		self.token = response1.headers.get("x-csrf-token")
		id = response1.json()["user_id"]

	def test_user_auth(self):
		response2 = requests.get(
			"https://playground.learnqa.ru/api/user/auth",
			cookies={"auth_sid":self.auth_sid},
			headers={"x-csrf_token":self.token}
		)
		assert "user_id" in response2.json(), "There is no user id in response2"

		id2 = response2.json()["user_id"]

		assert id == id2, "User id is not equel to user_id"


	@pytest.mark.parametrize("conditions", exclude)
	def test_negative_user_auth(self,  conditions):


		if conditions == "no cookies":
			response2 = requests.get(
			"https://playground.learnqa.ru/api/user/auth",
			headers={"x-csrf_token":self.token}
			)
		else:
			response2 = requests.get(
			"https://playground.learnqa.ru/api/user/auth",
			cookies={"auth_sid":self.auth_sid},
			)

		assert "user_id" in response2.json(), "There Is no "
		id = response2.json()["user_id"]
		assert id == 0, "User no autheras"

