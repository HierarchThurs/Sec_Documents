# Windows 10彻底关闭Windows defender

## 1.通过组策略关闭Windows defender

+ 首先使用 Windows + R 组合快捷键呼出“运行”操作框，然后键入 gpedit.msc ，之后点击下方的“确定”即可打开组策略编辑器
+ 打开Win10组策略编辑器之后，依次点击展开“计算机策略”“管理模板”“Windows组件”“Windows Defender防病毒程序”
+ 最后双击右侧的“关闭Windows Defender防病毒程序”，然后在打开的关闭设置中，将默认的“未配置”改为“已启用”，然后点击底部的“确定”保存设置即可。

## 2.通过注册表关闭Windows Defender

+ 使用 Windows + R 组合快捷键呼出，运行操作框，然后键入 regedit 并点击下方的确定，打开注册表
+ 打开Win10注册表之后，依次展开 `计算机\HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows Defender`
+ 接下来在右侧，点击鼠标右键，然后选择新建 DWORD(32位)值
+ 最后新值命名为DisableAntiSpyware，并双击赋值为1

## 3.关闭Defender的自启动

# 重启电脑生效

