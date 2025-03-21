import requests
from config import Settings
import pprint


class ClearMessages:
    def clear_masseges_func(self):
        self.response = requests.post(f'http://192.168.6.7/{Settings.stand}/api/Test/jobs/trigger?job=CleanMessages')
        print('Функция Clear Messages завершилась с кодом ответа',self.response.status_code)


class GetSubscribeInfoByExchangeClass:
    # Функция предназначена для получения конфигурация ИС-получателей
    def get_subscribe_info_by_exchange_class(self):
        self.response = requests.get(f'http://192.168.6.7/{Settings.stand}/api/Test/common/GetSubscribeInfoByExchangeClass')
        print(f'Функция GetSubscribeInfoByExchangeClass завершилась с кодом ответа {self.response.status_code}')
        return self.response.json()