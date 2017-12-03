# 蓝图
蓝图是可以用于应用程序内的子路由的对象。蓝图并没有向应用程序实例添加路由，而是定义了类似的方法来添加路由，然后以灵活且可插入的方式将其注册到应用程序中。

蓝图对于大型应用程序特别有用，您的应用程序逻辑可以分解为几个小组或责任区域。

# 我的第一个蓝图
以下显示了一个非常简单的蓝图，它在应用程序的根目录下注册了一个处理函数。

假设您将此文件保存为my_blueprint.py，稍后可将其导入到主应用程序中。
```
from sanic.response import json
from sanic import Blueprint

bp = Blueprint('my_blueprint')

@bp.route('/')
async def bp_root(request):
    return json({'my': 'blueprint'})
```
这会将蓝图添加到应用程序中，并注册该蓝图所定义的所有路线。在这个例子中，app.router中的注册路线如下所示：
```
[Route(handler=<function bp_root at 0x7f908382f9d8>, methods=None, pattern=re.compile('^/$'), parameters=[])]
```
# 使用蓝图
蓝图具有与应用程序实例相同的功能。
# WebSocket 路由
WebSocket处理程序可以使用@ bp.websocket装饰器或bp.add_websocket_route方法在蓝图上注册。
# 中间间
使用蓝图，您还可以在全局范围内注册中间件。
```
@bp.middleware
async def print_on_request(request):
    print("I am a spy")

@bp.middleware('request')
async def halt_request(request):
    return text('I halted the request')

@bp.middleware('response')
async def halt_response(request, response):
    return text('I halted the response')
```
# 异常

例外可以专门用于全局的蓝图。
```
@bp.exception(NotFound)
def ignore_404s(request, exception):
    return text("Yep, I totally found the page: {}".format(request.url))
```
# 静态文件
静态文件也可以被全局服务，在蓝图的前缀下
```
bp.static('/folder/to/serve', '/web/path')
```
# 开始和停止
蓝图可以在服务器的启动和停止过程中运行功能。如果以多处理器模式运行（超过1个worker），这些在worker fork之后触发。

可用的事件是：
-    `before_server_start`：在服务器开始接受连接之前执行
-    `after_server_start`：服务器开始接受连接后执行
-   ` before_server_stop`：在服务器停止接受连接之前执行
-    `after_server_stop`：在服务器停止并且所有请求完成之后执行
```
bp = Blueprint('my_blueprint')

@bp.listener('before_server_start')
async def setup_connection(app, loop):
    global database
    database = mysql.connect(host='127.0.0.1'...)

@bp.listener('after_server_stop')
async def close_connection(app, loop):
    await database.close()
```
# 用例：API版本控制
蓝图对于API版本管理非常有用，其中一个蓝图可能指向`/ v1 / <routes>`，另一个指向`/ v2 / <routes>`。

当蓝图被初始化时，它可以采用可选的url_prefix参数，该参数将被预置在蓝图上定义的所有路由上。这个特性可以用来实现我们的API版本控制方案。
```
# blueprints.py
from sanic.response import text
from sanic import Blueprint

blueprint_v1 = Blueprint('v1', url_prefix='/v1')
blueprint_v2 = Blueprint('v2', url_prefix='/v2')

@blueprint_v1.route('/')
async def api_v1_root(request):
    return text('Welcome to version 1 of our documentation')

@blueprint_v2.route('/')
async def api_v2_root(request):
    return text('Welcome to version 2 of our documentation')

```
当我们在应用程序上注册我们的蓝图时，routes / v1和/ v2现在将指向各个蓝图，允许为每个API版本创建子站点。
```
# main.py
from sanic import Sanic
from blueprints import blueprint_v1, blueprint_v2

app = Sanic(__name__)
app.blueprint(blueprint_v1, url_prefix='/v1')
app.blueprint(blueprint_v2, url_prefix='/v2')

app.run(host='0.0.0.0', port=8000, debug=True)
```
# 使用`url_for`方法来构建url
如果您希望为蓝图内的路由生成URL，请记住端点名称的格式为`<blueprint_name>.<handler_name>`。例如：
