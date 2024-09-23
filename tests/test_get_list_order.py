import allure
import requests
from src.data import Urls

@allure.suite('Проверяем возврат списка заказов')
class TestGetlistOrder:

    @allure.title('Проверяем код и тело ответа при запросе списка заказов')
    def test_get_list_order(self):
        response = requests.get(f"{Urls.BASE_URL}{Urls.GET_ORDER}")
        assert 200 == response.status_code and 'orders' in response.json()

