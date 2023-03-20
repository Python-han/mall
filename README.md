# BaykeShop（拜客商城系统）

For full documentation visit [bayke.shop（拜客商城系统）](http://www.bayke.shop).

## 项目简介

- **曾用名**：[django-happy-shop](https://gitee.com/xingfugz/happy-shop)【不再维护】
- **现用名**：[baykeShop](https://gitee.com/bayke/bayke-shop/)
- **baykeShop(拜客商城系统)** 的由来：
> `django-happy-shop`诞生于2022年，作为django框架的一个包出现，但商城作为一个综合性和定制性很强的项目，
单纯已三方包的形式维护并实现更多的功能就会显得非常臃肿，部署也变得更加困难，另外`django-happy-shop`在开发之初缺乏合理的架构设计，
很多地方设计并不合理，也不利于后期扩展，于是便萌生了重构的念想，也就有了现在的**拜客商城系统**，英文名称直接已域名命名为：**baykeShop**。

## 项目特色
一款更符合国人使用和学习的Python django开源商城项目，没有复杂的语法和过渡的封装，
一切符合django的使用方式，全部采用django的cbv模式开发，便于代码复用及二开和学习！

1、后台定制默认admin,支持动态菜单，兼容三方皮肤（如：django-simpleui）

2、完整的多规格商品逻辑，支持商品SPU和SKU及规格关系

3、支持余额支付、微信支付（开发中）、支付宝支付，配置简单收款便捷

4、凭借django强大的加持，可轻松配置多数据库Mysql/Sqlite3等

5、独立配置文件，通过简单的配置修改可控制全局相关功能

6、PC端采用django的模板系统开发，移动端通过DRF框架将分离开放标准的RestFull api接口（开发中）


## 快速上手

### 1、克隆项目源码
```
git clone https://gitee.com/bayke/bayke-shop.git
```
### 2、创建虚拟环境
```
cd bayke-shop
python3 -m venv venv
```
### 3、激活虚拟环境
```
Windows: venv\Scripts\activate
Liunx: source venv/bin/activate
```
### 4、安装依赖
```
pip install -r requirements.txt
```
### 5、配置Mysql数据库

> 项目默认配置了Mysql数据库和redis缓存，需要你自行在运行项目前，配置安装好Mysql数据库及redis！

- 配置Mysql数据库
项目根目录有个mysql.cnf的文件，修改其中的数据库信息为你自己的！
```
[client]
database = baykedb  # 数据库名
user = root         # 用户名
password = 123456   # 用户密码
host = 127.0.0.1
port = 3306
default-character-set = utf8
```
- redis默认无密码，你也不要配置密码，如果非要配置请在`bayke/settings.py`中的redis配置修改
```
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.redis.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379',
    }
}
```
------------------------------------------------------------------
#### 小白救命招
>不使用mysql及redis也可以（不建议），高手可略过....

将`bayke/settings.py`中的mysql及redis配置改为sqlit3和内存缓存

- 修改Mysql为sqlite3
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```
- 注释掉这段，默认则为内存缓存
```python
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.redis.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379',
    }
}
```
------------------------------------------------------------------

### 6、同步数据库
```bash
python manage.py makemigrations
python manage.py migrate
```
### 7、创建超级管理员
```python
python manage.py createsuperuser
```
### 8、初始化项目
```python
# 运行下边命令可自动生成初始的自定义管理菜单
python manage.py push

or

# 运行下边命令可自动生成初始的自定义管理菜单及相关演示数据
python manage.py push -test
```

### 9、运行项目
```
python3 manage.py runserver
```
### 10、查看项目
```
前台：http://127.0.0.1:8000
后台：http://127.0.0.1:8000/baykeadmin/

后台账号及密码是你在第五步创建的！
```

### 11、支付宝配置

虽然你可以通过修改baykeshop/conf/defaults.py中的默认配置来控制全局相关设置，但我不建议你这么做，这个配置文件作为默认选项的回退，尽量不要去修改，而是在项目bayke目录下的settings.py中覆盖默认项配置！
```python
# bayke/settings.py

BAYKE_SHOP = {
    "ALIPAY_PRIVATE_KEY": "应用私钥pem路径",
    "ALIPAY_PUBLIC_KEY": "支付宝公钥pem路径",
    "ALIPAY_APPID": "支付宝APPID",
    "ALIPAY_SIGN_TYPE": "加密方式，默认是RSA2",
}
```
以上就是配置支付宝收款你需要做的全部工作！

### 赞赏支持

如果该项目给您带来了帮助，您可以为该项目点点star或者写写文章宣传宣传！

当然，如果能给该项目提交PR也是非常欢迎的，开源不易，需要共建！
>![如果对您有帮助，请我喝杯咖啡吧！](baykeshop/static/baykeshop/img/wx.jpg)
如果对您有帮助，请我喝杯咖啡吧！

您的支持对我来说，也是非常重要哦，将有利于该项目的长久持续发展！
