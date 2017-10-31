静态文件和目录，如图像文件，是由Sanic在注册的`app.static`方法。该方法以一个端点URL和文件名。指定的文件将可通过给定端点。
```
from sanic import Sanic
app = Sanic(__name__)

# Serves files from the static folder to the URL /static
app.static('/static', './static')

# Serves the file /home/ubuntu/test.png when the URL /the_best.png
# is requested
app.static('/the_best.png', '/home/ubuntu/test.png')

app.run(host="0.0.0.0", port=8000)
```
 注：目前不能使用`url_for`静态文件创建一个URL。 
其实也没必要用`url_for`那么麻烦
