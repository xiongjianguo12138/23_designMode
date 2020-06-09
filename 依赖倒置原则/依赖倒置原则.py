from abc import ABCMeta, abstractmethod


class Person:
    # 对接口的依赖
    def receive(self, IReceiver):
        print(IReceiver.getInfo())


# 定义接口
class IReceiver(object):
    __mataclss__ = ABCMeta  # 指定这是一个抽象类

    @abstractmethod  # 抽象方法
    def getInfo(self):
        pass


class Email(IReceiver):
    def getInfo(self):
        return "电子邮件:hello,world"


class WeiChar(IReceiver):
    def getInfo(self):
        return "微信:hello,world"


if __name__ == '__main__':
    # 客户端无需改变
    Person().receive(Email())
    Person().receive(WeiChar())

# 依赖关系传递:接口传递,构造方法传递,setter传递
# 底层模块经量都要有抽象类或接口,或者两者都有,程序稳定性更好
# 变量的声明类型经量是抽象类或接口,这样我们的变量引用和实际对象间,就存在了一个缓存层,利于程序扩展和优化
# 继承时遵循里氏替换原则
