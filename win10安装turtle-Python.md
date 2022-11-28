# win10 Python安装turtle

```
https://pypi.org/project/turtle/#files
```

下载`turtle`的tar.gz文件，解压

修改`setup.py`

```python
# 第四十行
except ValueError, ve:
# 改成
except (ValueError, ve):
    
    
or

#改成
except ValueError as ve:
```

重新安装

```cmd
pip3 install D:\Net_Sec\PYlib\turtle-0.0.2
```

即可安装成功