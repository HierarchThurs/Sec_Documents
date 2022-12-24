# macOS settings

## command

command  ⌘   = windows徽标

option     ⌥   = Alt

Control     ^    = Ctrl 

## 允许所有应用

```terminal
sudo spctl --master-disable
```

## 重建缓存

```terminal
sudo kextcache -i /
```

## 显示器驱动信息

```terminal
ioreg -l | grep IODisplayEDID
EDID=00FFFFFFFFFFFF0006AF262000000000001C0104A51D127803EE95A3544C99260F5054000000010101010101010101010101010101013C66005AA0402E60302035001EB210000018CA51005AA0402E60302035001EB210000018000000FE0041554F0A202020202020202020000000FE004231333351414E30322E30200A005E
"DisplayVendorID" = 1711
"DisplayProductID" = 8230
```

## mac自动更新屏蔽红点

```terminal
defaults write com.apple.systempreferences AttentionPrefBundleIDs 0
Killall Dock
```

## Finder显示所有文件

Cmd + shift + .

## hosts位置

```terminal
/etc/hosts
sudo vim /etc/hosts
```

## Homebrew

```
git --version

/bin/zsh -c "$(curl -fsSL https://gitee.com/cunkai/HomebrewCN/raw/master/Homebrew.sh)"
```

## 多开

```terminal
open -n <app路径>
```

## mysql

安装好mysql桌面端后

```terminal
sudo vim ~/.zshrc

export PATH=${PATH}:/usr/local/mysql/bin

source ~/.zshrc
# 即可命令行使用mysql
```

