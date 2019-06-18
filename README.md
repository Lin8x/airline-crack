
# ![logo name](http://i67.tinypic.com/huekv8.jpg)

------------------------------------------------------------------------

## :airplane: &nbsp; About Aircrack &nbsp; :airplane:

This is a small tool which allows for easy accessability to spoofing your MAC Address and scanning IP addresses.
The idea behind this is to help you obtain free airplane wifi.

Authors and contibutors are not responsible for whatever you do with this tool. You are responsible for your own actions!
  
------------------------------------------------------------------------

## :unlock: &nbsp; Requirements &nbsp; :unlock:

Operating System:
* Mac OS X
* Linux (Debian/Ubuntu Based)

Packages:
* ![arp-scan](https://linux.die.net/man/1/arp-scan)
* ![macchanger](https://github.com/alobbs/macchanger)
* ![ipcalc](https://linux.die.net/man/1/ipcalc)

Python Library (Pip3):
* python3
* pip3
* ![os](https://docs.python.org/3/library/os.html)
* ![getmac](https://pypi.org/project/getmac/) >= 0.8.1
* ![platform](https://docs.python.org/3/library/platform.html)
* ![scapy](https://pypi.org/project/scapy-python3/)
* ![lanscan](https://pypi.org/project/lanscan/)

------------------------------------------------------------------------

## :inbox_tray: &nbsp; How to Install &nbsp; :inbox_tray:

You can install the program by:

**1. Downloading the file on the Github page**

Or by...

**2. Typing in your terminal - `git clone https://www.github.com/lin8x/airline-crack`**

*Once finished installing, please type `sudo python3 setup.py` to setup your program.*

------------------------------------------------------------------------

## :fire: &nbsp; How to Run &nbsp; :fire:

***For Mac OS X:***

Open the directory to the file: 'airline-crack' and run the program by typing: 
`sudo python3 airlinecrack.py`

***For Linux:***

Simply type `airline-crack` in your terminal to run the program.

##### Setup Information

During setup for Linux users, the python program _(core.py and airlinecrack.py)_ will go into the directory: `/usr/share/airline-crack`

As for the bash program, that will allow for running the program with the command 'airline-crack', will go to the directory: `/usr/bin`

This however does not work for Mac OS users as the `/usr/bin/` and `/usr/share` ***is not*** accessable even with sudo.
This is because Macs limit the power of the root account, so that even if you become root, you don't have full control over the system.

------------------------------------------------------------------------

## :camera: &nbsp; Screenshot &nbsp; :camera:

![screenshot of tool](http://i63.tinypic.com/sdjsjm.png)

------------------------------------------------------------------------

## :star2: &nbsp; Contributing &nbsp; :star2:

Please read ![CONTRIBUTING.md](https://github.com/Lin8x/airline-crack/blob/master/CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

You can see ![CHANGESLOG.md](https://github.com/Lin8x/airline-crack/blob/master/CHANGESLOG.md) for details of changes to the tool for each update.

See also the list of contributors who participated in this project.

------------------------------------------------------------------------

## :page_with_curl: &nbsp; License &nbsp; :page_with_curl:

This project is licensed under the GNU General Public License (v3.0) - see the ![LICENSE.md](https://github.com/Lin8x/airline-crack/blob/master/LICENSE) file for details.

------------------------------------------------------------------------
