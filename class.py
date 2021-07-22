class car(object):

    def __init__(self,model,color,company,speedlimit):
        self.color = color
        self.model = model
        self.company = company
        self.speedlimit = speedlimit

    def start(self):
        print("start")
    def stop(self):
        print("stop")
    def accelerate(self):
        print("accelerate")
    def changegear(self,gear_type):
        print("gearchanged")
    
bmw = car("B8","Blue","Bmw", 120)

print(bmw.start())
print(bmw.stop())
print(bmw.accelerate())
print(bmw.changegear(5))
