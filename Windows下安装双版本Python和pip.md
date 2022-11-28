# Windows下安装双版本Python和pip

+ 官网下载python3和python2安装包正常安装
+ 将```\python27```和```\python27\Scripts```添加到环境变量的path中
+ 修改```python.exe```和```pythonw.exe```的名字为```python2```及对应版本
+ 输入命令

```DOS
python3 -m pip install --upgrade pip --force-reinstall
python2 -m pip install --upgrade pip --force-reinstall
```

安装成功

```DOS
# 设置pip安装源
# 在系统目录C:\Users\用户\AppData\Roaming\pip中编辑pip.ini

[global]
index-url = https://pypi.tuna.tsinghua.edu.cn/simple/
[install]
trusted-host = pypi.tuna.tsinghua.edu.cn

```

pip安装时需要关闭代理软件的系统代理

