print(r"""
   _____         _____      _ _           _           
  / ____|  /\   / ____|    | (_)         | |          
 | (___   /  \ | |    _   _| |_ _ __   __| | ___ _ __ 
  \___ \ / /\ \| |   | | | | | | '_ \ / _` |/ _ \ '__|
  ____) / ____ \ |___| |_| | | | | | | (_| |  __/ |   
 |_____/_/    \_\_____\__, |_|_|_| |_|\__,_|\___|_|   
                       __/ |                          
                      |___/                           
""")
print("A=2πrh+2πr^2")
print("     ")
print("Surface Area of cylinder")
def numbercrunch():
    radius = input("Radius = ")
    height = input("Height = ")
    radiusflt = float(radius)
    heightflt = float(height)
    SAcylinder = 2 * 3.141592653589793 * radiusflt * heightflt + 2 * 3.141592653589793 * radiusflt * radiusflt
    SAcylinderstr = str(SAcylinder)
    print("Surface Area is " + SAcylinderstr)

numbercrunch()

for counter in range (100):
    solveanothercheck = input("Solve another? (Y/N) ")
    if solveanothercheck == "Y":
        numbercrunch()
    if solveanothercheck == "N":
        print("Thanks for using this software!")
        exit()