# Python imports
import time
import requests
import json
from random import randrange
from unidecode import unidecode
from controller import celery

# Flask imports
from flask import request

# Project imports
from controller import db
from controller.calculator import convert_rooms_to_number
from controller.sms import SMSAdapter
from controller.constant import *
from model.announcement import Announcement

__Author__ = "Amir Mohammad"


def change_local_ip():
    pass


# @celery.task()
def scrape_tehran(body, sleep_from=10, sleep_to=20):
    counter, value = 0, 6

    if body == 1:
        my_data = data_1
    elif body == 2:
        my_data = data_2
    elif body == 3:
        my_data = data_3
    elif body == 4:
        my_data = data_4
    else:
        my_data = data_0

    search_url = urls[0]
    adapter = SMSAdapter()
    # my_server_url = 'http://193.176.240.42:8080/api_1/insert/d1v4r'
    my_server_url = 'http://127.0.0.1:5000/api_1/insert/d1v4r'
    print('======================== button submitted ========================')

    first_request = requests.post(search_url, data=json.dumps(my_data), headers=headers)
    detail_first_request = first_request.json()['result']['post_list']
    print('Crawling {} Announcement from divar'.format(len(detail_first_request)))
    for each in detail_first_request:
        random_time = randrange(sleep_from, sleep_to)
        time.sleep(random_time)

        new_url = 'https://api.divar.ir/v5/posts/' + each['token']
        time.sleep(1)
        get_new_url = requests.get(new_url)
        jsonify_new_url = get_new_url.json()

        try:

            title = jsonify_new_url['data']['share']['title']
            desc = jsonify_new_url['data']['share']['description']
            place = jsonify_new_url['widgets']['header']['place']
            token = each['token']
            if jsonify_new_url['widgets']['list_data'][value]['title'] == 'متراژ':
                size_amount = jsonify_new_url['widgets']['list_data'][value]['value']
                size_amount = unidecode(str(size_amount))
            else:
                size_amount = '0'

            if jsonify_new_url['widgets']['list_data'][value - 1]['title'] == 'تعداد اتاق':
                rooms_num = jsonify_new_url['widgets']['list_data'][value - 1]['value']
                rooms_num = convert_rooms_to_number(rooms_num)
            else:
                rooms_num = 0

            if jsonify_new_url['widgets']['list_data'][value - 2]['title'] == 'آگهی‌دهنده':
                owner = jsonify_new_url['widgets']['list_data'][value - 2]['value']
            else:
                owner = 'Not valid data' + jsonify_new_url['widgets']['list_data'][value - 2]['title']

            if jsonify_new_url['widgets']['list_data'][value - 3]['title'] == 'سال ساخت':
                build_year = jsonify_new_url['widgets']['list_data'][value - 3]['value']
                build_year = unidecode(str(build_year))
            else:
                build_year = 0

            if jsonify_new_url['widgets']['list_data'][value - 4]['title'] == 'نوع آگهی':
                type_ = jsonify_new_url['widgets']['list_data'][value - 4]['value']
            else:
                type_ = 'Not valid data' + jsonify_new_url['widgets']['list_data'][value - 4]['title']

            try:
                lat = jsonify_new_url['widgets']['location']['latitude']
                long = jsonify_new_url['widgets']['location']['latitude']

            except:
                lat, long = 0.0, 0.0

            try:
                deposit_amount = jsonify_new_url['widgets']['list_data'][value + 1]['value']
                rent = jsonify_new_url['widgets']['list_data'][value + 2]['value']

            except:
                deposit_amount, rent = 0, 0

            get_contact = requests.get(new_url + '/contact')
            phone_number = get_contact.json()['widgets']['contact']['phone']

            information = {
                "title": title, "description": desc, "place": place, "size_amount": size_amount,
                "rooms_num": rooms_num, "owner": owner, "build_year": build_year, "type": type_,
                "lat": lat, "long": long, "deposit_amount": deposit_amount, "rent": rent,
                "phone_number": phone_number, "url": new_url, "market": "In divar", "token": token

            }

            sending = requests.post(my_server_url, data=json.dumps(information), headers=headers)
            if sending.status_code == 201:

                ann_id = sending.json()['ann_id']
                print('>>>>>>>>', ann_id, new_url, type_, owner, build_year, place,
                      '| sms send to {}'.format(phone_number))

                # adapter.send_link_divar(str(phone_number), str(ann_id))
                counter += 1
                if counter >= 24 or ann_id % 190 == 0:
                    print('Lets crawling again ...', end="\r")
                    scrape_tehran()
                    # change_local_ip()
            else:
                print('error {} occurred, please check this url'.format(sending.status_code), new_url)
                pass

        except Exception as e:
            if e == 'widgets':
                print('Error ! . Turn off the proxy ...')
            pass


def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()
