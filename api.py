import base64
import json
from asyncio.windows_events import NULL

import requests
import pprint
import xml.etree.ElementTree as et
import requests
from assertpy import assert_that
from lxml import etree
from requests.auth import HTTPBasicAuth
from Authorization import *


def authorization_esmtr(self):
    params = {'username': 'auvin', 'password': '111'}
    auth = requests.get(f'{Settings.mtr_stand}/ws/token', params=params).json()
    return 'Bearer ' + auth['token']


def authorization_adapter(self):
    username = 1
    password = 1
    credentials = f"{username}:{password}"
    encoded_credentials = base64.b64encode(credentials.encode('utf-8')).decode('utf-8')
    return encoded_credentials

# Функция предназначена для получения конфигурация ИС-получателей
def get_subscribe_info_by_exchange_class():
    request = requests.get('http://192.168.6.7/api/Test/common/GetSubscribeInfoByExchangeClass').json()
    pprint.pprint(request.json())


# Получить список внешних систем
def get_systems():
    header = {'Authorization': authorization_esmtr()}
    request = requests.get('https://esmtr24.sdi-solution.ru/sdi/rs/replica/ReplicaReadService/getSystems',
                           headers=header).json()
    # pprint.pprint(request.json())
    return request


def get_properties_by_eotd_id(eotd):
    header = {'Authorization': authorization_esmtr()}
    params = {'eotd': eotd}
    request = requests.get(
        'https://esmtr24.sdi-solution.ru/sdi/rs/meta/AttributeClassifierReadService/getPropertiesByEotdId',
        params=params,
        headers=header).json()
    # pprint.pprint(request)
    return request


def get_application_by_id(application_id):
    header = {'Authorization': authorization_esmtr()}
    params = {'applicationId': application_id}
    request = requests.get('https://esmtr24.sdi-solution.ru/sdi/rs/application/ApplicationReadService'
                           '/getApplicationById', params=params, headers=header).json()
    # pprint.pprint(request)
    return request


def get_attributes(application_ids):
    header = {'Authorization': authorization_esmtr()}
    params = {'applicationIds': application_ids}
    request = requests.get('https://esmtr24.sdi-solution.ru/sdi/rs/application/ApplicationReadService/getAttributes',
                           params=params, headers=header).json()
    # pprint.pprint(request)
    # print(request['5517'])
    return request


# Функция, которая отвечает за формирование сообщения с данными по заявке.
def get_material_orders_info(order_ids):
    params = {'orderIds': order_ids}
    request = requests.get('http://192.168.6.7/api/Test/materialOrders/GetMaterialOrdersInfo', params=params).json()
    return request


def get_subscribe_info(property_Id):
    params = {'propertyId': property_Id}
    request = requests.get('http://192.168.6.7/74324/api/Test/materialOrders/GetSubscribeInfo', params=params).json()
    return request


def get_exchange_class(class_id):
    header = {'Authorization': authorization_esmtr()}
    params = {'applicationIds': class_id}
    request = requests.get('https://esmtr24.sdi-solution.ru/sdi/rs/application/ApplicationReadService/getAttributes',
                           params=params, headers=header).json()
    # pprint.pprint(request)
    # print(request['5517'])
    return request


def test_get_material_orders_info(orderIds = 7933):
    getApplicationById = get_application_by_id(orderIds)  # Получение данных по заявкам
    getAttributes = get_attributes(orderIds)  # Получение данных по атрибутам заявок
    assert orderIds == getApplicationById['id'] and str(orderIds) in getAttributes.keys()  # Проверка хуйни неясной
    GetMaterialOrdersInfo = get_material_orders_info(orderIds)  # Вызов тестируемой функции GetMaterialOrdersInfo
    assert getApplicationById['uid'] in GetMaterialOrdersInfo[0]['uid'], 'Ошибка в параметре uid'
    assert getApplicationById['displayName'] in GetMaterialOrdersInfo[0]['name'], 'Ошибка в параметре displayName'
    assert getApplicationById['status'] in GetMaterialOrdersInfo[0]['status'], 'Ошибка в параметре status'
    assert getApplicationById['type'] in GetMaterialOrdersInfo[0]['type'], 'Ошибка в параметре type'
    assert getApplicationById['applicant'] in GetMaterialOrdersInfo[0]['applicant'], 'Ошибка в параметре applicant'
    assert str(orderIds) in GetMaterialOrdersInfo[0]['id'], 'Ошибка в параметре id'

    names = [item['name'] for item in GetMaterialOrdersInfo[0]['destinationSystem']]  # Получем все значения destinationSystem в ответе GetMaterialOrdersInfo (тестируемой функции)
    names = ', '.join(names)  # превращаем его в строку

    for i in getAttributes[str(orderIds)]:  # дробим ответ getAttributes на словари
        a = i  # сохраняем ответ в локальную переменную
        if a['category'] == 'Системы-получатели':  # проверяем что в словаре значение параметра 'category' = 'Системы-получатели'
            h = list(get_subscribe_info(a['propertyId']).keys())  # Получаем значения ключей
            h = ', '.join(h) # превращаем его в строку
            if h is not NULL:
                assert h in names, f"{h} не входит в {names}"

# def test_get_material_orders_info(orderIds):
#     getApplicationById = get_application_by_id(orderIds)  # Получение данных по заявкам
#     getAttributes = get_attributes(orderIds)  # Получение данных по атрибутам заявок
#     assert orderIds == getApplicationById['id'] and str(orderIds) in getAttributes.keys()  # Проверка данных
#     GetMaterialOrdersInfo = get_material_orders_info(orderIds)  # Вызов тестируемой функции GetMaterialOrdersInfo
#     assert getApplicationById['uid'] == GetMaterialOrdersInfo[0]['uid'], 'Ошибка в параметре uid'
#     assert getApplicationById['displayName'] == GetMaterialOrdersInfo[0]['name'], 'Ошибка в параметре displayName'
#     assert getApplicationById['status'] == GetMaterialOrdersInfo[0]['status'], 'Ошибка в параметре status'
#     assert getApplicationById['type'] == GetMaterialOrdersInfo[0]['type'], 'Ошибка в параметре type'
#     assert getApplicationById['applicant'] == GetMaterialOrdersInfo[0]['applicant'], 'Ошибка в параметре applicant'
#     assert str(orderIds) == GetMaterialOrdersInfo[0]['id'], 'Ошибка в параметре id'
#     names = ', '.join(item['name'] for item in GetMaterialOrdersInfo[0]['destinationSystem'])  # Получаем все значения destinationSystem в ответе GetMaterialOrdersInfo
#     for attribut in getAttributes[str(orderIds)]:  # Перебираем ответ getAttributes
#         if attribut['category'] == 'Системы-получатели':  # Проверяем значение параметра 'category'
#             response = ', '.join(get_subscribe_info(attribut['propertyId']).keys())  # Получаем и объединяем ключи
#             if response is not None:
#                 assert response in names, f"{response} не входит в {names}"
#
#
# # def test_get_subscribe_info(property_id):
# #     getSystems = get_systems()  # Получить список внешних систем
# #     systemId=[]
# #     for i in getSystems:
# #         systemId.append(str(i['systemId']))  # складываем systemId внешних систем в список
# #     properties=[]
# #     for k in systemId:
# #         if bool(get_properties_by_eotd_id(k)) == True:  # Проверяем что словарь не пустой
# #             properties.append(get_properties_by_eotd_id(k))   # Непустые словари добавляются в массив
# #     for m in properties:
# #         key = list(m.keys())[0]  # Получаем ключ первого элемента словаря (так как ключи могут меняться)
# #         if m[key]['id'] == property_id:
# #             response = {m[key]['eOTDid']:m[key]['id']}  # Получаем значение параметра 'id' и eOTDid
# #             assert get_subscribe_info(property_id) == response
#
#
# def test_get_subscribe_info(property_id):
#     systemIds = [str(system['systemId']) for system in get_systems()]
#     properties = [get_properties_by_eotd_id(i) for i in systemIds if get_properties_by_eotd_id(i)]
#     for props in properties:
#         key = list(props.keys())[0]
#         if props[key]['id'] == property_id:
#             response = {props[key]['eOTDid']:props[key]['id']}
#             assert get_subscribe_info(property_id) == response



