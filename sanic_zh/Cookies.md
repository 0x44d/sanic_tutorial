# Cookies
Cookies是在用户的浏览器内持续存在的数据片段。 Sanic可以读取和写入存储为键值对的cookie。
# 读取Cookies
用户的cookies可以通过Request对象的cookies字典访问。
```
from sanic.response import text

@app.route("/cookie")
async def test(request):
    test_cookie = request.cookies.get('test')
    return text("Test cookie set to: {}".format(test_cookie))
```
# 写Cookies
在返回响应时，可以在Response对象上设置cookie。
```
from sanic.response import text

@app.route("/cookie")
async def test(request):
    response = text("There's a cookie up in this response")
    response.cookies['test'] = 'It worked!'
    response.cookies['test']['domain'] = '.gotta-go-fast.com'
    response.cookies['test']['httponly'] = True
    return response

```
# 删除Cookies
可以在语义上或明确地删除Cookie。
```
from sanic.response import text

@app.route("/cookie")
async def test(request):
    response = text("Time to eat some cookies muahaha")

    # This cookie will be set to expire in 0 seconds
    del response.cookies['kill_me']

    # This cookie will self destruct in 5 seconds
    response.cookies['short_life'] = 'Glad to be here'
    response.cookies['short_life']['max-age'] = 5
    del response.cookies['favorite_color']

    # This cookie will remain unchanged
    response.cookies['favorite_color'] = 'blue'
    response.cookies['favorite_color'] = 'pink'
    del response.cookies['favorite_color']

    return response
```
响应cookie可以像字典值一样设置，并具有以下参数：

 -  ` expires`（datetime）：cookie在客户端浏览器上过期的时间。
 -  ` path`（字符串）：这个cookie适用的URL的子集。默认为/。
 -    `comment`（字符串）：评论（元数据）。
 -    `domain`（字符串）：指定cookie有效的域。明确指定的域必须始终以点开头。
  -   `max-age` （数字）：cookie的生存时间。

 -    `secure`（boolean）：指定cookie是否仅通过HTTPS发- 送。
 -   ` httponly`（boolean）：指定cookie是否不能被Javascript读取。

