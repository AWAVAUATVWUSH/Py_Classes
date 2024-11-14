from datetime import datetime

class Worker:
    def __init__(self, name:str="", yob:int=1980, pay:int=300000, pos:str=""):
        self.name = name
        self.yob = yob
        self.pay = pay
        self.pos = pos
        self.age = self.get_age()

    def get_age(self):
        self.age = (datetime.now().year)-self.yob
        return self.age
    
    def give_raise(self, amount:float = 0):
        self.pay = int(float(self.pay) + float(self.pay)*amount/100)

    def __str__(self):
        return f"Worker(name='{self.name}', yob={self.yob}, pay={self.pay}, pos='{self.pos}, age='{self.age}')"
    