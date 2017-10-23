写在开始:smile:
=====

Sanic是一个和Flask有些类似的框架，作者写这个框架的目的，也是想结合Python3.5之后新出的Asyncio异步库来使Web服务器性能更加强大。它是基于惊人的底层magicstack所做的工作，也是受于这篇文章的启发，也就是[UVLoop](https://magic.io/blog/uvloop-blazing-fast-python-networking/)一种新的事件循环机制。

除了和Flask的语法比较相像之外，Sanic还支持异步的请求处理机制，也就是意味着你可以使用Python3.5之后最新、最炫酷的async/await语法，让你的代码享受无阻塞的强烈快感。

Sanic在[GitHub](https://github.com/channelcat/sanic/)上开发的。欢迎大家踊跃投稿！

Sanic立志简洁地处理问题
====
```
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
```

启动
====
![系统界面展示](https://github.com/PythonScientists/sanic_tutorial/blob/master/sanic_img/2017-10-24-052444_1021x989_scrot.png)

指导
====
>下面本来没想翻译，因为是作者原本的API想法，感觉翻译了对大家也没什么帮助，但是为了“中国人”更好的有`读`的冲动，我也尝试着翻译下

* Getting Started（开始）
* RoutingRequest parameters （路由系统）
  * `HTTP` request types（http请求类型）
  * The `add_route` method（装饰器app.route调用的方法）
  * URL building with `url_for`（url构建的方法）
  * WebSocket routes （wb式的url参数）

* Request Data （请求数据） 
    * Accessing values using `get` and `getlist`（两个api请求方法）

* Response （响应类型）
  * Plain Text（简称text,就是普通文本）
  * HTML（不用多说了把）
  * JSON（更熟悉了）
  * File（类似获取文件）
  * Streaming（获取流数据，当数据量比较大时很好用）
  * File Streaming（文件流，比如调用方法下载表格文件）
  * Redirect（定向重导）
  * Raw（行）
  * Modify headers or status（自定义http头部和状态）

* Static Files（静态文件，感觉应该是模板之类）
* Exceptions（错误处理）
  * Throwing an exception（自定义抛出错误）
  * Handling exceptions（内部解决错误）
  * Useful exceptions（常用错误）

* Middleware And Listeners（中间件和监听器）
  * Middleware（中间件）
  * Modifying the request or response（修改器，还不知道是什么）
  * Responding early（还不懂）
  * Listeners（监听器）

* Blueprints（很熟悉的蓝图，类似flask）
  * My First Blueprint
  * Registering blueprints(建好蓝图之后还得注册蓝图)
  * Using blueprints（如何使用蓝图）
  * Start and stop（蓝图的开关）
  * Use-case: API versioning（API模式，也是flask常见的用法，模块隔离）
  * URL Building with `url_for`（实战咯）

* Configuration（配置文件）
  * Basics（基本）
  * Loading Configuration（如何加载）
  * Builtin Configuration Values（内建的配置值）

* Cookies（大家都不陌生吧）
  * Reading cookies（读取）
  * Writing cookies（写入）
  * Deleting cookies（删除）（很全）

* Handler Decorators（处理装饰器）
  * Authorization Decorator（验证装饰器）

* Streaming（流）
  * Request Streaming（请求流）
  * Response Streaming（响应流）

* Class-Based Views（类模板，不知道大家在flask有没有用过）
  * Defining views(定义一个)
  * URL parameters（url参数化）
  * Decorators（装饰器）
  * Using CompositionView

* Custom Protocols(自定义协议)
  * Example

* SSL Example（ssl实例）
* LoggingQuick （日志快速配置）
  * Start
  * Configuration

* Testing
* pytest-sanic（pytest的sanic版本）
* Deploying（部署方法）
  * Workers（相当于开几个进程）
  * Running via command(命令行启动)
  * Running via Gunicorn（gunicorn启动）
  * Asynchronous support（异步支持）

* Extensions
* Contributing
  * Installation
  * Running tests
  * Pull requests!
  * Documentation
  * Warning

以下就是所有api的模板参考，模块不是很多，但是性能却极强，厉害！
* API Reference
  * Submodules
  * sanic.app module
  * sanic.blueprints module
  * sanic.config module
  * sanic.constants module
  * sanic.cookies module
  * sanic.exceptions module
  * sanic.handlers module
  * sanic.log module
  * sanic.request module
  * sanic.response module
  * sanic.router module
  * sanic.server module
  * sanic.static module
  * sanic.testing module
  * sanic.views module
  * sanic.websocket module
  * sanic.worker module
  * Module contents
