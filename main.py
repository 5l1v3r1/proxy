#!/usr/bin/python3.6
# Wrote by iwHh | iran-cyber.NeT

#import modules
import time
import sys
import os
import re
try:
    from colorama import Fore, Style
except ImportError:
    if os.name == "nt":
        print("Installing colorama module ...\nwhen finished run me again bruh")
        time.sleep(4)
        os.system("python -m pip install colorama")
        sys.exit()
    else:
        print("Installing colorama module ...\nwhen finished run me again bruh")
        time.sleep(4)
        os.system("sudo pip install colorama")
        sys.exit()
try:
    from bs4 import BeautifulSoup
except ImportError:
    if os.name == "nt":
        print("Installing bs4 module ...\nwhen finished run me again bruh")
        time.sleep(4)
        os.system("python -m pip install bs4")
        sys.exit()
    else:
        print("Installing bs4 module ...\nwhen finished run me again bruh")
        time.sleep(4)
        os.system("sudo pip install bs4")
        sys.exit()
try:
    import requests
except ImportError:
    if os.name == "nt":
        print("Installing requests module ...\nwhen finished run me again bruh")
        time.sleep(4)
        os.system("python -m pip install requests")
        sys.exit()
    else:
        print("Installing requests module ...\nwhen finished run me again bruh")
        time.sleep(4)
        os.system("sudo pip install requests")
        sys.exit()
# Start my application

class Icg(object):

    # Init function
    def __init__(self):
        self.b = Fore.BLUE
        self.r = Fore.RED
        self.y = Fore.YELLOW
        self.g = Fore.GREEN
        self.w = Fore.WHITE
        self.m = Fore.MAGENTA
        self.c = Fore.CYAN
        self.reset = Style.RESET_ALL
        self.clear()
        self.print_logo()
        self.main()

    # Clear the console
    def clear(self):
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")

    # Print logo Func
    def print_logo(self):
        self.logo = """
        {}##############################
        {}#       {}ProxYGraBber {}v1.0    {}#
        {}#       {}Wrote by iwHh        {}#
        {}#       {}Iran-Cyber.NeT       {}#
        {}##############################{}"""
        print(self.logo.format(self.r, self.r, self.g, self.c, self.r, self.r, self.y, self.r, self.r, self.b, self.r, self.r, self.reset))

    # Main Function
    def main(self):
        self.conn = requests.get("https://www.sslproxies.org/")
        self.conn2 = requests.post("https://www3.yo-lang.ir/YOProxyBot/result.php", data={'username':640709375, 'pass':195})
        self.reg = re.findall(r"\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b:\d{2,5}", self.conn2.text)
        self.conn3 = requests.get("https://www.us-proxy.org/")
        self.bs = BeautifulSoup(self.conn.text, 'html.parser')
        self.bs2 = BeautifulSoup(self.conn3.text, 'html.parser')
        for tr in self.bs.find("tbody").findAll("tr"):
            self.finder = tr.findAll("td")
            self.ip = self.finder[0].text
            self.port = self.finder[1].text
            print("{}:{}".format(self.ip, self.port))
            with open("saved.txt", "a") as e:
                e.write("{}:{}\n".format(self.ip, self.port))
            time.sleep(0.08)
        time.sleep(2)
        for _ in range(len(self.reg)):
            print(self.reg[_])
            with open("saved.txt", "a") as e:
                e.write("{}\n".format(self.reg[_]))
            time.sleep(0.08)
        for tr in self.bs2.find("tbody").findAll("tr"):
            self.finder2 = tr.findAll("td")
            self.getip = self.finder2[0].text
            self.getport = self.finder2[1].text
            print("{}:{}".format(self.getip, self.getport))
            with open("saved.txt", "a") as e:
                e.write("{}:{}\n".format(self.getip, self.getport))
            time.sleep(0.08)
if __name__ == "__main__":
    run = Icg()
