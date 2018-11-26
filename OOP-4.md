

```python
# 属性案例
# 创建Student类，描述学生类
# 学生具有Student.name属性
# 但name格式并不统一
# 可以用增加一个函数，然后自动调用的方式，但很蠢
class Student():
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
        # 如果不想修改代码
        self.setName(name)
        
    # 介绍下自己
    def intro(self):
        print('hi my name is {0}'.format(self.name))
        
    def setName(self, name):
        self.name = name.upper()
s1 = Student('liu ying', 19)
s2 = Student('michi stangle', 24)
s1.intro()
s2.intro()
```

    hi my name is LIU YING
    hi my name is MICHI STANGLE
    


```python
# porperty案例
# 定义一个Person类，具有name，age属性
# 对于任意输入的姓名，我们希望都用大写方式保存
# 年龄，我们希望内部统一用整数保存
# x = property(fgget, fset, fdel, doc)
class Person():
    '''
    这是一个人，一个高尚的人，一个脱离了低级趣味的人
    他还有属性
    '''
    # 函数的名称可以任意
    def fget(self):
        return self._name * 2
    def fset(self, name):
        # 所有输入的姓名以大写形式保存
        self._name = name.upper()
    def fdel(self):
        self._name = 'NoName'
    name = property(fget, fset, fdel, '对name进行操作')
# 作业：
# 1.在用户输入年龄的时候，可以输入整数，小数，浮点数
# 2.但内部为了数据整洁，我们统一需要保存整数，直接舍去小数点
```


```python
p1 = Person()
p1.name = 'TuLing'
print(p1.name)
```

    TULINGTULING
    


```python
# 类的内置属性举例
print(Person.__dict__)
print(Person.__doc__)
print(Person.__name__)
print(Person.__bases__)
```

    {'__module__': '__main__', '__doc__': '\n    这是一个人，一个高尚的人，一个脱离了低级趣味的人\n    他还有属性\n    ', 'fget': <function Person.fget at 0x0000022CC31C99D8>, 'fset': <function Person.fset at 0x0000022CC31C98C8>, 'fdel': <function Person.fdel at 0x0000022CC31C9730>, 'name': <property object at 0x0000022CC31D2138>, '__dict__': <attribute '__dict__' of 'Person' objects>, '__weakref__': <attribute '__weakref__' of 'Person' objects>}
    
        这是一个人，一个高尚的人，一个脱离了低级趣味的人
        他还有属性
        
    Person
    (<class 'object'>,)
    


```python
# init 举例
class A():
    def __init__(self, name=0):
        print('哈哈，我被调用了')
a = A()
```

    哈哈，我被调用了
    


```python
# __call__举例
class A():
    def __init__(self, name=0):
        print('哈哈，我被调用了')
    def __call__(self):
        print('我被调用了again')
a = A()
a()
```

    哈哈，我被调用了
    我被调用了again
    


```python
# __str__举例
class A():
    def __init__(self, name=0):
        print('哈哈，我被调用了')
    def __call__(self):
        print('我被调用了again')
    def __str__(self):
        return '图灵学院的例子'
a = A()
print(a)
```

    哈哈，我被调用了
    图灵学院的例子
    


```python
# __getattr__
class A():
    name = 'NoName'
    age = 18
    def __getattr__(self, name):
        print('没找到呀没找到')
        print(name)
        return none
a = A()
print(a.name)
print(a.addr)
# 作业：
# 为什么会打印第四句话，而且第四句话是打印的 None
```

    NoName
    没找到呀没找到
    addr
    None
    


```python
# __setattr__案例
class Person():
    def __init__(self):
        pass
    def __setattr__(self, name, value):
        print('设置属性：{0}'.format(name))
        # 下面语句会导致问题，死循环
        #self.name = value
        # 此种情况，为了避免死循环，规定统一调用父类魔法函数
        super().__setattr__(name, value)
p = Person()
print(p.__dict__)
p.age = 18
        
```

    {}
    设置属性：age
    


```python
# __gt__
class Student():
    def __init__(self, name):
        self._name = name
        pass
    def __gt__(self, obj):
        # print('哈哈，{0}会比{1}大吗？'.format(self, obj))
        print('哈哈，{0}会比{1}大吗？'.format(self._name, obj._name))
        return self._name > obj._name
# 作业：
# 字符串的比较是按什么规则
stu1 = Student('one')
stu2 = Student('two')
print(stu1 > stu2)
```

    哈哈，one会比two大吗？
    False
    


```python
# 三种方法的案例：
class Person():
    # 实例方法
    def eat(self):
        print(self)
        print('Eating......')
        pass
    # 类方法
    # 类方法的第一个参数，一般命名为cls，区别于self
    @classmethod
    def play(cls):
        print(cls)
        print('Playing......')
        pass
    # 静态方法
    # 不需要用第一个参数表示自身或者类
    @staticmethod
    def say():
        print('saying......')
        pass
    
yueyue = Person()
# 实例方法
yueyue.eat()
# 类方法
Person.play()
yueyue.play()
# 静态方法
Person.say()
yueyue.say()
# 作业：
# 自行查找三种方法内存使用方面的区别
```

    <__main__.Person object at 0x000001A139A6C828>
    Eating......
    <class '__main__.Person'>
    Playing......
    <class '__main__.Person'>
    Playing......
    saying......
    saying......
    


```python

```
