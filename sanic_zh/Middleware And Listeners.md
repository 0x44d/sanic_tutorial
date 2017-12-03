# 中间件和监听组件
中间件是在对服务器的请求之前或之后执行的功能。它们可以用来修改对用户定义的处理函数的请求或响应。
此外，Sanic提供程序监听器允许您在应用程序生命周期的各个点运行代码。

#中间件

有两种类型的中间件：**请求**和**响应**。两者都是使用`@ app.middleware`装饰器声明的，装饰器的参数是一个表示其类型的字符串：`'request'`或`'response'`。响应中间件接收请求和响应作为参数。

最简单的中间件根本不修改请求或响应：
```
@app.middleware('request')
async def print_on_request(request):
    print("I print when a request is received by the server")

@app.middleware('response')
async def print_on_response(request, response):
    print("I print when a response is returned by the server")

```

#修改请求或者响应

中间件可以修改它给出的请求或响应参数，只要它不返回它。下面的例子显示了一个实际的用例。
```
app = Sanic(__name__)

@app.middleware('response')
async def custom_banner(request, response):
    response.headers["Server"] = "Fake-Server"

@app.middleware('response')
async def prevent_xss(request, response):
    response.headers["x-xss-protection"] = "1; mode=block"

app.run(host="0.0.0.0", port=8000)
```

上面的代码将按顺序应用这两个中间件。首先，中间件**custom_banner**将HTTP响应头Server更改为**Fake-Server**，第二个中间件**prevent_xss**将添加HTTP头以防止跨站点脚本攻击（XSS）。这两个函数在用户函数返回响应之后被调用。

# 提早响应

如果中间件返回一个`HTTPResponse`对象，请求将停止处理，并返回响应。如果在达到相关的用户路由处理程序之前发生这个请求，处理程序将永远不会被调用。返回响应也将阻止任何进一步的中间件运行。

#监听器

如果要在服务器启动或关闭时执行启动/拆卸代码，可以使用以下监听器：

- before_server_start
- after_server_start
- before_server_stop
- after_server_stop

这些监听器被实现为接受应用程序对象以及asyncio循环的函数的装饰器。

例如
```
@app.listener('before_server_start')
async def setup_db(app, loop):
    app.db = await db_setup()

@app.listener('after_server_start')
async def notify_server_started(app, loop):
    print('Server successfully started!')

@app.listener('before_server_stop')
async def notify_server_stopping(app, loop):
    print('Server shutting down!')

@app.listener('after_server_stop')
async def close_db(app, loop):
    await app.db.close()
```

如果您想在循环启动后安排后台任务运行，Sanic提供了add_task方法来轻松实现。
```


async def notify_server_started_after_five_seconds():
    await asyncio.sleep(5)
    print('Server successfully started!')

app.add_task(notify_server_started_after_five_seconds())


```
