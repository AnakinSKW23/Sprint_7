import allure
import requests
from src.data import CourierInfo, Urls, LoginAnswers

@allure.suite('Проверяем вход в личный кабинет курьера')
class TestLoginCourier:

    @allure.title('Проверяем код и тело ответа при входе в существующий личный кабинет курьера')
    def test_login_courier(self):
        courier_data = {
            'login': CourierInfo.login,
            'password': CourierInfo.password
        }
        response = requests.post(f"{Urls.BASE_URL}{Urls.LOG_IN}", data=courier_data)
        assert 200 == response.status_code and 'id' in response.json()

    @allure.title('Проверяем код и тело ответа при входе в существующий личный кабинет курьера без логина')
    def test_login_courier_without_login(self):
        courier_data = {
            'password': CourierInfo.password
        }
        response = requests.post(f"{Urls.BASE_URL}{Urls.LOG_IN}", data=courier_data)
        assert 400 == response.status_code and LoginAnswers.server_answer_code_400 == response.json()["message"]

    @allure.title('Проверяем код и тело ответа при входе в существующий личный кабинет курьера без пароля')
    def test_login_courier_without_password(self):
        courier_data = {
            'login': CourierInfo.login
        }
        response = requests.post(f"{Urls.BASE_URL}{Urls.LOG_IN}", data=courier_data)
        assert 400 == response.status_code and LoginAnswers.server_answer_code_400 == response.json()["message"]

    @allure.title('Проверяем код и тело ответа при входе в существующий личный кабинет курьера с неверным логином')
    def test_login_courier_wrong_login(self):
        courier_data = {
            'login': 'Какделанья',
            'password': CourierInfo.password
        }
        response = requests.post(f"{Urls.BASE_URL}{Urls.LOG_IN}", data=courier_data)
        assert 404 == response.status_code and LoginAnswers.server_answer_code_404 == response.json()["message"]

    @allure.title('Проверяем код и тело ответа при входе в существующий личный кабинет курьера с неверным паролем')
    def test_login_courier_wrong_password(self):
        courier_data = {
            'login': CourierInfo.login,
            'password': '7777'
        }
        response = requests.post(f"{Urls.BASE_URL}{Urls.LOG_IN}", data=courier_data)
        assert 404 == response.status_code and LoginAnswers.server_answer_code_404 == response.json()["message"]

