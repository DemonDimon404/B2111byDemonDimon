import requests

url = 'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json'

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    for currency in data:
        if currency['cc'] == 'USD':
            rate = currency['rate']
            print(f"Поточний курс долара США: {rate} грн/дол.")
            break
else:
    print("Не вдалося отримати дані з НБУ.")