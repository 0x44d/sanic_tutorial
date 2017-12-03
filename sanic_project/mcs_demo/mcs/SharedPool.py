#!/usr/bin/env python3
#-*-coding:utf-8-*-
# __datetime__
# __purpose__

class Host_Set:
    def __init__(self):
        pass
    hl = ["host1", "host2", "host3"]
    @staticmethod
    def host_list():
        hl_cfg = {
            "host1":{
                "username":"root",
                "hostname":"43.254.1.204",
                "port":22,
                "key":"/root/Downloads/KeyPair-85b5.pem"
                    },
            # "host2": {
            #     "username": "root",
            #     "hostname": "117.78.31.192",
            #     "port": 22,
            #     "key": "/root/Downloads/KeyPair-85b5.pem"
            # }
        }
        return hl_cfg