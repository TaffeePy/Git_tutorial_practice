from abc import ABC,abstractmethod

class phone:
    def __init__(self):
        print ('delta sms')

class samsung (phone):
    def __init__(self):
        super().__init__()
        print('Duo')
j7=samsung()


class employee(ABC):
    @abstractmethod
    def empId(self,name,age,salary):
        pass

class it(employee):
    def empId(self):
        print('>Information Technology Department<')

taffee=it()
taffee.empId()
