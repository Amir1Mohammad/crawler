# -*- coding: utf-8 -*-
__Author__ = "Amir Mohammad"

urls = ['https://search.divar.ir/json/', 'https://api.divar.ir/v5/posts/AXobNwZ1',
        'https://api.divar.ir/v5/posts/AXobNwZ1/contact']
#########################################################################################
# tehran
data_0 = {"jsonrpc": "2.0", "id": 1, "method": "getPostList",
        "params": [[["place2", 0, ["1"]], ["cat1", 0, [143]], ["v05", 0, ["-100"]]], 0]}

# shakhsi-ejare
data_1 = {"jsonrpc": "2.0", "id": 1, "method": "getPostList",
          "params": [[["place2", 0, ["1"]], ["cat2", 0, [213]], ["cat1", 0, [143]], ["v05", 0, ["1"]]], 0]}
# shakhsi-forosh
data_2 = {"jsonrpc": "2.0", "id": 1, "method": "getPostList",
          "params": [[["place2", 0, ["1"]], ["cat2", 0, [209]], ["cat1", 0, [143]], ["v05", 0, ["1"]]], 0]}

# amlak-forosh
data_3 = {"jsonrpc": "2.0", "id": 1, "method": "getPostList",
          "params": [[["place2", 0, ["1"]], ["cat2", 0, [209]], ["cat1", 0, [143]], ["v05", 0, ["2"]]], 0]}
# amlak-ejare
data_4 = {"jsonrpc": "2.0", "id": 1, "method": "getPostList",
          "params": [[["place2", 0, ["1"]], ["cat2", 0, [213]], ["cat1", 0, [143]], ["v05", 0, ["2"]]], 0]}

#########################################################################################
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

#########################################################################################
my_server_url = 'http://193.176.240.42:8080/api_1/insert/d1v4r'
# my_server_url = 'http://127.0.0.1:5000/api_1/insert/d1v4r'