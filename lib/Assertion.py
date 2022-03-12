import json.decoder

from requests import Response


class Assertion:
	@staticmethod
	def assert_json_by_name_value(response:Response, name, expected_value, error_message):
		try:
			json_as_dict = response.json()
		except json.decoder.JSONDecodeError:
			assert False, "Response is not in json format"

		assert name in json_as_dict, "Cannot find name in json_as_dict"
		assert json_as_dict[name] == expected_value, error_message

	@staticmethod
	def assert_json_has_key(response:Response, name):
		try:
			json_as_dict = response.json()
		except json.decoder.JSONDecodeError:
			assert False, "Response is not in json format"

		assert name in json_as_dict, f"Response is not in json format. Response test is '{response.text}'"

	@staticmethod
	def assert_json_has_keys(response:Response, names:list):
		try:
			json_as_dict = response.json()
		except json.decoder.JSONDecodeError:
			assert False, "Response is not in json format"
		for name in names:
			assert name in json_as_dict, f"Response is not in json format. Response test is '{name}'"

	@staticmethod
	def assert_code_status(response:Response, expecte_status_code):
		assert response.status_code == expecte_status_code,\
			f"Unexpected status code, expected {expecte_status_code}"

	@staticmethod
	def assert_json_has_not_key(response:Response, name):
		try:
			json_as_dict = response.json()
		except json.decoder.JSONDecodeError:
			assert False, f"Response is not in json format. Response test is '{response.text}'"

		assert name not in json_as_dict, f"Response JSON shouldn't have key {name}"

