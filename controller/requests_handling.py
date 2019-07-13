# Python imports
import requests
import json
import time

#
# # Flask imports
#
# # Project imports
# # from model.announcement import Announcement
#
# from controller.sms import SMSAdapter
__Author__ = "Amir Mohammad"

urls = ['https://search.divar.ir/json/', 'https://api.divar.ir/v5/posts/AXobNwZ1',
        'https://api.divar.ir/v5/posts/AXobNwZ1/contact']

# data = {"jsonrpc": "2.0", "id": 1, "method": "getPostList", "params": [
#     [["place2", 0, ["1"]], ["cat3", 0, [210]], ["cat2", 0, [209]], ["cat1", 0, [143]], ["query", 0, ["ØªÙØ±Ø§Ù"]],
#      ["v01", 1, ["100", "200"]]], 0]}

estate_agent_data = {"jsonrpc": "2.0", "id": 1, "method": "getPostList",
        "params": [[["place2", 0, ["1"]], ["cat1", 0, [143]], ["v05", 0, ["1"]]], 0]}

data = {"jsonrpc": "2.0", "id": 1, "method": "getPostList",
                     "params": [[["place2", 0, ["1"]], ["cat1", 0, [143]], ["v05", 0, ["-100"]]], 0]}

headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

# r = requests.post(urls[0], data=json.dumps(data), headers=headers)
# amir = r.json()['result']['post_list']
# for each in amir:
#
#     try:
#         value = 6
#         print('in try')
#         new_url = 'https://api.divar.ir/v5/posts/' + each['token']
#         time.sleep(1)
#         r = requests.get(new_url)
#         b = r.json()
#         print('title is : ', b['data']['seo']['title'])
#         print('description is : ', b['data']['seo']['description'])
#         print(b['widgets']['list_data'][value]['title'], '== ', b['widgets']['list_data'][value]['value'])  # metrage print(b['widgets']['list_data'][value - 1]['title'], '== ', b['widgets'][
#         print(b['widgets']['list_data'][value-1]['title'], '== ', b['widgets']['list_data'][value-1]['value'])  # metrage print(b['widgets']['list_data'][value - 1]['title'], '== ', b['widgets'][
#         print(b['widgets']['list_data'][value-2]['title'], '== ', b['widgets']['list_data'][value-2]['value'])  # metrage print(b['widgets']['list_data'][value - 1]['title'], '== ', b['widgets'][
#         print(b['widgets']['list_data'][value-3]['title'], '== ', b['widgets']['list_data'][value-3]['value'])  # metrage print(b['widgets']['list_data'][value - 1]['title'], '== ', b['widgets'][
#         print(b['widgets']['list_data'][value-4]['title'], '== ', b['widgets']['list_data'][value-4]['value'])  # metrage print(b['widgets']['list_data'][value - 1]['title'], '== ', b['widgets'][
#
#         r = requests.get(new_url + '/contact')
#         aa = r.json()['widgets']['contact']['phone']
#         print('phone_number is : ', aa)
#         print('========================================================')
#         time.sleep(3)
#
#     except Exception:
#
#         value = 5
#         print('in except')
#         new_url = 'https://api.divar.ir/v5/posts/' + each['token']
#         print(new_url)
#         time.sleep(1)
#         print('url is :', new_url)
#         r = requests.get(new_url)
#         b = r.json()
#         # print('title is : ', b['data']['seo']['title'])
#         # print('description is : ', b['data']['seo']['description'])
#         # print(b['widgets']['list_data'][value]['title'], '== ', b['widgets']['list_data'][value]['value'])  # metrage
#         # print(b['widgets']['list_data'][value - 1]['title'], '== ',
#         #       b['widgets']['list_data'][value - 1]['value'])  # tedad otagh
#         # print(b['widgets']['list_data'][value - 3]['title'], '== ',
#         #       b['widgets']['list_data'][value - 3]['value'])  # sal sakht
#         # print(b['widgets']['list_data'][value - 4]['title'], '== ',
#         #       b['widgets']['list_data'][value - 4]['value'])  # noe agahi
#
#
#         print('title is : ', b['data']['seo']['title'])
#         print('description is : ', b['data']['seo']['description'])
#         print(b['widgets']['list_data'][value]['title'], '== ', b['widgets']['list_data'][value]['value'])  # metrage print(b['widgets']['list_data'][value - 1]['title'], '== ', b['widgets'][
#         print(b['widgets']['list_data'][value-1]['title'], '== ', b['widgets']['list_data'][value-1]['value'])  # metrage print(b['widgets']['list_data'][value - 1]['title'], '== ', b['widgets'][
#         print(b['widgets']['list_data'][value-2]['title'], '== ', b['widgets']['list_data'][value-2]['value'])  # metrage print(b['widgets']['list_data'][value - 1]['title'], '== ', b['widgets'][
#         print(b['widgets']['list_data'][value-3]['title'], '== ', b['widgets']['list_data'][value-3]['value'])  # metrage print(b['widgets']['list_data'][value - 1]['title'], '== ', b['widgets'][
#         print(b['widgets']['list_data'][value-4]['title'], '== ', b['widgets']['list_data'][value-4]['value'])
#
#         r = requests.get(new_url + '/contact')
#         aa = r.json()['widgets']['contact']['phone']
#         print('phone_number is : ', aa)
#         print('========================================================')
#         time.sleep(3)
