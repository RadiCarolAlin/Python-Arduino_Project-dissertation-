import serial
import time
import classRoom
import generatorForBehaivor
import predictionMovement
flag=0
string1=""

counterSensor1=1
counterSensor2=0
stringForPrediction="a"
initRoom=classRoom.BedRoom("a","OFF","OFF","OFF")
listWithObject=[initRoom]

ArduinoSerial = serial.Serial('COM3',9600)
time.sleep(2)
while(flag<40):
 readLine = ArduinoSerial.readline()
 # print(b)
 string1=readLine.decode() # convert to string
 print(string1)
 if "Sensor1" in string1:
     index1=string1.find('1=')
     valueSensor1=int(string1[index1 + 2:])
     if valueSensor1<50 and counterSensor1%2==0:
         objectBedRoom= classRoom.BedRoom("a")
         listWithObject.append(objectBedRoom)
         stringForPrediction=stringForPrediction+"a"
         counterSensor1+=1
         time.sleep(4)
     elif valueSensor1<50 and counterSensor1%2!=0:
         objectDayRoom = classRoom.DayRoom("b")
         listWithObject.append(objectDayRoom)
         stringForPrediction = stringForPrediction + "b"
         counterSensor1 += 1
         time.sleep(4)

     print(valueSensor1)
     # t=False

 if "Sensor2" in string1:
     index2=string1.find('2=')
     valueSensor2=int(string1[index2 + 2:])
     if valueSensor2 < 50 and counterSensor2 % 2 == 0:
         objectBathRoom = classRoom.BathRoom("c")
         listWithObject.append(objectBathRoom)
         stringForPrediction = stringForPrediction + "c"
         counterSensor2 += 1
         time.sleep(4)
     elif valueSensor2 < 50 and counterSensor2 % 2 != 0:
         objectDayRoom = classRoom.DayRoom("b")
         listWithObject.append(objectDayRoom)
         stringForPrediction = stringForPrediction + "b"
         counterSensor2 += 1
         time.sleep(4)
     print(valueSensor2)
 print(stringForPrediction)
 print(listWithObject)
 print()
 flag+=1

 # s2=s1.rstrip()  # strip away excess characters
 # print(s2)

ArduinoSerial.close()
generatorForBehaivor.behaivorGenerator(listWithObject)
listwithString=predictionMovement.compress(stringForPrediction)
print(listwithString)
predictionMovement.roomPresentNumber(listwithString)

