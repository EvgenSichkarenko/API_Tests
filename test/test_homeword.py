import requests

class TestHomework:
	def test_short_phraze(self):
		phrase = input("Set a phrase: ")
		assert len(phrase) < 15, "Phraze has more than 15 characters"

	def test_check_cookies(self):
		response = requests.get("https://playground.learnqa.ru/api/homework_cookie")
		assert "HomeWork" in response.cookies, "Cookies do not has 'HomeWork' in response"

	def test_check_headers(self):
		response = requests.get("https://playground.learnqa.ru/api/homework_header")
		assert "x-secret-homework-header" in response.headers, "Response do not has headers"

	def test_user_agent(self):
		response1 = requests.get("https://playground.learnqa.ru/ajax/api/user_agent_check")
		print(response1.headers)



