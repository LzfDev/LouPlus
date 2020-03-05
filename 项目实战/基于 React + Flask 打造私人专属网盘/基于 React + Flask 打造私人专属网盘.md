# 一、React & SPA 介绍

## 1. 介绍

[React 中文资料](https://react.docschina.org/)

## 2. React初步

React 是什么？对前端有所了解的同学，想必都或多或少听到过 React 这个名字。React 是由 Facebook 公司发起的一个开源前端框架。React 在诞生之初，就是对传统前端开发的一种颠覆。经过若干年的发展，React 已经成为了目前世界上最流行的前端框架，可能没有之一。

React 并不是像 jQuery 那样的 JavaScript 框架，也不是像 Bootstrap 那样的 UI 框架。React 是一套基于**组件化**思想的，使用 **JavaScript** 语言的，用来构建前端**交互式** UI 的框架。这样的说法听起来会有一些抽象，下面我们将从零开始，完成一个 React 测试页面的搭建，通过这个过程，相信大家会对 React 形成自己的理解。

> React，Vue.js 和 Angular.js 是目前主流的三大前端框架。很多互联网公司在招聘前端工程师时都会在招聘条件里写上要求掌握这三个框架当中的至少一种。

### 2.1 环境准备

在使用 React 之前，我们首先需要安装基于 node 的支撑环境。node 是一个基于 Chrome JS 引擎的 JS 运行环境，node 可以用来做很多事情，包括脚本开发，服务器端开发等等，由于和本教程主要内容无关，这里就不再赘述了。在本教程中，我们只需要 node 作为一个工具。React 的开发工具大部分是基于 node 的。在 node 的帮助下我们开发 React 应用会简单很多。

> React 是一个纯前端框架，实际上我们也可以直接在网页端引入 React 的 JS，就像引用 jQuery 一样。不过现在并不推荐这种方式了。基于 node 的工具要好用很多。

打开终端，输入如下命令查看 node 的版本：

```
$ node --version   # 新开一个终端
v10.13.0
```

这样就说明 node 已经安装好了。

### 2.2 安装 create-react-app

在安装好 node 环境之后，我们就可以通过 npm 来安装各种工具和依赖了。npm 全称是 node package manager，即 node 的包管理工具，它的地位类似于 Ubuntu 中的 apt-get。后面很多地方我们都会使用 npm 来安装需要的包。

如果你使用的是实验楼的国内实验环境，或者是在自己的本地电脑上操作，推荐首先把 npm 的镜像地址设置成国内的淘宝镜像地址，这样安装 npm 包的速度会快很多：

```
$ npm config set registry http://registry.npm.taobao.org/
```

在安装依赖之前，我们先把 npm 升级到最新版本，在终端中输入：

```
$ npm install -g npm
```

等待脚本执行完成之后，使用 `npm --version` 查看 npm 的版本，本教程书写时，最新的 npm 版本是：

```
6.4.1
```

然后我们使用 npm 安装 `create-react-app`，它是 Facebook 官方的一个用来简化 React 开发的工具。在命令行中输入：

```
$ npm install -g create-react-app
```

等待安装完成之后，在命令行中输入 `create-react-app`，将看到它的简要帮助文档，说明工具已经成功安装上了。

![此处输入图片的描述](https://doc.shiyanlou.com/document-uid18510labid1375timestamp1543891786129.png/wm)

### 2.3 创建React工程

在安装好 node 环境之后，我们就可以通过 npm 来安装各种工具和依赖了。npm 全称是 node package manager，即 node 的包管理工具，它的地位类似于 Ubuntu 中的 apt-get。后面很多地方我们都会使用 npm 来安装需要的包。

如果你使用的是实验楼的国内实验环境，或者是在自己的本地电脑上操作，推荐首先把 npm 的镜像地址设置成国内的淘宝镜像地址，这样安装 npm 包的速度会快很多：

```
$ npm config set registry http://registry.npm.taobao.org/
```

在安装依赖之前，我们先把 npm 升级到最新版本，在终端中输入：

```
$ npm install -g npm
```

等待脚本执行完成之后，使用 `npm --version` 查看 npm 的版本，本教程书写时，最新的 npm 版本是：

```
6.4.1
```

然后我们使用 npm 安装 `create-react-app`，它是 Facebook 官方的一个用来简化 React 开发的工具。在命令行中输入：

```
$ npm install -g create-react-app
```

等待安装完成之后，在命令行中输入 `create-react-app`，将看到它的简要帮助文档，说明工具已经成功安装上了。

![此处输入图片的描述](https://doc.shiyanlou.com/document-uid18510labid1375timestamp1543891786129.png/wm)

### 2.4 第一个 React 页面

创建好的 React 项目 `cloud-disk-app` 的目录看起来是这样的：

```
- public
  - index.html
  - ...
- src
  - App.js
  - App.css
  - index.js
  - index.css
  - ...
- package.json
- README.md
```

主要的代码文件都存放在 `src` 目录里。

修改 `src/App.js` 文件：

```javascript
import React, { Component } from 'react';
import './App.css';

class App extends Component {
  render() {
    return (
      <div>
        <p>Hello React</p>
      </div>
    );
  }
}

export default App;
```

如果你没有关闭上一步 `npm start` 打开的 React Development Server，你会看到它自己编译了代码，并且刷新了浏览器。如果你关闭了 `npm start` 也没有关系，重新打开就好了。现在浏览器展示的页面已经变成了这样：

![此处输入图片的描述](https://doc.shiyanlou.com/document-uid18510labid9140timestamp1543829256935.png/wm)

这就是一个最简单的 React 页面。

对于 React 不了解的同学，可能会有一种蒙在鼓里的感觉。下面我们分析一下代码里做了些什么，以及 React 做了些什么。

首先我们声明了一个名叫 App 的类，它继承自 React 的 Component 类。Component，即组件，是 React 当中最重要的概念，React 的页面都是基于组件组织的。组件简单说就是一种可以重用的 UI 部件。就像机械零件一样，React 开发就是通过组装各种不同的组件，最终完成整个 App 的搭建。这个 App 就是我们的根组件，即最外层的组件。

所有的组件必须实现 render 方法，render 方法返回的是这个组件的内容。在 App 这个类的 render 方法当中，可以看到我们直接使用了标准的 HTML 语法，书写了一个简单的 ``，这种 JavaScript 和 HTML 结合的写法，被称为 JSX。JSX 本质上是 JavaScript 语言的一种扩展，方便我们更容易地编写 React 组件。React 会把 JSX 编译成纯 JavaScript 代码，然后在浏览器中执行。

> 熟悉 Java 的同学可能会联想到 JSP 和 Servlet 的关系。JSP 是使用标准的 HTML 语法加上 JSP 扩展进行编写，最后会编译成纯 Java 代码执行。

那 App 这个组件又是如何和最终出现的网页关联起来的呢？我们看到和 `App.js` 在同一级目录下，有一个 `index.js`，它看起来像是这样子：

```javascript
import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';

ReactDOM.render(<App />, document.getElementById('root'));
```

`ReactDOM.render` 顾名思义就是把一个 React 组件渲染到一个 HTML 节点上，这里渲染的是一个 id 为 `root` 的节点，那 `root` 又在哪里呢。打开 public 目录下的 `index.html`，在这个 HTML 中你可以找到真正的 root 节点。它是一个空节点，它的所有内容都将由 React 渲染：

```html
<body>
    <noscript>
      You need to enable JavaScript to run this app.
    </noscript>
    <div id="root"></div>
    <!-- ... -->
</body>
```

现在整个 React 页面的流程渲染终于真相大白了。在我们修改代码的时候，React Development Server 监控到代码的改动，将我们写的 JSX 代码编译成 JS 代码，然后通过 HTML 当中的 root 节点，使用 JS 渲染到网页中，最终呈现到浏览器里。

实际上 React 内部做的事情非常多，这里我们只是简单的介绍了一下它的流程。最终生成的网页中，root 节点仍然是空的，同时可以看到引入了一个 `bundle.js` 文件：

![此处输入图片的描述](https://doc.shiyanlou.com/document-uid18510labid1375timestamp1543892936569.png/wm)

这个文件就是 React 将我们的代码经过一系列处理完成之后的最终结果，这个文件非常大，里面的内容我们也不需要关心。大家只需要对 React 的基本原理和流程有所了解就可以了。

## 3. React SPA 初步

在介绍下面的内容之前，我们先引入一个新的概念，叫做 SPA。

SPA 全称是 Single Page Application，中文翻译过来是单页应用。SPA 并不是什么新概念，而是早已有之。熟悉或者使用过 Java 和 Python 等语言进行过 Web 后台开发的同学应该了解，在传统 Web 后台开发当中，通常需要使用模板引擎语言，后端把数据更新到模板引擎当中，然后由模板引擎渲染出 HTML，实现前端页面的动态更新。这种刷新通常是整个页面需要重新渲染。SPA 正好与之相反，所谓 SPA 单页应用就是从始至终只有一个页面，不进行整体刷新，而是使用 Javascript 进行 DOM 操作，在页面中更新已有的 UI 元素。

SPA 和传统 Web 开发相比的优点在于，实现了前端和后端的彻底解耦。后端只需要提供数据接口，完全无需关心数据的表现形式。前端只需要调用接口，也完全无需关心后端的具体实现。这种优势在现在前端轻量化和敏捷化的大趋势下，显得非常明显，也变得越来越流行。

> 追求模块之间的解耦是编程当中非常常见，也非常重要的一个追求，乃至在整个计算机科学层面看来，都是很重要的一个思想。
>
> 例如操作系统作为中间层，帮我们实现了硬件和应用程序之间的解耦，不管我们使用的是品牌机，组装机，笔记本等等，只要是同样的操作系统，都可以运行相同的程序；Java 语言中的 JVM 虚拟机作为中间层，帮我们实现了 Java 字节码和操作系统之间的解耦，同样的 Java 字节码可以在不同操作系统上的 JVM 上运行。类似的例子还有很多很多。

那么 SPA 和 React 又有什么关系呢？从前面的例子中可以看到，React 的所有内容都是由 JS 动态渲染的，后面的内容中我们会看到，React 能够根据数据动态更新组件的内容。总结起来，React 几乎天生就是用来做 SPA 的框架。下面的内容中，我们将学习如何让 React “动起来”，做到真正的 "React"。

### 3.1创建 React 组件

首先我们创建两个新的 React 组件。在 `src` 目录下创建一个新的文件夹，叫做 `Component`，然后在其中创建文件 `LoginForm.js` 和 `LoginForm.css`，分别是主页面文件和样式文件，然后在 `LoginForm.js` 文件中添加如下代码：

```javascript
import React, { Component } from 'react';
import './LoginForm.css';

class LoginForm extends Component {
    render() {
        return (
            <div>
              <h3>Login</h3>
            </div>
      );
    }
}

export default LoginForm;
```

可以看到 LoginForm 的样子和 App 没有太大差别，都是一个简单的 render 函数进行渲染。注意最后的导出语句 `export default` 很重要，没有它这个组件不能被外部引用和使用。CSS 文件先暂时留空，现在我们只需要看一下简单的效果，不需要添加样式。

同样的方法，我们再添加一个组件，名为 MainPanel，在这个目录下继续创建 `MainPanel.js` 和 `MainPanel.css`，并向 `MainPanel.js` 文件中添加如下代码：

```javascript
import React, { Component } from 'react';
import './LoginForm.css';

class MainPanel extends Component {
    render() {
        return (
            <div>
              <h3>MainPanel</h3>
            </div>
      );
    }
}

export default MainPanel;
```

以后在项目中添加新的组件，我们都会用类似的形式添加，就不再重复介绍了。

组件已经创建好了，下面我们让它们在主页面中展示出来。

### 3.2 Props & State

修改 `App.js`，引入我们刚才创建的两个组件：

```javascript
import React, { Component } from 'react';
import './App.css';

// 注意这里引入组件的写法
import LoginForm from './Component/LoginForm'; 
import MainPanel from './Component/MainPanel'; 

class App extends Component {
  constructor(props) {
    super(props);

    this.state = {
      login: true
    }
  }

  render() {
    if (this.state.login) {
      // React 组件可以像一个自定义 HTML 标签一样，直接书写
      return <MainPanel />;
    } else {
      return <LoginForm />
    }
  }
}

export default App;
```

在代码中，有两个新东西是之前没有提过的，在 App 的构造器中，唯一的参数是 props，另外还创建了一个自己的 state 变量。

首先我们来看 state。State 是组件**私有**的，在组件中**允许改变**的状态值。我们在代码中给 App 创建了 state 之后，在 render 函数里，通过 state 的 login 来判断返回哪个 Component。修改 state 中 login 的值，网页中渲染的页面会产生对应变化。

然后来看 props。React 当中的组件，既能引入别的组件，本身又可以被别的组件引用。Props 就是从组件**外部传入**的，在组件内**不可改变**的状态值。App 组件外部没有传入值，我们用 MainPanel 来做例子。

> 这种数据从父组件传入到根组件，不能反向传递的形式，叫做单向数据流(unidirectional data flow)，经过后面的学习，我们会对这种思想有进一步的理解。

修改 MainPanel 的 render 函数：

```javascript
render() {
   // 注意引用 props 的语法
   return (
      <div>
        <h3>{this.props.title}</h3>
      </div>
    );
}
```

然后在 App.js 中给 MainPanel 传入数据：

```javascript
render() {
  if (this.state.login) {
    return <MainPanel title="主页面"/>;
  } else {
    return <LoginForm />
  }
}
```

对应的，MainPanel 显示的内容就会发生变化。

### 3.3 setState

前面的内容说到，state 是可以改变的，同时 state 的改变会影响到内容，这也是 React 适合做 SPA 的一个主要特性。下面通过例子我们来学习如何使用 React 的 state。

我们想实现的是，通过按钮来切换 MainPanel 和 LoginForm，修改 `App.js`：

```javascript
class App extends Component {
  constructor(props) {
    super(props);

    this.state = {
      login: true
    }

    // 局限于 JS 中 this 作用域的问题，需要提前做 bind 操作
    this.switchOnClick = this.switchOnClick.bind(this);
  }

  switchOnClick() {
    // 注意一定要使用 setState，不要直接操作 state 对象
    this.setState({
      login: !this.state.login
    })
  }

  render() {
    var content;
    // React 组件还能像 JS 变量一样使用，可以用来给变量进行赋值
    if (this.state.login) {
      content = <MainPanel title="主页面"/>;
    } else {
      content = <LoginForm />
    }

    // 注意引用 content 的语法和 onClick 的写法
    return (
      <div>
        <button onClick={this.switchOnClick}>切换</button>
        {content}
      </div>
    )
  }
}
```

在代码中，我们给按钮的 onClick 事件绑定了 switchOnClick 这个函数，然后在函数中通过 setState 给 login 的值进行了取反，这样就可以使用按钮来进行页面切换了。一个使用 React 的 SPA 应用简单示例到这里就完成了。

# 二、Flask

## 1. 介绍

[Flask中文文档](https://dormousehole.readthedocs.io/en/latest/)

## 2. 环境准备

### 安装flask

`python3 -m pip install flask` 

或

`pip3 install flask`

## 3. Flask Testing

flask 提供了一个test_client专门用于测试。

```python
import os
import unittest
import tempfile
import json


from app import app

class CloudDiskTestCase(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.client = app.test_client()

    def test_index(self):
        rv = self.client.get('/', headers={'content-type': 'application/json'})
        data = json.loads(rv.data.decode('utf-8'))
        assert data['message'] == 'OK'


if __name__ == '__main__':
    unittest.main()
```

# 三、数据库操作

[SQLite 教程（中文）](http://www.runoob.com/sqlite/sqlite-tutorial.html)

[Peewee 官方文档](http://docs.peewee-orm.com/en/latest/)

## 2. SQLite初步

一般来讲，计算机程序里的数据，都是存放在内存当中的，而内存是一种易失性存储，即断电之后存储会丢失。为了防止这种丢失的情况，就需要把数据存放在硬盘当中，即所谓的“数据持久化”。数据库就是用来做数据持久化的一种工具。

了解过数据库，或者学习过实验楼有关课程的同学，应该对 MySQL，Microsoft SQL Server 等数据库有所耳闻。SQLite 和 MySQL 等一样，都属于**关系型数据库** 。在关系型数据库当中，数据是以二维表形式组织起来的，通过后面的学习，我们会对关系型数据库有更深入的理解。

SQLite 是一个非常轻量的关系型数据库，不过麻雀虽小，五脏俱全，SQLite 和 MySQL 一样也有完善的 SQL 语句查询，constraint 支持等等，足够我们学习使用了。

### 2.1 安装 SQLite

首先我们需要在实验环境中安装 SQLite：

```
$ sudo apt-get install sqlite3
```

等待安装完成之后，我们就可以在命令行中直接使用 sqlite3 工具。

我们先熟悉一下 sqlite 的基本操作，首先使用 sqlite3 创建一个数据库：

```
$ cd /home/shiyanlou/Code
$ sqlite3 test.db
```

命令行会看到下面的输出：

![此处输入图片的描述](https://doc.shiyanlou.com/document-uid18510labid9140timestamp1543829778411.png/wm)

这时我们已经进入了 sqlite 的交互式 shell，可以对数据库进行操作了。

使用 `.database` 可以看到我们当前正在操作的是哪个文件。

![此处输入图片的描述](https://doc.shiyanlou.com/document-uid18510labid9140timestamp1543829795022.png/wm)

使用 `.quit` 或 `.exit` 可以退出交互式 shell。

### 2.2 SQLite 基本操作

SQLite 大部分操作和语句和 MySQL 是相同的。对 SQL 语句以及 MySQL 操作比较熟悉的同学，可以跳过下面的内容，直接看下一小节。

首先我们创建一个新的 table：

```sql
create table user(id INT, name VARCHAR);
```

然后使用 `.tables` 命令和 `.schema` 命令可以看到我们新创建出的 Table 和它的 schema：

![此处输入图片的描述](https://doc.shiyanlou.com/document-uid18510labid9140timestamp1543829818269.png/wm)

> 之前使用过 MySQL 的同学会发现，我们没有用 `create database` 创建数据库，而是直接创建了 Table，因为 SQLite 是使用文件来区分数据库的，即每个文件就是一个数据库。

下面我们试着插入一列新数据：

```sql
insert into user values(1, "Tom");
```

然后使用 `select` 语句查询数据：

```sql
select * from user;
```

命令行输出如下：

![此处输入图片的描述](https://doc.shiyanlou.com/document-uid18510labid9140timestamp1543829839435.png/wm)

可以看到数据已经成功被写入了。使用 `.quit` 或 `.exit` 退出 sqlite，同时查看 `test.db` 这个文件，可以看到 `test.db` 已经有大小了，不是空文件。

再次使用 sqlite 打开 `test.db` 并执行查询，会得到同样的结果，即我们已经通过 sqlite 实现了数据的“持久化”：

![此处输入图片的描述](https://doc.shiyanlou.com/document-uid18510labid9140timestamp1543829859042.png/wm)

## 3. Peewee ORM 初步

### 3.1 安装 Peewee

首先我们使用 pip 来安装 peewee

```
$ sudo pip3 install peewee
```

等待安装完成之后，我们就可以在 Python 中使用 peewee 了。

### 3.2 使用 Peewee 创建数据库

下面我们通过例子学习一下 Peewee ORM 的使用。

首先创建一个文件 `Code/test_peewee.py`：

```python
from peewee import *

db = SqliteDatabase('test2.db') # 使用 test2. db 这个 SQLite 数据库

class User(Model):
    name = CharField()

    class Meta:
        database = db # 告诉 peewee 这个 model 要使用上面定义的 db


def create_all_tables():
    db.connect()
    db.create_tables([User]) # 创建 User 对应的 table


if __name__ == '__main__':
    create_all_tables()
```

可以看到在代码中我们完成了对 User 这个类的定义，同时告诉 peewee 要使用 test2.db 这个数据库，现在这个数据库还不存在，没有关系，peewee 会帮我们创建好。

使用 `python3 test_peewee.py` 执行这个脚本，脚本执行结束之后，会看到当前目录下，`test2.db` 已经被创建出来了。使用 sqlite 打开这个文件：

![此处输入图片的描述](https://doc.shiyanlou.com/document-uid18510labid9140timestamp1543829882646.png/wm)

可以看到 user 表已经被创建好了。

> 注意我们在定义 User 的时候并没有写 id，peewee 自动帮我们生成了一个 id 字段，并且定义成了 INTEGER 的 Primary Key。

### 3.3 使用 Peewee 进行数据库操作

创建好数据库之后，我们可以使用 peewee 进行数据操作了。在当前目录下打开 Python 交互式 shell，然后我们创建一个新的 user：

```python
from test_peewee import User

user1 = User.create(name='Tom')
user1.save()
```

通过这样几行代码，我们就已经把新数据插入到数据库当中了。相比使用 SQL 语句可以说是简单了很多。

退出 Python 使用 SQLite 打开 test2.db，可以看到数据已经写入：

![此处输入图片的描述](https://doc.shiyanlou.com/document-uid18510labid9140timestamp1543829898489.png/wm)

类似的，我们也可以使用 peewee 对数据进行查询，修改和删除操作：

```python
from test_peewee import User

users = User.select()
for user in users:
    print(user.name) # 将打印出所有的 User 的 name

tom = User.select().where(User.name=='Tom').get()
tom.name = 'Tommy' # 更新 Tom 的 name
tom.save()

tom.delete().execute() # 删除 Tom
```

注意上面的脚本最好都通过 Python 交互式 shell 来执行，可以多使用 peewee 进行操作，并且在数据库更改的操作之后，使用 sqlite 打开数据库，观察每个操作对数据库的影响。



# 四、登录与认证实现

在有了前面实验知识的基础之上，本次实验将开始搭建我们网盘应用的第一个界面，即用户登录界面。通过本次实验，我们将学习到如何将 React 前端和 Python 后端结合起来，对 SPA 开发流程有进一步的理解。

**知识点**

本实验中涉及到以下的知识点。

- 引入和使用第三方 React 组件
- Python itsdangerous + Cookie 实现认证
- 使用 fetch 发送网络请求

## 2. 前端页面搭建

### 2.1 页面搭建

首先我们来使用 React 搭建一个简单的登录界面，修改 `cloud-disk-app/src/Component/LoginForm.js` 文件：

```javascript
class LoginForm extends Component {
    constructor(props) {
        super(props);

        this.handleSubmit = this.handleSubmit.bind(this);
    }

    handleSubmit(e) {
        // 暂时留空
        e.preventDefault();
    }

    render() {
        return (
            <div>
                <h3>Login</h3>
                    <form id="loginForm" onSubmit={this.handleSubmit}>
                        <input type="text" placeholder="Email"/>
                        <input type="password" placeholder="Password" />
                        <input id="submitButton" type="submit" value="Login" />
                    </form>
            </div>
      );
    }
}
```

修改 `cloud-disk-app/src/Component/LoginForm.css`：

```css
#loginForm {
    display: flex;
    margin: 10px;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    width: 200px;
}

#submitButton {
    margin: 5px;
    width: 100px;
}
```

我们使用很简单的 HTML 和 CSS 写了一个登录页面。

修改 `cloud-disk-app/src/App.js` 内容如下，其中主要是把 login 这个 state 由 true 初始化为 false，同时去掉前面写的手动切换的按钮。

```js
import React, { Component } from 'react';
import './App.css';

import LoginForm from './Component/LoginForm';
import MainPanel from './Component/MainPanel';

class App extends Component {
    constructor(props) {
        super(props);
        this.state = {
            login: false
        }
    }
    render() {
        var content;
        if (this.state.login) {
            content = <MainPanel title="主页面"/>;
        } else {
            content = <LoginForm  onLogin={this.onLogin}/>
        }
        return content;
    }
}

export default App;
```

使用 `npm start` 运行程序，前端的效果看起来是这样的：

![此处输入图片的描述](https://doc.shiyanlou.com/document-uid18510labid9140timestamp1543829920739.png/wm)

### 2.2 引入第三方 React 组件

前面我们注意到，每个 React 组件其实都是平等的，即可以引用别的组件，又可以被别的组件引用。所谓组件化，就是可以大幅度提高组件的重用性，即我们写的组件可以被别人使用，同时我们也可以引用别人写好的组件。

为了简化 UI 工作量，我们引入一个第三方组件 `react-bootstrap`。之前了解过 Bootstrap 的同学应该知道，Bootstrap 是一个由 Twitter 出品的知名 UI 库。`react-bootstrap` 可以让我们直接在 React 中使用 bootstrap 的现成组件。

在 `cloud-disk-app` 文件夹下输入命令：

```
$ npm install --save react-bootstrap@0.32.4 bootstrap@3
```

等待依赖安装完毕，我们就可以使用 react-bootstrap 提供的组件和 bootstarp 的样式了。

> 使用 git 的同学会发现，安装新依赖之后，文件夹下的 package.json 和 package-json.lock 会发生变化，它们就是 npm 用来存储依赖的文件。一般为了固定依赖版本，会将它们的变化也提交到仓库当中。

修改 `cloud-disk-app/src/Component/LoginForm.js`：

```javascript
import React, { Component } from 'react';

// 注意这里组件的引入
import Col from 'react-bootstrap/lib/Col';
import FormGroup from 'react-bootstrap/lib/FormGroup';
import FormControl from 'react-bootstrap/lib/FormControl';

import './LoginForm.css';

class LoginForm extends Component {
    constructor(props) {
        super(props);

        this.handleSubmit = this.handleSubmit.bind(this);
    }

    handleSubmit(e) {
        // 暂时留空
        e.preventDefault();
    }

    render() {
        return (
            <Col md={4} mdOffset={4}>
                <h3>Login</h3>
                    <form id="loginForm" onSubmit={this.handleSubmit}>
                        <FormGroup>
                            <FormControl type="text" placeholder="Email" />
                        </FormGroup>
                        <FormGroup>
                            <FormControl type="password" placeholder="Password" />
                        </FormGroup>
                        <FormGroup>
                            <FormControl id="submitButton" type="submit" value="Login" /> 
                        </FormGroup>
                    </form>
            </Col>
      );
    }
}

export default LoginForm;
```

修改 `cloud-disk-app/src/Component/MainPanel.js`：

```javascript
import React, { Component } from 'react';
import Col from 'react-bootstrap/lib/Col';

import './MainPanel.css';

class MainPanel extends Component {
    render() {
        return (
            <Col md={4}>
              <h3>{this.props.title}</h3>
            </Col>
      );
    }
}

export default MainPanel;
```

可以看到，我们使用了 Bootstarp 的组件替换到了原生的 HTML。下面我们修改一下 `cloud-disk-app/src/App.js`，给页面加上统一的标题栏，主要的修改在 render 函数：

```javascript
import React, { Component } from 'react';
// 同样注意组件的引入
import Navbar from 'react-bootstrap/lib/Navbar';
import Row from 'react-bootstrap/lib/Row';
import Grid from 'react-bootstrap/lib/Grid';

import './App.css';
// 注意 bootstrap CSS 的引入
import 'bootstrap/dist/css/bootstrap.min.css';

import LoginForm from './Component/LoginForm';
import MainPanel from './Component/MainPanel';

class App extends Component {
  // 前面内容中已经出现过的，重复的代码将在示例代码中被省略掉。
  // 请大家注意修改的部分，不要一味复制粘贴。
  // ...
  render() {
    var content;
    if (this.state.login) {
      content = <MainPanel title="主页面"/>;
    } else {
      content = <LoginForm />
    }

    return (
      <Grid>
        <Row>
          <Navbar>
            <Navbar.Header>
              <Navbar.Brand>
                <a href="/">CloudDisk</a>
              </Navbar.Brand>
            </Navbar.Header>
          </Navbar>
          {content}
        </Row>
      </Grid>
    )
  }
}

export default App;
```

删除 LoginForm.css，App.css 和 index.css 当中的无用样式，现在网页看起来像是这样的：

![此处输入图片的描述](https://doc.shiyanlou.com/document-uid18510labid9140timestamp1543829954774.png/wm)

到这里登录的前端页面基本就已经搭建完成了。

> 我们之所以能够直接在 Javascript 中引入外部 CSS 文件，离不开 webpack 等前端构建工具的帮助。webpack 是非常强大的前端构建工具。React Development Server 依赖于 webpack 和一些其他工具来实现编译 JS 代码等操作，细节在这里我们不再讨论，有兴趣的同学可以查阅有关资料。
>
> 限于篇幅，本教程将专注于 React 框架的功能性使用，对于 Bootstrap 框架布局等知识将不再赘述。感兴趣的同学可以查阅有关资料或者参考实验楼有关 Bootstrap 的课程。

### 三、登录后台实现

### 3.1 基于 Token 的 Session 认证

由于本应用不面向外部提供注册，因此我们只需要在后台把用户名密码写死，然后验证用户名密码正确之后，返回成功就可以。

为了让我们可以登录一次之后，不需要每次操作都输入用户名和密码，需要实现一个简单的 session 机制。这里使用加密 token 作为 session 的标记符。所谓 token，翻译过来就是令牌。具体原理是，登录成功之后，服务器返回给浏览器一串加密过的，有过期时间的 token，浏览器将这个 token 写入 cookie 中，后面的请求全部都需要在 cookie 中带上这个 token，用来验证用户的身份。

> Session 的实现机制有很多种，加密 token 是其中的一种，还有例如 Java Web 开发中常见的 Session Id 等方法。

首先在 `/home/shiyanlou/cloud-disk-backend` 目录下，创建一个 `config.py` 文件，这里将存放配置有关的常量：

```python
EMAIL = 'test'
PASSWORD = 'test'
SECRET_KEY = 'THISISASECRET'
```

其中用户名和密码是写死的用来验证登录的，SECRET_KEY 是用来加密的一个 Seed，后面会用到。SECRET_KEY 可以任意生成，为了安全性应注意有足够的长度，同时不要泄露。

为了实现加密 token 机制，引入一个 Python 的第三方库 `itsdangerous`，它是专门用来生成类似加密 Token 的。

输入命令：

```
sudo pip3 install itsdangerous
```

等待依赖安装完毕，修改 `cloud-disk-backend/app.py`：

```python
# 注意引入了新的依赖 request
from flask import Flask, jsonify, request

from itsdangerous import (TimedJSONWebSignatureSerializer
as URLSafeSerializer, BadSignature, SignatureExpired)

app = Flask(__name__)
app.config.from_object('config')


@app.route('/login', methods=['POST'])
def login():
    req = request.get_json()
    # 验证用户名密码
    if req['email'] == app.config['EMAIL'] and req['password'] == app.config['PASSWORD']:
        # 生成 Token，有效期为一周
        s = URLSafeSerializer(app.config['SECRET_KEY'], expires_in=7 * 24 * 3600)

        return jsonify(message='OK',
                       token=s.dumps({'key': app.config['SECRET_KEY']}).decode('utf-8'))
    else:
        return jsonify(message='unauthorized'), 401

if __name__ == '__main__':
    app.run(debug=True)
```

借助于 `itsdangerous` 这个三方库，只需要这么几行代码，就可以生成加密的 Token 了。

使用 curl 来验证一下代码的正确性。首先使用 `python3 app.py` 打开调试服务器，然后新开一个终端在命令行中输入：

```plaintext
$ curl -X POST -H "Content-Type: application/json" --data '{"email": "test", "password": "test"}' http://localhost:5000/login
```

如果代码没有错误的话，可以看到类似这样的返回：

```plaintext
{
  "message": "OK",
  "token": "eyJhbGciOiJIUzUxMiIsImlhdCI6MTU0MjM3ODA1MiwiZXhwIjoxNTQyOTgyODUyfQ.eyJrZXkiOiJUSElTSVNBU0VDUkVUIn0.Jiccjb3QGzYk1ZeLrPuROFKN65nl3BY4fCgDfcE0kGhojqB8j7xOM36K1JclfIeVRpLfcRg4f6Obml0ze2E2tA"
}
```

可以看到 Token 已经正确返回。如果使用错误的用户名和密码，将会得到 401 响应。

> curl 是一个非常强大的网络请求工具，在不方便使用图形界面，或者图形界面还没有准备好的时候，我们可以使用它来调试网络有关的 API。

### 3.2 检查登录状态

前面的内容提到，浏览器在登录之后的所有请求，都需要带上合法的 Token ，服务器才能够正确验证浏览器的身份。为了简化服务端代码的书写，引入一个新的装饰器，叫做 `authorization_required`。这个装饰器的作用是检查用户的登录状态，只有登录状态正确，才执行后面的代码，否则返回 401。向 `cloud-disk-backend/app.py` 文件中添加如下代码：

```python
from functools import wraps
# ... 省略其他 import

def verify_auth_token(token):
    s = URLSafeSerializer(app.config['SECRET_KEY'])
    try:
        data = s.loads(token)
    except SignatureExpired:
        return None  # 有效但是过期的 token
    except BadSignature:
        return None  # 无效 token
    return 'key' in data and data['key'] == app.config['SECRET_KEY']


def test_authorization():
    cookies = request.cookies
    headers = request.headers
    args = request.args
    token = None
    # 这里支持 token 存放在 cookie，header 或者请求参数三个地方
    if 'token' in cookies:
        token = cookies['token']
    elif 'Authorization' in headers:
        token = headers['Authorization']
    elif 'token' in args:
        token = args['token']
    else:
        return False

    return verify_auth_token(token)


def authorization_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        # 验证失败，返回 401
        if not test_authorization():
            return jsonify(message='unauthorized'), 401
        # 执行原函数
        return f(*args, **kwargs)
    return wrapper
```

之前没有使用过 Python 装饰器的同学可能阅读代码会稍微困难一点。简单说装饰器就是把一个函数外部再封装一层，每次执行函数时，都会先执行装饰器，然后再执行原函数。以这里的代码为例，每次执行函数，都会先执行 `test_authorization`，如果判断验证失败，则直接返回 401，以达到我们进行认证的目的。

> 这种多层封装的思想，在一些框架（如 express）当中，被称为中间件（Middleware）

向 `cloud-disk-backend/app.py` 文件中添加如下代码：

```python
@app.route('/auth', methods=['GET'])
@authorization_required
def auth():
    return jsonify(message='OK')
```

使用 curl 发送请求，在没有 token 的情况下：

```plaintext
$ curl http://localhost:5000/auth
```

看到如下结果：

```
{
  "message": "unauthorized"
}
```

使用 token 的情况下(注意：这里的 token 值需要填写你之前返回的 token 值，下面的 token 值只是一个示例)：

```plaintext
$ curl -H "Cookie: token=eyJhbGciOiJIUzUxMiIsImlhdCI6MTU0MjM3ODA1MiwiZXhwIjoxNTQyOTgyODUyfQ.eyJrZXkiOiJUSElTSVNBU0VDUkVUIn0.Jiccjb3QGzYk1ZeLrPuROFKN65nl3BY4fCgDfcE0kGhojqB8j7xOM36K1JclfIeVRpLfcRg4f6Obml0ze2E2tA" http://localhost:5000/auth
```

看到如下结果：

```
{
  "message": "OK"
}
```

这样的输出，证明我们的代码是正确的。

最后一步，由于我们在开发阶段使用的 React 调试服务器和 Python 调试服务器不是同一个端口，在浏览器中访问时会出现跨域问题。因此我们需要让 Flask 允许跨域请求，首先安装依赖：

```plaintext
$ sudo pip3 install flask-cors
```

然后修改 `cloud-disk-backend/app.py`：

```python
from flask_cors import CORS, cross_origin
#...

app = Flask(__name__)
app.config.from_object('config')

# 允许跨域
CORS(app)
# ...
```

## 4.React 访问后端 API

### 4.1 Fetch API

熟悉 jQuery 的同学应该都了解 `$.ajax` 的使用。React 提供了类似的方法，叫做 `fetch`。我们将使用 fetch 来发送网络请求。

在 `/home/shiyanlou/cloud-disk-app/src` 目录下，创建一个名为 `Logic` 的文件夹，这里将存在有关业务逻辑的代码。在 `Logic` 文件夹中创建一个名为 `Api.js` 的文件，并向其中写入如下代码：

```javascript
const Api = {
    BASE_API: 'http://localhost:5000',

    login(email, password) {
        return fetch(this.BASE_API + "/login", {
            method: 'POST',
            body: JSON.stringify({email: email, password: password}),
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            },
        });
    },

    // 由于跨域的问题，我们暂时不能使用 Cookie 来认证，这里改用 Header 进行认证
    auth(token) {
        return fetch(this.BASE_API + "/auth", {
            method: 'GET',
            headers: {
                'Authorization': token,
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            },
        });
    }
}

export default Api;
```

### 4.2 登录逻辑，Cookie 和页面状态处理

有了前面的准备之后，可以开始实现登录的逻辑了，修改 `cloud-disk-app/src/Component/LoginForm.js` 文件：

```javascript
// ...
// 新引入
import Alert from 'react-bootstrap/lib/Alert';

import Api from '../Logic/Api';
// ...

class LoginForm extends Component {
    constructor(props) {
        super(props);

        // 登录错误的状态
        this.state = {
            error: false
        }

        this.handleSubmit = this.handleSubmit.bind(this);
    }

    handleSubmit(e) {
        e.preventDefault();
        const email = this.email
        const password = this.password;

        Api.login(email, password)
        .then(response => {
            if (!response.ok) {
                // 登录失败
                this.setState({ error: true });
                return;
            }

            // 登录成功，读取响应
            response.json()
            .then(data => this.props.onLogin(data));
        });
    }

    render() {
        var alert;
        if (this.state.error) {
            // 失败提醒
            alert = (
              <Alert bsStyle='danger'>
                <strong>Error: </strong>Wrong email or password.
              </Alert>
            );
          } else {
            alert = <span></span>;
        }

        // 注意 input 的 onChange 写法
        return (
            <Col md={4} mdOffset={4}>
                <h3>Login</h3>
                {alert}
                <form id="loginForm" onSubmit={this.handleSubmit}>
                    <FormGroup>
                        <FormControl type="text" placeholder="Email" onChange={evt => this.email = evt.target.value} />
                    </FormGroup>
                    <FormGroup>
                        <FormControl type="password" placeholder="Password" onChange={evt => this.password = evt.target.value} />
                    </FormGroup>
                    <FormGroup>
                        <FormControl id="submitButton" type="submit" value="Login" /> 
                    </FormGroup>
                </form>
            </Col>
      );
    }
}
```

总体流程是，在 input 的 onChange 里面，我们给 email 和 password 赋值，在 handleSubmit 的时候，调用 Api.js 中的 login 方法进行登录。如果登录失败，将 error 设置为 true，显示失败提示。如果成功，则试图调用 this.props.onLogin 方法。

为了在后面能够处理 cookie，先安装一个依赖库：

```plaintext
$ npm install --save js-cookie
```

前面我们讨论过，props 是外部传入的，在这里也就是由 App 传入的，修改 `cloud-disk-app/src/App.js`：

```javascript
// ...
import Cookies from 'js-cookie';

//...
import Api from './Logic/Api';

class App extends Component {
  constructor(props) {
    super(props);

    this.state = {
      login: false
    }

    this.onLogin = this.onLogin.bind(this);
  }

  componentDidMount() {
    // 试图从 Cookie 中拿到 token
    var token = Cookies.get('token');
    if (token) {
      // 验证 token
      Api.auth(token)
      .then(response =>
        {
          // token 合法，认为登录成功
          if (response.ok) {
            this.setState({
              login: true,
            });
          }
        })
    }
  }

  onLogin(data) {
    // 设置 token
    Cookies.set('token', data.token, { expires: 7 });
    this.setState({
      login: true,
    });
  }

  // ...
}
```

这里主要用到了 onLogin 这个函数，通过 props 传递给了 LoginForm，这是一种很常见的组件之间沟通的方式。另外在 componentDidMount 函数中，如果发现已经登录过，就直接跳转到主页面。componentDidMount 是 React 组件的生命周期函数之一，在组件加载完成之后被调用。

进入工程目录 `cloud-disk-app`，然后输入 `npm start`，在火狐浏览器中访问 `http://localhost:3000`，登录错误的页面看起来像这样：

![此处输入图片的描述](https://doc.shiyanlou.com/document-uid18510labid9140timestamp1543829987253.png/wm)

如果登录成功，则会显示主界面：

![此处输入图片的描述](https://doc.shiyanlou.com/document-uid18510labid9140timestamp1543830001728.png/wm)

登录成功之后，再次刷新页面，会发现页面自动跳转到了主页面，证明我们的 Session 机制是生效的。

本次实验中，我们使用 Flask 和 itsdangerous 实现了后端基于 Token 的登录和 Session 认证机制，在 React 前端通过 Fetch API 访问后端，将前后端结合起来，完成了简单的登录和 Session 的实现。同时我们还在前端引入了 Bootstrap 库，简化了 UI 的开发工作，让页面变的更加美观。

本次实验内容较多，对于之前没有接触过类似开发的同学，可能一时难以全部消化。希望同学们多看多写，将代码吃透，如果有问题可以查阅有关资料，也可以到实验楼课程下面的讨论区提问。

**参考资料**

- [itsdangerous 官方文档](https://itsdangerous.readthedocs.io/en/1.1.x/)
- [Bootstrap 3 中文文档](https://v3.bootcss.com/)

# 五、文件夹增加和删除

## 二、后端 API 设计与实现

首先为了简化复杂度，我们将只支持一级文件夹，即不能创建文件夹中的文件夹。

在进行设计之前，首先需要了解一下 RESTful API 的设计思想。RESTful 简单讲就是把 URL 看做一种资源，而 HTTP 的 GET，POST，PUT 等操作是对资源的修改。

### 2.1 RESTful API



下面我们通过例子来看一下如何设计文件夹的 RESTful API。

由于文件夹信息是需要持久化的，需要进行数据库操作。首先在 `cloud-disk-backend` 目录下新建一个文件 `model.py`，这里将存放数据库有关的内容：

```python
from peewee import *

db = SqliteDatabase('mydb.db', pragmas=(('foreign_keys', 'on'),))


class BaseModel(Model):

    class Meta:
        database = db


class Folder(BaseModel):
    name = CharField(max_length=64, unique=True)


def create_all_tables():
    db.connect()
    db.create_tables([Folder])

if __name__ == '__main__':
    create_all_tables()
```

根据前面的内容，使用 `python3 model.py` 执行这个文件，将会帮我们创建好 `mydb.db` 这个数据库。

在 `cloud-disk-backend/app.py` 中，创建 Folder 有关的 API 接口：

```python
#...
from model import Folder
import peewee
from playhouse.shortcuts import model_to_dict, dict_to_model
#...

@app.route('/folders', methods=['GET', 'POST'])
# TODO: @authorization_required
def folders():
    if request.method == 'POST':
        req = request.get_json()
        try:
            f = Folder.create(name=req['name'])
            f.save()
            return jsonify(message='OK'), 201
        except peewee.IntegrityError as e:
            return jsonify(message='error'), 409

    if request.method == 'GET':
        query = Folder.select()
        if (query.exists()):
            return jsonify(message='OK', data=[model_to_dict(folder) for folder in query])
        else:
            return jsonify(message='OK', data=[])


@app.route('/folders/<folder_name>', methods=['GET', 'DELETE'])
# TODO: @authorization_required
def folder(folder_name):
    try:
        folder = Folder.get(Folder.name==folder_name)
    except peewee.DoesNotExist:
        return jsonify(message='error'), 404

    if request.method == 'GET':
        return jsonify(message='OK', data=model_to_dict(folder))

    if request.method == 'DELETE':
        try:
            folder.delete_instance()
        except peewee.IntegrityError:
            return jsonify(message='error'), 409
    return jsonify(message='OK')
```

这里的代码也比较简单，基本上就是对数据库操作的简单封装。注意由于跨域的问题，为了方便调试，这里的代码暂时没有加上 auth 的验证。

> 在代码中加入 TODO 是一个好习惯，用来提醒自己和将来维护的人。

使用 peewee 数据库作为数据源，将它封装出了若干接口。使用 curl 测试我们的接口：

```plaintext
$ curl -X POST -H "content-type: application/json" --data '{"name": "test"}' http://localhost:5000/folders
{
  "message": "OK"
}
```

文件夹列表的 GET：

```plaintext
$ curl http://localhost:5000/folders
{
  "data": [
    {
        "id": 1,
        "name": "test"
    }
  ],
  "message": "OK"
}
```

单个 Folder 的 GET：

```plaintext
$ curl http://localhost:5000/folders/test
{
  "data": [
    {
      "id": 1,
      "name": "test"
    }
  ],
  "message": "OK"
}
```

这样我们就完成了后端接口的实现。

> 在 RESTful 规范中，POST 的语义代表新增，GET 的语义代表获取，PUT 的语义代表修改，DELETE 的语义代表删除。

## 三、前端 UI 实现



接下来，进行前端 UI 的实现。

### 3.1 文件夹列表实现



首先在 `cloud-disk-app/src/Logic/Api.js`文件中增加 folder 有关的操作：

```javascript
//...
    getFolders() {
        return fetch(this.BASE_API + "/folders", {
            method: 'GET',
            headers: {
                'Accept': 'application/json',
            },
        });
    },

    addFolder(name) {
        return fetch(this.BASE_API + "/folders", {
            method: 'POST',
            body: JSON.stringify({name: name}),
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            },
        });
    },

    getFolder(name) {
        return fetch(this.BASE_API + "/folders/" + name, {
            method: 'GET',
            headers: {
                'Accept': 'application/json',
            },
        });
    },

    deleteFolder(name) {
        return fetch(this.BASE_API + "/folders/" + name, {
            method: 'DELETE',
            headers: {
                'Accept': 'application/json',
            },
        });
    }
//...
```

修改 `cloud-disk-app/src/Component/MainPanel.js` 文件：

```javascript
import React, { Component } from 'react';
import Row from 'react-bootstrap/lib/Row';
import Col from 'react-bootstrap/lib/Col';
// 引入新组件
import ListGroup from 'react-bootstrap/lib/ListGroup';
import ListGroupItem from 'react-bootstrap/lib/ListGroupItem';
import Glyphicon from 'react-bootstrap/lib/Glyphicon';

import './MainPanel.css';

import Api from '../Logic/Api';

class MainPanel extends Component {
    constructor(props) {
        super(props);
        this.state = {
            folders: []
        };
    }

    refreshFolderList() {
        Api.getFolders()
        .then(response => {
            if (response.ok) {
                response.json()
                .then(responseJson => {
                    this.setState({
                        folders: responseJson.data
                    });
                })
            }
        })
    }

    componentDidMount() {
        this.refreshFolderList();
    }

    render() {
        // 处理数据，生成 folderList
        const folderList = this.state.folders.map(folder =>
            {
                return (
                <ListGroupItem role="menu" key={folder.id}>
                    <a>
                    <Glyphicon className="folderIcon" glyph='folder-close' />
                    <span className="folderName">{folder.name}</span>
                    </a>
                    <a>
                    <Glyphicon className="removeFolderIcon" glyph='remove' />
                    </a>
                </ListGroupItem>
                )
            });

        return (
            <Row>
                <Col md={4}>
                    <ListGroup>
                        {folderList}
                    </ListGroup>
                </Col>
            </Row>
      );
    }
}

export default MainPanel;
```

这里的代码也比较容易理解，需要注意的是对 folderList 的处理，请求数据，然后在 render 中根据数据生成所需要的组件 List，是一个很常见的 React 代码模式。

下面修改 `cloud-disk-app/src/Component/MainPanel.css` 给列表加上样式：

```css
.folderIcon {
    margin: 5px;
    cursor: pointer;
}

.folderName {
    cursor: pointer;
}

.removeFolderIcon {
    float: right;
    top: 5px;
    margin-right: 5px;
    cursor: pointer;
}
```

运行程序，看到的页面看是这样的：

![此处输入图片的描述](https://doc.shiyanlou.com/document-uid18510labid9140timestamp1543830038605.png/wm)



### 3.2 新增文件夹弹窗



我们需要在网页上提供一个能够新建文件夹的入口，使用 Bootstrap 的 Modal 组件来做这个事情。

为了进行弹窗提示，我们首先需要安装一个新库 SweetAlert，使用 `npm install sweetalert --save` 进行安装。

修改 `cloud-disk-app/src/Component/MainPanel.js` 文件：

```javascript
import React, { Component } from 'react';
import Row from 'react-bootstrap/lib/Row';
import Col from 'react-bootstrap/lib/Col';

// 引入若干新组件
import ListGroup from 'react-bootstrap/lib/ListGroup';
import ListGroupItem from 'react-bootstrap/lib/ListGroupItem';
import Glyphicon from 'react-bootstrap/lib/Glyphicon';
import Modal from 'react-bootstrap/lib/Modal';
import Button from 'react-bootstrap/lib/Button';
import FormControl from 'react-bootstrap/lib/FormControl';
import Alert from 'react-bootstrap/lib/Alert';

import swal from 'sweetalert';

import './MainPanel.css';

import Api from '../Logic/Api';

class MainPanel extends Component {
    constructor(props) {
        super(props);

        // 新增新建文件夹有关的状态
        this.state = {
            folders: [],
            showAddFolderDialog: false,
            addFolderError: false
        };

        this.addFolder = this.addFolder.bind(this);
    }

    // ...

    addFolder() {
        // 调用 API 新建文件夹
        Api.addFolder(this.newFolderName)
        .then(response =>
            {
                this.setState({
                    addFolderError: !response.ok,
                });

                // 添加成功，刷新文件夹列表
                if (response.ok) {
                    this.setState({
                        showAddFolderDialog: false
                    });
                    this.refreshFolderList();
                }
            });
    }

    render() {
        //...

        // 添加文件夹失败，显示 alert
        var addFolderAlert;
        if (this.state.addFolderError) {
            addFolderAlert = (
                <Alert bsStyle='danger'>
                <strong>Error: </strong>Please check your folder name again.
                </Alert>
            );
        } else {
            addFolderAlert = <span></span>;
        }

        // 新增 Modal 组件，使用 Modal 组件构建新建文件夹的对话框
        // 注意代码中 Button onClick 的写法
        return (
            <Row>
                <Col md={4}>
                    <Button id="addFolderButton" onClick={() => this.setState({showAddFolderDialog: true})} bsStyle='primary'>New Folder</Button>
                    <p></p>
                    <ListGroup>
                        {folderList}
                    </ListGroup>

                    <Modal show={this.state.showAddFolderDialog} onHide={() => this.setState({showAddFolderDialog: false})}>
                        <Modal.Header>
                            <Modal.Title>Add folder</Modal.Title>
                        </Modal.Header>

                        <Modal.Body>
                            {addFolderAlert}
                            <FormControl type="text" placeholder="Folder Name" onChange={evt => this.newFolderName = evt.target.value} />
                        </Modal.Body>

                        <Modal.Footer>
                            <Button onClick={() => this.setState({showAddFolderDialog: false})}>Close</Button>
                            <Button onClick={this.addFolder} bsStyle="primary">Add</Button>
                        </Modal.Footer>
                    </Modal>
                </Col>
            </Row>
      );
    }
}

export default MainPanel;
```

点击按钮后，浏览器示意效果：

![此处输入图片的描述](https://doc.shiyanlou.com/document-uid18510labid9140timestamp1543830060934.png/wm)

如果已添加过同名文件夹，会提示错误：

![此处输入图片的描述](https://doc.shiyanlou.com/document-uid18510labid9140timestamp1543830076273.png/wm)

### 3.3 删除文件夹



修改 `cloud-disk-app/src/Component/MainPanel.js`，添加删除文件夹有关内容：

```javascript
class MainPanel extends Component {
    // ...
    deleteFolder(folderName) {
        // 删除确认
        swal({
            title: "Are you sure?",
            text: "You will not be able to recover this folder!",
            icon: "warning",
            buttons: true,
            dangerMode: true,
        })
        .then((willDelete) => {
            if (willDelete) {
                // 调用 API 删除文件夹
                Api.deleteFolder(folderName)
                .then(response => {
                    if (response.ok) {
                        swal("Your folder has been deleted.", {
                            icon: "success",
                        });

                        // 删除成功，刷新列表
                        this.refreshFolderList();
                    }
                });
            } else {
              // 取消操作
              swal("Your folder is safe.");
            }
          });;
    }

    //...
    render() {
        // 设置删除按钮的 onClick 为 deleteFolder
        const folderList = this.state.folders.map(folder =>
            {
                return (
                <ListGroupItem role="menu" key={folder.id}>
                    <a>
                    <Glyphicon className="folderIcon" glyph='folder-close' />
                    <span className="folderName">{folder.name}</span>
                    </a>
                    <a onClick={() => this.deleteFolder(folder.name)}>
                    <Glyphicon className="removeFolderIcon" glyph='remove' />
                    </a>
                </ListGroupItem>
                )
            });
    }
    // ...
}
```

删除文件夹确认：

![此处输入图片的描述](https://doc.shiyanlou.com/document-uid18510labid9140timestamp1543830099354.png/wm)

删除文件夹成功：

![此处输入图片的描述](https://doc.shiyanlou.com/document-uid18510labid9140timestamp1543830113785.png/wm)



## 四、实验总结



本次实验中，我们完成了文件夹的增加和删除功能，后端提供了 RESTful 接口的 API，前端通过调用 API 来完成有关功能。对于 Python 部分可以看做是对 RESTful 架构的一个简单实践。对于 React 部分主要是综合前面学习的内容，其中列表有关的代码，以及通过 state 来控制 UI 组件的打开关闭，需要通过阅读和思考代码，才能掌握的更加深刻。

#### 参考资料

- [RESTful API 最佳实践](https://www.ruanyifeng.com/blog/2018/10/restful-api-best-practices.html)

# 六、文件上传和下载

## 一、实验介绍



在文件夹页面完成之后，下面我们完成网盘的核心功能，文件的上传和下载。需要修改数据库，加入“文件”这个结构，同时在前端和后端处理文件的上传以及和文件夹列表进行联动。

#### 知识点

本实验中涉及到以下的知识点。

- Peewee 关联表
- 上传和下载的前后端实现

## 二、后端设计与实现



接下来， 进入后端的设计以及代码的实现阶段。

### 2.1 数据库结构



首先我们需要修改数据库结构，存储文件有关的信息。文件是从属于文件夹的，因此两个表之间需要建立关联。修改 `cloud-disk-backend/model.py`：

```python
from peewee import *

db = SqliteDatabase('mydb.db', pragmas=(('foreign_keys', 'on'),))


class BaseModel(Model):

    class Meta:
        database = db


class Folder(BaseModel):
    name = CharField(max_length=64, unique=True)


class File(BaseModel):
    folder = ForeignKeyField(Folder, backref='files')
    filename = CharField()


def create_all_tables():
    db.connect()
    db.create_tables([Folder, File])


if __name__ == '__main__':
    create_all_tables()
```

我们创建了 File 这个 model，它使用一个 folder 作为外键，Folder 和 File 就建立起了一个一对多的关系。同时加入了一个 backref，方便我们可以直接找到 Folder 下面的所有 File。

修改 `model.py` 之后，把旧的 `mydb.db` 删除掉，然后重新执行 `python3 model.py`，更新表的结构。

> 有兴趣的同学可以看一下生成的 mydb.db 的数据库 schema，学习一下 Peewee 是如何处理外键依赖的。

### 2.2 文件上传后端实现



首先当文件上传到服务器上，需要有一个用来存储它的地方，这里为了实现上的方便，我们先用本地的一个路径来存储。修改 `cloud-disk-backend/config.py`，加入一个配置项：

```python
UPLOAD_FOLDER = '~/upload'
```

在用户目录下，创建好 `/home/shiyanlou/upload` 这个文件夹，然后修改 `cloud-disk-backend/app.py`：

```python
import os
import hashlib

from model import File
# ...

def generate_filename(folder, filename):
    return hashlib.md5(
                (folder + '_' + filename).encode('utf-8')).hexdigest()

def base36_encode(number):
    assert number >= 0, 'positive integer required'
    if number == 0:
        return '0'
    base36 = []
    while number != 0:
        number, i = divmod(number, 36)
        base36.append('0123456789abcdefghijklmnopqrstuvwxyz'[i])
    return ''.join(reversed(base36))

def generate_url():
    return base36_encode(get_random_long_int())

# 注意这里加入了 POST 支持
@app.route('/folders/<folder_name>', methods=['GET','POST', 'DELETE'])
# TODO: @authorization_required
def folder(folder_name):
    try:
        folder = Folder.get(Folder.name==folder_name)
    except peewee.DoesNotExist:
        return jsonify(message='error'), 404

    if request.method == 'POST':
        # 得到表单中的文件
        f = request.files['file']
        if f:
            # 生成文件名的 hash
            actual_filename = generate_filename(folder_name, f.filename)
            # 结合 UPLOAD_FOLDER 得到最终文件的存储路径
            target_file = os.path.join(os.path.expanduser(app.config['UPLOAD_FOLDER']), actual_filename)
            # 已存在同名文件，返回错误
            if os.path.exists(target_file):
                return jsonify(message='error'), 409

            try:
                # 保存文件，并写入数据库
                f.save(target_file)
                f2 = File.create(folder=folder, filename=f.filename)
                f2.save()
            except Exception as e:
                app.logger.exception(e)
                return jsonify(message='error'), 500

            return jsonify(message='OK'), 201

    if request.method == 'GET':
        # 注意这里将 backrefs 设置为 True，意味着取数据时，将会把 folder 当中的所有 file 也取出来
        return jsonify(message='OK', data=model_to_dict(folder, backrefs=True))

    if request.method == 'DELETE':
        try:
            folder.delete_instance()
        except peewee.IntegrityError:
            return jsonify(message='error'), 409
    return jsonify(message='OK')
```

上面的代码处理了文件的上传，注意由于上传的文件名可能会包含不合法或危险字符（例如 `/` 等），我们对文件名进行了简单的 hash 处理，最终存放在本地的文件名是一串 hash。

我们使用 curl 来测试这个 API，先创建了一个名为 `111` 的文件夹，现在在 `/home/shiyanlou` 目录下新建 `test.py` 文件，同时在这个目录下执行如下命令将 `test.py` 上传到 `111` 文件夹下：

```plaintext
$ curl -X POST -F file=@test.py http://localhost:5000/folders/111
{
  "message": "OK"
}
```

查看 111 文件夹下的内容：

```plaintext
$ curl http://localhost:5000/folders/111
{
  "data": {
    "files": [
      {
        "filename": "test.py",
        "id": 1
      }
    ],
    "id": 1,
    "name": "111"
  },
  "message": "OK"
}
```

### 2.3 文件下载后端实现



我们再创建一条 Route，专门用于查看文件信息和下载文件。修改 `cloud-disk-backend/app.py` 文件：

```python
# ...
from flask import Flask, jsonify, request, send_file

# ...

@app.route('/folders/<folder_name>/<filename>', methods=['GET', 'DELETE'])
# TODO:@authorization_required
def files(folder_name, filename):
    # 取文件的路径，和前面的上传部分类似
    actual_filename = generate_filename(folder_name, filename)
    target_file = os.path.join(os.path.expanduser(app.config['UPLOAD_FOLDER']), actual_filename)

    try:
        f = File.get(filename=filename)
    except peewee.DoesNotExist:
        return jsonify(message='error'), 404

    if request.method == 'GET':
        args = request.args
        # 发现有 query=info，返回文件的信息
        if 'query' in args and args['query'] == 'info':
            return jsonify(message='OK', data=model_to_dict(f))

        # 直接 GET，发送文件
        if os.path.exists(target_file):
            return send_file(target_file)
        else:
            return jsonify(message='error'), 404

    if request.method == 'DELETE':
        if os.path.exists(target_file):
            try:
                # 删除文件以及文件在数据库中的记录
                f.delete_instance()
                os.remove(target_file)
                return jsonify(message='OK')
            except Exception as e:
                app.logger.exception(e)
                return jsonify(message='error'), 500
        else:
            return jsonify(message='error'), 404
```

使用 curl 测试这个 API，当带上 `query=info` 时，会返回文件的有关信息：

```plaintext
$ curl http://localhost:5000/folders/111/test.py?query=info
{
  "data": {
    "filename": "test.py",
    "folder": {
      "id": 1,
      "name": "111"
    },
    "id": 1
  },
  "message": "OK"
}
```

当直接使用浏览器访问时，会触发下载：

![此处输入图片的描述](https://doc.shiyanlou.com/document-uid18510labid9140timestamp1543830135653.png/wm)

至此，文件上传下载的后端部分就搭建完成了。

> 注意到我们对于 RESTful API 的设计。`/folder` 的 POST 是创建文件夹，`/folder/111` 的 GET 是取出 111 文件夹的有关信息，`/folder/111` 的 POST 是创建 111 文件夹下面的文件，`/folder/111/test.py` 是取出 111 文件夹下面 test.py 这个文件的信息。这就是前面所说的 RESTful 的思想中把 URL 作为资源的一个体现，这种设计的层级关系是很清晰明确的。

## 三、前端 UI 实现



完成后端的功能之后，接下来完成前端 UI 实现

### 3.1 文件列表实现



文件列表的 UI 实现和上一个实验当中的文件夹列表是如出一辙的，这里不再详细介绍原理。有余力的同学可以试着不看代码，自己实现一遍。

首先修改 `cloud-disk-app/src/Logic/Api.js`，加入文件有关 API：

```javascript
// ...
    uploadFile(folder, file) {
        var data = new FormData();
        data.append('file', file);
        return fetch(this.BASE_API + "/folders/" + folder, {
            method: 'POST',
            body: data,
            headers: {
                Accept: 'application/json',
            },
        });
    },

    deleteFile(folder, filename) {
        return fetch(this.BASE_API + "/folders/" + folder + "/" + filename, {
            method: 'DELETE',
            headers: {
                'Accept': 'application/json',
            },
        });
    },

    generateFileDownloadUrl(folder, filename) {
        return this.BASE_API + "/folders/" + folder + "/" + filename;
    }
// ...
```

修改 `cloud-disk-app/src/Component/MainPanel.js`：

```javascript
class MainPanel extends Component {
    constructor(props) {
        super(props);
        this.state = {
            folders: [],
            showAddFolderDialog: false,
            addFolderError: false,

            // 用于文件列表的状态
            files: [],
            showUploadFileDialog: false,
            uploadFileError: false,

            // 当前选择的文件夹
            selectedFolder: '',
        };

        this.addFolder = this.addFolder.bind(this);
        this.uploadFile = this.uploadFile.bind(this);
    }

    refreshFolderList() {
        Api.getFolders()
        .then(response => {
            if (response.ok) {
                response.json()
                .then(responseJson => {
                    // 默认选择第一个文件夹
                    const firstFolder = responseJson.data[0];

                    // 在 setState 回调中刷新文件列表
                    this.setState({
                        folders: responseJson.data,
                        selectedFolder: firstFolder,
                    }, () => {
                        this.refreshFileList();
                    });
                })
            }
        })
    }

    refreshFileList() {
        // 无任何文件夹，直接返回
        if (!this.state.selectedFolder) {
            return;
        }

        Api.getFolder(this.state.selectedFolder.name)
        .then(response => {
            if (response.ok) {
                response.json()
                .then(responseJson => {
                    this.setState({
                        files: responseJson.data.files,
                    });
                })
            }
        })
    }

    changeSelectedFolder(id) {
        // 当前选择的文件夹 id 不变，不做任何事情
        if (this.state.selectedFolder.id === id) {
            return;
        }

        // 和前面类似，根据 id 找到文件夹名字，刷新右侧的文件夹列表
        this.setState({
            selectedFolder: this.state.folders.find(x => x.id == id)
        }, () => {
            this.refreshFileList();
        });
    }

    // ...

    uploadFile() {
        // 和新建文件夹的逻辑类似
        Api.uploadFile(this.state.selectedFolder.name, this.newUploadFile)
        .then(response =>
            {
                this.setState({
                    uploadFileError: !response.ok,
                });

                if (response.ok) {
                    this.setState({
                        showUploadFileDialog: false
                    });
                    this.refreshFileList();
                }
            });
    }

    deleteFile(filename) {
        // 和删除文件夹的逻辑类似
        swal({
            title: "Are you sure?",
            text: "You will not be able to recover this file!",
            icon: "warning",
            buttons: true,
            dangerMode: true,
        })
        .then((willDelete) => {
            if (willDelete) {
                Api.deleteFile(this.state.selectedFolder.name, filename)
                .then(response => {
                    if (response.ok) {
                        swal("Your file has been deleted.", {
                            icon: "success",
                        });

                        this.refreshFileList();
                    }
                });
            } else {
              swal("Your file is safe.");
            }
          });;
    }

    generateDownloadUrl(filename) {
        return Api.generateFileDownloadUrl(this.state.selectedFolder.name, filename);
    }

    render() {
        // 注意文件夹列表的点击，增加了 changeSelectedFolder 这个操作
        const folderList = this.state.folders.map(folder =>
            {
                return (
                <ListGroupItem role="menu" key={folder.id}>
                    <a onClick={() => this.changeSelectedFolder(folder.id)}>
                    <Glyphicon className="folderIcon" glyph='folder-close' />
                    <span className="folderName">{folder.name}</span>
                    </a>
                    <a onClick={() => this.deleteFolder(folder.name)}>
                    <Glyphicon className="removeFolderIcon" glyph='remove' />
                    </a>
                </ListGroupItem>
                )
            });


        // ...

        // 和文件夹列表逻辑类似，有下载和删除两个按钮
        const filesList = this.state.files.map(file =>
            {
                return (
                    <ListGroupItem key={file.id}>
                        <Glyphicon className="fileIcon" glyph='file' />
                        <span className="fileName">{file.filename}</span>
                        <a onClick={() => this.deleteFile(file.filename)}>
                        <Glyphicon className="removeFileIcon" glyph='remove' />
                        </a>
                        <a href={this.generateDownloadUrl(file.filename)}>
                        <Glyphicon className="downloadFileIcon" glyph='download-alt' />
                        </a>
                    </ListGroupItem>
                );
            });

        // 上传文件的错误提示
        var uploadFileAlert;
        if (this.state.uploadFileError) {
            uploadFileAlert = (
                <Alert bsStyle='danger'>
                <strong>Error: </strong>Please check your file name again.
                </Alert>
            );
        } else {
            uploadFileAlert = <span></span>;
        }

        return (
            <Row>
                {/* ...省略上个实验当中文件夹列表的内容... */}
                <Col md={8}>
                    <Button id="uploadFileButton" onClick={() => this.setState({showUploadFileDialog: true})} bsStyle='primary'>Upload File</Button>
                    <p></p>
                    <ListGroup>
                        {filesList}
                    </ListGroup>

                    <Modal show={this.state.showUploadFileDialog} onHide={() => this.setState({showUploadFileDialog: false})}>
                        <Modal.Header>
                            <Modal.Title>Upload File</Modal.Title>
                        </Modal.Header>

                        <Modal.Body>
                            {uploadFileAlert}
                            <FormControl type="file" placeholder="Upload file" onChange={evt => this.newUploadFile = evt.target.files[0]} />
                        </Modal.Body>

                        <Modal.Footer>
                            <Button onClick={() => this.setState({showUploadFileDialog: false})}>Close</Button>
                            <Button onClick={this.uploadFile} bsStyle="primary">Add</Button>
                        </Modal.Footer>
                    </Modal>
                </Col>
            </Row>
      );
    }
}
```

注意这里有一个新的点，setState 是有回调的。setState 是一个异步的操作，对 state 的更改不会马上生效。`refreshFileList` 中使用了 `selectedFolder` 这个 state，因此必须在回调中调用，才能拿到更新之后的值：

```javascript
this.setState({
    folders: responseJson.data,
    selectedFolder: firstFolder,
}, () => {
    this.refreshFileList();
});
```

修改 `cloud-disk-app/src/Component/MainPanel.css`，加上有关样式：

```css
.fileIcon {
    margin: 5px;
    cursor: pointer;
}

.fileName {
    cursor: pointer;
}

.removeFileIcon {
    float: right;
    top: 5px;
    margin-right: 5px;
    cursor: pointer;
}

.downloadFileIcon {
    float: right;
    top: 5px;
    margin-right: 10px;
    cursor: pointer;
}
```

最终的效果图类似这样：

![此处输入图片的描述](https://doc.shiyanlou.com/document-uid18510labid9140timestamp1543830171049.png/wm)

## 四、实验总结



本次实验中，我们完成了文件上传，下载和删除等功能，和前面的实验一样分成后端和前端两部分完成。本次实验中没有太多新的知识点，可以看做对之前知识的一个复习巩固，希望同学们通过本次实验加深对 React SPA 开发的理解。

文件的上传，下载，删除均是可用的，同时点击左边的文件夹，会切换对应文件夹的内容。

# 七、文件公开分享

# 一、实验介绍



为了能让他人不需要登录也可以访问我们存放在网盘中的文件，需要实现文件分享的功能。在本实验中将修改已有的数据结构，加入分享功能。

#### 知识点

本实验中涉及到以下的知识点。

- react-router 使用
- 临时 Token 认证

## 二、后端 API 设计与实现



首先，完成后端 API 的设计与实现。

### 2.1 数据库结构



首先修改 `cloud-disk-backend/model.py`，加入公开分享有关的字段：

```python
class File(BaseModel):
    folder = ForeignKeyField(Folder, backref='files')
    filename = CharField(index=True)
    public_share_url = CharField()
    open_public_share = BooleanField()
```

其中 `public_share_url` 是用来从分享渠道打开文件页面的 URL，`open_public_share` 是标记该文件是否允许公开分享。

注意修改 `model.py` 之后，需要把旧的 `mydb.db` 删除掉，然后重新执行 `python3 model.py`，更新表的结构。如果之前上传了文件，也需要把 UPLOAD_FOLDER 当中的文件清空，避免脏数据，也就是清除掉 `/home/shiyanlou/upload` 文件夹中的内容。

### 2.2 后端修改



后端数据注意要修改下面几个点，首先对于每个新上传的文件，需要生成新的短地址，修改 `cloud-disk-backend/app.py` 文件：

```python
# ...
import random

_random = random.SystemRandom()

def base36_encode(number):
    assert number >= 0, 'positive integer required'
    if number == 0:
        return '0'
    base36 = []
    while number != 0:
        number, i = divmod(number, 36)
        base36.append('0123456789abcdefghijklmnopqrstuvwxyz'[i])
    return ''.join(reversed(base36))

# 用于生成短地址
def generate_url():
    return base36_encode(get_random_long_int())


def get_random_long_int():
    return _random.randint(1000000000, 9999999999)
```

这里我们简单使用 base36 来生成随机短字符串。处理新上传的文件：

```python
@app.route('/folders/<folder_name>', methods=['GET','POST', 'DELETE'])
# TODO: @authorization_required
def folder(folder_name):
   # ...
            try:
                f.save(target_file)
                #生成短地址，默认关闭分享
                f2 = File.create(folder=folder, filename=f.filename,
                 public_share_url=generate_url(), open_public_share=False)
                f2.save()
            except Exception as e:
                app.logger.exception(e)
                return jsonify(message='error'), 500

            return jsonify(message='OK'), 201
    # ...
```

对于上传之后的文件，需要允许打开和关闭分享：

```python
# 注意新加入了 PATCH 方法
@app.route('/folders/<folder_name>/<filename>', methods=['GET', 'PATCH', 'DELETE'])
# TODO:@authorization_required
def files(folder_name, filename):
    actual_filename = generate_filename(folder_name, filename)
    target_file = os.path.join(os.path.expanduser(app.config['UPLOAD_FOLDER']), actual_filename)

    # ...

    if request.method == 'PATCH':
        share_type = request.args.get('shareType')
        if share_type == 'public':
            f.open_public_share = True
        elif share_type == 'none':
            f.open_public_share = False
        f.save()
        return jsonify(message='OK')
```

> 语义上，通常 PATCH 用来更新 model 的一部分，PUT 用来更新整个 model。

对于文件访问的认证，我们继续使用 Token 方式。新增加一个 API 用于获取分享文件有关的信息和下载文件：

```python
@app.route('/share/<path>', methods=['GET'])
def share(path):
    is_public = False

    try:
        # 查找对应的文件
        f = File.get(File.public_share_url == path)
        actual_filename = generate_filename(f.folder.name, f.filename)
        target_file = os.path.join(os.path.expanduser(app.config['UPLOAD_FOLDER']), actual_filename)

        is_public = True
    except peewee.DoesNotExist:
        return jsonify(message='error'), 404

    if not (is_public and f.open_public_share):
        return jsonify(message='error'), 404

    s = URLSafeSerializer(app.config['SECRET_KEY'], expires_in=24 * 3600)

    args = request.args
    if args.get('download') == 'true':
        # 如果是下载，验证 Cookie
        token = None
        cookies = request.cookies
        if 'token' in cookies:
            token = cookies['token']
            try:
                data = s.loads(token)
                if data['path'] == path:
                    if os.path.exists(target_file):
                        return send_file(target_file)
                    else:
                        return jsonify(message='error'), 404
                else:
                    return jsonify(message='unauthorized'), 401
            except:
                return jsonify(message='unauthorized'), 401

    # 如果是获取信息，设置上 Cookie

    # 注重这里设置的 Token 和登录是不同的，这里的 Token 不能用于验证登录有关的 API
    token = s.dumps({'path': path}).decode('utf-8')

    payload = {
        'filename': f.filename,
        'folder': f.folder.name,
        'open_public_share': f.open_public_share,
        'token': token,
    }

    return jsonify(message='OK', data=payload)
```

这里的实现和之前登录有相似的地方，只不过不需要验证用户名密码，而是直接返回一个有效期为 24 个小时的 token 供用户使用。

## 三、前端修改



后端功能完成后，接下来进行前端修改。

### 3.1 分享设置弹窗



首先还是修改 `cloud-disk-app/src/Logic/Api.js` 加入对后端的调用:

```javascript
// ...
    generateShareFileDownloadUrl(url) {
        return this.BASE_API + "/share/" + url + "?download=true";
    },

    updataFileShareType(folder, filename, shareType) {
        return fetch(this.BASE_API + "/folders/" + folder + "/" + filename + "?shareType=" + shareType, {
            method: 'PATCH',
            headers: {
                'Accept': 'application/json',
            },
        });
    },

    getFileInfoWithShareUrl(url) {
        return fetch(this.BASE_API + "/share/" + url, {
            method: 'GET',
            headers: {
                'Accept': 'application/json',
            },
        });
    },
// ...
```

我们加入一个弹窗，用于进行分享有关的设置，修改 `cloud-disk-app/src/Component/MainPanel.js` 文件：

```javascript
// ...
import Radio from 'react-bootstrap/lib/Radio';
import FormGroup from 'react-bootstrap/lib/FormGroup';

class MainPanel extends Component {
    constructor(props) {
        super(props);
        this.state = {
            // 加入新状态
            selectedFile: '',

            showFileShareDialog: false,
        };

        // ...
        this.saveFileShareType = this.saveFileShareType.bind(this)
    }

    // ...
    // 保存文件的分享状态
    saveFileShareType() {
        var shareType;
        if (this.publicShareRadioRef.checked) {
            shareType = "public";
        } else {
            shareType = "none";
        }

        Api.updataFileShareType(this.state.selectedFolder.name, this.state.selectedFile.filename, shareType)
        .then(response =>
            {
                if (response.ok) {
                    this.setState({
                        showFileShareDialog: false
                    });

                    this.refreshFileList();
                }
            });
    }

    // ...

    // 文件列表中加入 shareIcon
    //
    // 加入分享设置的 Modal Dialog
    render() {
            const filesList = this.state.files.map(file =>
            {
                return (
                    <ListGroupItem key={file.id}>
                        <Glyphicon className="fileIcon" glyph='file' />
                        <span className="fileName">{file.filename}</span>
                        <a onClick={() => this.deleteFile(file.filename)}>
                        <Glyphicon className="removeFileIcon" glyph='remove' />
                        </a>
                        <a href={this.generateDownloadUrl(file.filename)}>
                        <Glyphicon className="downloadFileIcon" glyph='download-alt' />
                        </a>
                        <a onClick={() => this.setState({selectedFile: file, showFileShareDialog: true})}>
                        <Glyphicon className="shareFileIcon" glyph='share' />
                        </a>
                    </ListGroupItem>
                );
            });

            {/* ... 省略中间重复代码 ... */}

            <Modal show={this.state.showFileShareDialog} onHide={() => this.setState({showFileShareDialog: false})}>
                        <Modal.Header>
                            <Modal.Title>Share</Modal.Title>
                        </Modal.Header>

                        <Modal.Body>
                            <ListGroup>
                                <ListGroupItem>
                                    <p>Public Share: {this.state.selectedFile.public_share_url}</p>
                                </ListGroupItem>
                                <ListGroupItem>
                                    <FormGroup>
                                        <Radio name="shareGroup" 
                                        inline
                                        defaultChecked={this.state.selectedFile.open_public_share}
                                        inputRef={ref => { this.publicShareRadioRef = ref; }}>                 Public
                                        </Radio>{' '}
                                        <Radio name="shareGroup"
                                        inline
                                        defaultChecked={!this.state.selectedFile.open_public_share}
                                        inputRef={ref => { this.noShareRadioRef = ref; }}>
                                            None
                                        </Radio>
                                        </FormGroup>
                                </ListGroupItem>
                            </ListGroup>
                        </Modal.Body>

                        <Modal.Footer>
                            <Button onClick={() => this.setState({showFileShareDialog: false})}>Close</Button>
                            <Button onClick={this.saveFileShareType} bsStyle="primary">Save</Button>
                        </Modal.Footer>
                    </Modal>

    }
}
```

和之前的上传文件等 Modal 类似，这里添加了一个新的用于设置文件分享状态的 Modal，修改 `cloud-disk-app/src/Component/MainPanel.css` 文件：

```css
.shareFileIcon {
    float: right;
    top: 5px;
    margin-right: 10px;
    cursor: pointer;
}
```

修改过后的效果类似这样：

![此处输入图片的描述](https://doc.shiyanlou.com/document-uid18510labid9140timestamp1543830190478.png/wm)

3.2 文件分享查看页面



为了让他人可以不用登录直接查看分享的文件，需要增加一个新页面。为了和我们自己访问的页面分开，需要使用一个新的 Path。这里引入一个新库，`react-router`。它是用来根据 URL 区分显示不同 React 界面的库，使用 npm 安装 `npm install --save react-router-dom@4`。等待安装完成之后，修改 `cloud-disk-app/src/App.js`：

```javascript
// ...
import Col from 'react-bootstrap/lib/Col';
import Glyphicon from 'react-bootstrap/lib/Glyphicon';
import Button from 'react-bootstrap/lib/Button';
import { BrowserRouter as Router, Route } from "react-router-dom";

// 我们将原来的 App 中的内容抽出来，变成了 MainPage
class MainPage extends Component {
  constructor(props) {
    super(props);

    this.state = {
      login: false
    }

    this.onLogin = this.onLogin.bind(this);
  }

  componentDidMount() {
    var token = Cookies.get('token');
    if (token) {
      Api.auth(token)
      .then(response =>
        {
          if (response.ok) {
            this.setState({
              login: true,
            });
          }
        })
    }
  }

  onLogin(data) {
    Cookies.set('token', data.token, { expires: 7 });
    this.setState({
      login: true,
    });
  }

  render() {
    var content;
    if (this.state.login) {
      return <MainPanel title="主页面"/>;
    } else {
      return <LoginForm onLogin={this.onLogin}/>
    }
  }
}

// 新建一个 SharePage
class SharePage extends Component {
  constructor(props) {
    super(props);
  }

  // 暂时留空
  render() {
    return (
      <p>SharePage</p>
    );
  }
}

// 注意下面 Router 和 Route 中参数的写法
const App = () => (
  <Router>
    <Grid>
      <Row>
          <Navbar>
            <Navbar.Header>
              <Navbar.Brand>
                <a href="/">CloudDisk</a>
              </Navbar.Brand>
            </Navbar.Header>
          </Navbar>
          <Route path="/" exact component={MainPage} />
          <Route path="/s/:path" component={SharePage} />
      </Row>
    </Grid>
  </Router>
);


export default App;
```

借助 react-router 我们实现了为分享单独使用 `/s` 这个 URL，放到 SharePage 展示。下面我们修改 SharePage：

```javascript
class SharePage extends Component {
  constructor(props) {
    super(props);
    this.state = {
      file: null
    }
  }

  componentDidMount() {
    // 从路径参数中拿到 path
    const path = this.props.match.params.path
    // 获取文件有关信息
    Api.getFileInfoWithShareUrl(path)
    .then(response => {
      if (response.ok) {
        response.json()
        .then(responseJson => {
          this.setState({
            file: responseJson.data
          })

          // 设置 Cookie 用于下载认证
          var token = Cookies.get('token');
          if (token) {
            return;
          }

          Cookies.set('token', responseJson.data.token, { expires: 1 });
        })
      }
    })
  }

  render() {
    if (!this.state.file) {
      return (
        <Col md={4} mdOffset={4}>
          <span> The file you are requesting does not exists! </span>
        </Col>
      );
    }
    return (
      <Row>
        <Col md={1} mdOffset={4}>
          <Glyphicon glyph='file' style={{ 'fontSize': '90px'}}/>
        </Col>
        <Col md={4}>
        <p>{this.state.file.filename}</p>
        <Button style={{ 'marginTop': '25px' }} href={Api.generateShareFileDownloadUrl(this.props.match.params.path)}><Glyphicon glyph='save-file' />Download</Button>
        </Col>
      </Row>
    );
  }
}
```

这样分享页面基本就完成了。

首先打开分享页面，其次我们需要模拟不是通过登录界面登录过的用户访问的情况，因此需要清空 Cookie。打开 Firefox 的“首选项” -> “隐私”，清空 localhost 的所有 cookie。

如果文件本身没有允许分享：

![此处输入图片的描述](https://doc.shiyanlou.com/document-uid18510labid9140timestamp1543830227558.png/wm)

如果打开了分享：

![此处输入图片的描述](https://doc.shiyanlou.com/document-uid18510labid9140timestamp1543830243663.png/wm)

在分享页面，文件也是可以正常下载的。

## 四、实验总结



本次实验中，我们完成了文件的公开分享功能。主要用到的新知识是 react-router 的使用。react-router 也是 SPA 应用当中非常常用的组件，希望同学们能够认真理解它的作用和使用。同时为了实现分享的下载，在后端生成了一个临时的 Token，要注意一下这种方式对于用户鉴权的作用。

#### 参考资料

- [React Router 文档](https://reacttraining.com/react-router/web/guides/quick-start)



# 八、文件私密分享

## 一、实验介绍



继续前一个实验的内容，对于不希望公开分享的文件，我们将加入私密分享的功能。和公开分享的功能类似，私密分享将验证密码，才会允许用户访问文件。

本实验可以看做上个实验的巩固练习，如果同学们有时间和余力，可以尝试自行实现这个功能。

#### 知识点

- 临时 Token 认证
- 简单短密码的生成
- 使用 React 组件生成二维码

## 二、后端实现



首先，进行后端功能的实现。



### 2.1 数据库结构



修改 `cloud-disk-backend/model.py` 文件中的数据库结构：

```python
class File(BaseModel):
    folder = ForeignKeyField(Folder, backref='files')
    filename = CharField(index=True)
    public_share_url = CharField()
    private_share_url = CharField()
    private_share_password = CharField()
    open_public_share = BooleanField()
    open_private_share = BooleanField()
```

加入私密分享有关的内容。然后删除当前目录下的 `mydb.db` 文件，执行 `python3 model.py` 命令重新生成数据表。



### 2.2 后端逻辑修改



修改 `cloud-disk-backend/app.py` 文件，向其中加入以下代码：

首先加入生成短密码的函数：

```python
def get_random_short_int():
    return _random.randint(100000, 999999)


def generate_password():
    return base36_encode(get_random_short_int())
```

创建 File 时，增加私密分享有关内容：

```python
# ...
f2 = File.create(folder=folder,
                filename=f.filename,
                public_share_url=generate_url(),
                private_share_url=generate_url(),
                private_share_password=generate_password(),
                open_public_share=False,
                open_private_share=False)
# ...
```

修改文件属性时：

```python
# ...
    if request.method == 'PATCH':
        share_type = request.args.get('shareType')
         if share_type == 'private':
            f.open_private_share = True
            f.open_public_share = False
        elif share_type == 'public':
            f.open_private_share = False
            f.open_public_share = True
        elif share_type == 'none':
            f.open_public_share = False
            f.open_private_share = False
        f.save()
        return jsonify(message='OK')
# ...
```

获取文件信息时，增加对于密码的校验：

```python
@app.route('/share/<path>', methods=['GET'])
def share(path):
    is_public = False
    is_private = False

    try:
        f = File.get(File.public_share_url == path)
        is_public = True
    except peewee.DoesNotExist:
        # 处理私密分享
        try:
            f = File.get(File.private_share_url == path)
            is_private = True
        except peewee.DoesNotExist:
            return jsonify(message='error'), 404

    actual_filename = generate_filename(f.folder.name, f.filename)
    target_file = os.path.join(os.path.expanduser(app.config['UPLOAD_FOLDER']), actual_filename)

    # 处理私密分享
    if not ((is_public and f.open_public_share) or (is_private and f.open_private_share)):
        return jsonify(message='error'), 404

    s = URLSafeSerializer(app.config['SECRET_KEY'], expires_in=24 * 3600)

    args = request.args
    if args.get('download') == 'true':
        token = None
        cookies = request.cookies
        if 'token' in cookies:
            token = cookies['token']
            try:
                data = s.loads(token)
                if data['path'] == path:
                    if os.path.exists(target_file):
                        return send_file(target_file)
                    else:
                        return jsonify(message='error'), 404
                else:
                    return jsonify(message='unauthorized'), 401
            except:
                return jsonify(message='unauthorized'), 401

    token = s.dumps({'path': path}).decode('utf-8')

     # 处理私密分享
    payload = {
        'filename': f.filename,
        'folder': f.folder.name,
        'open_public_share': f.open_public_share,
        'open_private_share': f.open_private_share,
        'token': token,
    }

    # 校验密码，密码不对不返回 token
    if is_private:
        if 'password' not in args or args['password'] != f.private_share_password:
            payload['token'] = ''

    return jsonify(message='OK', data=payload)
```



## 三、前端修改



完成后端功能，进行前端的修改。



### 3.1 分享设置修改



在 `cloud-disk-app/src/Logic/Api.js` 中加入密码参数：

```javascript
// ...
    getFileInfoWithShareUrl(url, password) {
        return fetch(this.BASE_API + "/share/" + url + "?password=" + password, {
            method: 'GET',
            headers: {
                'Accept': 'application/json',
            },
        });
    },
// ...
```

在分享设置中，加入有关私密分享的代码，修改 `cloud-disk-app/src/Component/MainPanel.js` 文件：

```javascript
// ...
    saveFileShareType() {
        var shareType;
        if (this.publicShareRadioRef.checked) {
            shareType = "public";
        } else if (this.privateShareRadioRef.checked) {
            shareType = "private";
        } else {
            shareType = "none";
        }

        Api.updataFileShareType(this.state.selectedFolder.name, this.state.selectedFile.filename, shareType)
        .then(response =>
            {
                if (response.ok) {
                    this.setState({
                        showFileShareDialog: false
                    });

                    this.refreshFileList();
                }
            });
    }
// ...
    render() {
        // ...
        <ListGroupItem>
                <p>Public Share: {this.state.selectedFile.public_share_url}</p>
                <p>Private Share: {this.state.selectedFile.private_share_url}， Password: {this.state.selectedFile.private_share_password}</p>
        </ListGroupItem>
        <ListGroupItem>
            <FormGroup>
                <Radio name="shareGroup" 
                inline
                defaultChecked={this.state.selectedFile.open_public_share}
                inputRef={ref => { this.publicShareRadioRef = ref; }}>
                Public
                </Radio>{' '}
                <Radio name="shareGroup" 
                inline
                defaultChecked={this.state.selectedFile.open_private_share}
                inputRef={ref => { this.privateShareRadioRef = ref; }}>
                Private
                </Radio>{' '}
                <Radio name="shareGroup"
                inline
                defaultChecked={!this.state.selectedFile.open_public_share && !this.state.selectedFile.open_private_share}
                inputRef={ref => { this.noShareRadioRef = ref; }}>
                None
                </Radio>
                </FormGroup>
        </ListGroupItem>
        // ...
    }
copy
```

运行程序，效果如图：

![此处输入图片的描述](https://doc.shiyanlou.com/document-uid18510labid9140timestamp1543830274569.png/wm)



### 3.2 分享显示页面修改



修改 `cloud-disk-app/src/App.js` 文件加入密码验证：

```javascript
import swal from 'sweetalert';

class SharePage extends Component {

  // ...
  componentDidMount() {
    const path = this.props.match.params.path
    Api.getFileInfoWithShareUrl(path)
    .then(response => {
      if (response.ok) {
        response.json()
        .then(responseJson => {
          this.setState({
            file: responseJson.data
          })

          var token = Cookies.get('token');
          if (token) {
            return;
            // 私密分享，验证密码
          } else if (responseJson.data.open_private_share) {
            swal({
              text: 'Please type the password',
              content: {
                element: "input",
                attributes: {
                  placeholder: "Type your password",
                  type: "password",
                },
              },
              button: {
                text: "Go",
                closeModal: false,
                closeOnEsc: false,
              },
              closeOnClickOutside: false,
            })
            .then(password => {
              Api.getFileInfoWithShareUrl(path, password)
              .then(response => {
                response.json()
                .then(responseJson => {
                  // 密码正确，设置 Token
                  if (responseJson.data.token) {
                    Cookies.set('token', responseJson.data.token, { expires: 1 });
                    swal.close();
                  } else {
                    swal("Wrong password");
                  }
                });
              })
            })
          }

          if (responseJson.data.token) {
            Cookies.set('token', responseJson.data.token, { expires: 1 });
          }
        })
      }
    })
  }
  // ...
}
```

运行程序。注意和公开分享类似，我们需要模拟非 admin 用户，即不是通过登录界面登录过的用户访问的情况，因此需要清空 Cookie。打开 Firefox 的“首选项” -> “隐私”，清空 localhost 的所有 cookie：

![此处输入图片的描述](https://doc.shiyanlou.com/document-uid18510labid9140timestamp1543830292693.png/wm)

然后访问分享页面：

![此处输入图片的描述](https://doc.shiyanlou.com/document-uid18510labid9140timestamp1543830308680.png/wm)

输入正确密码之后可以正常下载文件。



### 3.3 分享链接二维码



我们将使用纯前端实现二维码生成和展示。首先安装一个依赖库 `npm install qrcode.react --save`。然后修改 `cloud-disk-app/src/Component/MainPanel.js` 文件：

```javascript
// ...
import QRCode from 'qrcode.react';
// ...

// 修改分享设置页面
 <ListGroup>
    <ListGroupItem>
        <Row>
            <Col md={8}>  
            <p>Public Share: {window.location + "s/" + this.state.selectedFile.public_share_url}
            </p>
            </Col>
            <Col md={2} mdOffset={2}>
            <QRCode value={window.location + "s/" + this.state.selectedFile.public_share_url}
                size={64} 
                bgColor={'#ffffff'}
                fgColor={'#000000'}
                level={'L'}/>
            </Col>
        </Row>
        <Row>
            <Col md={8}>
                <p>Private Share: {window.location + "s/" + this.state.selectedFile.private_share_url}， Password: {this.state.selectedFile.private_share_password}</p>
            </Col>
            <Col md={2} mdOffset={2}>
                <QRCode value={window.location + "s/" + this.state.selectedFile.private_share_url}
                    size={64} 
                    bgColor={'#ffffff'}
                    fgColor={'#000000'}
                    level={'L'}/>
            </Col>
        </Row>
    </ListGroupItem>
// ...
```

注意我们在使用 `window.location` 时一定要加上 window，不然 React 会认为它是本地变量，无法识别。

这时候在设置界面就可以展示出二维码了。如图：

![此处输入图片的描述](https://doc.shiyanlou.com/document-uid18510labid9140timestamp1543830328658.png/wm)



四、实验总结



本次实验中，我们完成了文件的私密分享功能。私密分享的实现和公开分享大体结构上是相似的。希望同学们可以在实现的过程中多想多看，思考一下目前的实现有没有什么漏洞，还有没有可以完善的点。



# 九、项目总结回顾

## 一、实验介绍



欢迎来到本系列课程最后一个实验。本实验中将对整个项目的打包发布过程进行介绍，同时对整个实验进行总结。

#### 知识点

- React 打包发布
- Flask 静态页面部署

## 二、React 打包



在开发过程中我们一直使用 React Development Server，它可以把我们的修改实时反馈到页面上。正式发布时，需要完成 React 打包工作。在 `cloud-disk-app` 目录执行：

```plaintext
$ npm run build
```

经过一个有些长的等待之后，如果不出意外，会显示打包成功。然后会看到 `cloud-disk-app` 目录下多出了一个 `build` 文件夹，这就是 React 打包完成的结果，看起来目录结构像下面这样：

```plaintext
- build
  - static
    - js
    - css
    - media
  - index.html
  - ...
- node_modules
- public
- src
- package.json
- ...
```



## 三、部署静态页到 Flask



部署静态页的方法有很多，这里我们还是使用 Flask 作为例子。首先在 `cloud-disk-backend` 目录下创建一个 `static` 文件夹。然后将 `cloud-disk-app/build` 打包出的所有内容拷贝到 `cloud-disk-backend/static` 文件夹当中。

为了让 Flask 正确找到目录，我们需要调整一下 `cloud-disk-backend/static` 文件夹中的目录结构。将 `cloud-disk-backend/static/static` 文件夹中的文件移动到上一层文件夹也就是 `cloud-disk-backend/static` 中，其中的内容不需要做改动，仅仅是调整目录结构。最终的目录结构是下面这样：

```plaintext
- static
  - js
  - css
  - media
  - index.html
  - ...
- app.py
- model.py
- ...
```

然后修改 `cloud-disk-backend/app.py`，加入静态文件的路由配置：

```python
@app.route('/s/<path>', methods=['GET'])
def share_static(path):
    return app.send_static_file('index.html')


@app.route('/', methods=['GET'])
def index_static():
    return app.send_static_file('index.html')
```

运行程序，访问 `http://localhost:5000/` 可以看到页面正确显示。

此时也可以将 `cloud-disk-backend/app.py` 中之前没有加入的 `TODO:@authorization_required` 加入到代码当中了。

至此，我们的网盘应用就阶段性完成了。



## 四、总结与回顾



本系列实验从零开始，完成了一个小型网盘应用的前后端搭建，采用了 SPA 的开发模型，前端完全基于 React，后端只提供 RESTful API 接口，实现了前后端彻底分离和解耦。

当然本项目由于属于教程性质，完成的比较粗糙，仍然有很多点可以继续优化，例如：

- 当前只支持了一个用户，没有多用户支持，可以增加用户的注册，加入多用户支持。
- 代码没有考虑到登录用户本身访问分享页面的情况，目前的实现中，登录用户无法通过分享页面下载文件。
- Token 鉴权实现的比较简单，没有实现单点登录和 Token 的强制失效策略，而是完全依赖于时间。
- ...

本教程的结束不是一个终点，而是一个起点。希望本教程能够起到抛砖引玉的作用，让同学们收获到知识的同时，也能体会到亲手搭建一个应用的成就感。

