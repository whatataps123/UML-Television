# Import the from file ClassTV.py the class of TV
from ClassTV import TV

# Do Methods for TestTV
def TestTV():
# TV1 channel should be 30 and volume should be 3
    print("===============")
    print("TV 1 Controller")
    tv_1 = TV()
    tv_1.show() # Show to see the initial state of TV 1
    tv_1.TurnOn()
    tv_1.setChannel(30) 
    tv_1.setVolume(3)
    tv_1.show() # Show the new state of TV

# TV2 channel should be 3 and volume should be 2
    print("===============")
    print("TV 2 Controller")
    tv_2 = TV()
    tv_2.show() # Show the initial state of TV 2
    tv_2.TurnOn() 
    tv_2.setChannel(3)
    tv_2.setVolume(2)
    tv_2.show() # Show the new state of TV 2

TestTV()