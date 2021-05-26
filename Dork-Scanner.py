#!/usr/bin/env/python3
# This Python file uses the following encoding: utf-8



# ===== #
# Created April | Copyright (c) 2021 Sqwares
# ===== #

########################################################################

# A notice to all nerds and Sqwares...
# If you will copy the developer's work it will not make you a hacker..!
# Respect all developers, we doing this because it's fun Türkceye Cevirdim Yanlıs Anlamayın .d...

########################################################################


from __future__ import print_function
try:
    from googlesearch import search

except ImportError:
    print("")

import sys
import time


# Sqwares Scanner v1.0


if sys.version[0] in "2":
    print ("\n[x] .... Sqwares Scanner  Is Not Supported For python 2.x Use Python 3.x \n")
    print ("\n\n\tSqwares Scanner \033[1;91mI like to See Ya, Hacking \033[0m😃\n\n")
    exit()


class colors:
    CRED2 = "\33[91m"
    CBLUE2 = "\33[94m"
    ENDC = "\033[0m"


banner = ("""
  ██████   █████   █     █░ ▄▄▄       ██▀███  ▓█████   ██████ 
▒██    ▒ ▒██▓  ██▒▓█░ █ ░█░▒████▄    ▓██ ▒ ██▒▓█   ▀ ▒██    ▒ 
░ ▓██▄   ▒██▒  ██░▒█░ █ ░█ ▒██  ▀█▄  ▓██ ░▄█ ▒▒███   ░ ▓██▄   
  ▒   ██▒░██  █▀ ░░█░ █ ░█ ░██▄▄▄▄██ ▒██▀▀█▄  ▒▓█  ▄   ▒   ██▒
▒██████▒▒░▒███▒█▄ ░░██▒██▓  ▓█   ▓██▒░██▓ ▒██▒░▒████▒▒██████▒▒
▒ ▒▓▒ ▒ ░░░ ▒▒░ ▒ ░ ▓░▒ ▒   ▒▒   ▓▒█░░ ▒▓ ░▒▓░░░ ▒░ ░▒ ▒▓▒ ▒ ░
░ ░▒  ░ ░ ░ ▒░  ░   ▒ ░ ░    ▒   ▒▒ ░  ░▒ ░ ▒░ ░ ░  ░░ ░▒  ░ ░
░  ░  ░     ░   ░   ░   ░    ░   ▒     ░░   ░    ░   ░  ░  ░  
      ░      ░        ░          ░  ░   ░        ░  ░      ░  v1.0 """)


for col in banner:
    print(colors.CRED2 + col, end="")
    sys.stdout.flush()
    time.sleep(0.0025)

x = ("""
                Author:  Sqwares
                Github:  https://github.com/Sqwares \n """)
for col in x:
    print(colors.CBLUE2 + col, end="")
    sys.stdout.flush()
    time.sleep(0.0040)

y = "\n\t\tHi there, Shall we play a game..? 😃\n"
for col in y:
    print(colors.CRED2 + col, end="")
    sys.stdout.flush()
    time.sleep(0.0040)

z = "\n"
for col in z:
    print(colors.ENDC + col, end="")
    sys.stdout.flush()
    time.sleep(0.4)


try:
    data = input("\n[+] Çıktıyı Dosyaya Kaydetmek İster Misiniz? (Y/N) ").strip()
    l0g = ("")

except KeyboardInterrupt:
        print ("\n")
        print ("\033[1;91m[!] User Interruption Detected..!\033[0")
        time.sleep(0.5)
        print ("\n\n\t\033[1;91m[!] I like to See Ya, Hacking \033[0m😃\n\n")
        time.sleep(0.5)
        sys.exit(1)


def logger(data):
    file = open((l0g) + ".txt", "a")
    file.write(str(data))
    file.write("\n")
    file.close()


if data.startswith("y" or "Y"):
    l0g = input("[~] Dosyaya Bir Ad Verin: ")
    print ("\n" + "  " + "»" * 78 + "\n")
    logger(data)
else:
    print ("[!] Kaydedildi...")
    print ("\n" + "  " + "»" * 78 + "\n")


def dorks():
    try:
        dork = input("\n[+] Dorku Girin: ")
        amount = input("[+] Görüntülencek Web Sitelerinin Sayısını Girin : ")
        print ("\n ")

        requ = 0
        counter = 0

        for results in search(dork, tld="com", lang="en", num=int(amount), start=0, stop=None, pause=2):
            counter = counter + 1
            print ("[+] ", counter, results)
            time.sleep(0.1)
            requ += 1
            if requ >= int(amount):
                break

            data = (counter, results)

            logger(data)
            time.sleep(0.1)

    except KeyboardInterrupt:
            print ("\n")
            print ("\033[1;91m[!] Kullanıcı Kesintisi Algılandı..!\033[0")
            time.sleep(0.5)
            print ("\n\n\t\033[1;91m[!] I like to See Ya, Hacking \033[0m😃\n\n")
            time.sleep(0.5)
            sys.exit(1)

    print ("[•] Done... Exiting...")
    print ("\n\t\t\t\t\033[34mDorks Eye\033[0m")
    print ("\t\t\033[1;91m[!] İyi Hackler  \033[0m😃\n\n")
    sys.exit()


# =====# Main #===== #
if __name__ == "__main__":
    dorks()
