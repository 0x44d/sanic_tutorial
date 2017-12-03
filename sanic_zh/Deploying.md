# 系统部署

内置Web服务器使Sanic部署变得简单。在定义sanic.Sanic的一个实例之后，我们可以使用下面的关键字参数来调用run方法：

-    主机（默认“127.0.0.1”）：主机服务器的地址。
-    端口（默认8000）：主机服务器的端口。
-    调试（默认为False）：启用调试输出（减慢服务器）。
-    ssl（默认无）：SSLContext用于工作人员的SSL加密。
-    sock（默认无）：服务器接受连接的套接字。
-    worker（默认值1）：产生的工作进程的数量。
-    循环（默认无）：与asyncio兼容的事件循环。如果没有指定，Sanic创建自己的事件循环。
-    协议（默认HttpProtocol）：asyncio.protocol的子类。
# 进程数
默认情况下，Sanic仅使用一个CPU内核监听主进程。为了加速运行速度，只需指定运行参数中的`run` 数量即可。
```
app.run(host='0.0.0.0', port=1337, workers=4)
```
Sanic将自动启动多个进程并在它们之间路由流量。我们建议尽可能多的工人，因为你有可用的核心。
# 通过命令运行
如果您喜欢使用命令行参数，则可以通过执行模块来启动Sanic服务器。例如，如果您在名为`server.py`的文件中将`Sanic`初始化为应用程序，则可以像这样运行服务器：
```
python -m sanic server.app --host=0.0.0.0 --port=1337 --workers=4
```
用这种运行sanic的方法，不需要在你的Python文件中调用app.run。如果你这样做，确保你包装它，只有当解释器直接运行时才执行。
```
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1337, workers=4)

```
# 通过Gunicorn运行

Gunicorn'Green Unicorn'是一个用于UNIX的WSGI HTTP服务器。这是一个从Ruby的Unicorn项目移植过来的前叉工作者模型。

为了运行Gunicorn的Sanic应用程序，您需要使用特殊的sanic.worker.GunicornWorker来处理Gunicorn工人级的参数：
```
gunicorn myapp:app --bind 0.0.0.0:1337 --worker-class sanic.worker.GunicornWorker
```
如果您的应用程序遭受内存泄漏，您可以将Gunicorn配置为在处理完指定数目的请求后正常重启一个工作程序。这可以是一个方便的方法来帮助限制内存泄漏的影响。
# 异步支持
如果您需要与其他应用程序（特别是循环）共享sanic进程，则这是合适的。但是请注意，这种方法不支持使用多个进程，并不是一般运行应用程序的首选方式。

这里是一个不完整的例子（请参考`run_async.py`来更实用的例子）：
```
server = app.create_server(host="0.0.0.0", port=8000)
loop = asyncio.get_event_loop()
task = asyncio.ensure_future(server)
loop.run_forever()
```
