__Author__ = "Amir Mohammad"

urls = ['https://search.divar.ir/json/', 'https://api.divar.ir/v5/posts/AXobNwZ1',
        'https://api.divar.ir/v5/posts/AXobNwZ1/contact']

estate_agent_data = {"jsonrpc": "2.0", "id": 1, "method": "getPostList",
                     "params": [[["place2", 0, ["1"]], ["cat1", 0, [143]], ["v05", 0, ["1"]]], 0]}

data = {"jsonrpc": "2.0", "id": 1, "method": "getPostList",
        "params": [[["place2", 0, ["1"]], ["cat1", 0, [143]], ["v05", 0, ["-100"]]], 0]}

headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
