class Animal:
    def __init__(self):
        self.eyes = 2 

    def breathe(self):
        print("Hello")

class Fish(Animal):
    def __init__(self):
        super().__init__()
    
    def breathe(self):
        super().breathe()
        print("doing this underwater")

    def swim(self):
        print("Moving in water")

cash = Fish()
cash.breathe()