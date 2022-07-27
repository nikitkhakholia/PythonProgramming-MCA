## Question
# Design and develop a python program to implement the concept of inheritance.

## Answer
# This is Python 3 code snippet
# Developed by Nikit Khakholia
# On 28 September 2021

'''A script that implements the concept of inheritance. 
Here the classes Gear, Wheel, Engine, Seat, FUelTank 
are being inherited by the class Vehicle'''
class Gear:
    def __init__(self, maxGears) -> None:
        self.maxGears = maxGears
        self.currentGear=0
    def shiftUp(self)->int:
        if(self.currentGear==self.maxGears):
            print("Already on top gear.")
        else:
            self.currentGear=self.currentGear+1
            print("Gear shifted to "+str(self.currentGear))
        return self.currentGear
    def shiftDown(self)->int:
        if(self.currentGear==0):
            print("Already Neutral.")
        else:
            self.currentGear=self.currentGear-1
            print("Gear shifted to "+str(self.currentGear))
        return self.currentGear

class Wheel:
    def __init__(self,radius,spokes,alloy,typePressure) -> None:
        self.radius=radius
        self.spokes=spokes
        self.alloy=alloy
        self.typePressure=typePressure

class Engine:
    def __init__(self,rpm, valves) -> None:
        self.rpm=rpm
        self.valves=valves
        self.running= False
    def start(self):
        self.running=True
        print("Engine Started")
    def stop(self):
        self.running=False
        print("Engine Stopped")

class Seat:
    def __init__(self, capacity, fabric) -> None:
        self.capacity=capacity
        self.fabric=fabric
class FuelTank:
    def __init__(self, capacity, level) -> None:
        self.capacity=capacity
        self.level=level
    def addFuel(self,amount):
        self.level+=(amount/self.capacity*100)
        if(self.level>=100):
            print("Fuel Tank Full")
            self.level=100
        print("New Fuel Level "+str(self.level))
    def comsumeFuel(self,consumption):
        self.level-=consumption
        if(self.level<=10):
            print("Fuel Level less then 10%")
        elif(self.level==0):
            print("Fuel Empty")
        else:
            pass
        print("New Fuel Level "+str(self.level))

# multiple classes inherited in class vehicle and initialised them
class Vehicle(Gear,Wheel,Engine,Seat,FuelTank):
    def __init__(self, maxGears,radius,spokes,alloy,tyrePressure,rpm,valves, seatCapacity,fabric, fuelCapacity,level) -> None:
        Gear.__init__(self,maxGears)
        Wheel.__init__(self,radius,spokes,alloy,tyrePressure)
        Engine.__init__(self,rpm,valves)
        Seat.__init__(self,seatCapacity,fabric)
        FuelTank.__init__(self,fuelCapacity,level)

# creating object of class vehicle
v1 = Vehicle(
    int(input("Enter no of gears for the vehicle: ")),
    int(input("Enter radius of wheel: ")),
    int(input("Enter no of spokes in wheel: ")),
    bool(input("Is alloy wheel: ")),
    int(input("Enter tyre pressure: ")),
    int(input("Enter rpm of engine: ")),
    int(input("Enter valves in engine: ")),
    int(input("Enter seat capacity: ")),
    input("Enter seat fabric: "),
    int(input("Enter fuel capacity: ")),
    int(input("Enter fuel level: ")),
)

# accessing inherited functions of class vehicle
v1.start()
v1.shiftUp()
v1.shiftUp()
v1.shiftDown()
v1.addFuel(int(input("Refill fuel: ")))
v1.comsumeFuel(int(input("Consume fuel level: ")))
v1.stop()
