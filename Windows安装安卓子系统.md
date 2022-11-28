# Windows安装安卓子系统

打开

```
https://store.rg-adguard.net/
```

输入

```
https://www.microsoft.com/store/productid/9p3395vx91nr

选择Slow，对号
```

选择最后的文件

```
MicrosoftCorporationII.WindowsSubsystemForAndroid_2209.40000.26.0_neutral_~_8wekyb3d8bbwe.Msixbundle

不选择BlockMap
```

更新微软商店，下载安装`Microsoft.UI.Xaml.2.6`

管理员身份打开powershell

```
Add-AppxPackage "C:\Users\Hierarch\Desktop\MicrosoftCorporationII.WindowsSubsystemForAndroid_2209.40000.26.0_neutral_~_8wekyb3d8bbwe.Msixbundle"
```



