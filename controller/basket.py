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

                print('the json recieved =======================')

                # print(jsonify_new_url['widgets']['list_data'][value]['title'], '== ',
                #       jsonify_new_url['widgets']['list_data'][value]['value'])  # metrage

                if jsonify_new_url['widgets']['list_data'][value]['title'] == 'متراژ':
                    size_amount = jsonify_new_url['widgets']['list_data'][value]['value']

                if jsonify_new_url['widgets']['list_data'][value - 1]['title'] == 'تعداد اتاق':
                    rooms_num = jsonify_new_url['widgets']['list_data'][value - 1]['value']

                if jsonify_new_url['widgets']['list_data'][value - 3]['title'] == 'سال ساخت':
                    build_year = jsonify_new_url['widgets']['list_data'][value - 3]['value']

                if jsonify_new_url['widgets']['list_data'][value - 4]['title'] == 'نوع آگهی':
                    type = jsonify_new_url['widgets']['list_data'][value - 4]['value']

                print('the announcement recieved')

                # print(jsonify_new_url['widgets']['list_data'][value - 1]['title'], '== ',
                #       jsonify_new_url['widgets']['list_data'][value - 1]['value'])  # tedad otagh
                # print(jsonify_new_url['widgets']['list_data'][value - 3]['title'], '== ',
                #       jsonify_new_url['widgets']['list_data'][value - 3]['value'])  # sal sakht
                # print(jsonify_new_url['widgets']['list_data'][value - 4]['title'], '== ',
                #       jsonify_new_url['widgets']['list_data'][value - 4]['value'])  # noe agahi

                get_contact = requests.get(new_url + '/contact')
                phone_number = get_contact.json()['widgets']['contact']['phone']
                print('The contact recived =======================')

                announcement_obj = Announcement(title=title, description=desc, mobile_number=phone_number,
                                                size_amount=size_amount, type=type, build_year=build_year,
                                                rooms_num=rooms_num, market="Divar")

                # announcement_obj = Announcement(id=2, title='title', description='desc', mobile_number=phone_number,
                #                                 size_amount='size_amount', type='type', build_year='build_year',
                #                                 rooms_num='rooms_num', market="Divar")

                db.session.add(announcement_obj)
                db.session.commit()

                # print('phone_number is : ', phone_number)
                print('========================================================')
                # time.sleep(11)

            except:
                value = 5
                new_url = 'https://api.divar.ir/v5/posts/' + each['token']
                time.sleep(1)
                get_new_url = requests.get(new_url)
                jsonify_new_url = get_new_url.json()
                title = jsonify_new_url['data']['seo']['title']
                desc = jsonify_new_url['data']['seo']['description']

                print('the json recieved =======================')

                # print(jsonify_new_url['widgets']['list_data'][value]['title'], '== ',
                #       jsonify_new_url['widgets']['list_data'][value]['value'])  # metrage

                if jsonify_new_url['widgets']['list_data'][value]['title'] == 'متراژ':
                    size_amount = jsonify_new_url['widgets']['list_data'][value]['value']

                if jsonify_new_url['widgets']['list_data'][value - 1]['title'] == 'تعداد اتاق':
                    rooms_num = jsonify_new_url['widgets']['list_data'][value - 1]['value']

                if jsonify_new_url['widgets']['list_data'][value - 3]['title'] == 'سال ساخت':
                    build_year = jsonify_new_url['widgets']['list_data'][value - 3]['value']

                if jsonify_new_url['widgets']['list_data'][value - 4]['title'] == 'نوع آگهی':
                    type = jsonify_new_url['widgets']['list_data'][value - 4]['value']

                print('the announcement recieved')
                # print(jsonify_new_url['widgets']['list_data'][value - 1]['title'], '== ',
                #       jsonify_new_url['widgets']['list_data'][value - 1]['value'])  # tedad otagh
                # print(jsonify_new_url['widgets']['list_data'][value - 3]['title'], '== ',
                #       jsonify_new_url['widgets']['list_data'][value - 3]['value'])  # sal sakht
                # print(jsonify_new_url['widgets']['list_data'][value - 4]['title'], '== ',
                #       jsonify_new_url['widgets']['list_data'][value - 4]['value'])  # noe agahi

                get_contact = requests.get(new_url + '/contact')
                phone_number = get_contact.json()['widgets']['contact']['phone']
                # print('phone_number is : ', phone_number)
                print('The contact recived =======================')
                # announcement_obj = Announcement(id=that_id, title=title, description=desc, mobile_number=phone_number,
                #                                 size_amount=size_amount, type=type, build_year=build_year,
                #                                 rooms_num=rooms_num, market="Divar")

                announcement_obj = Announcement(title='title', description='desc',
                                                mobile_number=phone_number,
                                                size_amount='size_amount', type='type', build_year='build_year',
                                                rooms_num='rooms_num', market="Divar")

                db.session.add(announcement_obj)
                db.session.commit()
                print('Added Done with information', id, title, desc, phone_number,
                      size_amount, type, build_year, rooms_num, "In divar")
                # time.sleep(11)

        return "<h1>Done man</h1>"

    return render_template('basket.html', form=form)
