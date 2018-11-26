

```python
# 继承的语法
# 在python中，任何类都有一个共同的父类叫Object
class Person():
    name = 'NoName'
    age = 0
    __score = 0 # 考试成绩是秘密，只要自己知道
    _petname = 'sec' #小明，是保护的，子类可以用，但不能公用
    def sleep(self):
        print('Sleeping ... ...')
        
# 父类写在括号内
class Teacher(Person):
    teacher_id = '9527'
    def make_test(self):
        print('attention')
    
t = Teacher()
print(t.name)
# 受保护不能外部访问，为啥这里可以
print(t._petname)

# 私有访问问题
# 公开访问私有变量，报错
# print(t.__score)

t.sleep()
print(t.teacher_id)
t.make_test()
```

    NoName
    sec
    Sleeping ... ...
    9527
    attention
    


```python
# 子类和父类定义同一个名称变量，则优先使用子类本身
class Person():
    name = 'NoName'
    age = 0
    __score = 0 # 考试成绩是秘密，只要自己知道
    _petname = 'sec' #小明，是保护的，子类可以用，但不能公用
    def sleep(self):
        print('Sleeping ... ...')
    def work(self):
        print('make some money')
        
# 父类写在括号内
class Teacher(Person):
    teacher_id = '9527'
    name = 'DaNa'
    def make_test(self):
        print('attention')
        
t = Teacher()
print(t.name)
```

    DaNa
    


```python
# 子类扩充父类功能的案例
# 人有工作的函数，老师也有工作的函数，但老师的工作需要讲课
class Person():
    name = 'NoName'
    age = 0
    __score = 0 # 考试成绩是秘密，只要自己知道
    _petname = 'sec' #小明，是保护的，子类可以用，但不能公用
    def sleep(self):
        print('Sleeping ... ...')
    def work(self):
        print('make some money')
        
# 父类写在括号内
class Teacher(Person):
    teacher_id = '9527'
    name = 'DaNa'
    def make_test(self):
        print('attention')
    def work(self):
        # 扩充父类的功能只需要调用
        # Person.work(self)
        super().work()
        self.make_test()
        
t = Teacher()
t.work()
```

    make some money
    attention
    


```python
# 构造函数的概念

class Dog():
    # __init__就是构造函数
    # 每次实例化的时候，第一个被调用
    # 因为主要工作是进行初始化，所以得名
    def __init__(self):
        print('I a init in dog')

# 实例化的时候，括号内的参数需要跟构造函数参数匹配
kaka = Dog()
```

    I a init in dog
    


```python
# 继承中的构造函数
class Animal():
    pass

class BuruAni(Animal):
    pass

class Dog(BuruAni):
    # __init__就是构造函数
    # 每次实例化的时候，第一个被调用
    # 因为主要工作是进行初始化，所以得名
    def __init__(self):
        print('I a init in dog')
 
# 实例化的时候，自动调用了Dog的构造函数
kaka = Dog()
```

    I a init in dog
    


```python
# 继承中的构造函数 - 2
# 继承中的构造函数
class Animal():
    def __init__(self):
        print('Animal')

class BuruAni(Animal):
    def __init__(self):
        print('Buru Dongwu')

class Dog(BuruAni):
    # __init__就是构造函数
    # 每次实例化的时候，第一个被调用
    # 因为主要工作是进行初始化，所以得名
    def __init__(self):
        print('I a init in dog')
 
# 实例化的时候，自动调用了Dog的构造函数
kaka = Dog()

# 猫没有写构造函数
class Cat(BuruAni):
    pass

# 此时应该自动调用构造函数，因为Cat没有构造函数，所以查找父类构造函数
# 在BuruAni中查找到了构造函数，则停止向上查找
c = Cat()
```

    I a init in dog
    Buru Dongwu
    


```python
# 继承中的构造函数 - 3
class Animal():
    def __init__(self):
        print('Animal')

class BuruAni(Animal):
    def __init__(self, name):
        print('Buru Dongwu {0}'.format(name))

class Dog(BuruAni):
    # __init__就是构造函数
    # 每次实例化的时候，第一个被调用
    # 因为主要工作是进行初始化，所以得名
    def __init__(self):
        print('I a init in dog')

# 实例化Dog时，查找到Dog的构造函数，参数匹配，不报错
d = Dog()

class Cat(BuruAni):
    pass

# 此时，由于Cat没有构造函数，则向上查找
# 因为BuruAni的构造函数需要两个参数，实例化的时候给了一个，报错
c = Cat()
```

    I a init in dog
    


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-9-aeeb27a5668f> in <module>()
         23 # 此时，由于Cat没有构造函数，则向上查找
         24 # 因为BuruAni的构造函数需要两个参数，实例化的时候给了一个，报错
    ---> 25 c = Cat()
    

    TypeError: __init__() missing 1 required positional argument: 'name'



```python
# 继承中的构造函数 - 4
class Animal():
    def __init__(self):
        print('Animal')

class BuruAni(Animal):
    pass

class Dog(BuruAni):
    pass

# 实例化Dog时，查找到Dog的构造函数，参数匹配，不报错
d = Dog()

class Cat(BuruAni):
    pass

# 此时，由于Cat没有构造函数，则向上查找
# 因为BuruAni的构造函数需要两个参数，实例化的时候给了一个，报错
c = Cat()
```

    Animal
    Animal
    


```python
print(type(super))
help(super)
```

    <class 'type'>
    Help on class super in module builtins:
    
    class super(object)
     |  super() -> same as super(__class__, <first argument>)
     |  super(type) -> unbound super object
     |  super(type, obj) -> bound super object; requires isinstance(obj, type)
     |  super(type, type2) -> bound super object; requires issubclass(type2, type)
     |  Typical use to call a cooperative superclass method:
     |  class C(B):
     |      def meth(self, arg):
     |          super().meth(arg)
     |  This works for class methods too:
     |  class C(B):
     |      @classmethod
     |      def cmeth(cls, arg):
     |          super().cmeth(arg)
     |  
     |  Methods defined here:
     |  
     |  __get__(self, instance, owner, /)
     |      Return an attribute of instance, which is of type owner.
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __init__(self, /, *args, **kwargs)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  ----------------------------------------------------------------------
     |  Static methods defined here:
     |  
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __self__
     |      the instance invoking super(); may be None
     |  
     |  __self_class__
     |      the type of the instance invoking super(); may be None
     |  
     |  __thisclass__
     |      the class invoking super()
    
    


```python

```
