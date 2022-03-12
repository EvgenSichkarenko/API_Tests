import requests
from lib.my_requests import MyRequests
from lib.Assertion import Assertion
from lib.BaseCase import BaseCase

class TestUserEdit(BaseCase):
	def test_edit_just_created_user(self):

		#register
		register_data= self.prepare_register_data()
		response1 = MyRequests.post("/user/", data=register_data)

		Assertion.assert_code_status(response1, 200)
		Assertion.assert_json_has_key(response1, "id")

		email = register_data["email"]
		first_name = register_data["firstName"]
		password = register_data["password"]
		user_id = self.get_json_value(response1, "id" )

		#login

		login_data = {
			"email":email,
			"password":password
		}

		response2 = MyRequests.post("/user/login", data=login_data)
		auth_sid = self.get_cookies(response2, "auth_sid")

		token = self.get_headers(response2, "x-csrf-token")

		#edit
		new_name = "Change name"
		response3 = MyRequests.put(
			f"/user/{user_id}",
			headers={"x-csrf-token":token},
			cookies={"auth_sid":auth_sid},
			data={"firstName":new_name}
		)

		Assertion.assert_code_status(response3, 200)

		#GET
		response4 = MyRequests.get(
			f"/user/{user_id}",
			headers={"x-csrf-token":token},
			cookies={"auth_sid":auth_sid},
		)
		Assertion.assert_json_by_name_value(
			response4,
			"firstName",
			new_name,
			"Wrong name of the user after edit"
		)