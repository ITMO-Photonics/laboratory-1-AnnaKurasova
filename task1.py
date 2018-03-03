import math
pi = 3.14
def calculate(R, L):
	volume = pi * R * R * L

	return ('Volume: ' + str(volume))

R = int(input('please Enter the radius of a Cylinder: '))
L = int(input('please Enter the length of a Cylinder: '))

print(calculate(R,L))
