# Python imports
import os
import time
import requests
import json

# Flask imports
from flask_login import login_required
from flask import render_template

# Project imports
from controller import app, db
from form.option import OptionBazaar
from controller.requests_handling import data, headers, urls
from model.announcement import Announcement

__Author__ = "Amir Mohammad"


@login_required
@app.route('/scrape', methods=['GET', 'POST'])
def find_announcement():
    # First turn off any vpn or proxy

    search_url = urls[0]
    form = OptionBazaar()

    if form.validate_on_submit() and form.power.data:

        print('button submitted ======================')
        first_request = requests.post(search_url, data=json.dumps(data), headers=headers)
        detail_first_request = first_request.json()['result']['post_list']
        for each in detail_first_request:

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

                if jsonify_new_url['widgets']['list_data'][value - 3]['title'] == 'سال ساخت':
                    build_year = jsonify_new_url['widgets']['list_data'][value - 3]['value']
                else:
                    build_year = 0

                if jsonify_new_url['widgets']['list_data'][value - 4]['title'] == 'نوع آگهی':
                    type_ = jsonify_new_url['widgets']['list_data'][value - 4]['value']
                else:
                    type_ = 'none'

                get_contact = requests.get(new_url + '/contact')
                phone_number = get_contact.json()['widgets']['contact']['phone']
                announcement_obj = Announcement(title=title, description=desc, mobile_number=phone_number,
                                                size_amount=size_amount, type=type_, build_year=build_year,
                                                rooms_num=rooms_num, market="Divar")

                db.session.add(announcement_obj)
                db.session.commit()
                print('Added Done with information', title, desc, phone_number,
                      size_amount, type_, build_year, rooms_num, "In divar")
                time.sleep(10)

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

                if jsonify_new_url['widgets']['list_data'][value - 3]['title'] == 'سال ساخت':
                    build_year = jsonify_new_url['widgets']['list_data'][value - 3]['value']
                else:
                    build_year = 0

                if jsonify_new_url['widgets']['list_data'][value - 4]['title'] == 'نوع آگهی':
                    type_ = jsonify_new_url['widgets']['list_data'][value - 4]['value']
                else:
                    type_ = 'none'

                get_contact = requests.get(new_url + '/contact')
                phone_number = get_contact.json()['widgets']['contact']['phone']

                announcement_obj = Announcement(title=title, description=desc, mobile_number=phone_number,
                                                size_amount=size_amount, type=type_, build_year=build_year,
                                                rooms_num=rooms_num, market="Divar")

                db.session.add(announcement_obj)
                db.session.commit()
                print('Added Done with information', title, desc, phone_number,
                      size_amount, type_, build_year, rooms_num, "In divar")
                time.sleep(10)

    return render_template('basket.html', form=form)
