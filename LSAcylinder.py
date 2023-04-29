print("""
  _       _____                   _ _           _           
 | |     / ____|  /\             | (_)         | |          
 | |    | (___   /  \   ___ _   _| |_ _ __   __| | ___ _ __ 
 | |     \___ \ / /\ \ / __| | | | | | '_ \ / _` |/ _ \ '__|
 | |____ ____) / ____ \ (__| |_| | | | | | | (_| |  __/ |   
 |______|_____/_/    \_\___|\__, |_|_|_| |_|\__,_|\___|_|   
                             __/ |                          
                            |___/                           
""")
print("      ")
print("Lateral Surface Area of cylinder")
print("AL=2πrh")
def numbercrunch(): 
    radius = input("Radius = ")
    height = input("Height = ")
    radiusflt = float(radius)
    heightflt = float(height)
    LSAcylinder = 2 * 3.141592653589793 * radiusflt * heightflt
    LSAcylinderstr = str(LSAcylinder)
    print("Lateral Surface Area is " + LSAcylinderstr)

numbercrunch()

for counter in range (100):
    solveanothercheck = input("Solve another? (Y/N) ")
    if solveanothercheck == "Y":
        numbercrunch()
    if solveanothercheck == "N":
        print("Thanks for using this software!")
        exit()