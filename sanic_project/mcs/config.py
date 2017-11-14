#!/usr/bin/env python3
#-*-coding:utf-8-*-
# __datetime__
# __purpose__

"""define different level config"""
class Config:
    pass
class DevConfig(Config):
    debug = True
class ProConfig(Config):
    pass