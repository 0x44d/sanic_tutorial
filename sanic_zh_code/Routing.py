#-*-coding:utf-8-*-
# ___auther__:"linhanqiu"
# __create_date__:2017.10.23

from sanic.response import json
from sanic import Sanic
app = Sanic()
#基本请求
@app.route('/')
async def test(request):
    return json({"hello":"world"})

from sanic.response import text
#选择响应类型，这里是text
@app.route('/tag/<tag>')
async def tag_handler(req, tag):
    return text('tag -{}'.format(tag))

from sanic.response import text

@app.route('/number/<integer_arg:int>')
async def integer_handler(request, integer_arg):
    return text('Integer - {}'.format(integer_arg))

@app.route('/number/<number_arg:number>')
async def number_handler(request, number_arg):
    return text('Number - {}'.format(number_arg))

@app.route('/person/<name:[A-z]+>')
async def person_handler(request, name):
    return text('Person - {}'.format(name))

@app.route('/folder/<folder_id:[A-z0-9]{0,4}>')
async def folder_handler(request, folder_id):
    return text('Folder - {}'.format(folder_id))

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
@app.route("/both",methods=["GET","POST"])
async def both(request):
  if request.method=="GET":
      return text("this is from GET")
  if request.method=="POST":
      return text("this is from POST")


@app.post('/post')
async def post_handler(request):
    return text('POST request - {}'.format(request.json))

@app.get('/get')
async def get_handler(request):
    return text('GET request - {}'.format(request.args))

@app.route('/get', methods=['GET'], host='example.com')
async def get_handler(request):
    return text('GET request - {}'.format(request.args))

# if the host header doesn't match example.com, this route will be used
@app.route('/get', methods=['GET'])
async def get_handler(request):
    return text('GET request in default - {}'.format(request.args))

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

@app.route('/')
async def index(request):
    # generate a URL for the endpoint `post_handler`
    url = app.url_for('post_handler', post_id=5)
    # the URL is `/posts/5`, redirect to it
    return redirect(url)


@app.route('/posts/<post_id>')
async def post_handler(request, post_id):
    return text('Post - {}'.format(post_id))

if __name__ =="__main__":
    app.run()