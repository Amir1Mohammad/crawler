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
from controller.calculator import convert_rooms_to_number
from controller.sms import SMSAdapter
from controller.constant import *
from model.announcement import Announcement

__Author__ = "Amir Mohammad"


# @celery.task()
def scrape_tehran(body, sleep_from, sleep_to):
    counter, value = 0, 6
    token_list = []
    size_amount, build_year, rooms_num, deposit_amount, rent, type_, owner, price = 0, 1370, 0, 0, 0, '', '', ''
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

            list_data = jsonify_new_url['widgets']['list_data']

            for each_item in list_data:
                if each_item['title'] == 'متراژ':
                    size_amount = each_item['value']
                    size_amount = unidecode(str(size_amount))

                elif each_item['title'] == 'تعداد اتاق':
                    rooms_num = each_item['value']
                    rooms_num = convert_rooms_to_number(rooms_num)

                elif each_item['title'] == 'آگهی‌دهنده':
                    owner = each_item['value']

                elif each_item['title'] == 'سال ساخت':
                    build_year = each_item['value']
                    build_year = unidecode(build_year)
                    if build_year == 'qbl z 1370':
                        build_year = 1370

                elif each_item['title'] == 'نوع آگهی':
                    type_ = each_item['value']

                elif each_item['title'] == 'قیمت':
                    price = each_item['value']

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
                "rooms_num": rooms_num, "owner": owner, "build_year": build_year, "type": type_,"body":body,
                "lat": lat, "long": long, "deposit_amount": deposit_amount, "rent": rent, "price": price,
                "phone_number": phone_number, "url": new_url, "market": "In divar", "token": token

            }

            sending = requests.post(my_server_url, data=json.dumps(information), headers=headers)
            if sending.status_code == 201:

                announcement_id = sending.json()['announcement_id']
                print('>>>>>>>>', announcement_id, new_url, type_, owner, build_year, place,
                      '| sms send to {}'.format(phone_number))

                adapter.send_link_divar_with_place(phone_number, announcement_id, place)  # send sms

                counter += 1
                if counter >= len(detail_first_request):
                    print("======================== Let's crawling again ========================", end="\r")
                    scrape_tehran(body, sleep_from, sleep_to)


            else:
                print('error {} occurred, check this url'.format(sending.status_code), new_url)
                print(sending.content)
                scrape_tehran(body, sleep_from, sleep_to)

        except Exception as e:
            if e == 'widgets':
                print('Error ! . Turn off the proxy ...')
            pass


def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()

### token until before list data upper than for
# if jsonify_new_url['widgets']['list_data'][value]['title'] == 'متراژ':
#     size_amount = jsonify_new_url['widgets']['list_data'][value]['value']
#     size_amount = unidecode(str(size_amount))
# else:
#     size_amount = '0'
#
# if jsonify_new_url['widgets']['list_data'][value - 1]['title'] == 'تعداد اتاق':
#     rooms_num = jsonify_new_url['widgets']['list_data'][value - 1]['value']
#     rooms_num = convert_rooms_to_number(rooms_num)
# else:
#     rooms_num = 0
#
# if jsonify_new_url['widgets']['list_data'][value - 2]['title'] == 'آگهی‌دهنده':
#     owner = jsonify_new_url['widgets']['list_data'][value - 2]['value']
# else:
#     owner = 'Not valid data' + jsonify_new_url['widgets']['list_data'][value - 2]['title']
#
# if jsonify_new_url['widgets']['list_data'][value - 3]['title'] == 'سال ساخت':
#     build_year = jsonify_new_url['widgets']['list_data'][value - 3]['value']
#     build_year = unidecode(str(build_year))
# else:
#     build_year = 0
#
# if jsonify_new_url['widgets']['list_data'][value - 4]['title'] == 'نوع آگهی':
#     type_ = jsonify_new_url['widgets']['list_data'][value - 4]['value']
# else:
#     type_ = 'Not valid data' + jsonify_new_url['widgets']['list_data'][value - 4]['title']
