#-*-coding:utf-8-*-
# ___auther__:"linhanqiu"
# __create_date__:2017.10.23

from sanic import Sanic
#引入框架
from sanic.response import json
#获取响应的格式，目前这是json格式
app = Sanic()
#开场实例化，确实和flask很像
@app.route("/")
#装饰器引导路由，更像了
async def test(request):
#异步！异步！很兴奋
    return json({"hello": "world"})
#用到了json了，返回json格式串
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
  #最后的启动一样像