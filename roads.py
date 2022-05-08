import random

def road1():
    road = []
    road.append(["3","3", "3", "3", "3", "1","3"])
    road.append(["3","0", "0", "0", "3", "0","3"])
    road.append(["3","0", "3", "0", "3", "0","3"])
    road.append(["3","0", "3", "0", "0", "0","3"])
    road.append(["3","0", "3", "3", "3", "0","3"])
    road.append(["3","0", "0", "0", "3", "0","3"])
    road.append(["3","3", "3", "3", "3", "2","3"])
    return road

def road2():
    road = []
    road.append(["3","3", "3", "3", "3", "1", "3", "3", "3"])
    road.append(["3","0", "0", "0", "0", "0", "0", "0", "3"])
    road.append(["3","0", "3", "3", "0", "3", "3", "0", "3"])
    road.append(["3","0", "3", "0", "0", "0", "3", "0", "3"])
    road.append(["3","0", "3", "0", "3", "0", "3", "0", "3"])
    road.append(["3","0", "3", "0", "3", "0", "3", "0", "3"])
    road.append(["3","0", "3", "0", "3", "0", "3", "3", "3"])
    road.append(["3","0", "0", "0", "0", "0", "0", "0", "3"])
    road.append(["3","3", "3", "3", "3", "3", "3", "2", "3"])
    return road

def road3():
    road = []
    road.append(["3","3", "3", "3", "3", "1", "3"])
    road.append(["3","0", "0", "0", "0", "0", "3"])
    road.append(["3","0", "3", "3", "3", "0", "3"])
    road.append(["3","0", "0", "3", "0", "0", "3"])
    road.append(["3","3", "0", "0", "0", "3", "3"])
    road.append(["3","0", "0", "3", "3", "3", "3"])
    road.append(["3","2", "3", "3", "3", "3", "3"])
    return road

def road3():
    road = []
    road.append(["3","3", "3", "3", "3", "3", "3", "3", "3", "3", "3", "3", "3", "3", "3", "3", "3", "3", "3", "3", "3", "3", "3", "3", "3", "3", "3", "3", "3", "3", "3", "3", "3", "3", "3", "3"])
    road.append(["3","0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "2", "3"])
    road.append(["3","0", "3", "3", "3", "3", "3", "3", "3", "3", "3", "3", "3", "3", "3", "3", "3", "3", "3", "3", "3", "3", "3", "3", "3", "0", "3", "3", "3", "3", "3", "3", "3", "3", "0", "3"])
    road.append(["3","0", "3", "3", "0", "0", "0", "3", "0", "0", "0", "3", "0", "0", "0", "0", "0", "0", "3", "3", "3", "3", "3", "3", "3", "0", "0", "0", "3", "3", "0", "0", "0", "0", "0", "3"])
    road.append(["3","0", "3", "3", "0", "3", "0", "3", "0", "3", "0", "3", "0", "3", "3", "3", "3", "0", "3", "3", "3", "3", "3", "3", "3", "3", "3", "0", "3", "3", "0", "3", "3", "3", "3", "3"])
    road.append(["3","0", "3", "3", "0", "3", "0", "3", "0", "3", "0", "3", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "3", "3", "0", "3", "3", "0", "0", "0", "0", "0", "3"])
    road.append(["3","0", "3", "3", "0", "3", "0", "3", "0", "3", "0", "3", "0", "3", "0", "3", "3", "3", "3", "0", "0", "3", "3", "3", "0", "0", "0", "0", "3", "3", "3", "3", "3", "3", "0", "3"])
    road.append(["3","0", "3", "0", "0", "3", "0", "3", "0", "3", "0", "0", "0", "3", "0", "0", "0", "0", "3", "3", "0", "3", "3", "3", "3", "3", "3", "3", "3", "0", "0", "0", "0", "0", "0", "3"])
    road.append(["3","0", "3", "3", "0", "3", "0", "3", "0", "3", "3", "3", "3", "3", "3", "3", "3", "0", "3", "3", "0", "0", "0", "0", "0", "0", "0", "0", "3", "3", "0", "3", "3", "3", "3", "3"])
    road.append(["3","0", "3", "3", "0", "3", "0", "0", "0", "3", "3", "0", "0", "0", "0", "0", "0", "0", "3", "3", "3", "3", "3", "3", "3", "3", "3", "0", "3", "3", "0", "0", "0", "0", "0", "3"])
    road.append(["3","0", "0", "0", "0", "3", "3", "3", "3", "3", "3", "0", "3", "3", "3", "3", "3", "3", "3", "0", "0", "0", "0", "0", "0", "3", "3", "0", "3", "3", "3", "3", "3", "3", "0", "3"])
    road.append(["3","3", "3", "3", "3", "3", "0", "0", "0", "0", "0", "0", "3", "0", "0", "0", "0", "0", "0", "0", "3", "3", "3", "3", "0", "3", "3", "0", "3", "0", "0", "0", "0", "0", "0", "3"])
    road.append(["3","0", "0", "0", "0", "0", "0", "3", "3", "3", "3", "3", "3", "0", "3", "3", "3", "3", "3", "0", "3", "0", "0", "0", "0", "3", "3", "0", "3", "3", "0", "3", "3", "3", "3", "3"])
    road.append(["3","0", "3", "3", "3", "3", "3", "3", "0", "0", "0", "0", "0", "0", "3", "0", "0", "0", "0", "0", "0", "0", "3", "3", "3", "3", "3", "0", "3", "3", "0", "0", "0", "0", "0", "3"])
    road.append(["3","0", "0", "0", "0", "0", "0", "0", "0", "3", "3", "3", "3", "3", "3", "0", "3", "3", "3", "3", "3", "3", "3", "3", "3", "3", "3", "0", "3", "3", "0", "0", "3", "3", "0", "3"])
    road.append(["3","3", "3", "3", "3", "3", "3", "3", "3", "3", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "3", "3", "3", "3", "3", "3", "0", "3"])
    road.append(["3","1", "0", "0", "0", "0", "0", "0", "0", "0", "0", "3", "3", "3", "3", "3", "3", "3", "3", "3", "3", "3", "3", "3", "3", "3", "3", "0", "0", "0", "0", "0", "0", "0", "0", "3"])
    road.append(["3","3", "3", "3", "3", "3", "3", "3", "3", "3", "3", "3", "3", "3", "3", "3", "3", "3", "3", "3", "3", "3", "3", "3", "3", "3", "3", "3", "3", "3", "3", "3", "3", "3", "3", "3"])
    return road

def road4():
    road = []
    road.append(["3","3", "3", "3", "3", "3", "3", "3", "3", "3", "3", "3", "3", "3", "3", "3", "3", "3", "3", "3", "3", "3"])
    road.append(["3","0", "3", "3", "0", "0", "0", "0", "0", "0", "0", "0", "3", "0", "3", "0", "0", "0", "0", "0", "0", "3"])
    road.append(["3","0", "0", "0", "0", "3", "3", "3", "3", "3", "3", "0", "3", "0", "3", "3", "3", "3", "3", "3", "0", "3"])
    road.append(["3","3", "3", "3", "3", "3", "0", "0", "0", "0", "0", "1", "0", "0", "3", "0", "0", "0", "0", "0", "0", "3"])
    road.append(["3","0", "0", "0", "0", "3", "0", "3", "3", "3", "3", "3", "3", "0", "3", "3", "0", "3", "3", "3", "3", "3"])
    road.append(["3","0", "3", "3", "3", "3", "0", "3", "0", "0", "0", "0", "0", "0", "0", "0", "0", "3", "0", "0", "0", "3"])
    road.append(["3","0", "0", "0", "0", "0", "0", "0", "0", "3", "3", "3", "0", "3", "3", "3", "0", "0", "0", "3", "0", "3"])
    road.append(["3","3", "3", "3", "3", "3", "3", "3", "3", "3", "0", "0", "0", "0", "3", "3", "3", "3", "3", "3", "0", "3"])
    road.append(["3","2", "0", "0", "0", "0", "0", "0", "0", "0", "0", "3", "3", "0", "0", "0", "0", "0", "0", "0", "0", "3"])
    road.append(["3","3", "3", "3", "3", "3", "3", "3", "3", "3", "3", "3", "3", "3", "3", "3", "3", "3", "3", "3", "3", "3"])
    return road

def whichroad():
    ran = random.randint(1, 4)
    if ran == 1:
        print("Test case 1")
        road = road1()

    elif ran == 2:
        print("Test case 2")
        road = road2()

    elif ran == 3:
        print("Test case 3")
        road = road3()

    elif ran == 4:
        print("Test case 4")
        road = road4()
    return road