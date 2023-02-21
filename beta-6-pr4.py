global data
try:
    f=open("userlist.pythinux","r")
    data=f.read()
    f.close()
    data=data.split("/")
    data2=[]
    for item in data:
        data2.append(item.split("|"))
    data=data2
    data2=[]
    for item in data:
        if len(item) == 3:
            data2.append(item)
    data=data2
except:
    f=open("userlist.pythinux","w")
    f.write("root|root|2/guest|password|0")
    f.close()
global os, app_version, autologin
global username, password, user_lvl, user_type, user_type
import getpass
from time import ctime, strftime, sleep
import os
from secrets import choice

os,app_version,="Pythinux",[0,6,"PR4"]
autologin = 1
def debug_menu():
    div()
    print("[0] Return")
    print("[1] Crash")
    print("[2] Custom Crash")
    print("[3] Crashloop")
    print("[4] Custom Crashloop")
    print("[5] Custom AutoUser")
    div()
    try:
        ch=int(input(">"))
    except:
        main()
    if ch == 1:
        crash()
    elif ch == 2:
        crash(upper(input("Reason $")),upper(input("Subreason $")))
    elif ch == 3:
        crash("CRASH","GENERIC_CRASH",1)
    elif ch == 4:
        crash(upper(input("Reason $")),upper(input("Subreason $")),1)
    elif ch == 5:
        autologin = 1
        login(1,input("Username $"),input("Password $"))
    else:
        main()
def crash(reason="CRASH",subreason="GENERIC_CRASH",crash_loop=0):
    if crash_loop == 1:
        div()
        print("CRASH")
        div()
        print(f"The fatal error occured and {os} was forced to terminate itself in order to protect the hardware and software from irreversible damage.")
        div()
        print(f"{reason}:{subreason}")
        try:
            ch=input("Restart? Y/N $")
        except:
            sleep(2.5)
            crash(reason,subreason,1)
        sleep(2.5)
        crash(reason,subreason,1)
    else:
        div()
        print("CRASH")
        div()
        print(f"The fatal error occured and {os} was forced to terminate itself in order to protect the hardware and software from irreversible damage.")
        div()
        print(f"{reason}:{subreason}")
        try:
            ch=input("Restart? Y/N $")
        except:
            crash(reason,subreason)
        if lower(ch) != "n":
            sleep(2.5)
            login()
        else:
            crash(reason, subreason)
def is_god():
    global user_lvl
    if user_lvl >= 3:
        return True
    else:
        return False
def rng(a,b):
    # Uses secrets to generate a random number for "true" randomness
    return choice(list(range(a,b+1)))
def auth():
    div()
    print("AUTHENTICATION")
    div()
    global password
    newpass=getpass.getpass("Password $")
    if password == newpass:
        return True
    else:
        return False
def br():
    div()
    input("Press ENTER to continue.\n")
    return True
def is_root():
    global user_lvl
    if user_lvl >= 2:
        return True
    else:
        return False
def div():
    print("--------------------")
    return None
def upper(inp):
    if isinstance(inp,str) == True:
        return inp.upper()
    else:
        return "[UNDEFINED]"
def lower(inp):
    if isinstance(inp,str) == True:
        return inp.lower()
    else:
        return "[UNDEFINED]"
def godcheck():
    if user_lvl >= 3:
        print("God account detected.")
        return False
    else:
        return True
def main():
    global username, password, user_lvl, user_type
    godcheck()
    ch=lower(input(f"{user_type}@{username} $"))
    if ch == "help":
        print(f"This build of {os} is rewritten from the ground up, and has fewer commands. Trust me, this is for the best.")
        div()
        print(f"Command list:\nabout help logoff author rewrite mul rand rng time cls")
        print(f"echo started div add sub stopwatch timer getdetails bytegen chkroot")
        print(f"quit forgot power sysinfo")
        main()
    elif ch == "about":
        div()
        print(f"{upper(os)} v{app_version[0]}.{app_version[1]}.{app_version[2]}")
        div()
        print(f"{os} is (c) 2022 WinFan3672, some rights reserved.")
        print(f"{os} is distributed under the MIT license, a flexible license\nthat gives full control over source code and no warranty.")
        div()
        main()
    elif ch == "logoff":
        login()
    elif ch == "ping":
        print("Pong")
        main()
    elif ch == "author":
        div()
        print(f"{os} was written by WinFan3672.")
        print(f"WinFan3672 is a British developer making stupid things like this.")
        div()
        print(f"To find out why WinFan3672 made this rewritten {os}, type REWRITE.")
        main()
    elif ch == "":
        main()
    elif ch == "rewrite":
        div()
        print(f"{os} was made in early 2022.")
        print(f"It was the first major project I ever worked on, while I was still learning the basics of Python.")
        print(f"One day, I decided to work on {os}, and the first thing I noticed was how messy my code was.")
        print(f"Compared to my modern code, it was a mess.")
        print(f"I knew a rewrite was in order.")
        print(f"I had already started rewriting my previous stuff, and decided to get on with it.")
        print(f"The rewrite will have a much better UI and code.")
        print(f"Hopefully, this isn't something I end up regretting :)")
        br()
        main()
    elif ch == "mul":
        print("Syntax:")
        print("mul [int] [int]")
        main()
    elif "mul " in ch:
        try:
            ch=ch.split(" ")
            if len(ch) == 3:
                try:
                    print(int(ch[1])*int(ch[2]))
                except:
                    print("Invalid use of command.")
                    print("Correct use: mul [int] [int]")
            else:
                print("MUL requires [2] parameters, and [2] parameters only.")
        except:
            print("Invalid use of command.")
            print("Correct use: mul [int] [int]")
            main()
        main()
    elif ch == "time":
        print(strftime("%x %X"))
        main()
    elif ch == "rand":
        print(rng(100000,1000000))
        main()
    elif ch == "rng":
        print("RNG generates a random number from [1st parameter] to [2nd parameter]")
        div()
        print("Correct syntax:")
        print("rng [int] [int]")
        main()
    elif "rng " in ch:
        ch=ch.split(" ")
        if len(ch) == 3:
            try:
                print(rng(int(ch[1]),int(ch[2])))
            except:
                print("Only INT numbers are accepted.")
                main()
        else:
            base=[]
            for item in ch:
                if item != "":
                    base.append(item)
            ch=base
            print(f"RNG requires [2] parameters, got [{len(ch)-1}].")
        main()
    elif ch == "cls":
        for i in range(39):
            print()
        main()
    elif "echo " in ch:
        print(ch[5:])
        main()
    elif ch == "echo":
        print("echo <str>")
        main()
    elif ch == "started":
        div()
        print("GETTING STARTED GUIDE")
        div()
        print("In order to enter a list of commands, type HELP.")
        print("In order to log off, type LOGOFF.")
        main()
    elif ch == "div":
        print("Correct syntax:")
        print("div [int] [int]")
        main()
    elif "div " in ch:
        ch=ch.split(" ")
        if len(ch) == 3:
            try:
                print(int(int(ch[1])/int(ch[2])) if int(ch[1]) % int(ch[2]) == 0 else int(ch[1])/int(ch[2]))
            except:
                print("Incorrect syntax.")
        else:
            base=[]
            for item in ch:
                if item != "":
                    base.append(item)
            ch=base
            print(f"RNG requires [2] parameters, got [{len(ch)-1}].")
        main()
    elif ch == "add":
        print("Correct syntax:")
        print("add [int] [int]")
        main()
    elif "add " in ch:
        ch=ch.split(" ")
        if len(ch) == 3:
            try:
                print(int(ch[1])+int(ch[2]))
            except:
                print("Incorrect syntax.")
        else:
            base=[]
            for item in ch:
                if item != "":
                    base.append(item)
            ch=base
            print(f"RNG requires [2] parameters, got [{len(ch)-1}].")
        main()
    elif ch == "sub":
        print("Correct syntax:")
        print("sub [int] [int]")
        main()
    elif "sub " in ch:
        ch=ch.split(" ")
        if len(ch) == 3:
            try:
                print(int(ch[1])-int(ch[2]))
            except:
                print("Incorrect syntax.")
        else:
            base=[]
            for item in ch:
                if item != "":
                    base.append(item)
            ch=base
            print(f"RNG requires [2] parameters, got [{len(ch)-1}].")
        main()
    elif ch == "timer":
        print("Correct syntax:")
        print("timer [seconds(int)]")
        main()
    elif "timer " in ch:
        ch=int(ch[6:])
        while ch > 0:
            print(ch)
            sleep(1)
            ch -= 1
        main()
    elif ch == "stopwatch":
        print("[Press CTRL+C To Exit]")
        i = 1
        try:
            while True:
                print(i)
                i += 1
                sleep(1)
        except:
            main()
    elif ch == "getdetails":
        if is_root() == True:
            print(f"Username: {username}")
            newpass=""
            for item in password:
                newpass+="*"
            print(f"Password: {newpass}")
            main()
        else:
            print("You need to be root to access this command.")
            main()
    elif ch == "bytegen":
        print("Correct syntax:")
        print("bytegen [number of bytes (int)]")
        main()
    elif "bytegen " in ch:
        ch=ch.split(" ")
        if len(ch) == 2:
            try:
                for i in range(int(ch[1])):
                    print(f"{rng(0,1)} {rng(0,1)} {rng(0,1)} {rng(0,1)} {rng(0,1)} {rng(0,1)} {rng(0,1)} {rng(0,1)}")
            except:
                print("An error occured.")
                main()
        else:
            base=[]
            for item in ch:
                if item != "":
                    base.append(item)
            ch=base
            print(f"BYTEGEN requires [2] parameters, got [{len(ch)-1}].")
        main()
    elif ch == "chkroot":
        print(is_root())
        main()
    elif ch == "quit":
        import sys
        sys.exit()
    elif ch == "forgot":
        print("Warning! This tool will ask you for your password.")
        print("If you enter it wrong, you will be logged out.")
        print("By using this utility, you agree to this.")
        div()
        print("[1] Enter Tool")
        print("[0] Return")
        div()
        try:
            ch=int(input(">"))
        except:
            main()
        if ch == 1:
            if auth() == True:
                main()
            else:
                login()
        else:
            main()
    elif ch == "power":
        print("power [num1] [num2]")
        print("Outputs [num1] to the power of [num2]")
    elif "power " in ch:
        ch=ch.split(" ")
        if len(ch) == 3:
            try:
                print(str("{:,}".format(float(ch[1]) ** float(ch[2]))))
            except:
                print("ERROR.")
        else:
            base=[]
            for item in ch:
                if item != "":
                    base.append(item)
            ch=base
            print(f"POWER requires [2] parameters, got [{len(ch)-1}].")
        main()
    elif ch == "sysinfo":
        import platform
        print(platform.system(),platform.uname()[2])
        print("OS:",platform.platform())
        try:
            import tkinter as tk
            root = tk.Tk()
        except:
            root = "N/A"
        try:
            screen_width = root.winfo_screenwidth()
            screen_height = root.winfo_screenheight()
        except:
            screen_width = "N/A"
            screen_height = "N/A"
        try:
            root.withdraw()
        except:
            pass
        print("Screen width:",screen_width)
        print("Screen height:",screen_height)
        import sys
        v=platform.python_version()
        print("Python",v)
        th=platform.architecture()
        th=th[0]
        print("Architecture=",th)
        cpu=platform.processor()
        print("CPU:",cpu)
        br()
        main()
    elif ch == "debug" or ch == "root":
        if is_root() == True and auth() == True:
            debug_menu()
        else:
            div()
            print("An error occured:")
            print("[-] You are not a ROOT user")
            print("OR:")
            print("[-] You enter an incorrect password.")
            div()
            main()
    else:
        print(f"{upper(ch)} IS NOT A VALID COMMAND, PROGRAM OR MANUAL.")
        main()
        
def start(lvl):
    global username, password, user_lvl, user_type
    user_lvl = lvl
    if user_lvl == 0:
        user_type="guest"
    elif user_lvl == 1:
        user_type = "user"
    elif user_lvl == 2:
        user_type = "root"
    elif user_lvl == 3:
        user_type = "god"
    else:
        user_type="[INVALIDUSER]"
    print(f"Welcome to {os}.")
    print(f"[{os} v{app_version[0]}.{app_version[1]}.{app_version[2]}]")
    div()
    if user_lvl == 0:
        print("You are logged in on a guest account.")
        print("Guest accounts have limited access to commands and cannot run programs.")
    elif user_lvl == 1:
        pass
    elif user_lvl == 2:
        print("You are logged in as a root account.")
        print("If you do not know what this means, type LOGOUT right now.")
        print("DO NOT USE A ROOT ACCOUNT AS YOUR DAILY DRIVER ACCOUNT.")
    elif user_lvl == 3:
        pass
    else:
        print("[Error: The account type is invalid.]")
        login()
    main()
def login(al=0,al_username="root",al_password="root"):
    global username, password, user_lvl, user_type, autologin, data
    if al == 1:
        base=f"{al_username}:{al_password}"
        username,password=f"{al_username}",f"{al_password}"
        autologin = 0
    else:
        div()
        print(f"{upper(os)} LOGIN SYSTEM")
        div()
        print("Enter your login details.")
        print("If they are valid, you will be logged in.")
        div()
        print("Username = guest\nPassword = password\nFor a guest account")
        div()
        username=input("Username $")
        password=getpass.getpass("Password $")
        div()
        base=f"{username}:{password}"
    for item in data:
        try:
            if base == f"{item[0]}:{item[1]}":
                start(int(item[2]))
        except:
            continue
    if base == "root:root":
        start(2)
    elif base == "guest:password":
        start(0)
    else:
        print("Username or password is invalid.")
        login()
login(autologin)
