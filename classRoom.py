
class Room():
    def __init__(self,letter,light="ON",name="Room"):
        self.letter=letter
        self.light=light
        self.name=name
    def __repr__(self):
        return "("+self.letter+self.light+self.name+")"

class BedRoom(Room):
    def __init__(self,letter,light="OFF",tv="ON",laptop="ON",name="BedRoom"):
      super().__init__(letter,light,name)
      self.tv=tv
      self.laptop=laptop

    def __repr__(self):
        return "("+self.letter+self.light+self.tv+self.laptop+self.name+")"

class BathRoom(Room):
    def __init__(self,letter,light="ON",secondlight="ON",name="BathRoom"):
      super().__init__(letter,light,name)
      self.secondlight=secondlight

    def __repr__(self):
      return "(" +self.letter + self.light + self.secondlight +self.name+ ")"

class DayRoom(Room):
    def __init__(self,letter,light="ON",tvMainRoom="ON",name="DayRoom"):
      super().__init__(letter,light,name)
      self.tvMainRoom=tvMainRoom

    def __repr__(self):
      return "("+self.letter + self.light + self.tvMainRoom + self.name+ ")"
#
# x=Room("OFF")
# print(x.light)
# y=DayRoom("a")
# print(y)