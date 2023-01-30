# Write an Object oriented Python program to create two Time objects:
# currentTime, which contains the current time; and breadTime, which
# contains the amount of time it takes for a bread maker to make bread.
# Then we'll use addTime to figure out when the bread will be done.
# Write the printTime function to display the time when the bread will
# be done by the bread maker.

import time


class Time:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def addTime(self, time2):
        self.seconds += time2.seconds
        carry, self.seconds = self.seconds//60, self.seconds % 60

        self.minutes = self.minutes + time2.minutes + carry
        carry, self.minutes = self.minutes//60, self.minutes % 60

        self.hours = (self.hours + time2.hours + carry) % 24

    def printTime(self):
        print("%d:%02d:%02d" % (self.hours, self.minutes, self.seconds))


# currentTime = Time(time.localtime().tm_hour,
#                    time.localtime().tm_min, time.localtime().tm_sec)
currentTime = Time(*time.localtime()[3:6])

print("current time:")
currentTime.printTime()

breadTime = Time(1, 45, 30)

print("bread will be done by:")
currentTime.addTime(breadTime)
currentTime.printTime()
