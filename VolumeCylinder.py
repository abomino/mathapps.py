print(r""" 
 __      __        _ _           _           
 \ \    / /       | (_)         | |          
  \ \  / /__ _   _| |_ _ __   __| | ___ _ __ 
   \ \/ / __| | | | | | '_ \ / _` |/ _ \ '__|
    \  / (__| |_| | | | | | | (_| |  __/ |   
     \/ \___|\__, |_|_|_| |_|\__,_|\___|_|   
              __/ |                          
             |___/                           

""")
print("V=πr^2h")
print("Volume of cylinder")
print("     ")
def numbercrunch():
    radius = input("Radius = ")
    height = input("Height = ")
    radiusflt = float(radius)
    heightflt = float(height)
    VolCylinder = 3.141592653589793 * (radiusflt * radiusflt) * heightflt
    VolCylinderstr = str(VolCylinder)
    print("     ")
    print("Volume is " + VolCylinderstr)

numbercrunch()

for counter in range (100):
    solveanothercheck = input("Solve another? (Y/N) ")
    if solveanothercheck == "Y":
        numbercrunch()
    if solveanothercheck == "N":
        print("Thanks for using this software!")
        exit()