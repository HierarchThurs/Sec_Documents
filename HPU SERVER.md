# HPU SERVER

+ 登录账号

```
# 普通用户
xinguan
xg2602

#管理员
root
xg2602

# 数据库
root
xg2602mysql
```

+ 网卡

```
ip:      218.196.241.232
子网掩码：255.255.255.192
网关：    218.196.241.193
DNS：	218.196.240.8
	     218.196.240.18
```



```yaml
network:
  ethernets:
    enp2s0:
      dhcp4: false
      addresses: [218.196.241.232/26]
      gateway4: 218.196.241.193
      optional: true
      nameservers:
              addresses: [218.196.240.8,218.196.240.18]
    enp3s0:
      dhcp4: true
  version: 2
```

