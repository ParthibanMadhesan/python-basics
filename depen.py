
import requests
# api_url = "https://jsonplaceholder.typicode.com/todos/1"
# response = requests.get(api_url)
# print(response.json())
# print("--------------")
# print(response.status_code)
# print("--------------")
# print(response.__dict__)
# print("--------------")
# print(response.headers["Content-Type"])



api_url = "https://jsonplaceholder.typicode.com/todos"
todo = {"userId": 1, "title": "Buy milk", "completed": False}
response = requests.post(api_url, json=todo)
print(response.json())
print(response.status_code)
print(response.__dict__)
print("---------------")
print(response.headers["Content-Type"])