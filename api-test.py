import requests
message=input("User:")
response=requests.post(
    "http://127.0.0.1:5000/api/chat",
    json={"message":message}
)

print("Bot: ",response.json()["response"])