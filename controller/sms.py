#!/usr/bin/env python
# Python imports
import json
import requests

# Flask imports

# Project imports
from controller.environ import SEND_SMS_URL, SEND_SMS_VERIFY

__Author__ = "Amir Mohammad"


class SMSAdapter(object):
    def __init__(self):
        pass

    def send_sms(self, receptor, message):
        res = requests.post(
            url=SEND_SMS_URL,
            data={
                'receptor': receptor,
                'message': message,
            }
        )
        res = json.loads(res.text)
        if res['return'] and res['return']['status']:
            data = {'status': res['return']['status']}
        else:
            data = {'status': 500}
        print(data)
        return data

    def send_verified_message(self, receptor, token, template):
        res = requests.post(
            url=SEND_SMS_VERIFY,
            data={
                'receptor': receptor,
                'token': token,
                'template': template
            }
        )
        res = json.loads(res.text)
        if res['return'] and res['return']['status']:
            data = {'status': res['return']['status']}
        else:
            data = {'status': 500}
        return data

    def send_verify_sms(self, destination_number, verification_code):
        data = self.send_verified_message(
            destination_number,
            verification_code,
            'verifymobilenumber'
        )
        return data

    def send_announcement_status(self, destination_number, confirmed, message_or_url):
        data = self.send_verified_message(
            destination_number,
            message_or_url,
            'confirm-successful-message' if confirmed else 'confirm-fail-message'
        )
        return data

    def send_request_add_advice(self, destination_number, url):
        data = self.send_verified_message(
            destination_number,
            url,
            'requestAddAdvice'
        )
        return data

    def send_reset_password_sms(self, destination_number, code):
        data = self.send_verified_message(
            destination_number,
            code,
            'reset-password'
        )
        return data

    def send_app_link(self, destination_number):
        data = self.send_verified_message(
            destination_number,
            'https://play.google.com/store/apps/details?id=com.onlinejoo',
            'app-link'
        )
        return data

    def send_link_divar(self, destination_number, ann_id):
        my_link = 'https://www.onlinejoo.com/new/' + str(ann_id)
        data = self.send_verified_message(
            destination_number,
            my_link,
            'AcceptAnnouncement'
        )
        return data


if __name__ == '__main__':
    adapter = SMSAdapter()
    response = adapter.send_link_divar('09128020911', '123654')
    print('message sent')
