import allure
import requests
from src.data import Urls, CourierInfo, RegistrationAnswers
from src.helpers import RegisterNewCourier

@allure.suite('Проверяем создание курьера')
@allure.title('Проверяем код и текст ответа при успешном создании курьера')
def test_create_courier():
    courier_data = RegisterNewCourier.random_courier()
    response = requests.post(f"{Urls.BASE_URL}{Urls.CREATE}", data=courier_data)
    assert 201 == response.status_code and RegistrationAnswers.server_answer_code_201 == response.text

@allure.title('Проверяем код и текст ответа при создании двух курьеров с одинаковым набором данных')
def test_create_clone_courier():
    courier_data = RegisterNewCourier.random_courier()
    response = requests.post(f"{Urls.BASE_URL}{Urls.CREATE}", data=courier_data)
    response_second = requests.post(f"{Urls.BASE_URL}{Urls.CREATE}", data=courier_data)
    assert 409 == response_second.status_code and RegistrationAnswers.server_answer_code_409 == response_second.json()["message"]

@allure.title('Проверяем код и текст ответа при создании курьера без логина')
def test_create_courier_without_login():
    courier_data = {"password": CourierInfo.password, "firstName": CourierInfo.first_name}
    response = requests.post(f"{Urls.BASE_URL}{Urls.CREATE}", data=courier_data)
    assert 400 == response.status_code and RegistrationAnswers.server_answer_code_400 == response.json()["message"]

@allure.title('Проверяем код и текст ответа при создании курьера без пароля')
def test_create_courier_without_password():
    courier_data = {"login": CourierInfo.login, "firstName": CourierInfo.first_name}
    response = requests.post(f"{Urls.BASE_URL}{Urls.CREATE}", data=courier_data)
    assert 400 == response.status_code and RegistrationAnswers.server_answer_code_400 == response.json()["message"]

