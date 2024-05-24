# Екатерина Сомова,   16-я когорта - Финальный проект. Инженер по тестированию плюс
import requests
import configuration
import data

def post_new_order():
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
           json=data.order_body)


def get_order_info(track_number):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_INFO,
           params={"t": track_number})

def get_track_number_of_order():
    track_number = post_new_order()
    return track_number.json()["track"]

def test_create_and_track_order():
    track_number = get_track_number_of_order()
    get_response = get_order_info(track_number)
    assert get_response.status_code == 200