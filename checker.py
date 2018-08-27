#!/usr/bin/python3.6

# Import modules

import os, sys, time, threading

try:
    import requests
except ImportError:
    print("Installing Requests Module for you\nwhen finished run me again")
    time.sleep(4)
    if os.name == "nt":
        os.system("python -m pip install requests")
        sys.exit(0)
    else:
        os.system("pip install requests")
        sys.exit(0)
try:
    from colorama import Fore, Style
except ImportError:
    print("Installing colorama module for you\nwhen finished run me again")
    time.sleep(4)
    if os.name == "nt":
        os.system("python -m pip install colorama")
        sys.exit(0)
    else:
        os.system("pip install colorama")
        sys.exit(0)

# Start Coding :-)
class Icg(object):
    def __init__(self):
        self.r = Fore.RED
        self.b = Fore.BLUE
        self.g = Fore.GREEN
        self.y = Fore.YELLOW
        self.m = Fore.MAGENTA
        self.c = Fore.CYAN
        self.w = Fore.WHITE
        self.reset = Style.RESET_ALL
        self.clear()
        self.print_logo()
        self.main()

    # CLear The Console
    def clear(self):
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")

    #Print Our Logo :p
    def print_logo(self):
        self.logo = """
        {}$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        $          {}ProxyChecker {}v1.0       {}$
        $          {}Wrote by {}iwHh           {}$
        $          {}iran-cyber.NeT          {}$
        $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$${}
        """
        print(self.logo.format(self.c, self.r, self.m, self.c, self.y, self.b, self.c, self.g, self.c, self.reset))

    # run Function
    def run(self, PROXY, URL):

        try:
            self.req = requests.session()
            self.req.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
                                      ' (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
                                      'Cache-Control': 'max-age=0'}
            self.proxies = {'https': PROXY}

            self.done = self.req.get("http://" + URL, proxies={'http': PROXY} ,timeout=5)
            if self.done.status_code == 200:
                print("{}{} {}~> {}Ok".format(self.y, PROXY, self.b, self.g))
                with open("ok.txt", "a") as e:
                    e.write("{}\n".format(PROXY))
                    e.close()
            else:
                print("{}{} {}~> {}No".format(self.y, PROXY, self.b, self.g))
        except:
            print("{}{} {}~> {} No".format(self.y, PROXY, self.b, self.g))


    def main(self):
        try:
            with open("saved.txt", "r") as e:
                self.prx = e.read().splitlines()
        except FileNotFoundError:
            print("First Run main.py to find proxies then run me :*")
            sys.exit(0)
        self.thread = []
        url = "google.com"
        for proxy in self.prx:
            self.t = threading.Thread(target=self.run, args=(proxy, url))
            self.t.start()
            self.thread.append(self.t)
            time.sleep(0.07)

        for m in self.thread:
            m.join
if __name__ == "__main__":
    run = Icg()
