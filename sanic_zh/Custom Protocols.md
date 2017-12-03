# 自定义协议
注意：这是高级用法，大多数读者不需要这样的功能。

您可以通过指定一个自定义协议来更改`Sanic`协议的行为，该自定义协议应该是`asyncio.protocol`的子类。这个协议可以作为关键字参数协议传递给`sanic.run`方法。

自定义协议类的构造函数从Sanic接收以下关键字参数。

-   ` loop`: an `asyncio`-compatible event loop.
一个asyncio兼容的事件循环。

-   ` connections`: a `set` to store protocol objects. When Sanic receives `SIGINT` or `SIGTERM`, it executes `protocol.close_if_idle` for all protocol objects stored in this set.
一个存储协议对象的集合。当Sanic接收到SIGINT或者SIGTERM时，它为存储在这个集合中的所有协议对象执行protocol.close_if_idle。

-   ` signal`: a `sanic.server.Signal` object with the stopped attribute. When Sanic receives `SIGINT` or `SIGTERM`, `signal.stopped` is assigned `True`.
具有停止属性的sanic.server.Signal对象。当Sanic收到SIGINT或者SIGTERM时，signal.stopped被赋值为True。

-    `request_handler`: a coroutine that takes a `sanic.request.Request` object and a` response` callback as arguments.
以sanic.request.Request对象和响应回调作为参数的协程。

-    `error_handler`: a `sanic.exceptions.Handler` which is called when exceptions are raised.
一个sanic.exceptions.Handler在异常被引发时被调用。

-   ` request_timeou`t: the number of seconds before a request times out.
请求超时之前的秒数。

-   ` request_max_size`: an integer specifying the maximum size of a request, in bytes.
an integer specifying the maximum size of a request, in bytes.
# 例子
如果处理函数没有返回`HTTPResponse`对象，则在默认协议中发生错误。

通过重写`write_response`协议方法，如果处理程序返回一个字符串，它将被转换为一个`HTTPResponse`对象。
```
from sanic import Sanic
from sanic.server import HttpProtocol
from sanic.response import text

app = Sanic(__name__)


class CustomHttpProtocol(HttpProtocol):

    def __init__(self, *, loop, request_handler, error_handler,
                 signal, connections, request_timeout, request_max_size):
        super().__init__(
            loop=loop, request_handler=request_handler,
            error_handler=error_handler, signal=signal,
            connections=connections, request_timeout=request_timeout,
            request_max_size=request_max_size)

    def write_response(self, response):
        if isinstance(response, str):
            response = text(response)
        self.transport.write(
            response.output(self.request.version)
        )
        self.transport.close()


@app.route('/')
async def string(request):
    return 'string'


@app.route('/1')
async def response(request):
    return text('response')

app.run(host='0.0.0.0', port=8000, protocol=CustomHttpProtocol)
```
