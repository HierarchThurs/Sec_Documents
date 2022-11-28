# CentOS 7

### 安装后用命令行配置网卡

```
cd /etc/sysconfig/network-scripts/
vim ifcfg-ens33


把ONBOOT  改为yes,保存

service network restart
```

### 打开ssh

```
$ systemctl start sshd.service #开启ssh服务

$ systemctl restart sshd.service #重启ssh服务

$ systemctl enable sshd.service #设置ssh服务开机自启

$ systemctl status sshd.service #查看ssh服务状态
```

### 更新

```terminal
$ yum -y update：升级所有包同时也升级软件和系统内核；
$ yum -y upgrade：只升级所有包，不升级软件和系统内核
```

## 安装docker

```terminal
# 卸载旧版本
$ yum remove docker  docker-common docker-selinux docker-engine

# 安装软件包和依赖
$ yum install -y yum-utils device-mapper-persistent-data lvm2

# 设置yum源二选一
$ yum-config-manager --add-repo http://download.docker.com/linux/centos/docker-ce.repo（中央仓库）

$ yum-config-manager --add-repo http://mirrors.aliyun.com/docker-ce/linux/centos/docker-ce.repo（阿里仓库）

# 查看docker版本
$ yum list docker-ce --showduplicates | sort -r

# 安装docker
$ yum install docker-ce (这样写默认安装最新版本)
$ yum install  docker-ce-<VERSION_STRING> (指定安装版本) 
例： yum install docker-ce-18.03.1.ce

#启动并加入开机启动
$ systemctl start docker
$ systemctl enable docker
```

```terminal
# 更换仓库
$ vim /etc/docker/daemon.json
```

```json
{
  "registry-mirrors": [
    "https://mirror.ccs.tencentyun.com",
    "https://hub-mirror.c.163.com"
  ]
}
```

```terminal
$ sudo systemctl restart docker
$ docker info
```



## 重装新版本python

```terminal
# python2
$ wget https://www.python.org/ftp/python/2.7.18/Python-2.7.18.tgz

$ tar -xvzf Python-2.7.18.tgz

$ yum install gcc* openssl openssl-devel ncurses-devel.x86_64 bzip2-devel sqlite-devel python-devel zlib -y

$ cd Python-2.7.18

$ sudo ./configure --prefix=/usr/local

$ make #编译

$ make altinstall

$ mv /usr/bin/python /usr/bin/python2.7.5  #备份旧版本

$ ln -s /usr/local/bin/python2.7 /usr/bin/python  #链接新版本

#将以下3个文件首行的 #!/usr/bin/python 都改为 #!/usr/bin/python2.7
/usr/bin/yum
/usr/libexec/urlgrabber-ext-down
/usr/bin/yum-config-manager
```

```terminal
# python3
$ yum -y install zlib-devel bzip2 bzip2-devel readline-devel sqlite sqlite-devel openssl-devel xz xz-devel libffi-devel

$ mkdir -p /usr/local/python3

$ wget https://www.python.org/ftp/python/3.7.6/Python-3.7.6.tgz

$ tar -xvf Python-3.7.6.tgz

$ cd Python-3.7.6 && ./configure --prefix=/usr/local/python3 && make && make altinstall

$ ln -s /usr/local/python3/bin/python3.9 /usr/bin/python3
```

```terminal
# pip pip2 pip3
$ python2 -m pip install --upgrade --force pip
$ python3 -m pip3 install --upgrade --force pip

# 若python2无法安装
$ wget https://bootstrap.pypa.io/pip/2.7/get-pip.py
$ python2 get-pip.py

$ ln -s /usr/local/bin/pip2 /usr/bin/pip2
$ ln -s /usr/local/python3/bin/pip3 /usr/bin/pip3
```

## node

```terminal
$ cd /usr/local
$ wget https://nodejs.org/dist/v16.18.1/node-v16.18.1-linux-x64.tar.gz
$ tar -zxvf node-v16.18.1-linux-x64.tar.gz
$ mv node-v16.18.1-linux-x64 /usr/local/bin/Node.js
```

```terminal
$ ln -s /usr/local/bin/Node.js/bin/node /usr/bin/node
$ ln -s /usr/local/bin/Node.js/bin/npm /usr/bin/npm
$ ln -s /usr/local/bin/Node.js/bin/npx /usr/bin/npx
```

```terminal
vim /etc/profile

# 在最后一行添加
export NODE_HOME=/usr/local/bin/Node.js
export PATH=$PATH:$NODE_HOME/bin
export NODE_PATH=$NODE_HOME/lib/node_modules

# 执行
source /etc/profile
```

```
node -v
npm -v
npx -v
```



