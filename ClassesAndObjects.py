## Question
''' You are crazy about various automobiles. Today is The Day you can write python program on automobiles!!!
    Create a class called “Vehicle” which has attributes brand, model, type, fuel_tank_ size, fuel _level. 
    Initialize the variables in the “__init__” method and write the following methods
      · Fulltank()- which fills the entire tank and prints “Tank is Full”
      · Update_fuel_tank()- which updates the amount of fuel which is in the tank.You can pass a variable 
      called “new_level” and assign that to fuel_level. Print a warning if the fuel_level is <=3liters.
      · Get_fuel() – which takes in a variable “amount” and add it to fuel_level.Print warning if the 
      fuel_level is exceeding the capacity of the tank.
      · Drive() – which prints a message saying “WOW! I am Driving {model}”. The model is the vehicle 
      should be inserted instead of “{model}” 
    Create two objects of vehicles and call the functions.'''

## Answer
# This is Python 3 code snippet
# Developed by Nikit Khakholia
# On 21 September 2021

'''A python script that demonstrates classes and objects.'''

# creating a class
class Vehiche:

    # defining attributes
    brand=""
    model=""
    type=""
    fuelTankSize=0
    fuelLevel=0

    # defining default constructor
    def __init__(self, brand, model, type,fuelTankSize,fuelLevel):
        self.brand=brand
        self.model=model
        self.type=type
        self.fuelTankSize=fuelTankSize
        self.fuelLevel=fuelLevel

    # defining function to get fuel in liters
    def getFuelInLiters(self):
        return self.fuelLevel*self.fuelTankSize/100

    # defining function to full fuel tank
    def fullTank(self):
        self.fuelLevel=100
        print('Tank is Full')
        print("Fuel Level - "+str(self.fuelLevel))
    
    # defining function to update fuel tank level
    def updateFuelTank(self, fuelLevel):
        print("Update fuel level to "+str(fuelLevel))
        self.fuelLevel=fuelLevel
        if(self.getFuelInLiters()<=3):
            print("Warning!! LOW FUEL")
        print("Fuel Level - "+str(self.fuelLevel))

    # defining function to fill fuel in liters
    def getFuel(self, amount):
        print("Adding "+str(amount)+" liters of fuel.")
        self.fuelLevel+= amount/self.fuelTankSize*100
        if(self.fuelLevel>100):
            self.fuelLevel=100
            print("Warning!! FUEL OVERFLOW")
        print("Fuel Level - "+str(self.fuelLevel))
    
    # defining function to drive vehicle
    def drive(self):
        print('WOW! I am Driving '+ self.model)

    #defining a function to print object data
    def print(self):
        print("Brand: "+self.brand+"\nModel: "+self.model+"\nType: "+self.type+"\nTank Capacity: "+str(self.fuelTankSize)+"\nTank Level: "+str(self.fuelLevel)+"\n")
    


# creating objects on class defined above
v1 = Vehiche('Maruti Suzuki','Breeza','Zeta+',40,50)
v2 = Vehiche('KIA','Seltos','GTX+',45,40)

# printing created object
v1.print()
# calling functions from objects above and executing required tasks.
v1.fullTank()
v1.updateFuelTank(50)
v1.updateFuelTank(1)
v1.getFuel(20)
v1.getFuel(30)
v1.drive()
print("\n\n\n\n")

# printing created object
v2.print()
v2.fullTank()
v2.updateFuelTank(70)
v2.updateFuelTank(2)
v2.getFuel(10)
v2.getFuel(50)
v2.drive()
