#!/usr/bin/env python3
#-*-coding:utf-8-*-
# __datetime__
# __purpose__

from sanic.response import json
from sanic import Blueprint
reshell = Blueprint("rs",url_prefix="/rs")


@reshell.route("/")
async def remote_shell(request):
    return json({"a":"b"})