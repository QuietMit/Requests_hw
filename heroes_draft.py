print()
# from pprint import pprint
import json
import requests

def super_mind(*names):
    '''Функция выводит имя самого умного супергероя при помощи документации SuperHero API.
    
     В качестве параметров функции используется список произвольной длины с именами супергероев.'''
    intel_power = {} # создаём словарь с элементами "имя" : "уровень интеллекта"
    SEARCH_NAME = 'https://superheroapi.com/api/2619421814940190/search/' # константа адреса запроса по поиску Супергероя
    for name in names:
        url = SEARCH_NAME + name + '/get' # адрес запроса с методом
        resp = requests.get(url) # ответ ресурса на запрос
        character_dict = resp.json() # сохранение ответа в виде словаря json
        # запись данных словаря в файл формата json:
        with open('character.json', 'w', encoding='utf-8') as f:
            json.dump(character_dict, f)
        # файл character.json целиком прочитан в переменную: 
        with open('character.json', 'rt', encoding='utf-8') as fl:
            character_data = json.load(fl)
            # pprint(character_data) для проверки содержимомго файла
            characters_list = character_data['results'] # получение списка значений в виде словарей по ключу 'results'
            for elm in characters_list: # поиск по элементам-словарям внутри списка, по имени героя его id
                if name in elm.values():
                    character_id = elm['id'] # сохранение id супергероя в переменную
        # print(character_id) # для проверки
        # print(type(character_id)) # для проверки       
        URL_POWERSTATS = 'https://superheroapi.com/api/2619421814940190/' # константа адреса целевого запроса к ресурсу
        urls_end = '/powerstats/get' # константа подстановки целевого запроса к адресу ресурса
        url_1 = URL_POWERSTATS + character_id + urls_end # адрес целевого запроса данных powerstats по id супергероя
        # print(url_1) # для проверки
        result = requests.get(url_1) # переменная с ответом на запрос
        powerstats = result.json() # сохранение полученных данных в виде словаря
        # print(type(powerstats)) # проверка
        # pprint(powerstats) # проверка
        # print(powerstats['intelligence']) # проверка
        intel_power[name] = powerstats['intelligence'] # добавление в новый словарь по ключу-имени супергероя значения его уровня интеллекта
        
    # print(intel_power)
    return f'Самым умным супергероем является {max(intel_power)}'
print(super_mind('Hulk', 'Captain America', 'Thanos'))
print()