class Urls:

    BASE_URL = 'https://qa-scooter.praktikum-services.ru/'
    CREATE = 'api/v1/courier'
    LOG_IN = 'api/v1/courier/login'
    ORDER = 'api/v1/orders'
    GET_ORDER = 'api/v1/orders'

class CourierInfo:
    login = 'SoloMid'
    password = '3344'
    first_name = 'SubZero'

class OderInfo:
    firstName = "Naruto"
    lastName = "Uchiha"
    address = "Konoha, 142 apt."
    metroStation = 4
    phone = "+7 800 355 35 35"
    rentTime = 5
    deliveryDate = "2024-09-30"
    comment = "Saske, come back to Konoha"

class RegistrationAnswers:
    server_answer_code_201 = '{"ok":true}'
    server_answer_code_409 = 'Этот логин уже используется'
    server_answer_code_400 = 'Недостаточно данных для создания учетной записи'

class LoginAnswers:
    server_answer_code_400 = 'Недостаточно данных для входа'
    server_answer_code_404 = 'Учетная запись не найдена'


