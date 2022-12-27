import requests


c = 1

class SomeResourceClient:
    
res = requests.get('https://content.adriver.ru/AdRiverFPS.js')
print(res.text)
