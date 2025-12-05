def find_distance():
    speed = float(input("Enter the speed of the vehicle (km/h): "))
    hours = float(input("Enter hours: "))
    minutes = int(input("Enter minutes: "))

    time = hours + (minutes / 60)   # Converts into hours
    distance = speed * time   

    return distance

result = find_distance()
print(f"Distance is: {result} km")
