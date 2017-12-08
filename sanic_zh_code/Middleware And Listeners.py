#!/usr/bin/env python3
#-*-coding:utf-8-*-
# __all__=""
# __datetime__=""
# __purpose__=""

from sanic import Sanic
from sanic.response import text
app = Sanic(__name__)
import asyncio

# # 在请求发出之前打印
# @app.middleware('request')
# async def print_on_request(request):
#     print("I print when a request is received by the server")
# # 在响应回调之前打印
# @app.middleware('response')
# async def print_on_response(request, response):
#     print("I print when a response is returned by the server")
# #对响应头增加参数
# @app.middleware('response')
# async def custom_banner(request, response):
#     response.headers["Server"] = "Fake-Server"
# #对响应头增加参数
# @app.middleware('response')
# async def prevent_xss(request, response):
#     response.headers["x-xss-protection"] = "1; mode=block"

#增加后台循环任务
# async def notify_server_started_after_five_seconds():
#     await asyncio.sleep(1)
#     print('Server successfully started!')
loop = asyncio.get_event_loop()
@app.listener('after_server_start')
async def notify_server_started(app, loop):
    print('Server successfully startsdsadasded!')
# app.add_task(notify_server_started_after_five_seconds())
@app.route("/")
async def run(requests):
    a = "a"
    return text(a)
if __name__ == "__main__":
    app.run()

#区分 中间件和监听器
#中间件 主要处理响应和请求，对于这两个进行处理
#监听器 监听系统启动或者退出，执行相应其他的流程