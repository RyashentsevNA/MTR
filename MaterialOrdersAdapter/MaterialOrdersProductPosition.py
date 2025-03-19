from datetime import datetime
import datetime
import requests
from Authorization import Authorization
from config import Settings



class MaterialOrdersProductPosition(Authorization):
# Удаление указанного в запросе идентификатора заявки управлением из внешней системы (Удаляет заявку в esmtr24)
    def delete_material_orders_product_position(self):
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
        response = requests.post(f'http://192.168.6.7/{Settings.mtr_stand}/MaterialOrdersProductPosition.asmx',
                                 data=xml_body, headers=header)

        if response.status_code == 200:
            print('Успешно:', response.text)
        else:
            print('Ошибка:', response.status_code, response.text)


# Внутренняя функция, которая отвечает за создание заявок (Создает заявку в esmtr24)
    def create_material_orders_product_position(self):
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
                    <Comment>Создано автотестом ОТ {datetime.datetime.now()}</Comment>
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
        response = requests.post(f'http://192.168.6.7/{Settings.mtr_stand}/MaterialOrdersProductPosition.asmx',
                                 data=xml_body, headers=header)
        # Блок ассертов и проверок
        if response.status_code == 200:
            print('Успешно:', response.text)
        else:
            print('Ошибка:', response.status_code, response.text)

        return response.text


# Внутренняя функция, которая отвечает за перевод заявок в работу из статуса "Зарегистрировано"
    def provide_material_orders_product_position(self):
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
        response = requests.post(f'http://192.168.6.7/{Settings.mtr_stand}/MaterialOrdersProductPosition.asmx',
                                 data=xml_body, headers=header)

        if response.status_code == 200:
            print('Успешно:', response.text)
        else:
            print('Ошибка:', response.status_code, response.text)

#Обновление заявки по указанному идентификатору из внешней системы.
    def update_material_orders_product_position(self):
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
        response = requests.post(f'http://192.168.6.7/{Settings.mtr_stand}/MaterialOrdersProductPosition.asmx',
                                 data=xml_body, headers=header)

        if response.status_code == 200:
            print('Успешно:', response.text)
        else:
            print('Ошибка:', response.status_code, response.text)