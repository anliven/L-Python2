# Questions_Confusing_Code



## Code

### 01
以下代码的执行结果是什么？
```python
testList = ['a', 'b', 'c']
print(testList[5:])
```


### 02
以下代码的执行结果是什么？
```python
a = [123, "xxx", "yyy"]
b = a
c = a[:]

print(a is b, a is c, b is c)
print(a == b, a == c, b == c)
```


### 03
以下代码的执行结果是什么？
```python
tl = [[]] * 3
print(tl)
tl[0].append("aaa")
tl[1].append(111)
tl.append("AAA")
print(tl)
```


### 04
以下代码的执行结果是什么？
```python
list_1 = [111, 333, 555, "aaa", "ccc"]
list_2 = [111, 222, 333, "ccc"]
print(list_1 + list_2)
print([x for x in list_1 if x in list_2])
print([i for i in list_1 if i not in list_2])
print([i for i in list_2 if i not in list_1])
```

### 05
在Python3和Python2中分别执行如下代码，结果分别是什么？
```python
print(5/2, 5./2)
print(10//3, (-10)//3)
print(10//5, (-10)//5)
```


### 06
以下代码的执行结果是什么？
```python
class Parent():
    x = 1


class Child1(Parent):
    pass


class Child2(Parent):
    pass


print(Parent.x, Child1.x, Child2.x)
Child1.x = 2
print(Parent.x, Child1.x, Child2.x)
Parent.x = 3
print(Parent.x, Child1.x, Child2.x)
```


### 07
以下代码的执行结果是什么？
```python
def multipliers(x):
    return (x * i for i in range(5))


def test1():
    return [lambda x: x * i for i in range(5)]


def test2():
    for i in range(5):
        yield lambda x: i * x


def test3():
    return [lambda x, i=i: i * x for i in range(5)]


print(list(multipliers(2)))
print([m(2) for m in test1()])
print([m(2) for m in test2()])
print([m(2) for m in test3()])
```


### 08
以下代码的执行结果是什么？
```python
a = "abc"
b = ['c', 'b', 'a']
print(a.replace("a", "A"))
print(a)
b.sort()
print(b)
```


### 09
以下代码的执行结果是什么？
```python
a = 111
b = []


def fun(x):
    x = 222
    print(x)


def fun2(x):
    x.append("AAA")
    print(x)


fun(a)
fun2(b)
print(a, b)
```

### 10
以下代码的执行结果是什么？
```python
def extendList(val, tl=[]):
    tl.append(val)
    return tl


def extendList2(val, tl=None):
    if tl is None:
        tl = []
    tl.append(val)
    return tl


list1 = extendList(123)
list2 = extendList(789, [])
list3 = extendList('abc')
list4 = extendList2(111)
list5 = extendList2(999, [])
list6 = extendList2('ABC')

print("list1= %s, list2= %s, list3= %s" % (list1, list2, list3))
print("list4= %s, list5= %s, list6= %s" % (list4, list5, list6))
```


### 11
以下代码的执行结果是什么？
```python
class Person:
    name = "test"
    money = []


AAA = Person()
AAA.name = "winner"
AAA.money.append(100000000)
BBB = Person()

print(AAA.name, AAA.money, BBB.name, BBB.money, Person.name, Person.money)
```


### 12
以下代码的执行结果是什么？
```python
import copy

a = [1, 2, 3, ['a', 'b']]
b = a
cc = copy.copy(a)
cd = copy.deepcopy(a)

a.append(4)
a[3].append('c')
print("a= ", a, "\nb= ", b, "\ncc= ", cc, "\ncd= ", cd)
```


### 13
以下代码的执行结果是什么？
```python
test = dict(zip(('a', 'b', 'c', 'd', 'e'), (1, 2, 3, 4, 5)))
test1 = [test[x] for x in test]
test2 = {i: i * i for i in range(5)}
test3 = [[i, i * i] for i in range(10) if i % 2 == 0]

print("\n", test1, "\n", test2, "\n", test3)
```


### 14
以下代码的执行结果是什么？
```python
def f(x, li=[]):
    for i in range(x):
        li.append(i * i)
    print(li)


f(2)
f(3, [3, 2, 1])
f(3)
```


### 15
以下代码的执行结果是什么？
```python
class A(object):
    def go(self):
        print("class A go!")

    def stop(self):
        print("class A stop!")


class B(A):
    def go(self):
        super(B, self).go()
        print("class B go!")


class C(A):
    def go(self):
        super(C, self).go()
        print("class C go!")

    def stop(self):
        super(C, self).stop()
        print("class C stop!")


class D(B, C):
    def go(self):
        super(D, self).go()
        print("class D go!")

    def stop(self):
        super(D, self).stop()
        print("class D stop!")


class E(B, C):
    pass


a = A()
b = B()
c = C()
d = D()
e = E()

print("a.go", "#" * 20), a.go()
print("b.go", "#" * 20), b.go()
print("c.go", "#" * 20), c.go()
print("d.go", "#" * 20), d.go()
print("e.go", "#" * 20), e.go()

print("a.stop", "&" * 20), a.stop()
print("b.stop", "&" * 20), b.stop()
print("c.stop", "&" * 20), c.stop()
print("d.stop", "&" * 20), d.stop()
print("e.stop", "&" * 20), e.stop()
```



## Tips:

### 01
```
试图访问一个超过列表索引值的成员将导致“IndexError”。
访问一个起始索引超出列表成员数的列表切片将仅仅返回一个空列表。
```
### 02
```
列表的切片操作重新分配了对象。
“is”对比内存地址：是否完全相同，是否同一个对象；“==”对比值：内容是否相等（内存地址可以不同）。
```
### 03
```
区分：是对同一个列表的多次引用，还是独立的多个列表。
```
### 04
```
列表的交集与差集。
```
### 05
```
在Python3中“/ ”操作符是做浮点除法，而在Python2中则是整除。
“//”操作符总是做整除，但Python的整除运算会向0的方向取值。
```


### 06
```
在Python中，类变量在内部是作为字典处理的，如果一个变量名没有在当前类的字典中发现，将搜索祖先类直到被引用的变量名被找到。
如果这个被引用的变量名没找到，将会引发“AttributeError”异常。
在父类中设置一个类变量的值，那么其任何子类中均默认继承此变量的值。
如果子类重写了此变量值，那么该值仅仅在子类中被改变。
如果此变量值在父类中被改变，这个改变只会影响到任何未重写该变量值的子类。
```
### 07
```
lambda函数是一种快速定义单行的最小函数。
Python闭包的延迟绑定（late binding）：内部函数被调用时，参数的值在闭包内进行查找。
避免此问题的方法：使用Python生成器和yield关键字；或者在闭包中，使用默认参数立即绑定它的参数。
```
### 08
```
对象分为“不可更改”（immutable）和“可更改”（mutable）对象。
不可变对象调用对象自身的方法，不会改变该对象自身的内容，而是创建新的对象并返回，这样就保证了不可变对象本身永远不可变。
可变对象调用对象自身的方法，会改变该对象自身的内容。
```
### 09
```
类型是属于对象的，而不是变量。
在python中，strings、tuples,和numbers是不可更改的对象，而list、dict等则是可更改的对象。
```
### 10
```
带有默认参数的表达式在函数被定义的时候被计算，不是在调用的时候被计算。
```


### 11
```
类变量(供类使用的变量)与实例变量（供实例使用的变量）的关系。
```
### 12
```
引用的含义。
copy仅拷贝对象本身，而不拷贝对象中引用的其它对象。
deepcopy除拷贝对象本身，而且拷贝对象中引用的其它对象。
```
### 13
```
zip函数和列表解析（List Comprehension）的使用方法。
```
### 14
```
带有默认参数的表达式在函数被定义的时候被计算，不是在调用的时候被计算。
```
### 15
```
继承的定义和super函数的用法。
```