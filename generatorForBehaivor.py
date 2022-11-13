import classRoom
def behaivorGenerator(list):
    behaivorString=""
    for object in list:
        if object.name == "BedRoom":
                behaivorString=behaivorString+"Person1 go in "+object.name+"\n"
                if object.light=="ON":
                    behaivorString=behaivorString+ "In "+ object.name+ " light is "+object.light+"\n"
                else:
                    behaivorString=behaivorString+"In " + object.name + " light is " + object.light+"\n"
                if object.tv=="ON":
                    behaivorString=behaivorString+"In "+ object.name+ " Person1 watch at tv "+"\n"
                if object.laptop=="ON":
                    behaivorString=behaivorString+"In " + object.name + " Person1 watch on laptop "+"\n"
        if object.name == "DayRoom":
            behaivorString = behaivorString + "Person1 go in " + object.name + "\n"
            if object.light == "ON":
                behaivorString = behaivorString + "In " + object.name + " light is " + object.light + "\n"
            else:
                behaivorString = behaivorString + "In " + object.name + " light is " + object.light + "\n"
            if object.tvMainRoom == "ON":
                behaivorString = behaivorString + "In " + object.name + " Person1 watch at tv in main room " + "\n"
        if object.name == "BathRoom":
            behaivorString = behaivorString + "Person1 go in " + object.name + "\n"
            if object.light == "ON":
                behaivorString = behaivorString + "In " + object.name + " light is " + object.light + "\n"
            else:
                behaivorString = behaivorString + "In " + object.name + " light is " + object.light + "\n"
            if object.secondlight == "ON":
                behaivorString = behaivorString + "In " + object.name + " second light is " + object.light + "\n"
            else:
                behaivorString = behaivorString + "In " + object.name + " second light is " + object.light + "\n"

    print(behaivorString)


# object1=classRoom.BedRoom("a")
# object2=classRoom.BathRoom("b")
# object3=classRoom.BathRoom("c")
# list=[]
# list.append(object1)
# list.append(object2)
# list.append(object3)
# behaivorGenerator(list)