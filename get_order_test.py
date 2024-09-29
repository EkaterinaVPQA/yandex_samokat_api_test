# Екатерина Попова, 21-я когорта — Финальный проект. Инженер по тестированию плюс
import sender_stand_request
import data

#тест получение заказа по его номеру
def test_positive_assert():
    order_response = sender_stand_request.post_new_order(data.order_body)
    order_track = order_response.json()["track"]
    get_response = sender_stand_request.get_order(order_track)
    assert get_response.status_code == 200

