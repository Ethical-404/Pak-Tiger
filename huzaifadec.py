# uncompyle6 version 3.7.4
# Python bytecode 2.7
# Decompiled from: Python 2.7.18 (default, Mar 20 2021, 14:58:25)
# [GCC 4.2.1 Compatible Android (6454773 based on r365631c2) Clang 9.0.8 (https:/
# Embedded file name: Sumarr ID
import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, getpass
os.system('rm -rf .txt')
for n in range(9999):
    nmbr = random.randint(1111111, 9999999)
    sys.stdout = open('.txt', 'a')
    print nmbr
    sys.stdout.flush()

try:
    import requests
except ImportError:
    os.system('pip2 install requests')

try:
    import mechanize
except ImportError:
    os.system('pip2 install mechanize')
    time.sleep(1)
    os.system('python2 nmbr.py')

import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, requests, mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('user-agent', 'Mozilla/5.0 (Linux; Android 7.0; BAH-W09 Build/HUAWEIBAH-W09; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/63.0.3239.111 Safari/537.36 [FB_IAB/FB4A;FBAV/154.0.0.29.385;]')]
br.addheaders = [('user-agent', 'Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]')]
br.addheaders = [('user-agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0; KTXN B661094629A90240T1390849P1) like Gecko')]
br.addheaders = [('user-agent', 'Mozilla/5.0 (Linux; Android 8.0.0; STF-L09 Build/HUAWEISTF-L09; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/65.0.3325.109 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/169.0.0.46.94;]')]
br.addheaders = [('user-agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0; KTXN B667897245A77460T1297416P1) like Gecko')]
br.addheaders = [('user-agent', 'Mozilla/5.0 (Linux; Android 6.0.1; SM-J106H Build/MMB29Q; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/64.0.3282.137 Mobile Safari/537.36 SamsungBrowser/CrossApp/0.1.90')]
br.addheaders = [('user-agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0; KTXN B673272004A48129T1390849P1) like Gecko')]
br.addheaders = [('user-agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36 Mailbird/2.5.8.0/ Mailbird/2.5.8.0/')]
br.addheaders = [('user-agent', 'Millennium/20180228 CFNetwork/811.4.18 Darwin/16.5.0')]
br.addheaders = [('user-agent', 'Mozilla/5.0 (Linux; Android 7.0; VFD 610 Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/56.0.2924.87 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/162.0.0.45.94;]')]
br.addheaders = [('user-agent', 'Mozilla/5.0 (Linux; Android 5.0.2; VF-1497 Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Safari/537.36')]
br.addheaders = [('user-agent', 'Mozilla/5.0 (Linux; Android 7.0; BAH-W09 Build/HUAWEIBAH-W09; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/63.0.3239.111 Safari/537.36 [FB_IAB/FB4A;FBAV/154.0.0.29.385;]')]

def keluar():
    print '[!] EXIT!'
    print '[!] THANK YOU!'
    os.sys.exit()


def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!' + w[random.randint(0, len(w) - 1)] + i

    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x = x.replace('!%s' % i, '\x1b[%s;1m' % str(31 + j))

    x += '\x1b[0m'
    x = x.replace('!0', '\x1b[0m')
    sys.stdout.write(x + '\n')


def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.1)


B = '\x1b[0;94m'
R = '\x1b[1;91m'
G = '\x1b[1;92m'
W = '\x1b[1;97m'
S = '\x1b[1;96m'
P = '\x1b[1;95m'
Y = '\x1b[1;93m'
logo = '\n\x1b[1;33m ___  ____ _  _  \x1b[1;32m ____ ____ ____ ____ _  _\n\x1b[1;33m |__] |__| |_/   \x1b[1;32m |    |__/ |__| |    |_/\n\x1b[1;33m |    |  | | \\_  \x1b[1;32m |___ |  \\ |  | |___ | \\_\n\x1b[1;31m\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97\n\x1b[1;31m\xe2\x95\x91   \x1b[1;32mDEVELPOR  \x1b[1;31m:  \x1b[1;33mHUZAIFA BALOCH                  \x1b[1;31m\xe2\x95\x91\n\x1b[1;31m\xe2\x95\x91   \x1b[1;32mWHATSAPP  \x1b[1;31m:  \x1b[1;33m03087584706                     \x1b[1;31m\xe2\x95\x91\n\x1b[1;31m\xe2\x95\x91   \x1b[1;32mFACEBOOK  \x1b[1;31m:  \x1b[1;33mhttps://Facebook.com/HuXaifa.Xo \x1b[1;31m\xe2\x95\x91\n\x1b[1;31m\xe2\x95\x91   \x1b[1;32mGIT HUB   \x1b[1;31m:  \x1b[1;33mhttps://github.com/HuXaifa-Xo   \x1b[1;31m\xe2\x95\x91\n\x1b[1;31m\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d'

def tlogin():
    os.system('clear')
    print logo
    username = raw_input('\x1b[1;31m[+] \x1b[1;32mTOOL USERNAME :\x1b[1;33m ')
    if username == 'Huzaifa':
        os.system('clear')
        print logo
        print '\x1b[1;31m[\xe2\x9c\x93] \x1b[1;32mTOOL USERNAME :\x1b[1;33m ' + username + ' \x1b[1;34m(correct)'
    else:
        print '[!] Invalid Username.'
        time.sleep(1)
        tlogin()
    passw = raw_input('\x1b[1;31m[+] \x1b[1;32mTOOL PASSWORD :\x1b[1;33m ')
    if passw == 'Huzaifa':
        os.system('clear')
        print logo
        print '\x1b[1;31m[\xe2\x9c\x93] \x1b[1;32mTOOL USERNAME : \x1b[1;33m' + username + ' \x1b[1;34m(correct)'
        print '\x1b[1;31m[\xe2\x9c\x93] \x1b[1;32mTOOL PASSWORD : \x1b[1;33m' + passw + ' \x1b[1;34m(correct)'
        jalan('[!] \x1b[1;92mLOGIN APPROVED BY HUZAIFA BALOCH')
        time.sleep(2)
        os.system('python2 .README.md')
    else:
        print '\x1b[1;37m[!] Invalid Password'
        os.system('xdg-open https://Facebook.com/HuXaifa-Xo')
        time.sleep(1)
        tlogin()


if __name__ == '__main__':
    tlogin()
