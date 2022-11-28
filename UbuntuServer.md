# UbuntuServer常见问题

### ssh问题

+ ssh-server打开：

```linux
  sudo etc/init.d/ssh start 或 sudo service ssh start
```

​	重启ssh服务:

```linux
sudo /etc/init.d/ssh stop
sudo /etc/init.d/ssh start
```

ip地址查询    ``` ifconfig``` 

远程连接ssh显示  ```Access denied```

```linux
sudo vim /etc/sshd_config
修改 PermitRootLogin为 yes
```





### python问题

安装python2和python3以及对应pip

```linux
sudo apt install wget python python3 python3-pip python-ply python3-ply -y
wget https://bootstrap.pypa.io/pip/2.7/get-pip.py
python get-pip.py
```

若遇pip3版本太旧

```linux
sudo pip3 install --upgrade pip
hash -r
```



重启终端

```linux
python --version
python3 --version
pip --version
pip3 --version
```





### Mysql问题

+ 安装

```linux
apt-get install mysql-server -y
apt-get install mysql-client -y
apt-get install libmysqlclient-dev -y
apt install net-tools -y

#检查是否安装成功
sudo netstat -tap | grep mysql
# mysql处于listen状态则为安装成功
```

+ 更改root用户密码

```mysql
mysql -u root -p    初始密码为空
mysql> set password for 用户名@localhost = password('新密码');


update mysql.user set plugin="mysql_native_password" where user="root";
update mysql.user set authentication_string=password('new_password') where user = 'root' and Host = 'localhost';
exit;
```

+ 重启mysql服务```service mysql restart```密码修改成功。



### apache2问题

+ 安装

```linux
apt-get install apache2
```

+ 默认文档根目录是 Ubuntu上的 ```/var/www```目录
+ 配置文件是 ```/etc/apache2/apache2.conf```
+ 配置存储在的子目录在```/etc/apache2```目录





```linux
# 重启apache服务
sudo /etc/init.d/apache2 restart

# 开启apache服务
sudo /etc/init.d/apache2 start

# 关闭
sudo /etc/init.d/apache2 stop
```





### php问题

```linux
# 安装
sudo apt-get install software-properties-common
sudo add-apt-repository ppa:ondrej/php && sudo apt-get update
sudo apt-get -y install php7.2

# 如果之前有其他版本PHP，在这边禁用掉
sudo a2dismod php5
sudo a2enmod php7.2

# 安装常用扩展（建议安装）
sudo apt-get -y install php7.2-fpm php7.2-mysql php7.2-curl php7.2-json php7.2-mbstring php7.2-xml  php7.2-intl php7.2-odbc php7.2-cgi
```

