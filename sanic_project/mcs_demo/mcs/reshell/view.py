#!/usr/bin/env python3
#-*-coding:utf-8-*-
# __datetime__
# __purpose__

from sanic.response import json,text
from sanic import Blueprint
import paramiko
from ..SharedPool import Host_Set

reshell = Blueprint("rs",url_prefix="/rs")

#登录远程客户端

"""
:param None
:return s实例，直接运行命令
"""


class PSsh:
    def __init__(self):
        self.cfg = [Host_Set.host_list()[i] for i in Host_Set.hl if i in Host_Set.host_list().keys()][0]

    def r_ssh(self):
        key = paramiko.RSAKey.from_private_key_file(self.cfg["key"])
        s = paramiko.SSHClient()
        s.load_system_host_keys()
        s.connect(hostname=self.cfg["hostname"],port=self.cfg["port"],pkey=key)
        return s

    def __call__(self,command):
        s = self.r_ssh()
        stdin, stdout, stderr = s.exec_command(command)
        r = stdout
        return r.read().decode("utf-8")


@reshell.route("/")
async def remote_shell(request):
    r = PSsh()
    result = r("hostname")
    return json({"主机信息":result})
