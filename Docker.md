# Docker

## 启动docker

```docker
# 启动docker
sudo service docker start
or
sudo systemctl start docker
```

## image

```docker
# 列出本机所有的 image 文件
docker image ls

# 删除 image 文件
docker image rm [imageName]
```

## 实例

```docker
docker image pull library/hello-world
docker image pull hello-world
```

上面代码中，`docker image pull`是抓取 image 文件的命令。`library/hello-world`是 image 文件在仓库里面的位置，其中`library`是 image 文件所在的组，`hello-world`是 image 文件的名字。

由于 Docker 官方提供的 image 文件，都放在[`library`](https://hub.docker.com/r/library/)组里面，所以它的是默认组，可以省略

## 容器文件

```docker
docker container run hello-world
```

`docker container run`命令会从 image 文件，生成一个正在运行的容器实例。

注意，`docker container run`命令具有自动抓取 image 文件的功能。如果发现本地没有指定的 image 文件，就会从仓库自动抓取。因此，前面的`docker image pull`命令并不是必需的步骤。

```docker
# 查看正在运行的image
docker container ls

终止正在运行的image
docker container kill [containID]
```

## 进入退出docker容器

```docker
# 进入容器命令
docker attach [容器id]
or
docker exec -it [容器id]
or
docker exec -it [容器name] bash
```

```docker
# 退出容器命令
exit
or
Ctrl+P+Q
```

```docker
# 删除docker容器
docker container rm [containerID]
```

## 编写Dockerfile文件

koa-demos项目为例

```terminal
# 下载源码
git clone https://github.com/ruanyf/koa-demos.git
cd koa-demos
```

新建一个文本文件`.dockerignore`

```.dockerignore
.git
node_modules
npm-debug.log
```

上面代码表示，这三个路径要排除，不要打包进入 image 文件。如果你没有路径要排除，这个文件可以不新建。

在项目的根目录下，新建一个文本文件 Dockerfile

```dockerfile
FROM node:8.4
COPY . /app
WORKDIR /app
RUN npm install --registry=https://registry.npm.taobao.org
EXPOSE 3000
CMD node demos/01.js
```

```dockerfile
# 官方Dockerfile
FROM node:8.4
COPY . /app
WORKDIR /app
RUN ["npm", "install", "--registry=https://registry.npm.taobao.org"]
EXPOSE 3000/tcp
```

含义如下

```
FROM node:8.4：该 image 文件继承官方的 node image，冒号表示标签，这里标签是8.4，即8.4版本的 node。
COPY . /app：将当前目录下的所有文件（除了.dockerignore排除的路径），都拷贝进入 image 文件的/app目录。
WORKDIR /app：指定接下来的工作路径为/app。
RUN npm install：在/app目录下，运行npm install命令安装依赖。注意，安装后所有的依赖，都将打包进入 image 文件。
EXPOSE 3000：将容器 3000 端口暴露出来， 允许外部连接这个端口。
CMD node demos/01.js: 容器启动后自动执行node demos/01.js
```

`RUN`命令在 image 文件的构建阶段执行，执行结果都会打包进入 image 文件；`CMD`命令则是在容器启动后执行。另外，一个 Dockerfile 可以包含多个`RUN`命令，但是只能有一个`CMD`命令。

## 创建image文件

```docker
docker image build -t koa-demo .
# or
docker image build -t koa-demo:0.0.1 .
```

`-t`参数用来指定 image 文件的名字，后面还可以用冒号指定标签。如果不指定，默认的标签就是`latest`。最后的那个点表示 Dockerfile 文件所在的路径，上例是当前路径，所以是一个点。

注意，指定了`CMD`命令以后，`docker container run`命令就不能附加命令了（比如前面的`/bin/bash`），否则它会覆盖`CMD`命令。现在，启动容器可以使用下面的命令。

```docker
docker container run --rm -p 8000:3000 -it koa-demo:0.0.1
```



```docker
docker image ls
```

## 生成容器

```docker
docker container run -p 8000:3000 -it koa-demo /bin/bash
# or
docker container run -p 8000:3000 -it koa-demo :0.0.1 /bin/bash
```

参数意义

```docker
-p参数：容器的 3000 端口映射到本机的 8000 端口。
-it参数：容器的 Shell 映射到当前的 Shell，然后你在本机窗口输入的命令，就会传入容器。
koa-demo:0.0.1：image 文件的名字（如果有标签，还需要提供标签，默认是 latest 标签）。
/bin/bash：容器启动以后，内部第一个执行的命令。这里是启动 Bash，保证用户可以使用 Shell。
```

## 其他

```docker 
# 启动已经生成、已经停止运行的容器
docker container start [containerID]
```

```docker
# 查看docker容器的输出，即容器里面shell的标准输出
# 如果docker run 命令运行容器的时候，没有使用-it参数，就要用这个命令查看输出
docker container logs [containerID]
```

```docker
# 进入一个正在运行的docker容器。如果docker run命令运行容器的时候，没有使用-it参数，就要使用这个命令进入容器
docker container exec -it [containerID] /bin/bash
```

```docker
# 从正在运行的docker容器里面，将文件拷贝到本机。
docker container cp [containID]:[/path/to/file] .
```

## 查出容器的地址

```docker 
docker container inspect [containID] | grep IPAddress
# 查找IPAddress字段
```

## 使用已经打包好的镜像

![image-20220815210104409](F:\TyperaImage\image-20220815210104409.png)

```
docker load -i awd-web.tar
```

即可加载镜像

## 使用镜像

```
docker run -it -d -p xxxx:xx --rm {image_name}

-p 加参数xxxx为本机端口,xx为容器端口
-- rm容器关闭后自动删除
-d后台运行
```



