# Python imports
import time
import requests
import json
from random import randrange
from controller import celery

# Flask imports


# Project imports
from controller import db
from controller.sms import SMSAdapter
from controller.requests_handling import data, headers, urls
from model.announcement import Announcement

__Author__ = "Amir Mohammad"


@celery.task()
def my_scraper_divar_task():
    search_url = urls[0]
    adapter = SMSAdapter()

    print('======================== button submitted ========================')
    first_request = requests.post(search_url, data=json.dumps(data), headers=headers)
    detail_first_request = first_request.json()['result']['post_list']
    for each in detail_first_request:
        random_time = randrange(5, 20)
        time.sleep(random_time)
        try:
            value = 6
            new_url = 'https://api.divar.ir/v5/posts/' + each['token']
            time.sleep(1)
            get_new_url = requests.get(new_url)
            jsonify_new_url = get_new_url.json()
            title = jsonify_new_url['data']['seo']['title']
            desc = jsonify_new_url['data']['seo']['description']

            if jsonify_new_url['widgets']['list_data'][value]['title'] == 'متراژ':
                size_amount = jsonify_new_url['widgets']['list_data'][value]['value']
            else:
                size_amount = '0'

            if jsonify_new_url['widgets']['list_data'][value - 1]['title'] == 'تعداد اتاق':
                rooms_num = jsonify_new_url['widgets']['list_data'][value - 1]['value']
            else:
                rooms_num = 0

            if jsonify_new_url['widgets']['list_data'][value - 2]['title'] == 'آگهی‌دهنده':
                owner = jsonify_new_url['widgets']['list_data'][value - 2]['value']
            else:
                owner = 'Not valid data'

            if jsonify_new_url['widgets']['list_data'][value - 3]['title'] == 'سال ساخت':
                build_year = jsonify_new_url['widgets']['list_data'][value - 3]['value']
            else:
                build_year = 0

            if jsonify_new_url['widgets']['list_data'][value - 4]['title'] == 'نوع آگهی':
                type_ = jsonify_new_url['widgets']['list_data'][value - 4]['value']
            else:
                type_ = 'Not valid data'

            get_contact = requests.get(new_url + '/contact')
            phone_number = get_contact.json()['widgets']['contact']['phone']
            announcement_obj = Announcement(title=title, description=desc, url=new_url, mobile_number=phone_number,
                                            size_amount=size_amount, owner=owner, type=type_,
                                            build_year=build_year,
                                            rooms_num=rooms_num, market="Divar")

            db.session.add(announcement_obj)
            db.session.commit()
            # adapter.send_link_divar(phone_number, announcement_obj.id)
            print('>>>>>>>> ', new_url, phone_number,
                  size_amount, type_, build_year, owner, rooms_num,
                  "In divar", '| sms send to {}'.format(phone_number), "try")

        except IndexError:
            value = 5
            new_url = 'https://api.divar.ir/v5/posts/' + each['token']
            time.sleep(1)
            get_new_url = requests.get(new_url)
            jsonify_new_url = get_new_url.json()
            title = jsonify_new_url['data']['seo']['title']
            desc = jsonify_new_url['data']['seo']['description']

            if jsonify_new_url['widgets']['list_data'][value]['title'] == 'متراژ':
                size_amount = jsonify_new_url['widgets']['list_data'][value]['value']
            else:
                size_amount = 0

            if jsonify_new_url['widgets']['list_data'][value - 1]['title'] == 'تعداد اتاق':
                rooms_num = jsonify_new_url['widgets']['list_data'][value - 1]['value']
            else:
                rooms_num = 0

            if jsonify_new_url['widgets']['list_data'][value - 2]['title'] == 'آگهی‌دهنده':
                owner = jsonify_new_url['widgets']['list_data'][value - 2]['value']
            else:
                owner = 'Not valid data'

            if jsonify_new_url['widgets']['list_data'][value - 3]['title'] == 'سال ساخت':
                build_year = jsonify_new_url['widgets']['list_data'][value - 3]['value']
            else:
                build_year = 0

            if jsonify_new_url['widgets']['list_data'][value - 4]['title'] == 'نوع آگهی':
                type_ = jsonify_new_url['widgets']['list_data'][value - 4]['value']
            else:
                type_ = 'Not valid data'

            get_contact = requests.get(new_url + '/contact')
            phone_number = get_contact.json()['widgets']['contact']['phone']

            announcement_obj = Announcement(title=title, description=desc, url=new_url, mobile_number=phone_number,
                                            size_amount=size_amount, owner=owner, type=type_,
                                            build_year=build_year,
                                            rooms_num=rooms_num, market="Divar")
            db.session.add(announcement_obj)
            db.session.commit()
            # adapter.send_link_divar(phone_number, announcement_obj.id)
            print('>>>>>>>> ', new_url, phone_number,
                  size_amount, owner, type_, build_year, rooms_num,
                  "In divar", '| sms send to {}'.format(phone_number), "except")

        except IndexError:
            pass