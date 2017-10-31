from sanic import Sanic
from sanic import response

app = Sanic()
app.static('/img','/root/Downloads/0')

# @app.route('/img1')
# async def img(request):
#     url = app.url_for('/img')
#     return response.redirect(url)
app.run()