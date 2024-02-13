# import requests


# # 1
# hh = requests.get('http://207.90.194.130:8084/routes/21')
# a = hh.json()
# print(a)
# # 2
# hh = requests.get('http://207.90.194.130:8084/routes/stations/1')
# a = hh.json()
# for aa in a:
#     print(f" остановки вашего автобуса:  {aa['name']}")

# 3 остановки автобуса на карте

# hh = requests.get('http://207.90.194.130:8084/routes/map/21')
# a = hh.json()
# print(a)

# 4 какие автобусы с этой остановки и куда

# hh = requests.get('http://207.90.194.130:8084/routes/map/station/routes/5015')
# a = hh.json()
# for aa in a:
#     print(f"какие автобусы с этой остановки и куда:  {aa['id']}")
# for ass in a:
#     print(aa['name'])


# 5  получение на карте автобусов по id
# hha = requests.get('http://207.90.194.130:8084/routes/map/buses/21')
# a = hha.json()
# print(a)

# 6 Карта Узбекистанской линии метро

# h = requests.get('http://207.90.194.130:8084/routes/map/7816')
# a = h.json()
# for p in a:
#     print(p['id'])


# 7  Получение маршрутов метрополитена
# h = requests.get('http://207.90.194.130:8084/routes/all/type/1')

# a = h.json()
# for aa in a:
#     print(f" Названия линий в узб метро:   {aa['name']}")

# 8   Получение всех маршруток


# h = requests.get('http://207.90.194.130:8084/routes/all/type/6')
# a = h.json()
# for l in a:
#     print(f"Название маршруток и их путь {l['name']} , {l['nameB']}")

