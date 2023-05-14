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
    def __init__(self, channel=1, volumeLevel=1, on=False):
    # channel: int (Channel is from 1-120)
        self.channel = int(channel)
    # volumeLevel: int (Volume is from 1-7)
        self.volumeLevel = int(volumeLevel)
    # on: bool (on/off or True/False initially False assume tv is off)
        self.on = on

# Methods:
    def show(self):
        print(self.channel, self.volumeLevel, self.on)
    # turnon: None (Turns on TV)
    def TurnOn(self):
        self.on = True
    # turnoff: None (Turns off TV)
    def TurnOff(self):
        self.on = False
    # getChannel: int (Returns channel of TV)
    def getChannel(self):
        return self.channel
    # setChannel(channel: int): None (Sets new channel of TV)
    def setChannel(self, new_channel):
        if new_channel >=1 and new_channel <= 120:
            self.channel = new_channel
    # getVolume: int (gets/returns volume level of TV)
    def getVolume(self):
        return self.volumeLevel
    # setVolume(volumeLevel: int): None (Sets new volume of TV)
    def setVolume(self, new_volume):
        if new_volume >=1 and new_volume <= 7:
            self.volumeLevel = new_volume
    # channelUp: None (Increment channel by 1)
    def channelUp(self):
        if self.channel < 120:
            self.channel += 1
        else:
            self.channel = 1
    # channelDown: None (Decrement channel by 1)
    def channelDown(self):
        if self.channel > 1:
            self.channel -= 1
        else:
            self.channel = 120   
    # volumeUp: None (Increment volume by 1)
    def volumeUp(self):
        if self.volumeLevel < 7:
            self.volumeLevel += 1
        else:
            self.volumeLevel = 1
    # volumeDown: None (Decrement volume by 1)
    def volumeDown(self):
        if self.volumeLevel > 1:
            self.volumeLevel -= 1
        else:
            self.volumeLevel = 0
# try
# tv_1 = TV()
# tv_2 = TV()
# tv_1.show()
# print("====")
# tv_1.setChannel(120) #120
# tv_1.setVolume(1)
# tv_1.show()
# print("====")
# tv_1.channelUp() #1
# tv_1.show()
# print("===")
# tv_1.channelDown() #120
# tv_1.show()
# print("====")
# tv_1.channelDown()
# tv_1.volumeDown()
# tv_1.channelDown()
# tv_1.volumeDown()
# tv_1.show()

# tv_2.show()
