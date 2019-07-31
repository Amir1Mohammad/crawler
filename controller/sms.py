#!/usr/bin/env python
# Python imports
import json
import requests

# Flask imports

# Project imports
SMS_PANEL_API_KEY = '48457255443835526D536C4E5377317A6E4F645333413D3D'
SEND_SMS_VERIFY = 'https://api.kavenegar.com/v1/{}/verify/lookup.json'.format(SMS_PANEL_API_KEY)
SEND_SMS_URL = 'https://api.kavenegar.com/v1/{}/sms/send.json'.format(SMS_PANEL_API_KEY)
SMS_VERIFICATION_CODE_EXPIRED_TIME = int(5 * 60)  # 5 min
CREATE_USER_EXPIRED_TIME = 60 * 60  # 1 hour

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

    def send_verified_message_token2(self, receptor, token, token10, template):
        res = requests.post(
            url=SEND_SMS_VERIFY,
            data={
                'receptor': receptor,
                'token': token,
                'token10': token10,
                'template': template
            }
        )
        res = json.loads(res.text)
        if res['return'] and res['return']['status']:
            data = {'status': res['return']['status']}
        else:
            data = {'status': 500}

    def send_link_divar(self, destination_number, ann_id):
        my_link = 'https://www.onlinejoo.com/new/' + str(ann_id)
        return self.send_verified_message(destination_number, my_link, 'AcceptAnnouncement')

    def send_link_divar_with_place(self, destination_number, place, ann_id):
        my_link = 'https://www.onlinejoo.com/new/' + str(ann_id)
        return self.send_verified_message_token2(destination_number, place, my_link, 'AcceptAnnouncementPlace')


if __name__ == '__main__':
    adapter = SMSAdapter()
    # adapter.send_link_divar('09128020911', '123654')
    adapter.send_link_divar_with_place('09128020911', 'سعادت آباد', '123')
    print('message sent')
