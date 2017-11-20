#!/usr/bin/env python3
#-*-coding:utf-8-*-
# __all__=""
# __datetime__="2017.11.20"
# __purpose__="自定义异常处理"

class BaseError(Exception):
    pass

class CommandError(BaseError):
    def __init__(self,message):
        self.ms = message
    def __repr__(self):
        return "Error Command : {}".format(self.ms)
