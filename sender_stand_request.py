import configuration
import requests
import data

# Виктория Краснова, 8а когорта — Финальный проект. Инженер по тестированию плюс
# Функция создания заказа и сохранения трек-номера заказа
def post_create_order(order_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH, json=order_body)

# Cохраняем трек-номера заказа
track_number = post_create_order(data.order_body).json()["track"]

# Функция для получения заказа по трек-номеру
def get_order_by_number(track_number):
    return requests.get(configuration.URL_SERVICE + configuration.ORDER_TRACK_PATH + str(track_number))

# Получаем данные о заказе по трек-номеру
def test_get_order_by_number():
    data_order = get_order_by_number(track_number)
    # Проверяем, что код ответа равен 200
    assert data_order.status_code == 200
