from lib.BaseCase import BaseCase
from lib.Assertion import Assertion
import requests

class TestUserRegister(BaseCase):


	def test_create_user_successfully(self):
		data = self.prepare_register_data()

		response = requests.post("https://playground.learnqa.ru/api/user/", data=data)
		Assertion.assert_code_status(response, 200)
		Assertion.assert_json_has_key(response, "id")

	def test_create_user_with_existing_email(self):
		email="vinkotov@example.com"
		data = self.prepare_register_data(email)

		response = requests.post("https://playground.learnqa.ru/api/user/", data=data)

		Assertion.assert_code_status(response, 400)
		assert response.content.decode("utf-8") == f"Users with email '{email}' already exists", f"Unexpected response content {response.content}"