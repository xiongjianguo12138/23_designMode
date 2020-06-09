from abc import ABCMeta, abstractmethod
from zope.interface import Interface
from zope.interface.declarations import implementer


class interface1(object):
    __mataclss__ = ABCMeta  # 指定这是一个抽象类

    @abstractmethod  # 抽象方法
    def operation1(self):
        pass


class interface2(object):
    __mataclss__ = ABCMeta  # 指定这是一个抽象类

    @abstractmethod  # 抽象方法
    def operation2(self):
        pass

    @abstractmethod  # 抽象方法
    def operation3(self):
        pass


class interface3(object):
    __mataclss__ = ABCMeta  # 指定这是一个抽象类

    @abstractmethod  # 抽象方法
    def operation4(self):
        pass

    @abstractmethod  # 抽象方法
    def operation5(self):
        pass


# @implementer(interface1, interface2)
class B(interface1, interface2):
    def __init__(self):
        pass

    def operation1(self):
        print("B 中实现了operation1")

    def operation2(self):
        print("B 中实现了operation2")

    def operation3(self):
        print("B 中实现了operation3")


# @implementer(interface1, interface3)
class D(interface1, interface3):
    def __init__(self):
        pass

    def operation1(self):
        print("D 中实现了operation1")

    def operation4(self):
        print("D 中实现了operation4")

    def operation5(self):
        print("D 中实现了operation5")


class A:  # A 类通过接口Interface11 ,Interface12 依赖B类,但只会使用到1,2,3方法
    def depend1(self, interface):
        interface.operation1()

    def depend2(self, interface):
        interface.operation2()

    def depend3(self, interface):
        interface.operation3()


class C:  # C 类通过接口Interface1,Interface13 依赖D类,但只会使用到1,4,5方法

    def depend1(self, interface):
        interface.operation1()

    def depend4(self, interface):
        interface.operation4()

    def depend5(self, interface):
        interface.operation5()


if __name__ == '__main__':
    A().depend1(B())  # A类通过接口去依赖B类
    A().depend2(B())
    A().depend3(B())

    C().depend1(D())
    C().depend4(D())
    C().depend5(D())
# 客户端不应该依赖它不需要的接口,即一个类对另一个类的依赖应该建立在最小接口上
