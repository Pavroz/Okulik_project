import collections


with open('shops.txt', encoding='utf-8') as shop_file:
    shops = list(map(lambda x: x.replace('\n', ''), shop_file.readlines()))

print(shops)

city_shops = collections.defaultdict(list) # Собирает словарь, где под одним ключом может быть несколько значений
for line in shops:
    shop, city = line.split(':')
    city_shops[city].append(shop)
print(city_shops)

city_shops = {}
for line in shops:
    shop, city = line.split(':')
    if city not in city_shops:
        city_shops[city] = []
    city_shops[city].append(shop)
print(city_shops)


