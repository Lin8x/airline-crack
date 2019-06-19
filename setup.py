#!/usr/bin/python

import os
import platform
import core
import time

core.clear()
print("Welcome to Airline-Crack! \n")
print("Checking Dependencies for " + core.checksystem() + "... \n")

time.sleep(1)

def filesetup():
    print("")
    os.system("sudo mv airline-crack /usr/bin/")
    print("Heads Up!: Tried Moving 'airline-crack' to /usr/bin") 
    os.system('sudo mv airlinecrack.py /usr/share/airline-crack')
    print("Heads Up!: Tried Moving 'airlinecrack.py' to /usr/share/airline-crack'") 
    os.system('sudo mv core.py /usr/share/airline-crack')
    print("Heads Up!: Tried Moving 'core.py' to /usr/share/airline-crack") 

p = platform.system()
if "Linux" == p:
  try:
    os.system("sudo apt-get install -y macchanger")
    os.system("sudo apt-get install -y arp-scan")
    os.system("sudo apt-get install -y ipcalc")
    os.system("sudo apt-get install -y aircrack-ng")
    os.system("sudo apt-get install -y tcpdump")
    os.system("sudo pip3 install getmac")
    os.system("sudo pip3 install scapy")
    os.system("sudo pip3 install lanscan")
    filesetup()
    print("")
    print("You have finished the setup. Please type 'python3 airlinecrack.py' to run the tool.")
    print("If you are using Linux, there is a bash file in /usr/bin, so you just have to type 'airline-crack' to run it.")
    print("")
    input("Press {ENTER} to Continue... ")
  except:
    print("Error: Could not install macchanger and arp-scan. \nIs your connection online?")
elif "Windows" == p:
  print("Sorry. we don't support windows machines. \n Try using a virtual machine.")
  input("Press {ENTER} to Exit... ")
  core.quit()
elif "Darwin" == p:
  try:
    os.system("brew install macchanger")
    os.system("brew install arp-scan")
    os.system("brew install ipcalc")
    os.system("brew install aircrack-ng")
    os.system("brew install tcpdump")
    os.system("sudo pip3 install getmac")
    os.system("sudo pip3 install scapy")
    os.system("sudo pip3 install lanscan")
    print("")
    print("You have finished the setup. Please type 'python3 airlinecrack.py' to run the tool.")
    print("If you are using Linux, there is a bash file in /usr/bin, so you just have to type 'airline-crack' to run it.")
    print("")
    input("Press {ENTER} to Continue... ")
  except:
    print("Error: Could not install macchanger and arp-scan. \nIs your connection online? Did you make sure to install Brew?")
else:
  print("Could not find the type of OS. \nSorry, please use a unix operating system such as Linux or Mac.")
  input("Press {ENTER} to Exit... ")
  core.quit()
