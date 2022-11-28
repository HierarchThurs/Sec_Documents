#  HPU

### 提取压缩包

#### 法一

+ 打开后发现是校徽，拖进kali执行

```ternimal
binwalk HPU.jpg
```

+ 得到

```terminal
DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             JPEG image data, JFIF standard 1.01
63592         0xF868          Zip archive data, at least v2.0 to extract, compressed size: 2047, uncompressed size: 3151, name: rotation_and_translation.png
65779         0x100F3         Zip archive data, encrypted at least v2.0 to extract, compressed size: 41028, uncompressed size: 45568, name: flag.pptx
107660        0x1A48C         End of Zip archive, footer length: 22
```

+ 发现其中有压缩包，执行

```terminal
foremost HPU.jpg
```

+ 在output文件夹下即可查看分离的压缩包

#### 法二

+ 修改`HPU.jpg`后缀为`HPU.zip`即可解压

    （修改后缀得到压缩包的方法不适用于后续ARCHPR破解，故尽量使用法一）



### 修改二维码得到压缩包口令

分离二维码中间部分，左侧顺时针旋转90度，右侧逆时针旋转90度

![image-20220918122457380](F:\TyperaImage\image-20220918122457380.png)

得到修复后的二维码

![image-20220918122737349](F:\TyperaImage\image-20220918122737349.png)

扫码得到`4d696e67446552656e5a65`

十六进制转文本得到`MingDeRenZe`，此为`我们的口号是.zip`的压缩包密码

河南理工大学校训：明德任责

#### 破解ppt密码

找到`key.txt`的最下面的口令`公正爱国法治富强法治平等`

社会主义核心价值观编码解码得到密码为`hpu`

或使用`PPT password recovery`进行暴力破解三位数密码

打开ppt后在最后一页可以发现透明字体，字体改为其他颜色即可得到flag