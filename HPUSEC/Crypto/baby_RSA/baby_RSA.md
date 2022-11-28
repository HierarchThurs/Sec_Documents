# baby_RSA

+ 解压后得到`f1ag.key`（小写一）和`fIag.txt`（大写i）文件

+ 将`f1ag.key`放进kali里执行

```terminal
openssl rsa -pubin -text -modulus -in f1ag.key
```

+ 得到

```terminal
RSA Public-Key: (256 bit)
Modulus:
    00:a9:bd:4c:7a:77:63:37:0a:04:2f:e6:be:c7:dd:
    c8:41:60:2d:b9:42:c7:a3:62:d1:b5:d3:72:a4:d0:
    89:12:d9
Exponent: 65537 (0x10001)
Modulus=A9BD4C7A7763370A042FE6BEC7DDC841602DB942C7A362D1B5D372A4D08912D9
writing RSA key
-----BEGIN PUBLIC KEY-----
MDwwDQYJKoZIhvcNAQEBBQADKwAwKAIhAKm9THp3YzcKBC/mvsfdyEFgLblCx6Ni
0bXTcqTQiRLZAgMBAAE=
-----END PUBLIC KEY-----
```

+ 得到e和n

```terminal
e = 65537

Modulus=A9BD4C7A7763370A042FE6BEC7DDC841602DB942C7A362D1B5D372A4D08912D9
```

+ 其中`Modulus`为`n`的十六进制，转换为十进制后得到

```terminal
Modulus=A9BD4C7A7763370A042FE6BEC7DDC841602DB942C7A362D1B5D372A4D08912D9

n = 76775333340223961139427050707840417811156978085146970312315886671546666259161
```

+ 分解`n`的质因数，由于`http://factordb.com/`正在维护，故使用`yafu`进行分解
+ 定位到`yafu`所在目录，运行`yafu-x64.exe`

```cmd
yafu-x64

factor(76775333340223961139427050707840417811156978085146970312315886671546666259161)
```

+ 分解后得到

```cmd
***factors found***

P39 = 280385007186315115828483000867559983517
P39 = 273821108020968288372911424519201044333
```

+ 即为`p`和`q`的值
+ 运行脚本

```python
import gmpy2
import rsa
p = 273821108020968288372911424519201044333
q = 280385007186315115828483000867559983517
n = 76775333340223961139427050707840417811156978085146970312315886671546666259161
e = 65537
d = int(gmpy2.invert(e , (p-1)*(q-1)))
privatekey = rsa.PrivateKey(n , e , d , p , q)
with open("fIag.txt" , "rb") as f:  # 此处更改fIag.txt的位置
    print(rsa.decrypt(f.read(), privatekey).decode())
```

运行得到flag