# Sanic_Tutorial
This is teaching the new framework--sanic, including the Chinese translation, and practical exercises（这是新版框架--sanic的教学，包含中文翻译以及实战练习）:smile:

# 近期新增项目：

```
新增github泄漏监控项目！！！
```
`

并且会写些相关的项目测试框架的性能
下面模块都会涉及到的哦
![开工！！！！](https://github.com/PythonScientists/sanic_tutorial/blob/master/sanic_img/2017-10-24-052444_1021x989_scrot.png)

首先翻译的是官方文档部分，这部分在readthcodes里面，主要在这里。

还会增加实战项目

  * Plain Text（简称text,就是普通文本）
  * HTML（不用多说了把）
  * JSON（更熟悉了）
  * File（类似获取文件）
  * Streaming（获取流数据，当数据量比较大时很好用）
  * File Streaming（文件流，比如调用方法下载表格文件）
  * Redirect（定向重导）
  * Raw（行）
  * Modify headers or status（自定义http头部和状态）

* Static Files（静态文件，感觉应该是模板之类）
* [Exceptions](https://github.com/PythonScientists/sanic_tutorial/blob/master/sanic_zh/Exceptions.md)（错误处理）
  * Throwing an exception（自定义抛出错误）
  * Handling exceptions（内部解决错误）
  * Useful exceptions（常用错误）

* [Middleware And Listeners](https://github.com/PythonScientists/sanic_tutorial/blob/master/sanic_zh/Middleware And Listeners.md)（中间件和监听器）
  * Middleware（中间件）
  * Modifying the request or response（修改器，还不知道是什么）
  * Responding early（还不懂）
  * Listeners（监听器）

* [Blueprints](https://github.com/PythonScientists/sanic_tutorial/blob/master/sanic_zh/Blueprints.md)（很熟悉的蓝图，类似flask）
  * My First Blueprint
  * Registering blueprints(建好蓝图之后还得注册蓝图)
  * Using blueprints（如何使用蓝图）
  * Start and stop（蓝图的开关）
  * Use-case: API versioning（API模式，也是flask常见的用法，模块隔离）
  * URL Building with `url_for`（实战咯）

* [Configuration](https://github.com/PythonScientists/sanic_tutorial/blob/master/sanic_zh/Configuration.md)（配置文件）
  * Basics（基本）
  * Loading Configuration（如何加载）
  * Builtin Configuration Values（内建的配置值）

* [Cookies](https://github.com/PythonScientists/sanic_tutorial/blob/master/sanic_zh/Cookies.md)（大家都不陌生吧）
  * Reading cookies（读取）
  * Writing cookies（写入）
  * Deleting cookies（删除）（很全）

* Handler Decorators（处理装饰器）
  * Authorization Decorator（验证装饰器）

* Streaming（流）
  * Request Streaming（请求流）
  * Response Streaming（响应流）

* [Class-Based Views](https://github.com/PythonScientists/sanic_tutorial/blob/master/sanic_zh/Class-Based Views.md)（类模板，不知道大家在flask有没有用过）
  * Defining views(定义一个)
  * URL parameters（url参数化）
  * Decorators（装饰器）
  * Using CompositionView

* [Custom Protocols](https://github.com/PythonScientists/sanic_tutorial/blob/master/sanic_zh/Custom Protocols.md)(自定义协议)
  * Example

* SSL Example（ssl实例）
* LoggingQuick （日志快速配置）
  * Start
  * Configuration

* Testing
* pytest-sanic（pytest的sanic版本）
* [Deploying](https://github.com/PythonScientists/sanic_tutorial/blob/master/sanic_zh/Deploying.md)（部署方法）
  * Workers（相当于开几个进程）
  * Running via command(命令行启动)
  * Running via Gunicorn（gunicorn启动）
  * Asynchronous support（异步支持）

* Extensions
* Contributing
  * Installation
  * Running tests
  * Pull requests!
  * Documentation
  * Warning

以下就是所有api的模板参考，模块不是很多，但是性能却极强，厉害！
* [API Reference](https://github.com/PythonScientists/sanic_tutorial/blob/master/sanic_zh/API.md)
  * Submodules
  * sanic.app module
  * sanic.blueprints module
  * sanic.config module
  * sanic.constants module
  * sanic.cookies module
  * sanic.exceptions module
  * sanic.handlers module
  * sanic.log module
  * sanic.request module
  * sanic.response module
  * sanic.router module
  * sanic.server module
  * sanic.static module
  * sanic.testing module
  * sanic.views module
  * sanic.websocket module
  * sanic.worker module
  * Module contents
