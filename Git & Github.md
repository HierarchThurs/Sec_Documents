# Git & Github

## 首次安装

```cmd
git config --global user.name [username]
git config --global user.email [email address]

# 在C:\用户\user 目录下的 .gitconfig中可以修改
```

## 首次使用

在需要用git管理的文件夹下使用`git init`来初始化文件夹

## 常用命令

### 查看本地库状态

```cmd
git status
```

```cmd
Untracked files:
  (use "git add <file>..." to include in what will be committed)
        Hello.txt  # 此处文件名为红，表示当前文件只存在于本地
```

### 添加到暂存区

```cmd
git add <file>  # 将文件添加到暂存区
```

### 从暂存区删除

```cmd
git rm --cached <file>  # 将文件从暂存区内删除，但不会从工作区删除
```

### 提交本地库

```cmd
git commit -m "版本信息" <file>  # 添加版本信息和文件名
```

### 查看版本

```cmd
git reflog  # 查看版本信息
```

```cmd
git log  # 查看版本详细信息 
```

### 版本穿梭

```cmd
git reset --hard <版本号>
```

+ 在`.git`文件夹下的`HEAD`文件中，可以查看到当前版本所属分支
+ 在`.git\refs\heads`文件夹下的master中，可以查看到当前版本号

### 分支

```cmd
git branch <分支名>  # 创建分支
git branch -v       # 查看分支
git checkout <分支名>  # 切换分支
git merge <分支名>  # 把指定的分支合并到当前分支上
```

### 分支合并冲突

合并分支时，两个分支在**同一个文件的同一个位置**有两套完全不同的修改，Git无法替我们决定使用哪一个。必须**人为决定**新代码的内容。

+ `merge`合并的过程中报错无法合并，通过`git status`查看重复修改的文件名，然后修改此文件代码，并将`HEAD`等多余内容删除，保存文件
+ 重新`add`到暂存区后`commit`，此时`commit`无需添加文件名
+ 重新切换回其他分支后，需要将`master`分支合并到当前分支上即可继续修改

## 基于Github

### 创建别名

```cmd
git remote -v  # 查看当前别名

git remote add <别名> <https链接>

git remote rm <别名>  # 删除别名
```

### 推送库

```cmd
git push <别名 or 链接> <分支>
```

### 拉取

```cmd
git pull <别名> <分支>
```

### 克隆

```cmd
git clone <链接>
```

### 团队内协作

在GitHub的库中-> settings -> Collaborators -> Add people即可添加团队成员，成员点击邀请链接后同意方可进入团队

### 团队外协作

`folk`可以拉取库到自己的库

修改后`pull requests`可以推送库

### 添加ssh

在`C:\用户\user`下打开git bash，

```cmd
ssh-keygen -t rsa -C hierarchthurs@gmail.com
# 全部按空格
```

将`.ssh`下的`id_rsa.pub`的内容复制到GitHub个人账号

settings -> SSH and GPG keys -> New SSH key

中添加，即可完成ssh免密登录

## github克隆超时

```git
git config --global https.proxy

git config --global --unset https.proxy
```

s
