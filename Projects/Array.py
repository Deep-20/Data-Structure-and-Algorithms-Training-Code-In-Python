numberOfDays = int(input("How many day's temperature? "))
temperature = []

def getTemp(n):
    for i in range(n):
        temp = float(input("Day " + str(i+1) +  "'s high temp: "))
        temperature.append(temp)

def aboveAverage(avgTemp):
    count = 0
    for i in temperature:
        if i > avgTemp:
            count += 1
    return count
getTemp(numberOfDays)

averageTemp = sum(temperature)/len(temperature)

count = aboveAverage(averageTemp)

print("\nAverage: ", averageTemp)
print(count , " day(s) above average")