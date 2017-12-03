# 方法装饰器
由于Sanic处理程序是简单的Python函数，因此您可以使用类似于Flask的方式将修饰符应用于它们。一个典型的用例是当你想要一些代码在处理程序的代码执行之前运行。
# 授权装饰者
假设您要检查用户是否有权访问特定的端点。您可以创建一个包装处理函数的装饰器，在客户端有权访问资源时检查请求，并发送相应的响应。
```
from functools import wraps
from sanic.response import json

def authorized():
    def decorator(f):
        @wraps(f)
        async def decorated_function(request, *args, **kwargs):
            # run some method that checks the request
            # for the client's authorization status
            is_authorized = check_request_for_authorization_status(request)

            if is_authorized:
                # the user is authorized.
                # run the handler method and return the response
                response = await f(request, *args, **kwargs)
                return response
            else:
                # the user is not authorized. 
                return json({'status': 'not_authorized'}, 403)
        return decorated_function
    return decorator


@app.route("/")
@authorized()
async def test(request):
    return json({status: 'authorized'})
```
