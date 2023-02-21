def timeloop():
    if username == "root":
        from time import sleep
        from time import ctime
        print(ctime())
        sleep(1)
        timeloop()
    else:
        print("You are not root!")
        logged()
os="Python Linux"
version="Alpha 2"
print("Welcome to",os,version)
def logged():
    osk=input(username+" $")
    if osk == "about":
        print(os,version)
        logged()
    elif osk == "div":
        num1=int(input("Int $"))
        num2=int(input("Int $"))
        print(num1/num2)
        logged()
    elif osk == "help":
        print("For help on a particular command, enter man [command]")
        print("Dev note: man has not been added yet. Look in source!")
        print("help, div, about, ping, randint, author, mod, chngpass, rand, mul, quit, logoff, userlist, getdetails")
        print("ctime, chkroot, timeloop, vim")
        logged()
    elif osk =="randint":
        from random import randint
        num1=int(input("Int $"))
        num2=int(input("Int $"))
        num3=randint(num1,num2)
        print("Random number between",num1,"and",num2,"=",num3)
        logged()
    elif osk == "ping":
        print("Pong")
        logged()
    elif osk == "rand":
        from random import randint
        ans=randint(1,100000)
        print(ans)
        logged()
    elif osk == "chngpass":
        print("This change is NOT permanent.\nOnce you end this session, you will revert your password")
        oldpass=input("Old password $")
        if oldpass != password:
            print("Failed to authenticate user.")
            logged()
        else:
            print("this functionality is NOT available yet")
            logged()
    elif osk == "mul":
        num1=int(input("Int $"))
        num2=int(input("Int $"))
        print(num1,"*",num2,"=",num1*num2)
        logged()
    elif osk == "mod":
        num1=int(input("Int $"))
        num2=int(input("Int $"))
        print(num1%num2)
        logged()
    elif osk == "author":
        print(os,version,"was created by WinFan3672. (c)2022 WinFan3672.")
        logged()
    elif osk == "quit":
        quit()
    elif osk == "logoff":
        print("You have logged off.")
        login()
    elif osk == "osk":
        print("osk is a reserved variable not a command!")
        logged()
    elif osk == "userlist":
        print("Admin users: root")
        print("Normal users: user")
        print("Total users: 2")
        print("current user:",username)
        logged()
    elif osk == "started":
        print("Welcome to Python Linux.")
        print("To see a list of commands, type help")
        print("To see the syntax and usage for a command type man <command>")
        print("to see this again type started")
        print("to log off type logoff")
        logged()
    elif osk == "getdetails":
        if username != "root":
            print("You are not root.")
            logged()
        else:
            print("Username:",username)
            print("Password:",password)
    elif osk == "chkroot":
        if username =="root":
            print("Root=1")
            logged()
        else:
            print("Root=0")
            logged()
    elif osk == "ctime":
        from time import ctime
        print(ctime())
    elif osk == "timeloop":
        print("Error! You must access this command using sudo!")
        print("type: sudo timeloop")
        logged()
    elif osk == "sudo timeloop":
        print("Warning! This command cannot be exited from! To cancel, get your password wrong!")
        chkpass=input("Password $")
        if chkpass == password:
            timeloop()
        else:
            print("Wrong password.")
    elif "man" in osk:
        print("man has not been implemented")
        logged()
    elif osk == "sudo":
        print("This is for ROOT to access superuser commands. Most commands do not have a sudo version.")
    elif osk == "htop":
        if username == "root":
            print("1% CPU 1% MEM 0% GMEM 0% VIRTMEM")
            logged()
        else:
            print("You are not root.")
            logged()
    elif osk == "sudo help":
        print("These commands must have sudo in front of them:")
        print("These commands could be dangerous!")
        print("timeloop")
    elif osk == "vim":
        txt=input("Text to add to vim.txt $")
        saveto=open("vim.txt","a")
        saveto.write(txt+"\n")
        saveto.close()
        logged()
    else:
        print(osk,"is not a valid command")
        logged()
def login():
    global username
    global password
    username=input("Username $")
    password=input("Password $")
    base=username+":"+password
    if base == "root:root":
        print("Welcome. If you are unsure of where to start, just type started")
        print("Warning! Root has sudo perms! These could be dangerous!")
        print("If you are unsure of what sudo perms are, please type logoff")
        logged()
    elif base == "user:password":
        print("Welcome. If you are unsure of where to start, just type started")
        logged()
    else:
        print("The username or password is invalid.")
        login()

login()
