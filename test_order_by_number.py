import sender_stand_request


# Функция для позитивной проверки
def positive_assert():
    # В переменную order_response сохраняется результат запроса на получение заказа по трек-номеру
    order_response = sender_stand_request.get_order_on_number()
    assert order_response.status_code == 200


def test_order_on_number_get_response_200():
    positive_assert()
