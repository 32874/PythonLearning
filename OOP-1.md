

```python
class Student():
    name = 'dana'
    age = 18
Student.__dict__

# 实例化
yueyue = Student()
yueyue.__dict__
print(yueyue.name)
```

    dana
    


```python
class A():
    name = 'dana'
    age = 18
    # 注意say的写法，参数由一个self
    def say(self):
        self.name = 'aaaa'
        self.age = 200
# 此案例说明
# 类实例的属性和其对象的实例的属性在不对对象的实例属性赋值的情况下
# 指向同一个变量
print(A.name)
print(A.age)
print('*' * 20)
print(id(A.name))
print(id(A.age))
print('*' * 20)
a = A()
print(a.name)
print(a.age)
print(id(a.name))
print(id(a.age))
```

    dana
    18
    ********************
    1422894712904
    140712183984416
    ********************
    dana
    18
    1422894712904
    140712183984416
    


```python
# 此时，A称为类实例
print(A.name)
print(A.age)

print("*" * 20)
# id 可以鉴别一个变量是否和另一个变量是同一变量
print(id(A.name))
print(id(A.age))
print('*' * 20)
a = A()
# 查看A内所有的属性
print(A.__dict__)
print(a.__dict__)
a.name = "yaona"
a.age = 16
print(a.__dict__)
print(a.name)
print(a.age)
print(id(a.name))
print(id(a.age))
```

    dana
    18
    ********************
    1422894712904
    140712183984416
    ********************
    {'__module__': '__main__', 'name': 'dana', 'age': 18, 'say': <function A.say at 0x0000014B4B223AE8>, '__dict__': <attribute '__dict__' of 'A' objects>, '__weakref__': <attribute '__weakref__' of 'A' objects>, '__doc__': None}
    {}
    {'name': 'yaona', 'age': 16}
    yaona
    16
    1422893949032
    140712183984352
    


```python
class Student():
    name = 'dana'
    age = 18
    
    #注意say的写法，参数由一个self
    def say(self):
        self.name = 'aaaa'
        self.age = 200
        print('my name is {0}'.format(self.name))
        print('my age is {0}'.format(self.age))
    def sayAgain(s):
        print('my name is {0}'.format(s.name))
        print('my age is {0}'.format(s.age))   
yueyue = Student()
yueyue.say()
yueyue.sayAgain()
```

    my name is aaaa
    my age is 200
    my name is aaaa
    my age is 200
    


```python
class Teacher():
    name = 'dana'
    age = 19
    
    def say(self):
        self.name = 'yaona'
        self.age = 17
        print('my name is {0}'.format(self.name))
        # 调用类的成员变量 需要使用 __class__
        print('my age is {0}'.format(__class__.age))
        
    def sayAgain():
        print(__class__.name)
        print(__class__.age)
        print('hello, nice to see you again')
    
t = Teacher()
t.say()
# 调用绑定类函数使用类名
Teacher.sayAgain()
```

    my name is yaona
    my age is 17
    hello, nice to see you again
    


```python
# 关于self的案例
class A():
    name = 'liuying'
    age = 18
    
    def __init__(self):
        self.name = 'aaaa'
        self.age = 200
        
    def say(self):
        print(self.name)
        print(self.age)

class B():
    name = 'bbbb'
    age = 90
    
a = A()
# 此时，系统会默认把a作为第一个参数传入函数
a.say()

# 此时，self被a替换
A.say(a)
# 同样可以把A作为参数传入
A.say(A)

# 此时，传入的是类实例B，因为B具有name和age属性，所以不会报错
A.say(B)

# 以上代码，利用了鸭子模型
```

    aaaa
    200
    aaaa
    200
    liuying
    18
    bbbb
    90
    


```python
# 私有变量案例

class Person():
    # name是公有的成员
    name = 'liuying'
    # __age就是私有成员
    __age = 18

p = Person()
# name是公有变量
print(p.name)
# __age是私有变量
# 注意报错信息
# print(p.__age)
p._Person__age = 19
print(p._Person__age)
```

    liuying
    19
    


```python
# name mangling技术
print(Person.__dict__)

p._Person__age = 19
print(p._Person__age)
```

    {'__module__': '__main__', 'name': 'liuying', '_Person__age': 18, '__dict__': <attribute '__dict__' of 'Person' objects>, '__weakref__': <attribute '__weakref__' of 'Person' objects>, '__doc__': None}
    


```python

```
