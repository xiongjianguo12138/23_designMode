class Person:
    def receive(self, Email):
        print(Email.getInfo())


class Email:
    def getInfo(self):
        return "电子邮件:hello,world"

#
if __name__ == '__main__':
    Person().receive(Email())
