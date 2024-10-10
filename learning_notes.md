# python flask 入门教程

[学习网站地址：Flask 入门教程](https://tutorial.helloflask.com/)

## 1. 预备知识

1. 会使用 html，css，javascript 构建简单的页面。css 可以不做了解，html 与 javascript 需要了解，并且着重了解使用 javascript 发送 Ajax 请求的部分。
2. 了解 web 的基本工作流程，尤其是 http 的基本原理。
3. python 语言基础。

## 2. Hello Flask

**这部分主要是关于如何使用 flask 构建一个简单的主页，了解 flask 是如何接受请求并返回响应的。**

### 2.1 构建主页

首先，创建虚拟环境并安装 flask 包。

```shell
$ python -m venv .venv # 在项目根目录下运行以创建虚拟环境
$ ./.venv/Script/activate # 激活虚拟环境
$ pip install flask # 安装 flask 及相关依赖包

# 如果想关闭虚拟环境，直接运行 deactivate
```

接下来，在项目根目录下创建一个 app.py 文件，作为应用程序的入口文件。app.py 中的代码如下：

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_flask():
    return "hello flask"

if __name__ == "__main__":
    app.run();
```

然后，在项目根目录下运行下面的命令：

```shell
$ python app.py # 启动服务器
```

最后，打开浏览器，在网址中输入 `http://localhost:5000/` 就可以看到浏览器页面上会显示一行字 `hello flask`。

### 2.2 细致分析

接下来逐行解释上面的代码。

```python
from flask import Flask
```

从 flask 包中导入 Flask 构造函数。

```python
app = Flask(__name__)
```

使用 Flask 构造函数构造出一个 app 对象，代表整个应用程序。

```python
@app.route("/")
```

`@app.route()` 是一个 python 装饰器，用来将一个 python 的普通函数装饰成一个特殊函数，这个特殊函数可以用来接收请求并返回响应。这个装饰器接收一个必选参数和一系列的可选参数。这个必选参数是一个字符串，表示 url。如果浏览器请求的 url 和这个装饰器的 url 匹配，那么被装饰的函数就会调用。

---

_什么是 url？_

_url(Uniform Resouce Locator) 指的是统一资源定位符，是互联网上用来定位资源的唯一标识，也就是我们通常说的网址。通常由以下部分构成：`[协议]://[ip地址]:[端口号]/[资源在主机中的路径]?[查询参数]#[锚点链接]`_。

_`[协议]`：http（超文本传输协议），https（加密的超文本传输协议）_

_`[ip地址]`：网络中一台主机的标识。ipv4，即 ip4 版本为 32 位二进制数，每八位以点分隔，每八位为一个字节并使用十进制数（0~255）表示。例如：`0111111.00000000.00000000.00000001`即`127.0.0.1`代表环回地址。ipv6 暂不考虑。_

_`[端口号]`：端口号为主机中的网络应用程序的编号。如果主机中的一个网络应用程序进程需要使用网络收发数据，那么操作系统就要为这个进程分配一个端口号。端口号范围是 0 ~ 65535。其中，0 ~ 1023 这些端口是知名端口，即已经被固定分配给了某些服务，其他服务不可占用。例如 http 服务的 80 端口，ssh 远程链接服务的 22 端口等。1024 ~ 49151 这些端口是用户端口，用户和企业可以为自己的网络应用程序申请使用这些的端口。49152 ~ 65535 这些端口是动态端口，不固定分配给某个服务，很多服务都可以使用。_

_`[资源在主机中的路径]`：定位到了具体主机的具体网络应用程序之后，我们还需要知道请求的资源的具体路径。对于静态资源，该路径为`/静态资源路径/静态资源名称`，对于某个服务，该路径为`/具体服务路径`。这个`/具体服务路径`就是上述`@app.route()`装饰器中的字符串参数。_

_`[查询参数]`：查询参数是浏览器在发送请求时可以携带的额外信息。服务器在解析请求时可以拿到并使用这些信息。格式为`?参数名1=参数值1&参数名2=参数值2&...`，以`?`开头，以`&`分隔，数量不限，值的类型为字符串。_

_`[锚点链接]`：锚点链接指的是请求的内容在资源内部的具体定位，当我们想要请求某个资源的具体内容时，可以使用它。_

_其中，协议，ip 地址，端口号和资源路径是必须的，剩下的可以不用设置。_

---

```python
def hello_flask():
    return "hello flask"
```

一个普通的函数，在被`@app.route()`装饰后，其返回值可以作为响应传回浏览器。该例子将`"hello flask"`字符串传回给前端，我们还可以返回其它类型的数据。

```python
import json

# ...

def hello_flask1():
    return json.dumps({"name": "Sallie Santiago", "age": 18});
```

可以返回 json 数据

```python
def hello_flask2():
    return "<h1>Hello Flask</h1>";
```

可以返回 html 模板

```python
if __name__ == "__main__":
    app.run();
```

启动 app.py，如果没有传递参数，表示默认启动在 ip 为 127.0.0.1，端口为 5000 上。我们可以传递参数来指定它的启动方式。

```python
if __name__ == "__main__":
    # 表示在ip 0.0.0.0，端口 5001 上以debug模式启动。debug可以进入监视模式，当文件发生变化时自动重启。
    app.run("0.0.0.0", 5001, debug=True)
```

### 2.3 请求响应过程

接下来梳理一下当我们在浏览器上输入网址到页面呈现在浏览器上时都发生了什么（这里只是大致过程，细究则需要深入计算机网络）。

首先，当我们输入网址`http://localhost:5000/`时，浏览器首先将这个网址包装成 http 请求报文，然后通过 ip 地址 localhost（127.0.0.1）在互联网中找到服务器主机（在这里就是本机）并将报文发送给服务器，服务器收到报文后根据端口号（在这里就是 5000）将其交给对应的网络应用程序（在这里就是 app.py），然后网络应用程序解包并根据资源路径（在这里就是"/"）找到对应的静态资源或服务（在这里就是`@app.route("/")`装饰的 python 函数）。然后该服务被调用，并将其返回值包装成 http 响应报文，`"hello flask"`字符串在响应体部分，并以相反的过程返回给浏览器。浏览器收到后解包并取出响应体部分的数据解析并显示在页面上。

### 2.4 延申部分

`@app.route("/")`这个装饰器，又被称作后端路由，或者后端接口。这个字符串`"/"`又被称作路由规则或者 url 规则。我们可以修改这个路由规则来进行多样化的服务。

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Hello, this is home page</h1>"

@app.route("/profile")
def profile():
    return '{"username": "Kathryn Stephens", userId: "a4bd0a54-c6b6-51cb-802b-867c8a214750"}'

@app.route("/orders")
def orders():
    return '[{"productId": 1, "productName": "pens"}, {"productId": 2, "productName": "shoes"}]'

if __name__ == "__main__":
    app.run()
```

`"/"`这个路由规则通常情况下是根路由，用户请求根路由资源一般应该返回应用程序的主页面。例如在这个例子中，用户输入网址`http://localhost:5000/`，服务器就会根据这个网址的资源路径`"/"`匹配相应的路由规则`"/"`，调用对应的`index()`服务，并返回一个 html 标题标签响应给浏览器，浏览器获得这个响应之后会解析并渲染这个标题标签，在页面上就会出现一个`hello, this is home page`的一级大标题。注意，网址`http://localhost:5000`和`http://localhost:5000/`是一样的，都是请求根路由资源。

除此之外还添加了`"/profile"`和`"/orders"`的路由规则。用户输入网址`http://localhost:5000/profile`时，服务器就会根据资源路径`"/profile"`匹配对应的路由规则`"/profile"`，然后调用`profile()`服务，返回一个 json 格式的用户个人资料数据给浏览器。同理当用户输入网址`http://localhost:5000/orders`时，会返回一个 json 格式的订单数据给浏览器。

我们还可以在路由规则里指定变量

```python
from flask import Flask

app = Flask(__name__)

@app.route("/user/<name>")
def hello(name):
    return f"hello {name}"

if __name__ == "__main__":
    app.run()
```

当用户输入网址`http://localhost:5000/user/KyleButler`时，根据资源路径`/user/KyleButler`匹配到路由规则`/user/<name>`，然后把`<name>`对应位置的字符串作为参数传递给服务 `hello(name)`。

我们还可以为一个服务添加多个路由规则

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
@app.route("/hello")
@app.route("/hi")
def hello(name):
    return f"hello flask"

if __name__ == "__main__":
    app.run()
```

这样，网址`http://localhost:5000/`，`http://localhost:5000/hello`，`http://localhost:5000/hi`都可以访问这个服务。

被`app.route()`装饰后的服务函数被称作视图函数，视图函数的名称没有要求一定要和路由规则一样。和其它变量和函数一样，只需要让它具有合适的意义即可。此外，这个视图函数名称可以用来计算它对应的路由规则。

```python
from flask import Flask, url_for
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Hello, this is home page</h1>"

@app.route("/user/<name>")
def profile(name):
    return '{"username": {name}, "userId": "a4bd0a54-c6b6-51cb-802b-867c8a214750"}'.format(name=escape(name))

@app.route("/test_url_for")
def orders():
    print(url_for("index"))  # /
    print(url_for("profile", name="KatieWeber"))  # /user/KatieWeber
    print(url_for("profile", username="NancyManning", userid="0001"))  # /user?username=NancyManning&userid=0001
    return "test url_for"

if __name__ == "__main__":
    app.run()
```

可以使用`url_for()`获得一个视图函数对应的 url 规则。如果传递了多余的关键字参数，那么找到对应 url 规则之后会在里面查找对应的变量，如果找到，则变量的值就是关键字参数的值，如果没有找到，会把这些关键字参数当作查询参数处理。
