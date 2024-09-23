import allure
import requests
import pytest
from src.data import OderInfo, Urls

@allure.suite('Проверяем заказ самоката')
class TestOrder:

    @allure.title('Проверяем код и тело ответа при заказе самоката разных цветов - Черный, Серый, Черный и Серый, Цвет не указан')
    @pytest.mark.parametrize('colors', ['BLACK', 'GREY', 'BLACK, GREY', ''])
    def test_order_colors_scooter(self, colors):
        order_data = {
                "firstName": OderInfo.firstName,
                "lastName": OderInfo.lastName,
                "address": OderInfo.address,
                "metroStation": OderInfo.metroStation,
                "phone": OderInfo.phone,
                "rentTime": OderInfo.rentTime,
                "deliveryDate": OderInfo.deliveryDate,
                "comment": OderInfo.comment,
                "color": [colors]
        }
        response = requests.post(f"{Urls.BASE_URL}{Urls.ORDER}", json=order_data)
        assert 201 == response.status_code and 'track' in response.json()

