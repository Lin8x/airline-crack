#!/usr/bin/python3

import os
import core
import getmac
import lanscan
import platform

r = core.r
p = core.pink
re = core.lred
y = core.yellow
g = core.lgreen
lc = core.lcyan
pu = core.purple
bo = core.bold
ul = core.ul

global macspoof
macspoof = "None Found"
mac_id = getmac.get_mac_address()
        

def start():
    try:
        core.clear()
        print("--------------------- \n")
        os.system("ifconfig")
        print("\n--------------------- \n")
        os.system("lanscan interfaces")
        print("\n--------------------- \n")
        answer = input("Please type your wireless adapter's name (Default: wlan0): ")
        if answer == "":
            mon = "wlan0"
        else:
            mon = answer
        startup(mon)
    except KeyboardInterrupt:
        core.quit()

def tcpscan(mon):
    print("\n---------------------")
    CH = input("Please type the channel of the wifi you're trying to crack: ")
    print("---------------------")
    oss = core.checksystem()
    if oss == "Linux":
        try:
            monnew = mon + "mon"
            print("Scanning...")
            os.system("sudo tcpdump -i " + mon)
            print("")
            save = input("Would you like to save these outputs? (Default = No): ")
            if save == "y" or save == "yes" or save == "Y" or save == "Yes" or save == "YES":
                  savename = input("What would you like to call the file? (default: tcpdump-interface): ")
                  if savename == "":
                      savename = "tcpdump-" + mon
                  os.system("sudo tcpdump -i " + mon + " > " + savename + ".log")
                  print("")
                  input("Your output was saved in " + savename + ".log")
                  startup(mon)
            else:
                  input("\nAlright, your output was not saved.")
                  startup(mon)
        except:
            print("Error: Could not scan packets of a WiFi or do the TCPdump process. Make sure you have TCPdump and aircrack-ng installed.")
            
    else:
        try:
            print("\n---------------------")
            print("Sniffing the Wifi of the channel " + CH + "...")
            print("")
            os.system("sudo airport " + mon + " sniff " + CH)
            print("")
            print("---------------------")
            print("")
            WIFIDIR = input("Please type the Directory the packets were saved in (Default:  /tmp/airportSniffFLWZie.cap): ")
            if WIFIDIR == "":
                WIFIDIR =  "/tmp/airportSniffFLWZie.cap"
            print("")
            print("Scanning...")
            os.system("tcpdump -r " + WIFIDIR + " | less")
            print("")
            save = input("Would you like to save these outputs? (Default = No): ")
            if save == "y" or save == "yes" or save == "Y" or save == "Yes" or save == "YES":
                  savename = input("What would you like to call the file? (default: tcpdump-Channel): ")
                  if savename == "":
                      savename = "tcpdump-" + CH
                  os.system("tcpdump -r " + WIFIDIR + " | less" + " > " + savename + ".log")
                  print("")
                  input("Your output was saved in " + savename + ".log")
                  startup(mon)
            else:
                  input("\nAlright, your output was not saved.")
                  startup(mon)
            
        except:
            print("Error: Could not scan packets of a WiFi or do the TCPdump process. Make sure you have airports, TCPdump, and aircrack-ng installed.")

def wepCrack(mon):
    #print("sudo airport " + en0 sniff 6")
    print("\n---------------------")
    CH = input("Please type the channel of the wifi you're trying to crack: ")
    print("---------------------")
    oss = core.checksystem()
    if oss == "Linux":
        try:
            monnew = mon + "mon"
            os.system("sudo airmon-ng start" + monnew)
            print("\n---------------------")
            print("")
            CH = input("Please type the CHANNEL of the WiFi: ")
            BSSID = input("Please type the BSSID of the WiFi: ")
            print("")
            #besside-ng -b 7C:CA:ED:A4:9B:EE -c 11 wlan0mon
            os.system("besside-ng -b " + BSSID + " -c " + CH + " " + monnew)
            print("")
            WIFIDIR = input("Please type the Directory the packets were saved in (Default:  ~/wep.cap): ")
            if WIFIDIR == "":
                WIFIDIR =  "~/wep.cap"
            os.system("aircrack-ng ./wep.cap")
        except:
            print("Error: Could not scan packets of a WiFi or start cracking process. Make sure you have airports and aircrack-ng installed.")

    else:
        try:
            print("\n---------------------")
            print("Sniffing the Wifi of the channel " + CH + "...")
            print("")
            os.system("sudo airport " + mon + " sniff " + CH)
            print("")
            print("---------------------")
            print("")
            WIFIDIR = input("Please type the Directory the packets were saved in (Default:  /tmp/airportSniffFLWZie.cap): ")
            if WIFIDIR == "":
                WIFIDIR =  "/tmp/airportSniffFLWZie.cap"
            BSSID = input("Please type the BSSID of the WiFi: ")
            print("")
            os.system("aircrack-ng -1 -a 1 -b " + BSSID + " " + WIFIDIR)
            print("")
            
        except:
            print("Error: Could not scan packets of a WiFi or start cracking process. Make sure you have airports and aircrack-ng installed.")

def wifiscan(mon):
    oss = core.checksystem()
    if oss == "Linux":
        try:
            monnew = mon + "mon"
            print("")
            os.system("airmon-ng start " + monnew)
            print("")
            os.system("sudo airodump-ng " + monnew)
            print("")
            save = input("Would you like to save these outputs? (Default = No): ")
            if save == "y" or save == "yes" or save == "Y" or save == "Yes" or save == "YES":
                  savename = input("What would you like to call the file? (default: airmon-ng_scan): ")
                  if savename == "":
                      savename = "airmon-ng_scan"
                  os.system("sudo airodump-ng " + monnew + " > " + savename + ".log")
                  print("")
                  input("Your output was saved in " + savename + ".log")
                  os.system("airmon-ng stop " + monnew)
                  input("Stopped " + monnew + ".")
                  startup(mon)
            else:
                  input("\nAlright, your output was not saved.")
                  startup(mon)
        except:
            print("Could not run airmon-ng and airodump-ng with your network interface. Are you using a wireless adapter without monitor mode? Make sure you have one that does monitor mode.")

    else:
        try:
            os.system("sudo ln -s /System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport /usr/sbin/airport")
        except:
            print("Error: Could not move /System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport to /usr/sbin/airport. Maybe it was already moved?")
        print("")
        os.system("sudo airport -s")
        print("")
        save = input("Would you like to save these outputs? (Default = No): ")
        if save == "y" or save == "yes" or save == "Y" or save == "Yes" or save == "YES":
            savename = input("What would you like to call the file? (default: airport_scan): ")
            if savename == "":
                savename = "airport_scan"
            os.system("sudo airport -s  > " + savename + ".log")
            print("")
            input("Your output was saved in " + savename + ".log")
            startup(mon)
        else:
            input("\nAlright, your output was not saved.")
            startup(mon)
        

def startup(mon):
  core.clear()
  core.logo()
  print(r + ul + bo + "Welcome to Airline-Crack!" + r + "\n")
  print("Your device: " + core.checksystem())
  print("Your network interface: " + mon)
  print("Your original mac address: " + str(mac_id))
  os.system("macchanger -s " + mon)
  print("")
  print(bo + "Scanning:" + r)
  print(r + "(" + lc + "1" + r + ")" + "  Scan for access points. (Airport)")
  print(r + "(" + lc + "2" + r + ")" + "  Scan IPs and MAC-Addresses/Devices on network (Arp-Scan)")
  print(r + "(" + lc + "3" + r + ")" + "  Scan for packets on a network (Airport + TCPdump)")
  print(r + "(" + lc + "4" + r + ")" + "  Scan an IP Address (Nmap)")
  print(r + "(" + lc + "5" + r + ")" + "  Scan an IP Address (Ipcalc)")
  print(bo + "MAC Address:" + r)
  print(r + "(" + lc + "6" + r + ")" + "  Become a specific MAC address (Macchanger)")
  print(r + "(" + lc + "7" + r + ")" + "  Become a random MAC address (Macchanger)")
  print(bo + "Password Cracking:" + r)
  print(r + "(" + lc + "8" + r + ")" + "  Make a password list (Crunch)")
  print(r + "(" + lc + "9" + r + ")" + "  Crack WEP WiFi passwords (Airport + Aircrack)")
  print(bo + "Extra:" + r)
  print(r + "(" + lc + "r" + r + ")" + "  Reload/Clear the screen")
  print(r + "(" + lc + "99" + r + ")" + " Exit the tool (CNTRL + C) \n")

  while True:
      answer = input(bo + "Airline" + r + "-" + re + "C" + y + "r" + g + "a" + lc + "c" + p + "k" + lc + " > " + r)

      if answer == "1":
          wifiscan(mon)

      if answer == "2":
          print("")
          os.system("sudo arp-scan -l")
          print("")
          save = input("Would you like to save these outputs? (Default = No): ")
          if save == "y" or save == "yes" or save == "Y" or save == "Yes" or save == "YES":
              savename = input("What would you like to call the file? (Default: arp-scan): ")
              if savename == "":
                  savename = "arp-scan"
              os.system("sudo arp-scan -l > " + savename + ".log")
              print("")
              input("Your output was saved in " + savename + ".log")
              startup(mon)
          else:
              input("\nAlright, your output was not saved.")
              startup(mon)

      elif answer == "3":
          tcpscan(mon)

      elif answer == "4":
          print("")
          IP = input("Please type a specific IP Address: ")
          print("")
          os.system("sudo nmap -A " + IP)
          print("")
          save = input("Would you like to save these outputs? (Default = No): ")
          if save == "y" or save == "yes" or save == "Y" or save == "Yes" or save == "YES":
              savename = input("What would you like to call the file? (default: nmap-xxx.xxx.x.x): ")
              if savename == "":
                  savename = "nmap-" + IP
              os.system("sudo nmap -A " + IP + " > " + savename + ".log")
              print("")
              input("Your output was saved in " + savename + ".log")
              startup(mon)
          else:
              input("\nAlright, your output was not saved.")
              startup(mon)
              
      elif answer == "5":
          print("")
          IP = input("Please type a specific IP Address: ")
          print("")
          os.system("ipcalc " + IP)
          print("")
          save = input("Would you like to save these outputs? (Default = No): ")
          if save == "y" or save == "yes" or save == "Y" or save == "Yes" or save == "YES":
              savename = input("What would you like to call the file? (default: ipcalc-xxx.xxx.x.x): ")
              if savename == "":
                  savename = "ipcalc-" + IP
              os.system("sudo nmap -A " + IP + " > " + savename + ".log")
              print("")
              input("Your output was saved in " + savename + ".log")
              startup(mon)
          else:
              input("\nAlright, your output was not saved.")
              startup(mon)
              
      elif answer == "6":
          print("")
          macspoof = input("Please type a specific Mac Address: ")
          print("")
          os.system("macchanger -m " + macspoof + " " + mon)
          print("")
          input("Finished! Please press {ENTER} to continue...")
          startup(mon)

      elif answer == "7":
          print("")
          macspoof = os.system("macchanger -r " + mon)
          print("")

      elif answer == "8":
          print("")
          print("---------------------")
          crunchname = input("Please type the name of the password text file (Default: rockyou): ")
          if crunchname == "" or crunchname == " ":
              crunchname = "rockyou"
          crunchname = crunchname.replace(" ", "_")
          print("---------------------")
          print("Ex: ~/Desktop")
          crunchdir = input("Type the directory you want the file to be in: ")
          print("---------------------")
          crunchmin = input("Minimum # of characters for passwords: ")
          print("---------------------")
          crunchmax = input("Maximum # of characters for passwords: ")
          print("---------------------")
          print("@ = Any character/number (Wildcard)")
          print("123... = Any number")
          print("Ex: 123456789abcd = characters that can be the # 1-9 or a-d in the alphabet.")
          crunchset = input("Enter the setup for passwords: ")
          print("")
          os.system("crunch " + crunchmin + " " + crunchmax + " " + crunchset + " -o " + crunchdir + "/" + crunchname + ".txt")
          print("")
          input("Finished! Your password file, " + crunchname + ".txt is at " + crunchdir)
          startup(mon)

      elif answer == "9":
          wepCrack(mon)

      elif answer == "r":
          startup(mon)

      elif answer == "99":
          core.quit()

      elif answer == "exit":
          core.quit()

      else:
          print("\nThe choice '" + answer + "' was not found. Please pick a choice above. \n")
start()
