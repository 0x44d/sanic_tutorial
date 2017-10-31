响应
==
使用在`sanic.response`模块中的方法来创建相应

纯文本
==
```
from sanic import response
#引入最普通的相应

@app.route('/text')
def handle_request(request):
    return response.text('Hello world!')
#返回一个普通的文本格式
```
Json格式
==
```
from sanic import response
#引入最普通的相应


#返回一个json格式数据
```
文件格式
==
```
from sanic import response

@app.route('/file')
async def handle_request(request):
    return await response.file('/srv/www/whatever.png')


#因为async，用await异步
```
流格式
==
```
from sanic import response

@app.route("/streaming")
async def index(request):
    async def streaming_fn(response):
        response.write('foo')
        response.write('bar')
    return response.stream(streaming_fn, content_type='text/plain')

```
文件流格式
==
对于非常大的文件来说，需要使用文件和流的组合
```
from sanic import response

@app.route('/big_file.png')
async def handle_request(request):
    return await response.file_stream('/srv/www/whatever.png')

```
重定向
==
```
from sanic import response


@app.route('/redirect')
def handle_request(request):
    return response.redirect('/json')
```
源
==
没有经过编码的元数据
```
from sanic import response


@app.route('/raw')
def handle_request(request):
    return response.raw('raw data')


```
修改头部和状态
==

若要修改头或状态代码，请将标头或状态参数传递给这些函数：
```
from sanic import response


@app.route('/json')
def handle_request(request):
    return response.json(
        {'message': 'Hello world!'},
        headers={'X-Served-By': 'sanic'},
        status=200
    )
```
