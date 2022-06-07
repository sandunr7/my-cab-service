from prettytable import PrettyTable

vehicleDetails = []
hireDetails=[]
print("CAB SERVICE")

class Hired:
    def _init_(self, id, type, person, status):

        self.id = id
        self.carType = type
        self.hiredPerson = person
        self.status = status

class Vehicle:
    def _init_(self,id, type, passengers, acType, size, load, hiredStatus):
        self.id = id
        self.type = type
        self.passengers = passengers
        self.acType = acType
        self.size = size
        self.load = load
        self.hiredStatus = hiredStatus


def addVehicle( ):
    type=input("enter Vehicle Type : ")
    passengers=input("enter passenger  : ")
    acType=input("Ac or Non Ac : ")
    size=input("enter size : ")
    load=input("enter load : ")


    vehicleCount=len(vehicleDetails)
    vehicleCount+=1
    vehicleDetails.append(Vehicle(vehicleCount, type, passengers, acType, size, load, True))

    t = PrettyTable(['ID', 'Car Type', 'Passengers','AC or Non AC','size','Load'])
    for v in vehicleDetails:
        if(v.hiredStatus == False):
            continue
        t.add_row([v.id, v.type, v.passengers,v.acType,v.size,v.load])
    print(t)
    menu()


def addHire():
    # first show available vehicle list
    t = PrettyTable(['ID', 'Car Type', 'Passengers'])
    for v in vehicleDetails:
        t.add_row([v.id, v.type, v.passengers])
    print(t)

    # second get inputs from terminal for Hired Object
    vahicleid = input("Enter Vehicle id")
    carType = input("Enter Vehicle type")
    passenger = input("Enter hired person name")

    # append input data to Hired object
    hireDetails.append(Hired(vahicleid, carType,passenger,True))

    for hired in hireDetails:
        print(hired.carType + hired.hiredPerson)
    menu()

def removeHiredDetails():
    # get inputs remove hired detail

    inputHiedId = input("Enter Hired Vehicle Id")

    for hired in hireDetails:
        if(inputHiedId == hired.id):
            hireDetails.remove(hired)
            for vehical in vehicleDetails:
                if(inputHiedId == vehical.id):
                    vehical
        else:
            continue

    print("Hired Removed Successfully")

    t = PrettyTable(['ID', 'Car Type', 'Person'])
    for h in hireDetails:
        t.add_row([h.id, h.carType, h.hiredPerson])
    print(t)
    menu()

def searchVehicle(): # car
    countCar = 0
    countVan = 0
    count3Wheel = 0
    countTruck=0
    countLorry=0

    for v in vehicleDetails:
        if("car"==v.type):
            countCar+=1
        elif("van"==v.type):
            countVan+=1
        elif("3 wheels"==v.type):
            count3Wheel+=1
        elif ("truck" == v.type):
            countTruck += 1
        elif ("lorry" == v.type):
            countLorry += 1
        else :
            continue


    print("Cars : "+str(countCar))
    print("Vans : " + str(countVan))
    print("3 Wheels : " + str(count3Wheel))
    print("Truck : " + str(countTruck))
    print("Lorry : " + str(countLorry))
    menu()

def menu():
    print("1: Add A Vehicle")
    print("2: Remove A Vehicle")
    print("3: Assign A job")
    print("4: Available Vehicle List")


    add=input("Choose one : ")
    if(add=="1"):
        addVehicle()
    elif(add=="2"):
        removeHiredDetails()
    elif(add=="3"):
        addHire()
    elif(add=="4"):
        searchVehicle()
    else:print("not valid code")

menu()
# addVehicle()
#
# searchVehicle()
#
# addHire()
#
# removeHiredDetails()
#
# addVehicle("ddsd","4","djfs","6987kg","hbbjdf")







