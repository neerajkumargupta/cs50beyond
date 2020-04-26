class Point:

    def __init__(self, x, y):
        super().__init__()
        print("Using parameterized const.....")
        self.x = x
        self.y = y
   
        

p=Point(10,20)

print(p.x)
print(p.y)
