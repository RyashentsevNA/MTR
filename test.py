import requests
import pprint # преобразует JSON в виде словаря

r = requests.get(url='https://yandex.ru')
print(r.status_code)
print(r.ok) #возвращает тру если код ответа меньше 400
print(r.text) #возвращает HTML
print(r.content) # возвращает байты если файл

print('---2------------2----------2------------------2---------------2---------------2--------')

b = requests.get(url='https://api.github.com')
c =b.json()
print(b.status_code)
pprint.pprint(c)  # pprint преобразует JSON в виде словаря
print('------------------------------------------------------------------------------------------')
print(b.headers)
print('------------------------------------------------------------------------------------------')
print(b.request.headers) # заголовки запроса

print('---3--------Передача заголовка--------3-------------------3--------Передача заголовка---------3--------------3--------')
# Передача заголовка
q = requests.get(url='https://api.github.com')
user_agent = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'}
q = requests.get(url='https://api.github.com', headers=user_agent)
print(q.request.headers) # заголовки запроса


print('---4-----Передача параметров------4----4--------Передача параметров------4----------------------4-------------4-------')
# Передача параметров
params = {'q': 'python'}
e = requests.get('https://api.github.com/search/repositories', params=params)
tt = e.json()
pprint.pprint(tt)
print('------------------------------------------------------------------------------------------')
print(tt['total_count'])


print('---5---Передача куки---------5---5-----Передача куки--------5-------Передача куки--------5-------------5-------')
# Передача куки

cookies = {'session_token': '123456789'}
n = requests.get('https://httpbin.org/cookies', cookies=cookies)
print(n.text)


print('---5---Передача куки---------5---5-----Передача куки--------5-------Передача куки--------5-------------5-------')
