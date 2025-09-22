class parent:
    def method1(self):
        print("Parent method1")

class child(parent):
    def method1(self):
        print("Child method2")

obj = child()
obj.method1()
