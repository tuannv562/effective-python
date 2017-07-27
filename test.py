class Person(object):
    def __init__(self, name):
        self.name = name

    def talk(self, message):
        raise NotImplementedError


class Student(Person):
    def __init__(self, name):
        super().__init__(name)

    def talk(self, message):
        print('{} talk {}'.format(self.name, message))


class Worker(Person):
    def __init__(self, name):
        super().__init__(name)


s = Student('Tuan')
s.talk('abc')
w = Worker('Minh')
w.talk('def')
