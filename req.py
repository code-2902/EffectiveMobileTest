import requests

url_test='https://code-2902.github.io/CHECKER/'
url='https://api.petrushkazelenaia.com/partnershops'

try:
    response=requests.get(url_test)
    if response.status_code==200:
        data=response.json()
        print(data)
    else:
        print(f"Ошибка {response.status_code}")
except requests.exceptions.RequestException as err:
    print(f"Ошибка запроса {err}")