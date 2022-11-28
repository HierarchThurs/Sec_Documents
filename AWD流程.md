# 流程

## !!!备份源码2份!!!

```
# 修改登录密码
passwd
```

## 上传并运行`check.sh`

## 文件对比

+ check.sh内容对比
+ beyond compare对比

## 查看flag格式

+ 确认key{\*\*\*\*\*} or flag{\*\*\*\*\*}

## 上传并执行defense.sh

+ 修改key格式

## 上传waf 

```
# 路径
/home/team/workdir/
```

## 上传并执行deployWaf.sh

```php
# 单文件包含waf
include '/home/team/workdir/waf.php'; # 相对路径
```

## 部署waf后监控流量

```terminal
find / -name log_is*

tail -f [filename]
```

## mysql备份

```terminal
# 查看数据库用户名和密码
$ cat /home/team/workdir/config/emmm_config.php | grep mysqlp

# 进入mysql查看数据库
mysql -u [username] -p [passwd]
show databases;

exit;

$ mysqldump -u bestctf -p [passwd] --databases emmm > /home/team/workdir/backupsql.sql

# mysql数据库删除
mysql> drop database [dbname];

# 数据库恢复
mysql> source /home/team/workdir/backupsql.sql;
```

## mysql 修改bestctf用户密码立即修改`/home/team/workdir/config/emmm_config.php`中的`$mysqlpass`参数值

```terminal
# 进入mysql
mysql -u [username] -p
mysql> set password for 用户名@localhost = password('新密码');

# 方法二：用mysqladmin 
格式：mysqladmin -u用户名 -p旧密码 password 新密码 
例子：mysqladmin -uroot -p123456 password 123 

# 方法3：用UPDATE直接编辑user表 
# 首先登录MySQL。 
mysql> use mysql; 
mysql> update user set password=password('123') where user='root' and host='localhost'; 
mysql> flush privileges; 



service mysql restart
```

```terminal
vim /home/team/workdir/config/emmm_config.php

# 修改
'mysqlpass' => '新密码',    // 数据库登录密码

# 修改口令码
```

## 在后台修改admin密码

```
/admin.php
用户，管理员角色，编辑
```



## 安装watchBird

```terminal
php watchbird.php --install [web目录]

php watchbird.php --uninstall [web目录]
```





## 获取flag

```terminal
4.5.1.101
su team
cd /home/team/workdir
wget -q -O - http://172.22.0.1/Getkey
 
 
4.5.16.100
su ctf
cd 
wget -q -O - http://172.22.0.1/Getkey
 
 
 16、15、17、18、2、30、5、6、36、39、50、51、52、5
```



