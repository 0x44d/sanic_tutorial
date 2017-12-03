#!/usr/bin/env python3
#-*-coding:utf-8-*-
# __all__=""
# __datetime__=""
# __purpose__=""
# 类视图
基于类的视图只是实现对请求的响应行为的类。它们提供了一种在相同的端点上划分不同HTTP请求类型的处理方式。端点可以被分配一个基于类的视图，而不是定义和装饰三个不同的处理函数，一个用于每个端点支持的请求类型。
# 定义视图
基于类的视图应该继承`HTTPMethodView`。然后，您可以为要支持的每个`HTTP`请求类型实现类方法。如果收到一个没有定义方法的请求，将产生`405：方法不允许的响应`。

要在端点上注册基于类的视图，将使用`app.add_route`方法。第一个参数应该是被调用的`as_view`方法定义的类，第二个参数应该是`URL`端点。

可用的方法有`get`，`post`，`put`，`patch`和`delete`。使用所有这些方法的类将如下所示。
```
from sanic import Sanic
from sanic.views import HTTPMethodView
from sanic.response import text

app = Sanic('some_name')

class SimpleView(HTTPMethodView):

  def get(self, request):
      return text('I am get method')

  def post(self, request):
      return text('I am post method')

  def put(self, request):
      return text('I am put method')

  def patch(self, request):
      return text('I am patch method')

  def delete(self, request):
      return text('I am delete method')

app.add_route(SimpleView.as_view(), '/')


```
您也可以使用异步语法。

```
from sanic import Sanic
from sanic.views import HTTPMethodView
from sanic.response import text

app = Sanic('some_name')

class SimpleAsyncView(HTTPMethodView):

  async def get(self, request):
      return text('I am async get method')

app.add_route(SimpleAsyncView.as_view(), '/')
```

# url参数
如果您需要路由指南中讨论的任何URL参数，请将其包括在方法定义中。

```
class NameView(HTTPMethodView):

  def get(self, request, name):
    return text('Hello {}'.format(name))

app.add_route(NameView.as_view(), '/<name>')
```
# 装饰器
如果你想添加任何装饰器到类，你可以设置装饰器类的变量。`as_view`被调用时，这些将被应用到类。
```
class ViewWithDecorator(HTTPMethodView):
  decorators = [some_decorator_here]

  def get(self, request, name):
    return text('Hello I have a decorator')

app.add_route(ViewWithDecorator.as_view(), '/url')
```
# 构建url
如果您希望为HTTPMethodView构建一个URL，请记住该类名将是您将传递给url_for的端点。例如：

```
@app.route('/')
def index(request):
    url = app.url_for('SpecialClassView')
    return redirect(url)


class SpecialClassView(HTTPMethodView):
    def get(self, request):
        return text('Hello from the Special Class View!')


app.add_route(SpecialClassView.as_view(), '/special_class_view')
```
# 使用组合类
作为`HTTPMethodView`的替代方法，您可以使用`CompositionView`在视图类之外移动处理函数。

每个支持的HTTP方法的Handler函数在源文件中的其他地方定义，然后使用`CompositionView.add`方法添加到视图中。第一个参数是要处理的HTTP方法列表（例如`['GET'，'POST']`），第二个参数是处理函数。以下示例显示了具有外部处理函数和内联lambda的`CompositionView`用法：
```
from sanic import Sanic
from sanic.views import CompositionView
from sanic.response import text

app = Sanic(__name__)

def get_handler(request):
    return text('I am a get method')

view = CompositionView()
view.add(['GET'], get_handler)
view.add(['POST', 'PUT'], lambda request: text('I am a post/put method'))

# Use the new view to handle requests to the base URL
app.add_route(view, '/')
```
