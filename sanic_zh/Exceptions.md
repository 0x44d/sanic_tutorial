异常
==
在请求处理方法中的异常可以被捕获，然后自动被`Sanic`框架处理，异常会发出一个信息作为它们的第一个参数，也能返回一个状态码来作为`HTTP`请求的响应。

抛出异常
===
为了捕获一个异常，很简单地抛出一个异常来自`Sanic.exceptions`模块的相关异常。
例如：
```
from sanic.exceptions import ServerError

@app.route('/killme')
def i_am_ready_to_die(request):
    raise ServerError("Something bad happened", status_code=500)
```
你也可以使用`abort`这个功能来抛出
```
from sanic.exceptions import abort
from sanic.response import text

@app.route('/youshallnotpass')
def no_no(request):
        abort(401)
        # this won't happen
        text("OK")
```
处理异常
===


为了重载Sanic的默认的异常处理的方法，使用@app.exception装饰器，装饰器希望将一个异常列表作为参数处理。你可以通过sanicexception赶上他们！装饰异常处理函数必须将请求和异常对象作为参数。 
例如：
```
from sanic.response import text
from sanic.exceptions import NotFound

@app.exception(NotFound)
def ignore_404s(request, exception):
    return text("Yep, I totally found the page: {}".format(request.url))
```
有用的异常
====
下面列出了最有用的异常

* `Notfound`

 当找不到请求的合适路由时调用。 
* `ServerError`

当服务器出现问题时调用。如果用户代码中出现异常，通常会出现这种情况。 
可以看`sanic.exceptions`模块来查看所有的异常情况

