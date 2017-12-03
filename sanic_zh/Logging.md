# 日志系统
Sanic允许您根据基于python3 logging API的请求执行不同类型的日志记录（访问日志，错误日志）。如果你想创建一个新的配置，你应该对python3日志有一些基本的知识。
# 快速开始
一个简单的例子使用默认设置将是这样的：
```
from sanic import Sanic
from sanic.config import LOGGING

# The default logging handlers are ['accessStream', 'errorStream']
# but we change it to use other handlers here for demo purpose
LOGGING['loggers']['network']['handlers'] = [
    'accessSysLog', 'errorSysLog']

app = Sanic('test')

@app.route('/')
async def test(request):
    return response.text('Hello World!')

if __name__ == "__main__":
  app.run(log_config=LOGGING)

```
要关闭日志记录，只需分配`log_config` = None：
```
if __name__ == "__main__":
  app.run(log_config=None)

```
处理请求时会跳过调用日志记录功能。而且你甚至可以在生产中进一步提高速度：
# 配置

默认情况下，log_config参数设置为使用sanic.config.LOGGING字典进行配置。默认配置提供了几个预定义的处理程序：

-    内部（使用logging.StreamHandler）
    用于内部信息控制台输出。

-    accessStream（使用logging.StreamHandler）
    用于请求在控制台中登录信息

-    errorStream（使用logging.StreamHandler）
    用于控制台中的错误消息和追踪记录。

-    accessSysLog（使用logging.handlers.SysLogHandler）
    用于请求信息记录到系统日志。目前支持Windows（通过localhost：514），Darwin（/ var / run / syslog），Linux（/ dev / log）和FreeBSD（/ dev / log）。
    如果目录不存在，您将无法访问此属性。 （请注意，在Docker中，您必须自己启用所有功能）

-    errorSysLog（使用logging.handlers.SysLogHandler）
    对于错误消息和跟踪记录到syslog。目前支持Windows（通过localhost：514），Darwin（/ var / run / syslog），Linux（/ dev / log）和FreeBSD（/ dev / log）。
    如果目录不存在，您将无法访问此属性。 （请注意，在Docker中，您必须自己启用所有功能）

和过滤器：

-    accessFilter（使用sanic.log.DefaultFilter）
    在DEBUG，INFO和NONE（0）中只允许级别的过滤器

-    errorFilter（使用sanic.log.DefaultFilter）
    该过滤器只允许在WARNING，ERROR和CRITICAL级别

sanic中有两个记录器，如果你想创建你自己的记录配置，必须定义它：

-    sanic：
    用于记录内部消息。

-    network：
    用于记录来自网络的请求，以及来自这些请求的任何信息。

日志格式：

除了由python（asctime，levelname，message）提供的默认参数之外，Sanic还为accessFilter提供了网络记录器的附加参数：

    主机（str）
    request.ip

    请求（str）
    request.method +“”+ request.url

    状态（int）
    response.status

    字节（int）
    LEN（response.body）

默认的访问日志格式是
```
%(asctime)s - (%(name)s)[%(levelname)s][%(host)s]: %(request)s %(message)s %(status)d %(byte)d
```
