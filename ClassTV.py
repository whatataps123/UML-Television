# Joshua Lemuel Z. Centina BS CPE 1-4
# Class TV

# Create a Python Code for creating the Class named TV and a Test Driver program named 
# TestTV that will create two objects from Class TV and will produce the following output:

# pseudocode
# create class TV
class TV:
# constructor
    def __init__(self, channel, volumeLevel, on):
    # channel: int
        self.channel = int(channel)
    # volumeLevel: int
        self.volumeLevel = int(volumeLevel)
    # on: bool
        self.on = on

# Methods:
    # turnon: None
    def TurnOn(self):
        self.on = True
    # turnoff: None
    def TurnOff(self):
        self.on = False
    # getChannel: int
    # setChannel(channel: int): None
    # getVolume: int
    # setVolume(volumeLevel: int): None
    # channelUp: None
    # channelDown: None
    # volumeUp: None
    # volumeDown: None

tv = TV(1, 13, False)
tv.TurnOn()
print("TV is on", tv.on)
