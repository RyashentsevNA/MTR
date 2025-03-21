import database
from MaterialOrdersAdapter.MaterialOrdersProductPosition import MaterialOrdersProductPosition
from Common.Functions import *
from database import DataBase
import variables


class TestCreate(MaterialOrdersProductPosition):
    # Создает заявку на вкладке "Журнал заявок"
    def test_create_material_orders_product_position(self):
        self.create_material_orders_product_position()








#весь класс готов
class TestGetSubscribeInfoByExchangeClass(GetSubscribeInfoByExchangeClass):
    def test_get_subscribe_info_by_exchange_class(self):
        assert variables.test_get_subscribe_info_by_exchange_class_var == self.get_subscribe_info_by_exchange_class()


#весь класс готов
class TestClearMessages(ClearMessages, DataBase):
# Функция предназначена для очистки обработанных(state_code="SUCCESS") записей таблицы MESSAGE_TRACKING_INFO. ест создает запись  БД со state_code = "SUCCESS" и  запускает функцию clear_masseges, проверяет что запись удалена
    def test_clear_masseges_func_with_state_code_success(self):
        self.database_insert(state_code="SUCCESS")
        assert variables.assertion_success in self.database_select()
        self.clear_masseges_func()
        assert variables.assertion_success not in self.database_select()

# Функция предназначена для очистки необработанных(state_code="WAITING"), но просроченных записей таблицы MESSAGE_TRACKING_INFO. Тест создает запись  БД со state_code = "WAITING" и  устанавливает для записи дату 1111-11-11,  запускает функцию clear_masseges, проверяет что запись удалена
    def test_clear_masseges_func_with_state_code_waiting(self):
        self.database_insert(state_code="WAITING")
        assert variables.assertion_waiting in self.database_select()
        self.clear_masseges_func()
        assert variables.assertion_waiting not in self.database_select()

#Кейс создает запись в БД со state_code = "WAITING" и  текущей датой, запускает функцию clear_masseges, проверяет что запись есть, устанавливает для записи дату 1111-11-11, запускает функцию clear_masseges, проверяет что запись удалена
    def test_clear_masseges_func_with_state_code_waiting_and_now_date(self):
        self.database_insert(state_code = "WAITING", request_dates = database.time)
        self.clear_masseges_func()
        assert self.database_select(query_param = f"where request_date = '{str(database.time)}'") is not []
        self.database_update(sql_query="UPDATE public.message_tracking_info SET request_date = '1111-11-11 11:11:11.111' WHERE request_id='autotest_request_ids' AND item_id='autotest_item_id';")
        self.clear_masseges_func()
        assert variables.assertion_waiting not in self.database_select()
