class parent:
    def method1(self):
        print('parent method1')

class child1(parent):
    def method2(self):
        print('child method1')
class child2(parent):
    def method3(self):
        print('child method2')
obj = child2()
obj.method3()
obj.method1()
