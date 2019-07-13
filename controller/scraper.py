# Python imports
import time
import requests
import json
from random import randrange

# Flask imports
from flask_login import login_required
from flask import render_template
from flask import request

# Project imports
from controller import app, db
from controller.sms import SMSAdapter
from form.option import OptionBazaar
from controller.requests_handling import data, headers, urls
from model.announcement import Announcement

__Author__ = "Amir Mohammad"


@app.route('/scrape', methods=['GET', 'POST'])
@login_required
def find_announcement():
    # First turn off any vpn or proxy

    search_url = urls[0]
    form = OptionBazaar()
    adapter = SMSAdapter()
    if form.validate_on_submit() and form.power.data:

        print('====================== button submitted ======================')
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
                print('t>>>>>>>> ', new_url, phone_number,
                      size_amount, type_, build_year, owner, rooms_num, "In divar", '| sms send to {}'.format(phone_number))
                # adapter.send_link_divar(phone_number, announcement_obj.id)

                announcement_obj.send_sms = True
                db.session.add(announcement_obj)
                db.session.commit()

            except:
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
                print('e>>>>>>>> ', new_url, phone_number,
                      size_amount, owner, type_, build_year, rooms_num, "In divar")
                # adapter.send_link_divar(phone_number, announcement_obj.id)
                print('sms has been send to {}'.format(phone_number))
                announcement_obj.send_sms = True
                db.session.add(announcement_obj)
                db.session.commit()

    return render_template('basket.html', form=form)


def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()


@login_required
@app.route('/shutdown', methods=['GET', 'POST'])
def shutdown():
    shutdown_server()
    return 'Server shutting down...'
