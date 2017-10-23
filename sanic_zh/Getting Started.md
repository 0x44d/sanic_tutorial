#写在开始
Sanic是一个和Flask有些类似的框架，作者写这个框架的目的，也是想结合Python3.5之后新出的Asyncio异步库来使Web服务器性能更加强大。它是基于惊人的底层magicstack所做的工作，也是受于这篇文章的启发，也就是[UVLoop](https://magic.io/blog/uvloop-blazing-fast-python-networking/)一种新的事件循环机制。

除了和Flask的语法比较相像之外，Sanic还支持异步的请求处理机制，也就是意味着你可以使用Python3.5之后最新、最炫酷的async/await语法，让你的代码享受无阻塞的强烈快感。

Sanic在[GitHub](https://github.com/channelcat/sanic/)上开发的。欢迎大家踊跃投稿！

#Sanic立志简洁地处理问题
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

#启动


#指导
* Getting Started
* RoutingRequest parameters
  * HTTP request types
  * Theadd_route
  * method
  * URL building withurl_for
  * WebSocket routes

* Request Data
Accessing values using get and getlist

* Response
  * Plain Text
  * HTML
  * JSON
  * File
  * Streaming
  * File Streaming
  * Redirect
  * Raw
  * Modify headers or status

* Static Files
* Exceptions
  * Throwing an exception
  * Handling exceptions
  * Useful exceptions

* Middleware And Listeners
  * Middleware
  * Modifying the request or response
  * Responding early
  * Listeners

* Blueprints
  * My First Blueprint
  * Registering blueprints
  * Using blueprints
  * Start and stop
  * Use-case: API versioning
  * URL Building withurl_for

* Configuration
  * Basics
  * Loading Configuration
  * Builtin Configuration Values

* Cookies
  * Reading cookies
  * Writing cookies
  * Deleting cookies

* Handler Decorators
  * Authorization Decorator

* Streaming
  * Request Streaming
  * Response Streaming

* Class-Based Views
  * Defining views
  * URL parameters
  * Decorators
  * Using CompositionView

* Custom Protocols
  * Example

* SSL Example
* LoggingQuick 
  * Start
  * Configuration

* Testing
* pytest-sanic
* Deploying
  * Workers
  * Running via command
  * Running via Gunicorn
  * Asynchronous support

* Extensions
* Contributing
  * Installation
  * Running tests
  * Pull requests!
  * Documentation
  * Warning

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
