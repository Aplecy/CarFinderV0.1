#ADDED ALLOWED VEHICLES
AllowedVehiclesList = [ 'Ford F-150', 'Chevrolet Silverado', 'Tesla CyberTruck', 'Toyota Tundra', 'Nissan Titan' ]

#create a option to call for the list
def Input1():
    print("hi")

#create an option to exit the menu
def Input2():
    print("Thank you for using the AutoCountry Vehicle Finder, good-bye!")

#create a defined menu for AutoCountry
def menu():
    print("********************************")
    print("AutoCountry Vehicle Finder V.01")
    print("********************************")
    print("Please Enter the following number below from the following menu:")
    print("")
    print("1. PRINT all Authorized Vehicles")
    print("2. Exit")
    option = int(input(""))
    if option == 1:
        Input1()
    elif option == 2:
        Input2()    

menu()

