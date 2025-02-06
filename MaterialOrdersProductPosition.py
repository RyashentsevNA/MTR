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
from Authorization import Authorization

class TestMaterialOrdersProductPosition(Authorization):
# Удаление указанного в запросе идентификатора заявки управлением из внешней системы (Удаляет заявку в esmtr24)
    def test_DeleteMaterialOrdersProductPosition(self):
        header = {'Content-Type': 'text/xml; charset=utf-8',
                  'Authorization': f'Basic {Authorization.authorization_adapter(self)}'}
        xml_body = f"""<Envelope xmlns="http://schemas.xmlsoap.org/soap/envelope/">
                <Body>
                    <DeleteMaterialOrdersProductPosition xmlns="http://tempuri.org/">
                        <Request>
                            <OrderId>321</OrderId>
                            <Comment>321</Comment>
                            <Meta>
                                <SystemId>IUSMTR</SystemId>
                                <MessageId>777</MessageId>
                            </Meta>
                        </Request>
                    </DeleteMaterialOrdersProductPosition>
                </Body>
            </Envelope>"""
        response = requests.post('http://192.168.6.7/10001/MaterialOrdersProductPosition.asmx',
                                 data=xml_body, headers=header)

        if response.status_code == 200:
            print('Успешно:', response.text)
        else:
            print('Ошибка:', response.status_code, response.text)

# Внутренняя функция, которая отвечает за создание заявок (Создает заявку в esmtr24)
    def test_CreateMaterialOrdersProductPosition(self):
        header = {'Content-Type': 'text/xml; charset=utf-8',
                  'Authorization': f'Basic {Authorization.authorization_adapter(self)}'}
        xml_body = f"""<Envelope xmlns="http://schemas.xmlsoap.org/soap/envelope/">
    <Body>
        <CreateMaterialOrdersProductPosition xmlns="http://tempuri.org/">
            <Request>
                <OrderTemplateId>4659</OrderTemplateId>
                <IsAutoProviding>true</IsAutoProviding>
                <OrderFields>
                    <SupDoc>ЛОГ.txt</SupDoc>
                    <RefGroup>70543135</RefGroup>
                    <Producer>Производитель</Producer>
                    <Comment>Создано авто тестом ОТ</Comment>
                    <ObjectCode>70646865</ObjectCode>
                    <CustomerDo>Наименование дочерней организации заказчика</CustomerDo>
                </OrderFields>
                <ClassFields>
                  <AttributeId>24365</AttributeId>
                  <Value>true</Value>
                </ClassFields>
                <ClassFields>
                  <AttributeId>24755</AttributeId>
                  <Value>2024-12-19</Value>
                </ClassFields>
                <ClassFields>
                  <AttributeId>13662</AttributeId>
                  <Value>проверка стринги</Value>
                </ClassFields>
                <ClassFields>
                  <AttributeId>24840</AttributeId>
                  <Value>26767144</Value>
                </ClassFields>
                <Meta>
                    <SystemId>88005353535</SystemId>
                    <MessageId>IUSMTR</MessageId>
                </Meta>
            </Request>
        </CreateMaterialOrdersProductPosition>
    </Body>
</Envelope>"""
        response = requests.post('http://192.168.6.7/10001/MaterialOrdersProductPosition.asmx',
                                 data=xml_body, headers=header)
        if response.status_code == 200:
            print('Успешно:', response.text)
        else:
            print('Ошибка:', response.status_code, response.text)

# Внутренняя функция, которая отвечает за перевод заявок в работу из статуса "Зарегистрировано"
    def test_ProvideMaterialOrdersProductPosition(self):
        header = {'Content-Type': 'text/xml; charset=utf-8',
                  'Authorization': f'Basic {Authorization.authorization_adapter(self)}'}
        xml_body = f"""<Envelope xmlns="http://schemas.xmlsoap.org/soap/envelope/">
    <Body>
        <ProvideMaterialOrdersProductPosition xmlns="http://tempuri.org/">
            <Request>
                <OrderId>5749</OrderId>
                <Comment>5728</Comment>
                <Meta>
                    <SystemId>1</SystemId>
                    <MessageId>1</MessageId>
                </Meta>
            </Request>
        </ProvideMaterialOrdersProductPosition>
    </Body>
</Envelope>"""
        response = requests.post('http://192.168.6.7/10001/MaterialOrdersProductPosition.asmx',
                                 data=xml_body, headers=header)

        if response.status_code == 200:
            print('Успешно:', response.text)
        else:
            print('Ошибка:', response.status_code, response.text)

#Обновление заявки по указанному идентификатору из внешней системы.
    def test_UpdateMaterialOrdersProductPosition(self):
        header = {'Content-Type': 'text/xml; charset=utf-8',
                  'Authorization': f'Basic {Authorization.authorization_adapter(self)}'}
        xml_body = f"""<Envelope xmlns="http://schemas.xmlsoap.org/soap/envelope/">
    <Body>
        <UpdateMaterialOrdersProductPosition xmlns="http://tempuri.org/">
            <Request>
                <OrderId>6134</OrderId>
                <IsAutoProvidingMaterialOrders>true</IsAutoProvidingMaterialOrders>
                <OrderFields>
                    <SupDoc>ЛОГ.txt</SupDoc>
                    <RefGroup>70543135</RefGroup>
                    <Producer>Производитель</Producer>
                    <Comment>Комментарий</Comment>
                    <ObjectCode>70646865</ObjectCode>
                    <CustomerDo>Наименование дочерней организации заказчика</CustomerDo>
                </OrderFields>
               <ClassFields>
                  <AttributeId>24365</AttributeId>
                  <Value>true</Value>
                </ClassFields>

                <!-- Проверка DATETIME -->
                <ClassFields>
                  <AttributeId>24755</AttributeId>
                  <Value>2025-12-19</Value>
                </ClassFields>

                <!--Проверка string  -->
                <ClassFields>
                  <AttributeId>24592</AttributeId>
                  <Value>проверкаа UpdateMaterialOrdersProductPosition</Value>
                </ClassFields>

                <!-- Значение для выбора из справочника берется из урла https://esmtr24.sdi-solution.ru/content/classifier?classifierId=325&treeItemId=26767144&tableItemId=-1  -->
                <ClassFields>
                  <AttributeId>24840</AttributeId>
                  <Value>26767144</Value>
                </ClassFields>

                <Meta>
                    <SystemId>88005353535</SystemId>
                    <MessageId>IUSMTR</MessageId>
                </Meta>
            </Request>
        </UpdateMaterialOrdersProductPosition>
    </Body>
</Envelope>"""
        response = requests.post('http://192.168.6.7/10001/MaterialOrdersProductPosition.asmx',
                                 data=xml_body, headers=header)

        if response.status_code == 200:
            print('Успешно:', response.text)
        else:
            print('Ошибка:', response.status_code, response.text)