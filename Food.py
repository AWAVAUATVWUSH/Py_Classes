class Food:
    def __init__(self, name:str="", cost:int=1000, timeToMake:float=1.1):     # <-- this is a constructor
        self.name = name
        self.cost = cost
        self.timeToMake = timeToMake
        self.state="készül"
    def makefood(self):
        self.state="kész"
    def __str__(self):
        return f"Food(name='{self.name}', cost={self.cost}, timeToMake={self.timeToMake}, state='{self.state}')"