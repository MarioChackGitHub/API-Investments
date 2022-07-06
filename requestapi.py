import requests

url = 'http://mariochack.pythonanywhere.com/predict'
dict_req = {"TV": 100, "radio":50, "newspaper":100}
req = requests.post(url, json=dict_req)
print(req.json())
# print(req.status_code)
# print(req.content)
# print(req.headers)

# req = requests.post(url, json=dict_req)

# req = requests.get(url)