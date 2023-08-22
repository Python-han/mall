# 常用命令

启动：daphne -b 0.0.0.0 -p 8000 bayke.asgi:application

启动进程：supervisord -c deploy/supervisord.conf

查看进程：ps -ef | grep supervisord

杀死指定进程：kill -s SIGTERM 3652

**nginx常用命令：**

1. 启动nginx: `service nginx start`
2. 停止nginx：`service nginx stop`
3. 重启nginx：`service nginx restart`
4. 重载配置文件：`service nginx reload`
5. 查看nginx状态：`service nginx status`

cp bayke /etc/nginx/sites-enabled

```
supervisorctl -c deploy/supervisord.conf stop asgi
```

备份菜单数据：python manage.py dumpdata badmin.baykefrontedmenus > baykeshop/conf/baykefrontedmenus.json

备份权限数据：python manage.py dumpdata badmin.baykepermissionaction > baykeshop/conf/baykepermissionaction.json
