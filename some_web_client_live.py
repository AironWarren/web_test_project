import requests

class SomeResourceClient:
    
res = requests.get('https://content.adriver.ru/AdRiverFPS.js')
print(res.text)
