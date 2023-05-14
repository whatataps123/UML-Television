# Joshua Lemuel Z. Centina BS CPE 1-4
# Class TV

# Create a Python Code for creating the Class named TV and a Test Driver program named 
# TestTV that will create two objects from Class TV and will produce the following output:

# pseudocode
# channel is from 1 to 120
# volume is from 1 to 7
# create class TV
class TV:
# constructor
    def __init__(self, channel, volumeLevel, on):
    # channel: int (Channel is from 1-120)
        self.channel = int(channel)
    # volumeLevel: int (Volume is from 1-7)
        self.volumeLevel = int(volumeLevel)
    # on: bool (on/off or True/False initially False assume tv is off)
        self.on = True

# Methods:
    def show(self):
        print(self.channel, self.volumeLevel, self.on)
    # turnon: None (Turns on TV)
    def TurnOn(self):
        self.on = True
        print("on")
    # turnoff: None (Turns off TV)
    def TurnOff(self):
        self.on = False
        print("off")
    # getChannel: int (Returns channel of TV)
    def getChannel(self):
        return self.channel
    print(3)
    # setChannel(channel: int): None (Sets new channel of TV)
    def setChannel(self, new_channel):
        if new_channel >=1 and new_channel <= 120:
            self.channel = new_channel
    # getVolume: int (gets/returns volume level of TV)
    # setVolume(volumeLevel: int): None (Sets new volume of TV)
    # channelUp: None (Increment channel by 1)
    # channelDown: None (Decrement channel by 1)
    # volumeUp: None (Increment volume by 1)
    # volumeDown: None (Decrement channel by 1)

tv = TV(1, 13, False)
tv.show()
tv.TurnOn()
print("TV is on", tv.on)
