from requests import get
from re import findall
from threading import Thread
from time import sleep
from sys import exit
from sys import argv
from os import name
from os import system
try:
    from bs4 import BeautifulSoup
except ImportError:
    print("Try pip install bs4")
    exit(1)
try:
    from colorama import Fore, Style
except ImportError:
    print("Try pip install colorama")
    exit(1)


headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

def check_connection():
    r = get("http://www.aliveproxy.com/high-anonymity-proxy-list", timeout=5)
    if "http://10.10.34.34" in r.text:
        print("Please Start Your Vpn Service Then Run {}{}".format(argv[0], Style.RESET_ALL))
        exit(1)
    else:
        pass

def cleaner():
    if name == "nt":
        system("cls")
    else:
        system("clear")


def get_prx(url):
    r = get(url, headers=headers, timeout=5)
    finder = findall("(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3}):(?:[\d]{1,5})", r.text)
    for n in finder:
        with open(get_name, mode="a") as e:
            e.write("{}\n".format(n))
            e.close()
        sleep(0.0005)


def get_prxbs(url):
    try:
        r = get(url, headers=headers, timeout=5).text
        bs = BeautifulSoup(r, "html.parser")
        for tr in bs.find("tbody").findAll("tr"):
            finder = tr.find_all("td")
            proxy = "{}:{}".format(finder[0].get_text(), finder[1].get_text())
            with open(get_name, mode="a") as e:
                e.write("{}\n".format(proxy))
                e.close()
            sleep(0.0003)
    except:
        pass


def get_prxv2(url, word1, word2):
    r = get(url, headers=headers, timeout=5).text
    bs = BeautifulSoup(r, "html.parser")
    for tag in bs.findAll(word2, word1):
        links = tag.a.get("href")
        result = get(links, headers=headers, timeout=5).text
        for line in result:
            ip = findall("(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3}):(?:[\d]{1,5})", result)
            if ip:
                for x in ip:
                    with open(get_name, mode="a") as e:
                        e.write("{}\n".format(x))
                        e.close()


urls = ["http://www.aliveproxy.com/high-anonymity-proxy-list/", "http://www.aliveproxy.com/anonymous-proxy-list/",
		"http://www.aliveproxy.com/fastest-proxies/", "http://www.aliveproxy.com/us-proxy-list/", "http://www.aliveproxy.com/gb-proxy-list/",
		"http://www.aliveproxy.com/fr-proxy-list/", "http://www.aliveproxy.com/de-proxy-list/", "http://www.aliveproxy.com/jp-proxy-list/",
		"http://www.aliveproxy.com/ca-proxy-list/", "http://www.aliveproxy.com/ru-proxy-list/", "http://www.aliveproxy.com/proxy-list-port-80/",
		"http://www.aliveproxy.com/proxy-list-port-81/", "http://www.aliveproxy.com/proxy-list-port-3128/", "http://www.aliveproxy.com/proxy-list-port-8000/",
		"http://www.aliveproxy.com/proxy-list-port-8080/", "http://webanetlabs.net/publ/24", "http://www.proxz.com/proxy_list_high_anonymous_0.html",
		"http://www.proxz.com/proxy_list_anonymous_us_0.html", "http://www.proxz.com/proxy_list_uk_0.html", "http://www.proxz.com/proxy_list_ca_0.html",
		"http://www.proxz.com/proxy_list_cn_ssl_0.html", "http://www.proxz.com/proxy_list_jp_0.html", "http://www.proxz.com/proxy_list_fr_0.html",
		"http://www.proxz.com/proxy_list_port_std_0.html", "http://www.proxz.com/proxy_list_port_nonstd_0.html", "http://www.proxz.com/proxy_list_transparent_0.html",
		"http://www.proxylists.net/", "https://www.my-proxy.com/free-proxy-list.html","https://www.my-proxy.com/free-elite-proxy.html",
		"https://www.my-proxy.com/free-anonymous-proxy.html", "https://www.my-proxy.com/free-transparent-proxy.html","https://jffjdjkbfek.000webhostapp.com/proxy.txt",
		"https://proxyscrape.com/proxies/HTTP_Working_Proxies.txt", "https://cyber-hub.net/proxy/http.txt", "http://multiproxy.org/txt_all/proxy.txt", "http://www.proxylists.net/http_highanon.txt",
		"http://www.proxylists.net/http.txt", "http://rootjazz.com/proxies/proxies.txt", "http://twotux.tripod.com/Proxylist.txt", "http://freeproxy.ru/download/lists/goodproxy.txt",
		"http://freeproxy.ru/download/lists/goodproxy.txt", "http://fravia.2113.ch/proxitk3.txt", "http://alexa.lr2b.com/proxylist.txt", "http://promicom.by/tools/proxy/proxy.txt", "http://api.foxtools.ru/v2/Proxy.txt"]

bs = ["http://free-proxy-list.net/", "https://www.us-proxy.org/"]

def get_proxies():
    cleaner()
    global get_name
    get_name = input("{}Proxy File name {}-> {}".format(Fore.CYAN, Fore.RED, Fore.GREEN))
    print("{}Filename -> {}{}".format(Fore.CYAN, Fore.GREEN, get_name))
    print("{}Start Grabbing ...{}".format(Fore.YELLOW, Style.RESET_ALL))
    for x in urls:
        t = Thread(target=get_prx, args=(x,)).start()
    t2 = Thread(target=get_prxv2, args=("https://proxylistdaily4you.blogspot.com/", "post-body entry-content", "div")).start()
    t3 = Thread(target=get_prxv2, args=("http://www.proxyserverlist24.top/", "post-title entry-title", "h3")).start()
    for _x in bs:
        t4 = Thread(target=get_prxbs, args=(_x,))

def check_proxies(proxy):
    try:
        r = get("https://google.com", proxies={"http": proxy}, headers=headers, timeout=5)
        if r.status_code == 200:
            with open("Good-Proxy.txt", mode="a") as e:
                e.write("{}\n".format(proxy))
                e.close()
            print("{}[{}+{}] {}{} {}-> {}oK ".format(Fore.YELLOW, Fore.RED, Fore.YELLOW, Fore.CYAN, proxy, Fore.GREEN, Fore.RED))
        else:
            print("{}[{}+{}] {}{} {}-> {}nO ".format(Fore.YELLOW, Fore.RED, Fore.YELLOW, Fore.CYAN, proxy, Fore.GREEN, Fore.RED))
    except:
        print("{}[{}+{}] {}{} {}-> {}nO ".format(Fore.YELLOW, Fore.RED, Fore.YELLOW, Fore.CYAN, proxy, Fore.GREEN, Fore.RED))


def check_p():
    get_name = input("{}Proxy File name {}-> {}".format(Fore.CYAN, Fore.RED, Fore.GREEN))
    print("{}Filename -> {}{}".format(Fore.CYAN, Fore.GREEN, get_name))
    with open(get_name, mode="r") as e:
        e = e.read().splitlines()
    for n in e:
        run_check = Thread(target=check_proxies, args=(n,)).start()

def main():
    cleaner()
    print("\t\t\t\t\t\t\t{}!{} Proxy Grabber v2.0 Wrote by iwHH <3 {}!".format(Fore.BLUE, Fore.CYAN, Fore.BLUE))
    print("\t\t\t\t\t\t\t{} github.com/iwhh/proxy {}- {}iran-cyber.NeT".format(Fore.GREEN, Fore.RED, Fore.MAGENTA))
    print("\t\t\t\t\t\t\t{} Telegram Username {}: {}@FireW4ll".format(Fore.MAGENTA, Fore.RED, Fore.CYAN))
    check_connection()
    print("\t{}[{}1-{}]{} Get ProxyList".format(Fore.RED, Fore.YELLOW, Fore.RED, Fore.BLUE))
    print("\t{}[{}2-{}]{} Check ProxyList".format(Fore.RED, Fore.YELLOW, Fore.RED, Fore.BLUE))
    print("\t{}[{}3-{}]{} Exit".format(Fore.RED, Fore.YELLOW, Fore.RED, Fore.BLUE))
    get_goc = int(input("\t{}$ {}{}".format(Fore.CYAN, Fore.MAGENTA, Style.RESET_ALL)))
    if get_goc == 1:
        get_proxies()
    elif get_goc == 2:
        check_p()
    else:
        print("{}GoodBye <3{}".format(Fore.GREEN, Style.RESET_ALL))
        exit(1)


if __name__ == "__main__":
    main()
