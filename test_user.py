from urllib import response
import requests

BASE = "http://localhost:5000/"

print("post user 1")
response = requests.post(
    BASE + "user/1", {"nama": "hikmat", "umur": 31, "hp": 123})
print(response.json())

print("get user 1")
response = requests.get(BASE + "user/1")
print(response.json())

print("put user 1")
response = requests.put(
    BASE + "user/1", {"nama": "oky", "umur": 32, "hp": 1234})
print(response.json())

print("get user 1")
response = requests.get(BASE + "user/1")
print(response.json())

response = requests.delete(BASE + "user/1")
print("delete user 1")
print(response.json())

response = requests.get(BASE + "user/1")
print("get user 1")
print(response.json())
