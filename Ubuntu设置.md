# Ubuntu设置

## 创建root用户密码

```linux
sudo passwd root
```

## SSH远程登录

```linux
sudo apt-get update && sudo apt-get upgrade -y
sudo apt install openssh-client
sudo apt install openssh-server
sudo service ssh restart
sudo vim /etc/ssh/sshd_config
```

+ 取消`Port:22`的注释
+ 更改`PermitRootLogin yes`并取消注释

```linux
sudo service ssh restart
```

## 更换源

源的位置为`/etc/apt/sources.list`

安装过程中更换源

```linux
http://mirrors.aliyun.com/ubuntu
https://mirrors.tuna.tsinghua.edu.cn
```

+ Ubuntu1804清华源

```linux
# 默认注释了源码镜像以提高 apt update 速度，如有需要可自行取消注释
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic main restricted universe multiverse
# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic main restricted universe multiverse
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic-updates main restricted universe multiverse
# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic-updates main restricted universe multiverse
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic-backports main restricted universe multiverse
# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic-backports main restricted universe multiverse
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic-security main restricted universe multiverse
# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic-security main restricted universe multiverse
```

+ Ubuntu2004清华源

```linux
# 默认注释了源码镜像以提高 apt update 速度，如有需要可自行取消注释
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ focal main restricted universe multiverse
# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ focal main restricted universe multiverse
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ focal-updates main restricted universe multiverse
# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ focal-updates main restricted universe multiverse
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ focal-backports main restricted universe multiverse
# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ focal-backports main restricted universe multiverse
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ focal-security main restricted universe multiverse
# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ focal-security main restricted universe multiverse
```

```linux
sudo apt-get update && sudo apt-get upgrade -y
```



## 配置静态网卡

```linux
sudo vim /etc/netplan/00
```

+ 若遇ens33不存在inet地址

```linux
sudo dhclient ens33
```

+ 部分时候会遇到配置好静态ip后无法访问外部网络，更改静态ip地址为自动获取的ip地址即可

```yaml
network:
  ethernets:
    ens33:
      dhcp4: false
      addresses: [192.168.1.100/24]
      gateway4: 192.168.1.1
      optional: true
      nameservers:
              addresses: [114.114.114.114, 8.8.8.8]
  version: 2
```

+ 查看电脑默认dns服务器

```DOS
nslookup
```

+ 应用网卡更改

```linux
sudo netplan apply
```

+ 动态IP地址

```yaml
network:
  ethernets:
  	ens33:
  	  dhcp4: true
  	  dhcp6: true
  version: 2
```

+ 查看动态获取的ip地址和默认网关

```terminal
ifconfig
route -n
```



## 安装Python

```linux
sudo apt install wget python2 python3 python3-pip python-ply python3-ply -y
wget https://bootstrap.pypa.io/pip/2.7/get-pip.py
python2 get-pip.py

//若遇pip3版本落后，执行
python3 -m pip install --upgrade pip

//重启终端
python2
python3
pip2 -V
pip3 -V
```

## docker安装

+ 卸载旧版本

```linux
sudo apt-get remove docker docker-engine docker.io
```

+ 安装

```linux
sudo apt-get install -y apt-transport-https ca-certificates curl gnupg2 software-properties-common
```

+ 添加GPG密钥

```linux
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
```

+ 加入官方仓库

```linux
sudo add-apt-repository \
   "deb [arch=amd64] https://mirrors.tuna.tsinghua.edu.cn/docker-ce/linux/ubuntu \
   $(lsb_release -cs) \
   stable"
```

+ 用apt安装

```linux
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io -y
```

+ 安装docker-compose

```linux
pip3 install docker-compose
docker-compose version
```

```linux
sudo apt install docker -y
sudo apt install docker-compose -y
chmod +x /usr/local/bin/docker-compose
```

+ 更改docker的镜像源

```linux
sudo vim /etc/docker/daemon.json

//添加如下内容
{
  "registry-mirrors": ["https://mirror.ccs.tencentyun.com"]
}

sudo service docker restart //重启docker服务
docker info | grep Mirrors -A 1   //查看配置是否生效
```



## MySQL安装配置

```linux
sudo apt install mysql-server -y
sudo apt install mysql-client -y
sudo apt install libmysqlclient-dev -y

//检查是否安装成功
sudo netstat -tap | grep mysql

//登录
mysql -u root -p

//设置root的初始密码
mysql -u root -p    初始密码为空

ALTER user 'root'@'localhost' IDENTIFIED BY 'newpassword';
flush privileges;

exit;
sudo service mysql restart
```

## 阿里源Ubuntu 1804

```linux
deb https://mirrors.aliyun.com/ubuntu/ bionic main restricted universe multiverse
deb-src https://mirrors.aliyun.com/ubuntu/ bionic main restricted universe multiverse

deb https://mirrors.aliyun.com/ubuntu/ bionic-security main restricted universe multiverse
deb-src https://mirrors.aliyun.com/ubuntu/ bionic-security main restricted universe multiverse

deb https://mirrors.aliyun.com/ubuntu/ bionic-updates main restricted universe multiverse
deb-src https://mirrors.aliyun.com/ubuntu/ bionic-updates main restricted universe multiverse

# deb https://mirrors.aliyun.com/ubuntu/ bionic-proposed main restricted universe multiverse
# deb-src https://mirrors.aliyun.com/ubuntu/ bionic-proposed main restricted universe multiverse

deb https://mirrors.aliyun.com/ubuntu/ bionic-backports main restricted universe multiverse
deb-src https://mirrors.aliyun.com/ubuntu/ bionic-backports main restricted universe multiverse

```

## 阿里源Ubuntu 2004

```linux
deb https://mirrors.aliyun.com/ubuntu/ focal main restricted universe multiverse
deb-src https://mirrors.aliyun.com/ubuntu/ focal main restricted universe multiverse

deb https://mirrors.aliyun.com/ubuntu/ focal-security main restricted universe multiverse
deb-src https://mirrors.aliyun.com/ubuntu/ focal-security main restricted universe multiverse

deb https://mirrors.aliyun.com/ubuntu/ focal-updates main restricted universe multiverse
deb-src https://mirrors.aliyun.com/ubuntu/ focal-updates main restricted universe multiverse

# deb https://mirrors.aliyun.com/ubuntu/ focal-proposed main restricted universe multiverse
# deb-src https://mirrors.aliyun.com/ubuntu/ focal-proposed main restricted universe multiverse

deb https://mirrors.aliyun.com/ubuntu/ focal-backports main restricted universe multiverse
deb-src https://mirrors.aliyun.com/ubuntu/ focal-backports main restricted universe multiverse

```

