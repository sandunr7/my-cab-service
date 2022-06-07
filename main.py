import sys
from prettytable import PrettyTable

vehicleList = []

class Vehicle:
    def __init__(self, id, type, maxPassengers, acAvailable, size, maxLoad, isAvailable):
        self.id = id
        self.type = type
        self.maxPassengers = maxPassengers
        self.acAvailable = acAvailable
        self.size = size
        self.maxLoad = maxLoad
        self.isAvailable = isAvailable

def main():
    print("\n\tWelcome to the HM Cab Service!\n\t==============================")
    mainMenu()

def mainMenu():
    selectedOption = 0

    # main menu
    print("\n\t\tMain Menu")
    print("\t1. Add a new vehicle")
    print("\t2. Remove a vehicle")
    print("\t3. See available vehicles")
    print("\t4. Hire a vehicle")
    print("\t5. Release a vehicle")
    print("\t6. Quit")

    selectedOption = input("\nPlease select one of the above options (1,2,3,4,5 or 6 ) : ")

    while selectedOption < 1 or selectedOption > 6 or selectedOption.isdigit() == False:
        print("The selected option is invalid.")
        selectedOption = int(input("\nPlease select one of the above options (1,2,3,4,5 or 6 ) : "))

    if selectedOption == 1:
        addVehicle()
    elif selectedOption == 2:
        getVehiclesList()
        selectedId = int(input("\nPlease enter the vehicle Id that you need to remove : "))
        removeVehicle(selectedId)
    elif selectedOption == 3:
        getAvailableVehiclesList()
        mainMenu()
    elif selectedOption == 4:
        hireVehicle()
    elif selectedOption == 5:
        releaseVehicle()
    else:
        print("Closing program .........")
        sys.exit()


def addVehicle():
    print("\n\tAdd a new vehicle")

    # vehicle type menu
    print("\n\t\tVehicle Type ")
    print("\t1. Car")
    print("\t2. Van")
    print("\t3. Three Wheeler")
    print("\t4. Truck")
    print("\t5. Lorry")

    vehicleTypeId = int(input("\nPlease select the vehicle type that you need to add (1,2,3,4, or 5 ) : "))

    while vehicleTypeId < 1 or vehicleTypeId > 5 or vehicleTypeId.isdigit() == False:
        print("The selected option is invalid.")
        vehicleTypeId = int(input("\nPlease select the vehicle type that you need to add (1,2,3,4, or 5 ) : "))

    vehicleType = getVehicleTypeById(vehicleTypeId)

    maxPassengers = int(input("\nPlease enter the maximum number of passengers allowed : "))
    acAvailable = int(input("\nAC available ? (0 - NO \t1 - YES) : "))

    if acAvailable == 1:
        acAvailable = "YES"
    else:
        acAvailable = "NO"

    size = int(input("\nPlease enter the size of the vehicle (in feet) : "))
    maxLoad = int(input("\nPlease enter the maximum load allowed (in KG) : "))

    vehicleCount: int = len(vehicleList)
    vehicleCount += 1
    vehicleList.append(Vehicle(vehicleCount, vehicleType, maxPassengers, acAvailable, size, maxLoad, True))
    print("\nVehicle added successfully.")

    getVehiclesList()
    mainMenu()


def removeVehicle(selectedId):
    while selectedId > len(vehicleList):
        print("\nThe selected id is not available.")
        selectedId = int(input("\nPlease enter the vehicle Id that you need to remove : "))

    vehicleList.pop(selectedId - 1)
    print("\nVehicle removed successfully.")

    getVehiclesList()
    mainMenu()


def getAvailableVehiclesList():
    t = PrettyTable(['ID', 'Vehicle Type', 'Maximum passengers allowed', 'AC available', 'Size (In Ft)',
                     'Max load allowed (In KG)'])
    for v in vehicleList:
        if not v.isAvailable:
            continue
        t.add_row([v.id, v.type, v.maxPassengers, v.acAvailable, v.size, v.maxLoad])

    print("\nAvailable Vehicles List")
    print(t)


def hireVehicle():
    print("\n\tHire a vehicle")

    # vehicle type menu
    print("\n\t\tVehicle Type ")
    print("\t1. Car")
    print("\t2. Van")
    print("\t3. Three Wheeler")
    print("\t4. Truck")
    print("\t5. Lorry")

    vehicleTypeId = int(input("\n\tSelect the vehicle type that you need to hire (1,2,3,4, or 5 ) : "))

    while vehicleTypeId < 1 or vehicleTypeId > 5:
        print("The selected type is invalid.")
        vehicleTypeId = int(input("\n\tPlease select the vehicle type that you need to add (1,2,3,4, or 5 ) : "))

    vehicleType = getVehicleTypeById(vehicleTypeId)
    getAvailableVehiclesListByCategory(vehicleType)


def releaseVehicle():
    print("\n\tRelease a vehicle")
    getHiredVehiclesList()

    selectedId = int(input("\nPlease enter the vehicle Id that you need to complete hire : "))

    while selectedId > len(vehicleList):
        print("\nThe selected id is not available.")
        selectedId = int(input("\nPlease enter the vehicle Id that you need to complete hire : "))

    for v in vehicleList:
        if v.id == selectedId:
            v.isAvailable = True
            print("\nSelected vehicle is released successfully !.")

    getVehiclesList()
    mainMenu()


def getVehiclesList():
    t = PrettyTable(['ID', 'Vehicle Type', 'Maximum passengers allowed', 'AC available', 'Size (In Ft)',
                     'Max load allowed (In KG)', 'IsAvailableToHire'])
    for v in vehicleList:
        t.add_row([v.id, v.type, v.maxPassengers, v.acAvailable, v.size, v.maxLoad, v.isAvailable])

    print("\nVehicles List")
    print(t)


def getHiredVehiclesList():
    t = PrettyTable(['ID', 'Vehicle Type', 'Maximum passengers allowed', 'AC available', 'Size (In Ft)',
                     'Max load allowed (In KG)'])
    for v in vehicleList:
        if v.isAvailable:
            continue
        t.add_row([v.id, v.type, v.maxPassengers, v.acAvailable, v.size, v.maxLoad])

    print("\nAlready hired Vehicles List")
    print(t)


def getAvailableVehiclesListByCategory(category):
    filteredList = []
    t = PrettyTable(['ID', 'Maximum passengers allowed', 'AC available', 'Size (In Ft)',
                     'Max load allowed (In KG)'])
    for v in vehicleList:
        if v.type == category and v.isAvailable:
            filteredList.append(v)
            t.add_row([v.id, v.maxPassengers, v.acAvailable, v.size, v.maxLoad])

    print("\nAvailable " + category + " List")
    print(t)

    selectedId = int(input("\nPlease enter the vehicle Id that you need to hire : "))

    while selectedId > len(vehicleList):
        print("\nThe selected id is not available.")
        selectedId = int(input("\nPlease enter the vehicle Id that you need to hire : "))

    for f in filteredList:
        if f.id == selectedId:
            f.isAvailable = False
            print("\nSelected vehicle hired successfully !.")

    getVehiclesList()
    mainMenu()


def getVehicleTypeById(id):
    switcher = {
        1: "Car",
        2: "Van",
        3: "Three Wheeler",
        4: "Truck",
        5: "Lorry",
    }
    return switcher.get(id, "nothing")


def check_is_digit(input):
    return input.strip().isdigit()


main()
