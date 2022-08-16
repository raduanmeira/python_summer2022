## Fill in the following methods for the class 'Clock'

class Clock:
    def __init__(self, hour, minutes):
      self.minutes = minutes
      self.hour = hour
      while self.minutes > 60:
        self.hour = self.hour + 1
        self.minutes = self.minutes - 60
      while self.hour > 24:
        self.hour = self.hour - 24
      
    ## Print the time
    def __str__(self):
      return "%02d:%02d" % (self.hour,self.minutes)

    ## Add time
    ## Don't return anything
    def __add__(self,otherMinutes):
        self.minutes = self.minutes + otherMinutes
        while self.minutes >60:
          self.hour = self.hour + 1
          self.minutes = self.minutes - 60
        if self.hour >= 24:
          self.hour = self.hour - 24
       
    ## Subtract time
    ## Don't return anything
    def __sub__(self, otherMinutes):
        self.minutes = self.minutes - otherMinutes
        while self.minutes <0:
          self.hour = self.hour - 1
          self.minutes = 60 + self.minutes
        if self.hour <0:
          self.hour = 24 + self.hour
    
    ## Are two times equal?
    def __eq__(self, other):
      return "%02d:%02d" % (self.hour,self.minutes) == "%02d:%02d" % (other.hour,other.minutes)
    
    ## Are two times not equal?
    def __ne__(self, other):
      return "%02d:%02d" % (self.hour,self.minutes) != "%02d:%02d" % (other.hour,other.minutes)


# You should be able to run these
clock1 = Clock(23, 5)
print(clock1) # 23:05
clock2 = Clock(12, 45)
print(clock2) # 12:45
clock3 = Clock(12, 45)
print(clock3) # 12:45

print(clock1 == clock2) ## False
print(clock1 != clock2) ## True
print(clock2 == clock3) ## True

print("testing addition")
clock1 + 60
print(clock1) # 00:05
print(clock1 == Clock(0, 5)) # True

print("testing subtraction")
clock1 - 100
print(clock1) # 22:25

