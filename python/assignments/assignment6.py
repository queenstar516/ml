hours = int(input("Input number of hours: "))

def calculateParkingFee(hours):
    fee = 0
    if hours <= 5:
        fee = hours * 1
    elif hours > 5 and hours < 24:
        fee = 5 + ((hours - 5) * 0.5)
    elif hours == 24:
        fee = 15
    elif hours % 24 == 0:
        fee = 15 * (hours / 24)
    elif hours > 24:
        fee = 15 + ((hours - 24) * 0.5)
    return f"Your fee is ${fee}"

print(calculateParkingFee(hours))
