import configuration
import data
import requests

#создание заказа
def post_new_order (body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                        json=body)
order_track = post_new_order(data.order_body).json().get('track')

#получение заказа по его номеру
def get_order (track):
    return requests.get(configuration.URL_SERVICE + configuration.ORDER_TRACK_PATH + str(track))
