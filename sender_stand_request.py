import configuration
import requests
import data


# Функция создания заказа и сохранения трек-номера заказа
def post_create_order(order_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH, json=order_body)


response = post_create_order(data.order_body)
print(response.status_code)
print(response.json()["track"])


# Функция для получения заказа по трек-номеру
def get_order_on_number():
    track = post_create_order(data.order_body).json()["track"]
    return requests.get(configuration.URL_SERVICE + configuration.ORDER_TRACK_PATH + str(track))


response = get_order_on_number()
print(response.status_code)
