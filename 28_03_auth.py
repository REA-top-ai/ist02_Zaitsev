import requests
from requests.auth import HTTPBasicAuth
from requests.auth import HTTPDigestAuth

user = 'vasilii'
psswd = '12345'
ubasic = f'https://httpbin.org/basic-auth/{user}/{psswd}'
a = requests.get(ubasic, auth = HTTPBasicAuth(user, psswd))
print(a.json())

ubearer = f'https://httpbin.org/bearer'
token = ('eyJhbGciOiJub25lIn0.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6ImtpcmlsbCBtaWxsZXIiLCJhZG1pbiI6dHJ1ZSwiaWF0IjoxNzc0ODYzMjAwfQ.')
a2 = requests.get(ubearer, headers = {'Authorization': f'Bearer {token}'})
print(a2.json())

url_diq = f'https://httpbin.org/digest-auth/auth/{user}/{psswd}'
print(requests.get(url_diq, auth=HTTPDigestAuth(user, psswd)).json())