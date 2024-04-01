earth_weight = float(input("What is your earth weight: "))
planet = int(input("The planet number as an integer: "))

if planet == 1:
    destination_weight = earth_weight * 0.38
elif planet == 2:
    destination_weight = earth_weight * 0.91
elif planet == 3:
    destination_weight = earth_weight * 0.38
elif planet == 4:
    destination_weight = earth_weight * 2.53
elif planet == 5:
    destination_weight = earth_weight * 1.07
elif planet == 6:
    destination_weight = earth_weight * 0.89
elif planet == 7:
    destination_weight = earth_weight * 1.14
else:
    print('Invalid planet number')