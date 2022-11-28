# edge无法翻译＆安装商店扩展

+ 获取正确的ip地址
    + 打开`http://ping.chinaz.com/microsoftedge.microsoft.com`获得最合适的ip地址
    + ![edgeIp](F:\TyperaImage\edgeIp.png)

+ 打开`C:\Windows\System32\drivers\etc`在`host`文件中添加

```host
//无法添加扩展和翻译
13.107.9.158 edge.microsoft.com #Edge翻译
13.107.9.158 msedgeextensions.sf.tlu.dl.delivery.mp.microsoft.com #Edge商店扩展



//无法登录
13.107.9.158 logincdn.msauth.net #微软账户
13.107.9.158 login.live.com #微软账户 
13.107.9.158 account.live.com #微软账户
13.107.9.158 acctcdn.msauth.net #微软账户
```

+ 其中的ip地址更改为检测到的正确的IP地址