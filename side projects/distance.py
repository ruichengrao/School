import math



def distance():
    x1 = input("Insert your first x coordinate: ")
    y1 = input("Insert your first y coordinate: ")
    x2 = input("Insert your second x coordinate: ")
    y2 = input("Insert your second y coordinate: ")
    #change all the input (str) -> (float)
    fx1 = float(x1)
    fx2 = float(x2)
    fy1 = float(y1)
    fy2 = float(y2)


    exX = (fx2 - fx1)**2
    exY = (fy2 - fy1)**2
    add = float(exY) + float(exX)
    distance = math.sqrt(add)
    print(distance)

    
    
distance()