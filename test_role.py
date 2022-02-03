from urllib import response
import requests

BASE = "http://localhost:5000/"

print("post test")
response = requests.get(
    BASE + "test")
print(response.json())

print("put role 1")
response = requests.post(
    BASE + "role/100", {"jobs": "admin", "ket": "job sebagai admin"})
print(response.json())

# print("get role 1")
# response = requests.get(BASE + "role/1")
# print(response.json())

# print("put role 1")
# response = requests.put(
#     BASE + "role/1", {"job": "admin", "ket":"job sebagai admin"})
# print(response.json())

# print("get role 1")
# response = requests.get(BASE + "role/1")
# print(response.json())

# response = requests.delete(BASE + "role/1")
# print("delete role 1")
# print(response.json())

# response = requests.get(BASE + "role/1")
# print("get role 1")
# print(response.json())
