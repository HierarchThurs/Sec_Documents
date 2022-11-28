# Cardinal搭建

## 平台的搭建

+ 下载`Cardinal_linux_amd64`版通过SFTP导入到Ubuntu中

```linux
//创建AWD项目文件夹
mkdir AWD

//压缩包移动到AWD中
//解压
tar -zxvf Cardinal_xxxxx.tar.gz

//更改Cardinal的权限
chmod +x Cardinal

//启动数据库
sudo service mysql start
mysql -u root -p  //登录

//创建一个普通用户
CREATE USER new_user@localhost IDENTIFIED BY 'user_password';

//给普通用户授权创建数据库
GRANT ALL PRIVILEGES ON cardinal.*  To 'database_user'@'localhost';

//切换普通用户创建一个新的数据库并命名为cardinal
CREATE DATABASE `cardinal` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

show databases;
exit;

//运行Cardinal
./ Cardinal

:port   //选手入口
:port/manager   //管理员入口
```



## 靶机的配置

