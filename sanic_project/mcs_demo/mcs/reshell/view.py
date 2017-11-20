#!/usr/bin/env python3
#-*-coding:utf-8-*-
# __all__=""
# __datetime__="2017.11.20"
# __purpose__="reshell蓝图模块"

from sanic.response import json,text
from sanic import Blueprint
import re
import paramiko
from ..SharedPool import Host_Set
from ..ErrorSet import CommandError

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
        if not command.isdigit():
            s = self.r_ssh()
            stdin, stdout, stderr = s.exec_command(command)
            r = stdout
        else:
            raise CommandError(command)
        return r.read().decode("utf-8")

#本机执行远程命令
@reshell.route("/",methods=["GET"])
@reshell.route("/<command:string>",methods=["GET"])
async def remote_shell(request,command=None):
    r = PSsh()
    if not command:
        result = r("hostname")
    elif isinstance(command,str):
        try:
            result = r(command)
        except CommandError as e:
            result = repr(e)
    else:
        pass
    return json({"result":result})

