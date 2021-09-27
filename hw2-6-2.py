#author : LM 09/26/2021

radius = input("What is the radius of the cylinder? ")
height = input("WHat is the height of the cyclinder? ")

area = 2 * 3.14 * int(radius) * (int(height + radius))

volume = 3.14 * (int(radius) **2) * int(height) 
print("The area of the cylinder is " + str(area) + " and the volume of the cylinder is " + str(volume) + ".")
