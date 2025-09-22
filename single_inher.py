class parent:
    def method1(self):
        print("this is parent class")

class child(parent):
    def method2(self):
        print("this is child class")


obj1=child()
obj1.method1()
obj1.method2()