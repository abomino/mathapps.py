print("""
  ____          _____      _ _           _           
 |  _ \   /\   / ____|    | (_)         | |          
 | |_) | /  \ | |    _   _| |_ _ __   __| | ___ _ __ 
 |  _ < / /\ \| |   | | | | | | '_ \ / _` |/ _ \ '__|
 | |_) / ____ \ |___| |_| | | | | | | (_| |  __/ |   
 |____/_/    \_\_____\__, |_|_|_| |_|\__,_|\___|_|   
                      __/ |                          
                     |___/                           

""")
print("     ")
print("Base Area of cylinder")
print("AB=πr^2")

def numbercrunch():
    radius = input("Radius = ")
    radiusflt = float(radius)
    BAcylinder = 3.141592653589793 * radiusflt * radiusflt
    BAcylinderstr = str(BAcylinder)
    print("Base Area is " + BAcylinderstr)

numbercrunch()

for counter in range (100):
    solveanothercheck = input("Solve another? (Y/N) ")
    if solveanothercheck == "Y":
        numbercrunch()
    if solveanothercheck == "N":
        print("Thanks for using this software!")
        exit()