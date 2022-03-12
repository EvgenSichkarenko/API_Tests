import pytest
from lib.BaseCase import BaseCase
from lib.my_requests import MyRequests
import datetime
from lib.Assertion import Assertion
import allure

@allure.epic("Authorization cases")
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

		response1 = MyRequests.post("/user/login", data=data)
		self.auth_sid = self.get_cookies(response1, "auth_sid")
		self.token = self.get_headers(response1, "x-csrf-token")
		self.user_id_from_auth_method = self.get_json_value(response1, "user_id")

	@allure.description("This test successfully authorize user by email and password")
	def test_user_auth(self):
		response2 = MyRequests.get(
			"/user/auth",
			cookies={"auth_sid":self.auth_sid},
			headers={"x-csrf-token":self.token}
		)
		Assertion.assert_json_by_name_value(
			response2,
			"user_id",
			self.user_id_from_auth_method,
			"User id does not compare id"
		)



	@allure.description("This test check authorization status w/o sending auth cookies or token")
	@pytest.mark.parametrize("conditions", exclude)
	def test_negative_user_auth(self,  conditions):

		if conditions == "no cookies":
			response2 = MyRequests.get(
			"/user/auth",
			headers={"x-csrf_token":self.token}
			)
		else:
			response2 = MyRequests.get(
			"/user/auth",
			cookies={"auth_sid":self.auth_sid},
			)
		Assertion.assert_json_by_name_value(
			response2,
			"user_id",
			0,
			f"User is authorized with conditions {conditions}"
		)


