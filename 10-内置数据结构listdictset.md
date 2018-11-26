
# 关于元组的函数
- 先看代码
- 以下函数，对list基本适用


```python
# len：获取元组的长度
t = (1, 2, 3, 4, 5)
len(t)
```




    5




```python
# max, min：最大最小值
# 如果，列表或元组中有多个最大最小值，则实际打印出哪个
print(max(t))
print(min(t))
```

    5
    1
    


```python
# tuple:转化或创建元组
l = [1, 2, 3, 4, 5]
t = tuple(l)
print(t)

t = tuple()
print(t)
```

    (1, 2, 3, 4, 5)
    ()
    

# 元组的函数
- 基本跟list通用


```python
# count:计算指定数据出现的次数
t = (2, 1, 2, 3, 45, 1, 1, 2,)
print(t.count(2))

# index:求指定元素在元组中的索引位置
print(t.index(45))

# 如果需要查找的数字是多个，则返回第一个
print(t.index(1))
```

    3
    4
    1
    

# 元组变量交换法
- 两个变量交换值


```python
# 两个变量交换值
a = 1
b = 3
print(a)
print(b)
print("*" * 20)
# java程序员会这么写
c = a
a = b
b = c
print(a)
print(b)

print("*" * 20)
# python的写法
a,b = b,a
print(a)
print(b)
```

    1
    3
    ********************
    3
    1
    ********************
    1
    3
    

# 集合-set
- 集合是高中数学中的一个概念
- 一堆确定的无序的唯一的数据，集合中每一个数据成为一个元素


```python
# 集合的定义
s = set()
print(type(s))
print(s)

# 此时，大括号内一定要有值，否则定义出的是一个dict
s = {1, 2, 3, 4, 5, 6, 7}
print(type(s))
print(s)
```

    <class 'set'>
    set()
    <class 'set'>
    {1, 2, 3, 4, 5, 6, 7}
    


```python
# 如果只是用大括号定义，则定义的是一个dict类型
d = {}
print(type(d))
print(d)
```

    <class 'dict'>
    {}
    

# 集合的特征
- 集合内数据无序，即无法使用索引和分片
- 集合内部数据元素具有唯一性，可以用来排除重复数据
- 集合内的数据， str, int, float, tuple, 冰冻集合等， 即内部只能放置可哈希数据

# 集合序列操作


```python
# 成员检测
# in, not in
s = {4, 5, "i", "love", "wangxiaojing"}
print(s)

if 'love' in s:
    print('爱呀')
    
if 'haha' not in s:
    print("爱个锤子")
```

    {'love', 'wangxiaojing', 4, 5, 'i'}
    爱呀
    爱个锤子
    

# 集合遍历操作


```python
# for循环
s = {4, 5 , "i", "love", "wangxiaojing"}

for i in s:
    print(i, end=" ")
```

    love wangxiaojing 4 5 i 


```python
# 带有元组的集合遍历
s = {(1, 2, 3), ('i', 'love', 'wangxiaojing'), (4, 5, 6)}

for k,m,n in s:
    print(k, '--', m, '--', n)
    
for k in s:
    print(k)
```

    i -- love -- wangxiaojing
    4 -- 5 -- 6
    1 -- 2 -- 3
    ('i', 'love', 'wangxiaojing')
    (4, 5, 6)
    (1, 2, 3)
    

# 集合的内涵


```python
# 普通集合内涵
s = {23, 223, 545, 3, 1, 2, 3, 4, 3, 2, 3, 1, 2, 4, 3}
print(s)

# 普通集合内涵
ss = {i for i in s}
print(ss)
```

    {545, 1, 3, 2, 4, 23, 223}
    {545, 2, 3, 4, 1, 23, 223}
    


```python
# 带条件的集合内涵
sss = {i for i in s if i % 2 == 0}
print(sss)
```

    {2, 4}
    


```python
# 多循环的集合内涵
s1 = {1, 2, 3, 4}
s2 = {'i', 'love', 'wangxiaojing'}
s = {m*n for m in s2 for n in s1}
print(s)
s = {m*n for m in s2 for n in s1 if n ==2}
print(s)
```

    {'love', 'lovelovelovelove', 'wangxiaojing', 'wangxiaojingwangxiaojing', 'wangxiaojingwangxiaojingwangxiaojingwangxiaojing', 'lovelove', 'i', 'ii', 'iiii', 'lovelovelove', 'iii', 'wangxiaojingwangxiaojingwangxiaojing'}
    {'lovelove', 'wangxiaojingwangxiaojing', 'ii'}
    

# 集合函数/关于集合的函数


```python
# len, max, min:跟其他基本函数一致
s = {43, 23, 56, 223, 4, 2, 1222, 4, 323, 1}
print(len(s))
print(max(s))
print(min(s))
```

    9
    1222
    1
    


```python
# set:生成一个集合
l = [1, 2, 3, 4, 3, 23, 1, 2, 3, 4]
s = set(l)
print(s)
```

    {1, 2, 3, 4, 23}
    


```python
# add:向集合内添加元素
s = {1}
s.add(334)
print(s)
```

    {1, 334}
    


```python
# clear
s = {1, 2, 3, 4, 5}
print(id(s))
s.clear()
print(id(s))
# 结果表明clear函数是原地清空数据
```

    2435861107880
    2435861107880
    


```python
# copy：拷贝
# remove：移除指定的值
# discard：移除集合中指定的值，跟remove一样，但是如果要删除的话，不报错
s = {23, 3, 4, 5, 1, 2, 3}
s.remove(4)
print(s)
s.discard(1)
print(s)

print('*' * 20)
s.discard(1100)
print(s)

s.remove(1100)
print(s)
# 为啥remove不存在的值会报keyerror
```

    {1, 2, 3, 5, 23}
    {2, 3, 5, 23}
    ********************
    {2, 3, 5, 23}
    


    ---------------------------------------------------------------------------

    KeyError                                  Traceback (most recent call last)

    <ipython-input-22-0ece812997e7> in <module>()
         12 print(s)
         13 
    ---> 14 s.remove(1100)
         15 print(s)
    

    KeyError: 1100



```python
# pop随机移除一个元素
s = {1, 2, 3, 4, 5, 6, 7}
d = s.pop()
e = s.pop()
print(d)
print(e)
print(s)

```

    1
    2
    {3, 4, 5, 6, 7}
    


```python
# 集合函数
# intersection:交集
# difference:差集
# union：并集
# issubset:检查一个集合是否是另一个子集
# issuperset:检查一个集合是否是另一个超集
s1 = {1, 2, 3, 4, 5, 6}
s2 = {5, 6, 7, 8, 9}

s_1 = s1.intersection(s2)
print(s_1)

s_2 = s1.difference(s2)
print(s_2)

s_3 = s1.issubset(s2)
print(s_3)
```

    {5, 6}
    {1, 2, 3, 4}
    False
    


```python
# 集合的数学操作
s1 = {1, 2, 3, 4, 5, 6}
s2 = {5, 6, 7, 8, 9}

s_1 = s1 - s2
print(s_1)

s_2 = s1 + s2
print(s_2)
```

    {1, 2, 3, 4}
    


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-30-3c9fa500e5d3> in <module>()
          6 print(s_1)
          7 
    ----> 8 s_2 = s1 + s2
          9 print(s_2)
    

    TypeError: unsupported operand type(s) for +: 'set' and 'set'


# frozen set:冰冻集合
- 冰冻集合就是不可以进行任何修改的集合
- frozenset是一种特殊集合


```python
# 创建
s = frozenset()
print(type(s))
print(s)
```

    <class 'frozenset'>
    frozenset()
    

# dict字典
- 字典是一种组合数据，没有顺序的组合数据，数据以键值对形式出现


```python
# 字典的创建
# 创建空字典1
d = {}
print(d)

# 创建空字典2
d = dict()
print(d)

# 创建有值的字典，每一组数据用冒号隔开，每一个键值对用逗号隔开
d = {'one':1,'tow':2,'three':3}
print(d)

# 用dict创建有内容字典1
d = dict({'one':1,'tow':2,'three':3})
print(d)

# 用dict创建有内容字典2
# 利用关键字参数
d = dict(one=1, two=2, three=3)
print(d)


d = dict([('one',1),('two',2),('three',3)])
print(d)
```

    {}
    {}
    {'one': 1, 'tow': 2, 'three': 3}
    {'one': 1, 'tow': 2, 'three': 3}
    {'one': 1, 'two': 2, 'three': 3}
    {'one': 1, 'two': 2, 'three': 3}
    

# 字典的特征
- 字典是系列类型，但是是无序序列，所以没有分片和索引
- 字典中的数据每个都有键值对组成，即kv对
    - key:必须是可哈希的值，比如int， string， float， tuple，但是，list，set，dict不行
    - value:任何值

# 字典常见操作


```python
# 访问数据
d = dict(one=1, two=2, three=3)
# 注意访问格式
# 中括号内是键值
print(d['one'])

d['one'] = 'eins'
print(d)

# 删除某个操作
# 使用del操作
del d["one"]
print(d)
```

    1
    {'one': 'eins', 'two': 2, 'three': 3}
    {'two': 2, 'three': 3}
    


```python
# 成员检测，in，not in
# 成员检测检测的是key内容
d = dict(one=1, two=2, three=3)

if 2 in d:
    print('value')
    
if 'two' in d:
    print('key')
    
if ('two', 2) in d:
    print('kv')
```

    key
    


```python
# 遍历在python2 和 3 中区别比较大，代码不通用
# 按key来使用for循环
d = {'one':1, 'two':2, 'three':3}
# 使用for循环，直接按key值访问
for k in d:
    print(k , d[k])
    
# 上述代码可以改写成如下
for k in d.keys():
    print(k, d[k])
    
# 只访问字典的值
for v in d.values():
    print(v)
    
# 注意以下特殊用法
for k,v in d.items():
    print(k, '--', v)
```

    one 1
    two 2
    three 3
    one 1
    two 2
    three 3
    1
    2
    3
    one -- 1
    two -- 2
    three -- 3
    

# 字典生成式


```python
d = {'one':1, 'two':2, 'three':3}

# 常规字典生成式
dd = {k:v for k,v in d.items()}
print(dd)

# 加限制条件的字典生成式
dd = {k:v for k,v in d.items() if v % 2 ==0}
print(dd)
```

    {'one': 1, 'two': 2, 'three': 3}
    {'two': 2}
    

# 字典相关函数 


```python
# 通用函数： len, max, min, dict
# str(字典)： 返回字典的字符串格式
d = {'one':1, 'two':2, 'three':3}
print(str(d))
```

    {'one': 1, 'two': 2, 'three': 3}
    


```python
# clear:清空字典
# items：返回字典的键值对组成的元组格式

d = {'one':1, 'two':2, 'three':3}
i = d.items()
print(type(i))
print(i)
```

    <class 'dict_items'>
    dict_items([('one', 1), ('two', 2), ('three', 3)])
    


```python
# keys:返回字典的键组成的一个结构
k = d.keys()
print(type(k))
print(k)
```

    <class 'dict_keys'>
    dict_keys(['one', 'two', 'three'])
    


```python
# values:同理，一个可迭代的结构
v = d.values()
print(type(v))
print(v)
```

    <class 'dict_values'>
    dict_values([1, 2, 3])
    


```python
# get:根据指定键返回相应的值，好处是，可以设置默认值
d = {'one':1, 'two':2, 'three':3}
print(d.get('on333'))

# get默认值是None，可以设置
print(d.get('one',100))
print(d.get('one333',100))

# 体会以下代码跟上面代码的区别
print(d['on333'])
```

    None
    1
    100
    


    ---------------------------------------------------------------------------

    KeyError                                  Traceback (most recent call last)

    <ipython-input-10-6e404d54bfb2> in <module>()
          8 
          9 # 体会以下代码跟上面代码的区别
    ---> 10 print(d['on333'])
    

    KeyError: 'on333'



```python
# fromkeys:使用指定的序列作为键，使用一个值作为字典的所有的键的值
l = ['eins', 'zwei', 'dree']
# 注意fromkeys两个参数的类型
# 注意fromkyes的调用主体
d = dict.fromkeys(l, 'hahahahha')
print(d)
```

    {'eins': 'hahahahha', 'zwei': 'hahahahha', 'dree': 'hahahahha'}
    
