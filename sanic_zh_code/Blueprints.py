#!/usr/bin/env python3
#-*-coding:utf-8-*-
# __all__=""
# __datetime__=""
# __purpose__=""

from sanic import Sanic
from sanic import Blueprint
from sanic.response import json,text


app = Sanic(__name__)
bbbb = Blueprint("a",url_prefix="/a")
@bbbb.route("/")
async  def a(request):
    return json({1:"a"})

@bbbb.middleware('request')
async def halt_request(request):
    print("I preceived by the server")
# @app.middleware('request')
# async def halt_request(request):
#     print("I print when a request is received by the server")
@app.route("/")
async  def aa(request):
    return json({1:"aa"})
app.blueprint(bbbb)
app.run()