import json
import datetime
from requests import Response

class BaseCase:

	def get_cookies(self, response:Response, cookie_name):
		assert cookie_name in response.cookies, f"Cannot find cookie with name {cookie_name} in last response "
		return response.cookies[cookie_name]

	def get_headers(self, response:Response, headers_name):
		assert headers_name in response.headers, f"Cannot find token with name {headers_name} in last response "
		return response.headers[headers_name]

	def get_json_value(self, response:Response, name):
		try:
			response_as_dict = response.json()
		except json.decoder.JSONDecodeError:
			assert False, f"Response is not in JSON format. Response text is {response.text}"

		assert name in response_as_dict, f"Response json doesn't have key {name}"
		return response_as_dict[name]

	def prepare_register_data(self, email = None):
		if email is None:
			base_part = "learnqa"
			domain = "example.com"
			random_part = datetime.datetime.now().strftime("%m%d%y%h%M%S")
			email = f"{base_part}{random_part}@{domain}"
		return {
			"password": "123",
			"firstName": "learnqa",
			"lastName": "learnqa",
			"username": "learnqa",
			"email": email
		}