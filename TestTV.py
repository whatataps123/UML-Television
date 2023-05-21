# Import the from file ClassTV.py the class of TV
import time
import sys
from TV import TV

# Do Methods for TestTV
def TestTV():
# TV1 channel should be 30 and volume should be 3
    print("=" * 65)
    print("\033[1;31m" + "Loading:" + "\033[1;m")
    #animation = ["10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%", "90%", "100%"]
    animation = ["[■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]
    for i in range(len(animation)):
        time.sleep(0.2)
        sys.stdout.write("\r" + animation[i % len(animation)])
        sys.stdout.flush()
    print("\n\033[1;35m" + "TV 1 Controller" + "\033[1;m")
    tv_1 = TV()
    tv_1.show() # Show to see the initial state of TV 1
    tv_1.TurnOn()
    tv_1.setChannel(30) 
    tv_1.setVolume(3)
    tv_1.show() # Show the new state of TV

# TV2 channel should be 3 and volume should be 2
    print("=" * 65)
    print("\033[1;31m" + "Loading:" + "\033[1;m")
    #animation = ["10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%", "90%", "100%"]
    animation = ["[■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]
    for i in range(len(animation)):
        time.sleep(0.2)
        sys.stdout.write("\r" + animation[i % len(animation)])
        sys.stdout.flush()
    print("\n\033[1;36m" + "TV 2 Controller" + "\033[1;m")
    tv_2 = TV()
    tv_2.show() # Show the initial state of TV 2
    tv_2.TurnOn() 
    tv_2.setChannel(3)
    tv_2.setVolume(2)
    tv_2.show() # Show the new state of TV 2
    print("=" * 65)
TestTV()
