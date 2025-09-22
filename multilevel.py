class parent:
    def method1(self):
        print('parent method1')

class child(parent):
    def method2(self):
        print('child method2')

class child2(child):
    def method3(self):
        print('child method3')
obj = child2()
obj.method3()
obj.method1()
obj.method2()