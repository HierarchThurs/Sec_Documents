# 在微软应用商店安装Linux系统，报错WslRegisterDistribution failed with error: 0x8007019e

powershell（管理员）运行

```cmd
Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Windows-Subsystem-Linux
```

YES

