请求数据
==
当一个端点接收到一条`http`请求的时候，路由系统会将这个请求转发给相应的请求结构。
下面是`Request`这个结构的变量：
  * `json` (any) -JSON body
```
from sanic.response import json
#查看请求数据的json格式
@app.route("/json")
def post_json(request):
    return json({ "received": True, "message": request.json })
```
  * `args` (dict) -查询字符变量，一个查询字符串是一个
 类似于URL的部分`?key1=value1&key2=value2` ， 如果URL被解析，`args`字典会像`{ 'key1”：[ 'value1”]，“”：[ 'value2 KEY2 ] }`。请求的`query_string`变量持有的未解析的字符串值。 
```
from sanic.response import json
#查看请求子串
@app.route("/query_string")
def query_string(request):
    return json({ "parsed": True, "args": request.args, "url": request.url, "query_string": request.query_string })

```

  * `raw_args` (dict) - 很多例子中你会收到这个url的参数在一个很小的打包好的字典中，就像这些url`?key1=value1&key2=value2`,那么这个参数字典就像这样`{'key1': 'value1', 'key2': 'value2'}`
  * `files` (文件结构的字典)-一个有着名字，主体，类型的文件列表
```
from sanic.response import json
#查看请求的文件类型
@app.route("/files")
def post_json(request):
    test_file = request.files.get('test')
#文件就是一个完整的主体
    file_parameters = {
        'body': test_file.body,
        'name': test_file.name,
        'type': test_file.type,
    }

    return json({ "received": True, "file_names": request.files.keys(), "test_file_parameters": file_parameters })
```
  * `form` (字典) -传输表单变量
```
from sanic.response import json
#表单提交数据
@app.route("/form")
def post_json(request):
    return json({ "received": True, "form_data": request.form, "test": request.form.get('test') })

```
  
* `body` (字节) 原始数据。此属性允许检索请求的原始数据，而不考虑内容类型。 
```
from sanic.response import text

@app.route("/users", methods=["POST",])
def create_user(request):
    return text("You are trying to create a user with the following POST: %s" % request.body)
```
  * `ip`(字符) -请求者的ip地址
  * `app` - 指的是处理这个请求的Sanic应用对象。这对于在没有访问全局应用程序对象的模块中的蓝图或其他处理程序中非常有用。 
```
from sanic.response import json
from sanic import Blueprint

bp = Blueprint('my_blueprint')
#类似于flask里的请求钩子
@bp.route('/')
async def bp_root(request):
    if request.app.config['DEBUG']:
        return json({'status': 'debug'})
    else:
        return json({'status': 'production'})
```
  * `url`: 完整的请求的url地址, ie: `http://localhost:8000/posts/1/?foo=bar`

  * `scheme`: 和请求相关联的方案: `http` or `https`

  * `host`: 和请求相关联的域名: `localhost:8080`

  * `path`:请求的路径:` /posts/1/`

  * `query_string`: 请求的查询子串: `foo=bar` or a blank string ''

  * `uri_template`: 路由解决的模板: `/posts/<id>/`

用`get` 和 `getlist`来获取变量
===

 请求属性返回一个字典实际上返回一个子类，叫RequestParameters。关键的区别使用这个对象时`get`和`getlist`之间的区别。 
  * `get(key, default=None)`  正常运行，但当给定键的值为列表时，只返回第一个项。 
  * `getlist(key, default=None)`  正常操作，返回整个列表。 

```
from sanic.request import RequestParameters

args = RequestParameters()
args['titles'] = ['Post 1', 'Post 2']

args.get('titles') # => 'Post 1'

args.getlist('titles') # => ['Post 1', 'Post 2']

```
