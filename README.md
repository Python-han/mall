<div align="center">

![logo](fronted/scui/public/img/logo.png)


<h1>baykeShop开源商城系统</h1>

</div>

### 项目简介

baykeShop（拜客商城系统）是一款全开源Python栈商城系统，管理后台完全前后端分离重写以适配项目，前后端100%开源，后台前端采用开源[SCUI](https://gitee.com/lolicode/scui)开源库对接开发，美观、易用、符合当前时下流行的技术栈，后端依托django强大的框架体系，深度结合rest_framework第三方包，使得前后端共用一套接口体系分发扩展，商城PC端采用接口数据可视化的方式采用html渲染还原页面，使其更符合web端的需求，更利于SEO优化，摆脱了前后端分离所带来的打包过程，以及上手难度，更易维护，开发，学习！

本项目融合了django的传统模版体系，同时结合了前后端分离的开发方式，在不同场景选择了不同的技术栈，使其更具学习和研究价值，是python django初学者开发上手学习的不二选择！

### 快速上手

一、 将本仓库拉取到本地，也就是当前你看到的分支main

```git
git clone https://gitee.com/bayke/bayke-shop.git
```

二、 创建python虚拟环境

在项目根目录中，也就是在manage.py的同级创建，命令如下：
```python
python -m venv venv
```
运行该命令之后会创建一个venv的文件夹，此时虚拟环境则创建成功！

三、 激活虚拟环境，安装依赖

3.1 **激活虚拟环境：**
```python
# windows系统
venv\Scripts\activate

# Liunx系统
source venv/bin/activate
```
激活成功后在终端命令行最开始会出现（venv）则代表激活成功，**注意，后边所有的操作都是在激活虚拟环境的状态下进行的**！

3.2 **安装项目依赖：**

在安装依赖之前有必要先对项目的配置有个简单的了解。

项目目录为`bayke`目录，其中将配置文件拆分成了三部分：

01. `settings.py`为共用配置，也就是在开发环境和生产环境共同的配置项

02. `development.py`为开发环境配置，当前的默认配置

03. `production.py`为生产环境配置，部署上线时尽量启用该配置（非必须）

> 备注：为了使用简便，降低开发者理解难度，我们仅是通过引入包的方式 `from .development import *`将开发环境或生产环境配置引入到了settings.py中，也就是说你可以在开发时随意引入他们两个的任何一个，没有局限，不同之处是`production.py`中启用了mysql数据库和redis，需要安装对应的依赖，已包含在依赖列表`requirements.txt`中!

由于mysql数据库的依赖包mysqlclient在不同的环境下安装时会常出现安装失败的现象，目前测试在windows和ubuntu中都没有问题，但在Centos系统中会出现莫名其妙的错误，导致安装失败，由于每个人出现的错误可能不一样，没有一个通用的行之有效的解决方案，目前暂时建议开发环境选择windows或ubuntu其中一个，部署系统选择Ubuntu即可！

如果不启用mysql，则可以在`requirements.txt`中注释掉mysqlclient依赖项之后再运行安装命令！

安装依赖：`pip install -r requirements.txt`

注意：当启用了mysql之后，需在根目录的mysql.cnf配置中配置自己的数据库信息！

```python
[client]
database = baykedb
user = root
password = 123456
host = 127.0.0.1
port = 3306
default-character-set = utf8
```
四、初始化项目

4.1 同步数据库并建表
```
python manage.py redb
```
> 该命令会清空新建app中应用的迁移文件并重新生成，然后自动向数据库执行建表操作，也就是说他会自动执行makemigrations和migrate命令！

5.1 导入初始化数据及权限接口数据
```
python manage.py pushdata
```
> 注意：与之对应的有一个`exportdata`的导出命令，当你改变了后台的扩展配置、后台菜单、接口管理中的任何一项，则可以使用到处命令进行备份，以便在别的地方部署时及时导入，这几个数据是本项目运行的必要数据，所以必须要有！（其他数据备份的方式自行决定！）

五、创建超级管理员运行项目

5.1 创建超级管理员
```python
python manage.py createsuperuser
```
5.2 运行项目后端
```
python manage.py runserver 3000
```
到这里项目的后端接口就已经运行起来了，PC端商城也可以预览了，但管理后台采用了前后端分离的方式开发，需要再配置运行一下前端！

六、后台前端运行

后台前端源码目录在根目录的`fronted/scui`中，标准的vue项目，选择scui这个开源项目就是因为其上手简单易使用组件众多，便于开发，没有使用TS，徒增心智负担，对很多项目来说都是没有必要的！

这里启动和运行可以参考scui本身的文档：https://lolicode.gitee.io/scui-doc/guide/

在这里再次感谢scui开源作者的辛苦付出！

注意：开发环境由于前端和后端不同域，会存在跨域问题，后端需要再配置文件的`CORS_ALLOWED_ORIGINS`和`CSRF_TRUSTED_ORIGINS`配置中放行前端地址！如下所示：

```python
# 配置允许跨域访问的站点列表
CORS_ALLOWED_ORIGINS = [
    'http://192.168.31.174',
    'http://127.0.0.1:2800'
]

# csrf可信来源
CSRF_TRUSTED_ORIGINS = [
    'http://192.168.31.174',
    'http://127.0.0.1:2800'
]
```



