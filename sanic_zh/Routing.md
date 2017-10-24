路由系统
=
`app`就是`Sanic`的生成实例
```
from sanic.response import json

@app.route("/")
async def test(request):
    return json({ "hello": "world" })
```
当用户请求`http://server.url/`的时候`/`会匹配相应的处理方法就是上文`@app.route("/")`，例如上面示例中的会调用`test(request)`方法，最后返回一个`json`对象。

Sanic的处理方法都是**异步**函数，必须通过`async def`语法来定义。
###请求参数
Sanic支持请求参数。

要指定请求参数，通过角引号包裹参数，例如`<PARAM>`， 请求的参数可以作为处理函数的参数，例如：
```
from sanic.response import text
#选择响应类型，这里是text
@app.route('/tag/<tag>')
async def tag_handler(req, tag):
    return text('tag -{}'.format(tag))
```
通过`:type`还可以指定参数的类型。这个`type`可以是正则表达式。
```
from sanic.response import text

@app.route('/number/<integer_arg:int>')
async def integer_handler(request, integer_arg):
    return text('Integer - {}'.format(integer_arg))

@app.route('/number/<number_arg:number>')
async def number_handler(request, number_arg):
    return text('Number - {}'.format(number_arg))

@app.route('/person/<name:[A-z]>')
async def person_handler(request, name):
    return text('Person - {}'.format(name))

@app.route('/folder/<folder_id:[A-z0-9]{0,4}>')
async def folder_handler(request, folder_id):
    return text('Folder - {}'.format(folder_id))
```
如果请求的路由找不到，或者参数的类型不匹配，Sanic会抛出`NotFound('Requested URL {} not found.'.format(url))`的错误，客户端将会出现将会出现`404:Page not found`的错误
###HTTP请求类型
默认情况下的`URL`请求都是使用`GET`方法，但`@app.route`支持可选参数用于指定支持的请求方法类型，例如可以是`POST`请求，或者两者都有。
```
from sanic.response import text
#单独使用POST
@app.route('/post', methods=['POST'])
async def post_handler(request):
    return text('POST request - {}'.format(request.json))
#单独使用GET
@app.route('/get', methods=['GET'])
async def get_handler(request):
    return text('GET request - {}'.format(request.args))
#两者同时使用
@app.route("/both",method=["GET","POST"])
async def both(request):
  if request.method=="GET":
      return text("this is from GET")
  if request.method=="POST":
      return text("this is from POST")
```
当然，如果不想使用methods参数，可以使用简写的修饰器，例如`@app.post('/url')`或
`@app.get('/url')`：
```
from sanic.response import text

@app.post('/post')
async def post_handler(request):
    return text('POST request - {}'.format(request.json))

@app.get('/get')
async def get_handler(request):
    return text('GET request - {}'.format(request.args))
```
除了支持不同的请求方式外，还支持`host`参数，它的值可以是字符串或列表，用于限制未带host参数的请求，默认是不带host参数，用于限制以及指定ip用户访问：
```
@app.route('/get', methods=['GET'], host='example.com')
async def get_handler(request):
    return text('GET request - {}'.format(request.args))

# if the host header doesn't match example.com, this route will be used
@app.route('/get', methods=['GET'])
async def get_handler(request):
    return text('GET request in default - {}'.format(request.args))
```

###add_route方法
正如上面我们所看到的代码中，作为请求处理方法，都使用了类似`@app.route('/url')`的修饰器，但这些修饰器实际上是app.add_route方法的封装，我们也可以通过如下的方式来完成：

```
from sanic.response import text

#Define the handler functions
#自定义handler方法，也就是请求逻辑方法
async def handler1(request):
    return text('OK')

async def handler2(request, name):
    return text('Folder - {}'.format(name))

async def person_handler2(request, name):
    return text('Person - {}'.format(name))

# Add each handler function as a route
#为每个方法增加指定路由，app之前是Sanic实例
app.add_route(handler1, '/test')
app.add_route(handler2, '/folder/<name>')
app.add_route(person_handler2, '/person/<name:[A-z]>', methods=['GET'])

```

###url_for构建URL
Sanic提供一个url_for的方法，在基本的解决方法名上来统计所有的URL，这是很有用的如果你想要避免去制造一些很难编码的url路径，除此之外，你也能参考解决方法名，说起来有点绕口，然后熟悉了flask的开发者应该对这个不陌生，例如
```
@app.route('/')
async def index(request):
    # generate a URL for the endpoint `post_handler`
    url = app.url_for('post_handler', post_id=5)
    # the URL is `/posts/5`, redirect to it
    return redirect(url)


@app.route('/posts/<post_id>')
async def post_handler(request, post_id):
    return text('Post - {}'.format(post_id))
```

当使用`url_for`这个方法的时候请记住，关键字参数传递给url_for时不请求参数将包含在URL的查询字符串。例如: 
```
url = app.url_for('post_handler', post_id=5, arg_one='one', arg_two='two')
# /posts/5?arg_one=one&arg_two=two
```
 多值参数可以传递给`url_for`。例如: 
```
url = app.url_for('post_handler', post_id=5, arg_one=['one', 'two'])
# /posts/5?arg_one=one&arg_one=two
```
也有一些特殊的参数（`_anchor`，`_external`，`_scheme`，`_method`，`_server`）通过`url_for`将有特殊的URL建筑（`_method`不支持现在和将被忽略）。例如:
```
url = app.url_for('post_handler', post_id=5, arg_one='one', _anchor='anchor')
# /posts/5?arg_one=one#anchor

url = app.url_for('post_handler', post_id=5, arg_one='one', _external=True)
# //server/posts/5?arg_one=one
```
`_external`需要在`app.config`或URL传递的参数`_server`或`server_name`，如果没有的话将等于无`_external`
```
url = app.url_for('post_handler', post_id=5, arg_one='one', _scheme='http', _external=True)
# http://server/posts/5?arg_one=one
```
当指定`_schema`时，自动将`_external`置为`True`

同时传递所有参数
```
url = app.url_for('post_handler', post_id=5, arg_one=['one', 'two'], arg_two=2, _anchor='anchor', _scheme='http', _external=True, _server='another_server:8888')

# http://another_server:8888/posts/5?arg_one=one&arg_one=two&arg_two=2#anchor
```
  所有有效的参数必须通过url_for建立一个URL。如果没有提供参数，如果参数指定的类型不匹配，将抛出一个URLBuildError。

###WebSocket 路由
对于WebSocket协议的路由可以通过`@app.websocket`修饰器:
```
@app.websocket('/feed')
async def feed(request, ws):
 while True: 
    data = 'hello!' 
    print('Sending: ' + data) 
    await ws.send(data) 
    data = await ws.recv() 
    print('Received: ' + data)
```
类似的，`app.add_websocket_route`可以用于替换`@app.websocket`修饰器，例如：
```
async def feed(request, ws): 
    passapp.add_websocket_route(my_websocket_handler, '/feed')
```
[](http://fanyi.baidu.com/?aldtype=16047###)

对于一个`WebSocket`路线处理是通过请求作为第一个参数，和`WebSocket`协议对象作为第二个参数。协议对象发送`send`和`recv`方法来发送和接收数据分别。
