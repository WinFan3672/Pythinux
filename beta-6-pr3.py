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

os,app_version,="Pythinux",[0,6,"PR3"]
autologin = 0
def rng(a,b):
    # Uses secrets to generate a random number for "true" randomness
    return choice(list(range(a,b+1)))
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
        print(f"")
        main()
    elif ch == "about":
        print(f"{upper(os)} v{app_version[0]}.{app_version[1]}.{app_version[2]}")
        main()
    elif ch == "logoff":
        login()
    elif ch == "ping":
        print("Pong")
        main()
    elif ch == "author":
        print(f"{os} was written by WinFan3672.")
        print(f"WinFan3672 is a British developer making stupid things like this.")
        div()
        print(f"To find out why WinFan3672 made this rewritten {os}, type REWRITE.")
        main()
    elif ch == "":
        main()
    elif ch == "rewrite":
        print(f"{os} was made in early 2022.")
        print(f"It was the first major project I ever worked on, while I was still learning the basics of Python.")
        print(f"One day, I decided to work on {os}, and the first thing I noticed was how messy my code was.")
        print(f"Compared to my modern code, it was a mess.")
        print(f"I knew a rewrite was in order.")
        print(f"I had already started rewriting my previous stuff, and decided to get on with it.")
        print(f"The rewrite will have a much better UI and code.")
        print(f"Hopefully, this isn't something I end up regretting :)")
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
def login():
    global username, password, user_lvl, user_type, autologin, data
    if autologin == 1:
        base="root:root"
        username,password="root","root"
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
        if base == f"{item[0]}:{item[1]}":
            start(int(item[2]))
    if base == "root:root":
        start(2)
    elif base == "guest:password":
        start(0)
    else:
        print("Username or password is invalid.")
        login()
login()
