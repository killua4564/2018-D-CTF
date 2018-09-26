import requests

data = {
    'user': "admin@leftover.dctf",
    'pass': 'password'
}

r = requests.post("https://password-policy.dctfq18.def.camp/", data=data)

print(r.text)
