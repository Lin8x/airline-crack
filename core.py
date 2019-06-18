#!/usr/bin/python3
import os
import platform

r = '\033[0m'     #reset
bold = '\033[01m'
d = '\033[02m'     #disable
ul = '\033[04m' #underline
reverse = '\033[07m'
st = '\033[09m' #strikethrough
invis = '\033[08m'#invisible
white = '\033[0m'
cwhite = '\33[37m'
black ='\033[30m'
red = '\033[31m'
green = '\033[32m'
orange = '\033[33m'
blue = '\033[34m'
purple = '\033[35m'
cyan = '\033[36m'
lgrey = '\033[37m'
grey = '\033[90m'
lred = '\033[91m'
lgreen = '\033[92m'
yellow = '\033[93m'
lblue = '\033[94m'
pink = '\033[95m'
lcyan = '\033[96m'
bgreen = '\33[42m'
blgreen = '\33[102m'
bred = '\33[41m'
blred = '\33[101m'
borange = '\33[43m'
byellow = '\33[33m'
bcyan = '\33[44m'
blcyan = '\33[104m'
br = '\33[108m'
brown = '\33[33m'
bwhite = '\33[107'

def clear():
    x = 0
    while x <= 5:
      os.system("clear")
      x = x + 1

def logo():
    print("""____________       __________                   _________                   ______  
___    |__(_)_________  /__(_)___________       __  ____/____________ _________  /__
__  /| |_  /__  ___/_  /__  /__  __ \  _ \_______  /    __  ___/  __ `/  ___/_  //_/
_  ___ |  / _  /   _  / _  / _  / / /  __//_____/ /___  _  /   / /_/ // /__ _  ,<   
/_/  |_/_/  /_/    /_/  /_/  /_/ /_/\___/       \____/  /_/    \__,_/ \___/ /_/|_|  
                                                                                    """)

def checksystem():
    p = platform.system()
    if "Linux" == p:
      plat = "Linux"
    elif "Darwin" == p:
      plat = "Mac OS X"
    return plat

def quit():
    clear()
    exit()
        
