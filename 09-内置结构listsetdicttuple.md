

```python
# 传值和传地址的区别
# 对于简单的数值，采用传值操作，即在函数内对参数的操作不怕影响外面的变量
# 对于复杂变量，采用传地址操作，此时函数内的参数和外部变量是同一份内容，任何地方对此内容的更改都影响另外的变量或参数的使用

def a(n):
    n[2] = 300
    print(n)
    return None
    
def b(n):
    n += 100
    print(n)
    return None

an = [1, 2, 3, 4, 5, 6]
bn = 9

print(an)
a(an)
print(an)

print(bn)
b(bn)
print(bn)
```

    [1, 2, 3, 4, 5, 6]
    [1, 2, 300, 4, 5, 6]
    [1, 2, 300, 4, 5, 6]
    9
    109
    9
    

# 关于列表的函数


```python
l = ['a', 'i love wangxiaojing', 45, 766, 5+4j]
l
```




    ['a', 'i love wangxiaojing', 45, 766, (5+4j)]




```python
# append 插入一个内容
a = [i for i in range(1,5)]
print(a)
a.append(100)
print(a)
```

    [1, 2, 3, 4]
    [1, 2, 3, 4, 100]
    


```python
# insert:制定位置插入
# insert(index, data), 插入位置是index前面
print(a)
a.insert(3,666)
print(a)
```

    [1, 2, 3, 4, 100]
    [1, 2, 3, 666, 4, 100]
    


```python
# 删除
# del 删除
# pop,从对位拿出一个元素，即把最后一个元素取出来
print(a)
last_ele = a.pop()
print(last_ele)
print(a)
```

    [1, 2, 3, 666, 4, 100]
    100
    [1, 2, 3, 666, 4]
    


```python
# remove:在列表中删除指定的值的元素
# 如果被删除的值没在list中，则报错
# 即，删除list指定值的操作应该使用try...except语句，或者先进行判断
a.insert(4,666)
print(a)
print(id(a))
a.remove(666)
print(a)
print(id(a))

# 输出两个id值一样，说明，remove操作是在原list直接操作
```

    [1, 2, 3, 4, 666]
    139662142183752
    [1, 2, 3, 4]
    139662142183752
    


```python
# clear:清空
print(a)
print(id(a))
a.clear()
print(a)
print(id(a))

# 如果不需要列表地址保持不变，则清空列表可以使用以下方式
# a = list()
# a = []
```

    [1, 2, 3, 4]
    139662142183752
    []
    139662142183752
    


```python
# reverse:翻转列表内容，原地址翻转

a= [1, 2, 3, 4, 5]
print(a)
print(id(a))

a.reverse()

print(a)
print(id(a))
```

    [1, 2, 3, 4, 5]
    139662142184840
    [5, 4, 3, 2, 1]
    139662142184840
    


```python
# extend:扩展列表，两个列表，把一个直接拼接到后一个上

a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 10]
print(a)
print(id(a))

a.extend(b)

print(a)
print(id(a))
```

    [1, 2, 3, 4, 5]
    139662142304520
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    139662142304520
    


```python
# count:查找列表中指定值或元素的个数
print(a)
a.append(8)
a.insert(4,8)
print(a)
a_len = a.count(8)
print(a_len)
```

    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    [1, 2, 3, 4, 8, 5, 6, 7, 8, 9, 10, 8]
    3
    


```python
# copy:拷贝，浅拷贝

# 列表类型变量赋值示例
a = [1, 2, 3, 4, 5, 666]
print(a)
b = a
# list类型，简单赋值操作，是传地址
b[3] = 777
print(a)
print(id(a))
print(b)
print(id(b))

print('*' * 20)
#为了解决以上问题，list赋值需要从用copy函数
b = a.copy()
print(a)
print(id(a))
print(b)
print(id(b))

print('*' * 30)
b[3] = 888
print(a)
print(b)
```

    [1, 2, 3, 4, 5, 666]
    [1, 2, 3, 777, 5, 666]
    139662142183624
    [1, 2, 3, 777, 5, 666]
    139662142183624
    ********************
    [1, 2, 3, 777, 5, 666]
    139662142183624
    [1, 2, 3, 777, 5, 666]
    139662142184840
    ******************************
    [1, 2, 3, 777, 5, 666]
    [1, 2, 3, 888, 5, 666]
    


```python
# 深拷贝和浅拷贝的区别
# 出现下面问题的原因是，copy 函数是个浅拷贝函数，即只拷贝一层内容
# 深拷贝需要使用特定工具
a = [1, 2, 3, [10, 20, 30]]
b = a.copy()
print(id(a))
print(id(b))
print(id(a[3]))
print(id(b[3]))
a[3][2] = 666
print(a)
print(b)
```

    1935853885256
    1935853166984
    1935853168328
    1935853168328
    [1, 2, 3, [10, 20, 666]]
    [1, 2, 3, [10, 20, 666]]
    

# 元组-tuple
- 元组可以看成是一个不可更改的list
## 元组创建


```python
# 创建空元组
t = ()
print(type(t))

# 创建一个只有一个值的元组
t = (1,)
print(type(t))
print(t)

# 创建多个值的元组
t = (1, 2, 3, 4, 5)
print(type(t))
print(t)

l = [1, 2, 3, 4, 5]
t = tuple(l)
print(type(t))
print(t)
```

    <class 'tuple'>
    <class 'tuple'>
    (1,)
    <class 'tuple'>
    (1, 2, 3, 4, 5)
    <class 'tuple'>
    (1, 2, 3, 4, 5)
    

## 元组的特性
- 是有序列表，有序
- 元组数据值可以访问，不能修改，不能修改，不能修改
- 元组数据可以是任意类型
- 总之，list所有特性，除了可修改外，元组都具有
- 也就意味着，list具有的一些操作，比如索引，分片，序列相加，相乘，成员资格操作等，一模一样


```python
# 索引操作
t = (1, 2, 3, 4, 5)
print(t[4])
```

    5
    


```python
# 超标错误
print(t[12])
```


    ---------------------------------------------------------------------------

    IndexError                                Traceback (most recent call last)

    <ipython-input-5-0db0bf4ec3b5> in <module>()
          1 # 超标错误
    ----> 2 print(t[12])
    

    IndexError: tuple index out of range



```python
t = (1, 2, 3, 4, 5, 6)
t1 = t[1::2]
print(id(t))
print(id(t1))
print(t1)

# 切片可以超标
t2 = t[2:100]
print(t2)
```

    1163841731944
    1163841223560
    (2, 4, 6)
    (3, 4, 5, 6)
    


```python
# 序列相加
t1 = (1, 2, 3)
t2 = (5, 6, 7)

# 传址操作
print(t1)
print(id(t1))
t1 = t1 + t2
print(t1)
print(id(t1))

# 以上操作
t1 = (1, 2, 3)
t1 = (2, 3, 4)

# tuple的不可修改，指的是内容的不可修改
# 修改tuple内容会导致报错
t1[1] = 100
```

    (1, 2, 3)
    1163841811944
    (1, 2, 3, 5, 6, 7)
    1163820372424
    


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-13-5f37037dea8c> in <module>()
         16 # tuple的不可修改，指的是内容的不可修改
         17 # 修改tuple内容会导致报错
    ---> 18 t1[1] = 100
    

    TypeError: 'tuple' object does not support item assignment



```python
# 元组相乘
t = (1, 2, 3)
t = t * 3
print(t)
```

    (1, 2, 3, 1, 2, 3, 1, 2, 3)
    


```python
# 成员检测
t = (1, 2, 3)
if 2 in t:
    print("yes")
else:
    print("no")
```

    yes
    


```python
# 元组遍历，一般采用for
# 1. 单层元组遍历
t = (1, 2, 3, "wangxiaojing", "i", "love")
for i in t:
    print(i,end=" ")
```

    1 2 3 wangxiaojing i love 


```python
# 2. 双层元组的遍历
t = ((1, 2, 3), (2, 3, 4), ("i", "love", "wangxiaojing"))

# 对以上元组的遍历，可以如下
# 1.
for i in t:
    print(i)
    
for k,m,n in t:
    print(k, '---', m, '---', n)
```

    (1, 2, 3)
    (2, 3, 4)
    ('i', 'love', 'wangxiaojing')
    1 --- 2 --- 3
    2 --- 3 --- 4
    i --- love --- wangxiaojing
    
