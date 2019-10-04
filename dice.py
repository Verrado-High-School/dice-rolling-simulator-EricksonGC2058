# Garrett Erickson
# P6
# Dice Rolling Simulator
import random

x = 1
Num1 = 0
Num2 = 0
Num3 = 0
Num4 = 0
Num5 = 0
Num6 = 0
numRolls = int(input("How many rolls?: "))
while x <= numRolls:
	randomNum = random.randint(1, 6)
	print(str(x) + ": " + str(randomNum))
	x += 1
	if randomNum == 1:
		Num1 += 1
	elif randomNum == 2:
		Num2 += 1
	elif randomNum == 3:
		Num3 += 1
	elif randomNum == 4:
		Num4 += 1
	elif randomNum == 5:
		Num5 += 1
	elif randomNum == 6:
		Num6 += 1

print("Total 1s: " + str(Num1))
print("Total 2s: " + str(Num2))
print("Total 3s: " + str(Num3))
print("Total 4s: " + str(Num4))
print("Total 5s: " + str(Num5))
print("Total 6s: " + str(Num6))
print("Percentage of 1s: " + str(Num1 / x * 100) + "%")
print("Percentage of 2s: " + str(Num2 / x * 100) + "%")
print("Percentage of 3s: " + str(Num3 / x * 100) + "%")
print("Percentage of 4s: " + str(Num4 / x * 100) + "%")
print("Percentage of 5s: " + str(Num5 / x * 100) + "%")
print("Percentage of 6s: " + str(Num6 / x * 100) + "%")
