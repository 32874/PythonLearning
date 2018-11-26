

```python
class A():
    pass

class B(A):
    pass

class C(A, B):
    pass

print(A.__mro__)
print(B.__mro__)
```

    (<class '__main__.A'>, <class 'object'>)
    (<class '__main__.B'>, <class '__main__.A'>, <class 'object'>)
    


```python
# 多继承的例子
# 子类可以直接拥有父类的属性和方法，私有属性和方法除外
class Fish():
    def __init__(self, name):
        self.name = name
    def swim(self):
        print("i am swimming......")
        
class Bird():
    def __init__(self, name):
        self.name = name
    def fly(self):
        print("I am flying......")

class Person():
    def __init__(self, name):
        self.name = name
    def work(self):
        print('Working......')
        
class SuperMan(Person, Bird, Fish):
    def __init__(self, name):
        self.name = name
#多继承的例子
class SwimMan(Person, Fish):
    def __init__(self, name):
        self.name = name
# 单继承的例子
class Student(Person):
    def __init__(self, name):
        self.name = name
stu = Student('yueyue')
stu.work()


s = SuperMan('yueyue')
s.fly()
s.swim()
```

    Working......
    I am flying......
    i am swimming......
    


```python
# 菱形继承问题
class A():
    pass
class B(A):
    pass
class C(A):
    pass

class D(B, C):
    pass
```


```python
# 构造函数例子
class Person():
    # 对Person类进行实例化的时候
    # 姓名要确定
    # 年龄要确定
    # 地址肯定有
    def __init__(self):
        self.name = 'NoName'
        self.age = 18
        self.address = 'Studentwhonheim'
        print('In init func')
# 实例化一个人
p = Person()
```

    In init func
    


```python
# 构造函数的调用顺序 - 1
# 如果子类没有写构造函数，则自动向上查找，直到找到位置
class A():
    def __init__(self):
        print('A')
class B(A):
    def __init__(self):
        print('B')

class C(B):
    pass

# 此时，首先查找C的构造函数
# 如果没有，则向上按照MRO顺序查找父类的构造函数，直到找到
c = C()
```

    B
    


```python
# 构造函数的调用顺序 - 2

class A():
    def __init__(self):
        print('A')
class B(A):
    def __init__(self, name):
        print('B')
        print(name)

class C(B):
    pass

# 此时，首先查找C的构造函数
# 如果没有，则向上按照MRO顺序查找父类的构造函数，直到找到
# 此时，会出现参数结构不对应错误
c = C()
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-7-90beffbd4d0a> in <module>()
         15 # 如果没有，则向上按照MRO顺序查找父类的构造函数，直到找到
         16 # 此时，会出现参数结构不对应错误
    ---> 17 c = C()
    

    TypeError: __init__() missing 1 required positional argument: 'name'



```python
# 构造函数的调用顺序 - 3

class A():
    def __init__(self):
        print('A')
class B(A):
    def __init__(self, name):
        print('B')
        print(name)

class C(B):
    # c中想扩展B的构造函数
    # 即调用B的构造函数后再添加一些功能
    # 有两种方法实现
    # 第一种是通过父类名嗲用
    '''
    def __init__(self, name):
        B.__init__(self, name)
        print('这是C中附加的功能')
    '''
    # 第二种，使用super
    def __init__(self, name):
        # 首先调用父类构造函数
        super(C, self).__init__(name)
        # 其次，再增加自己的功能
        print("这是C中附加的功能")
    

# 此时，首先查找C的构造函数
# 如果没有，则向上按照MRO顺序查找父类的构造函数，直到找到
# 此时，会出现参数结构不对应错误
c = C('我是C')
```

    B
    我是C
    这是C中附加的功能
    


```python
# Mixin案例
class Person():
    name = 'liuying'
    age = 18
    def eat(self):
        print("eat......")
    def drink(self):
        print('drink......')
    def sleep(self):
        print('sleep......')
class Teacher(Person):
    def work(self):
        print('work')
class Student(Person):
    def study(self):
        print('study')
class Tutor(Teacher, Student):
    pass
t = Tutor()
print(Tutor.__mro__)
print(t.__dict__)
print(Tutor.__dict__)

print('*' * 20)
class TeacherMixin():
    def work(self):
        print('work')
class StudentMixin():
    def study(self):
        print('study')
class TutorM(Person, TeacherMixin, StudentMixin):
    pass
tt = TutorM()
print(TutorM.__mro__)
print(tt.__dict__)
print(TutorM.__dict__)
```

    (<class '__main__.Tutor'>, <class '__main__.Teacher'>, <class '__main__.Student'>, <class '__main__.Person'>, <class 'object'>)
    {}
    {'__module__': '__main__', '__doc__': None}
    ********************
    (<class '__main__.TutorM'>, <class '__main__.Person'>, <class '__main__.TeacherMixin'>, <class '__main__.StudentMixin'>, <class 'object'>)
    {}
    {'__module__': '__main__', '__doc__': None}
    


```python
# issubclass
class A():
    pass
class B(A):
    pass
class C():
    pass
print(issubclass(B,A))
print(issubclass(C,A))
print(issubclass(B, object))
```

    True
    False
    True
    


```python
# isinstance
class A():
    pass
a = A()
print(isinstance(a, A))
print(isinstance(A,A))
```

    True
    False
    


```python
# hasattr
class A():
    name = 'noname'
a = A()
print(hasattr(a, 'name'))
print(hasattr(a, 'age'))
```

    True
    False
    


```python
# help案例
# 我想 知道setattr的具体用法
help(setattr)
```

    Help on built-in function setattr in module builtins:
    
    setattr(obj, name, value, /)
        Sets the named attribute on the given object to the specified value.
        
        setattr(x, 'y', v) is equivalent to ``x.y = v''
    
    


```python
# dir 案例
class A():
    pass
#dir(A)
a = A()
dir(a)
```




    ['__class__',
     '__delattr__',
     '__dict__',
     '__dir__',
     '__doc__',
     '__eq__',
     '__format__',
     '__ge__',
     '__getattribute__',
     '__gt__',
     '__hash__',
     '__init__',
     '__init_subclass__',
     '__le__',
     '__lt__',
     '__module__',
     '__ne__',
     '__new__',
     '__reduce__',
     '__reduce_ex__',
     '__repr__',
     '__setattr__',
     '__sizeof__',
     '__str__',
     '__subclasshook__',
     '__weakref__']




```python

```
