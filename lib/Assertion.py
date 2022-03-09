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