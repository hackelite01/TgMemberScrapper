# -*- coding: utf-8 -*-
#!/bin/env python3
# Modified by @hackelite01
# Telegram Group: http://t.me/hackelite
# Please give me credits if you use any codes from here.


import os, sys
import configparser
re="\033[1;31m"
gr="\033[1;32m"
cy="\033[1;36m"
def banner():
	os.system('clear')
	print(f"""
	{re}╔═╗{cy}┌─┐┌┬┐┬ ┬┌─┐
	{re}╚═╗{cy}├┤  │ │ │├─┘
	{re}╚═╝{cy}└─┘ ┴ └─┘┴   v1.2
	""")
banner()
print(gr+"[+] Installing requierments ...")
os.system('python3 -m pip install telethon')
os.system('pip3 install telethon')
banner()
os.system("touch config.data")
cpass = configparser.RawConfigParser()
cpass.add_section('cred')
xid = input(gr+"[+] Enter API ID : "4140714")
cpass.set('cred', 'id', xid)
xhash = input(gr+"[+] Enter Hash : "7ceb347fba5ab20a59e7670203c4747c")
cpass.set('cred', 'hash', xhash)
xphone = input(gr+"[+] Enter Phone Number: "+r94764841864")
cpass.set('cred', 'phone', xphone)
setup = open('config.data', 'w')
cpass.write(setup)
setup.close()
print(gr+"[+] Setup complete!")
print(gr+"[+] Now you can run any tool!")
print(gr+"[+] Make sure to read README.md before using this tool.")
print(gr+"[+] https://github.com/hackelite01/TgMemberScrapper/blob/master/README.md")
print("\033[92m[+] Telegram Group: \033[96mhttp://t.me/hackelite01\033[0m")
