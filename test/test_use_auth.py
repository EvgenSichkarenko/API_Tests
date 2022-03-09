import requests
import pytest
from lib.BaseCase import BaseCase
import datetime
from lib.Assertion import Assertion

class TestUserAuth(BaseCase):
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

		self.auth_sid = self.get_cookies(response1, "auth_sid")
		self.token = self.get_headers(response1, "x-csrf-token")
		self.id = self.get_json_value(response1, "user_id")

	def test_user_auth(self):
		response2 = requests.get(
			"https://playground.learnqa.ru/api/user/auth",
			cookies={"auth_sid":self.auth_sid},
			headers={"x-csrf-token":self.token}
		)
		Assertion.assert_json_by_name_value(
			response2,
			"user_id",
			self.id,
			"User id does not compare id"
		)


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
		Assertion.assert_json_by_name_value(
			response2,
			"user_id",
			0,
			f"User is authorized with conditions {conditions}"
		)


