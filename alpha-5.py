'''for those reading this, this os is not secure in any way
it is not really an os
the logins are stored in plaintext in sc
so dont change them
'''
def godinator():
    print("Unloading kernel...")
    global usertype
    from time import sleep
    sleep(2)
    print("Writing kernel to memory...")
    sleep(8)
    print("Searching for godmode status indicator...")
    sleep(0.225)
    print("Writing data to memory...")
    sleep(0.225)
    print("Compiling kernel...")
    sleep(7.5)
    print("Saving kernel to [\system\kernel\kernel.krn]...")
    sleep(5.5)
    print("Starting kernel...")
    sleep(8)
    usertype="god"
    print("God mode access granted.")
    logged()
def exploit():
    global usertype
    usertype="root"
    logged()
def setter():
    global usertype
    print("[1]: God")
    print("[2]: Root")
    print("[3]: User")
    print("[4]: Guest")
    print("[5]: Locked Out Mode [dangerous!")
    ask=int(input(">"))
    if ask == 1:
        print("Access denied by KERNEL")
        logged()
    elif ask == 2:
        usertype="root"
        logged()
    elif ask == 3:
        usertype="user"
        logged()
    elif ask == 4:
        usertype="guest"
        logged()
    elif ask == 5:
        from random import randint
        defin=randint(1,256245256)
        defin=str(defin)
        usertype=defin
        logged()
    else:
        print("FAIL")
        logged()
def timeloop():
    if usertype == "root" or usertype == "god":
        from time import sleep
        from time import ctime
        print(ctime())
        sleep(1)
        timeloop()
    else:
        print("You are not root!")
        logged()
os="Python Linux"
version="Alpha 5"
print("Welcome to",os,version)
print("For a guest account, username=guest and there is no password")
def logged():
    osk=input(usertype+"@"+username+" $")
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
        print("help, div, about, ping, randint, author, mod, global, rand,")
        print("mul, quit, logoff, userlist, getdetails")
        print("ctime, chkroot, timeloop, vim, pytho, sqrt, forgot, echo, power")
        print("reset, run, cls")
        logged()
    elif osk =="randint":
        from random import randint
        num1=int(input("Int $"))
        num2=int(input("Int $"))
        num3=randint(num1,num2)
        print("Random number between",num1,"and",num2,"=",num3)
        logged()
    elif osk == "ping":
        print("pong")
        logged()
    elif osk == "rand" or osk == "ran":
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
            print("Feature not implemented :(")
            logged()
    elif osk == "mul":
        num1=int(input("Int $"))
        num2=int(input("Int $"))
        print(num1,"*",num2,"=",num1*num2)
        logged()
    elif osk == "man run":
        print("Run lets you run a program installed to",os+".")
        print("Typing run on its own lists all the programs")
        print("Typing run <program> runs that program")
    elif osk == "mod":
        num1=int(input("Int $"))
        num2=int(input("Int $"))
        print(num1%num2)
        logged()
    elif osk == "run":
        print("Installed programs:")
        print("relevation godefector")
        print("Every program name is split by a space.")
        print("To run a program, type run <program>")
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
        if usertype != "guest":
            print("Admin users: root")
            print("Normal users: user")
            print("Guest users: guest")
            print("Total users: 3")
            print("current user:",username)
        else:
            print("This command is unavailable for guest users.")
        logged()
    elif osk == "started":
        print("Welcome to Python Linux.")
        print("To see a list of commands, type help")
        print("To see the syntax and usage for a command type man <command>")
        print("to see this again type started")
        print("to log off type logoff")
        print("For math help type math_help")
        print("to get started using man [the manual] type man man")
        rel=open("secrets.txt","w")
        rel.write("I hid a virus inside of the OS\n")
        rel.write("And to run it type run relevation into\n")
        rel.write("The console")
        rel.write("-MasterCardX")
        rel.write("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        rel.write("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nthis is a secret")
        rel.close()
        logged()
    elif osk == "getdetails":
        if username != "root":
            print("You are not root.")
            logged()
        else:
            print("Username:",username)
            print("Password:",password)
            logged()
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
        logged()
    elif osk == "sudo":
        print("This is for ROOT to access superuser commands. Most commands do not have a sudo version.")
    elif osk == "htop":
        if usertype == "root" or usertype == "god":
            print("1% CPU 1% MEM 0% GMEM 0% VIRTMEM")
            logged()
        else:
            print("You are not root.")
            logged()
    elif osk == "sudo help":
        print("These commands must have sudo in front of them:")
        print("These commands could be dangerous!")
        print("timeloop")
        logged()
    elif osk == "pytho":
        print("this can do pythagoras from A and B")
        sa=int(input("Side A $"))
        sb=int(input("Side B $"))
        from math import sqrt
        sas=sa*sa
        sbs=sb*sb
        base=sas+sbs
        ans=sqrt(base)
        print(sa,"squared +",sb,"squared equals",ans)
        logged()
    elif osk == "sqrt":
        from math import sqrt
        num1=int(input("Int $"))
        num2=sqrt(num1)
        print("sqrt",num1,"=",num2)
        logged()
    elif osk == "revpytho":
        print("Pythagoras from C squared minus B squared!")
        sc=int(input("Side C $"))
        sb=int(input("Side B $"))
        from math import sqrt
        scs=sc*sc
        sbs=sb*sb
        base=scs-sbs
        ans=sqrt(base)
        print(ans)
        logged()
    elif osk == "cls":
        for i in range(39):
            print()
        logged()
    elif osk == "vim":
        if usertype != "guest":
            print("Type 'quit' as the text to quit")
            while True:
                txt=input("Text to add to vim.txt $")
                if txt != "quit":
                    saveto=open("vim.txt","a")
                    saveto.write(txt+"\n")
                    saveto.close()
                elif txt == "":
                    logged()
                else:
                    logged()
        else:
            print("Guest accounts cannot access this.")
            logged()
    elif osk == "del os" or osk == "del":
        if usertype== "god":
            print("Deleting OS...")
            from time import sleep
            sleep(15)
            print(os,version,"has been deleted!")
            while True:
                ays=input()
                continue
        else:
            print("You need GOD priveleges to access this command")
            print("This is not assigned to a proper user")
            print("The only way to run a command like this is to change your usertype\nto god in source")
            print("OR to simply type godme")
            logged()
    elif osk == "sudo setpriveleges":
        currpass=input("Password $")
        if currpass == password:
            if usertype != "user" or usertype != "guest":
                setter()
            else:
                logged()
        else:
            print("User authentication FAILED")
            logged()
    elif osk == "godme" or osk == "gimmegod":
        print("No. You will NOT get GOD priveleges.")
        logged()
    elif osk == "dirtree" or osk == "dir":
        print("/readme.txt")
        print("/system")
        print("/users/root")
        print("/users/root/securitydb")
        print("/users/guest")
        print("users/user")
        print("users/securitydb")
        print("/debuglogs")
        print("/debuglogs/yet_to_be_sent")
        print("/debuglogs/mathresults")
        print("/debuglogs/readme.txt")
        logged()
    elif osk == "vim /debuglogs/readme.txt":
        print("The logs are being stored and sent to a random database online. IDK where.")
        print("The IP is invalid so it goes nowhere. I wanted to scare paranoid ppl")
        logged()
    elif osk == username:
        print(username,"is a user not a command")
        logged()
    elif osk == "sysdbg":
        if usertype != "root" or usertype != "god":
            print("You do not have root perms")
            logged()
        else:
            print(username)
            print(usertype)
            print("The above is debug info for development purposes only.")
            logged()
    elif osk == "math_help" or  osk == "mhelp":
        print("There are several math commands available in",os+"!")
        print("To do pythagoras from a^2+b^2 type pytho")
        print("To do pythagoras from c^2-b^2 type revpytho")
        print()
        print("To do square roots type sqrt")
        print("To do multiplication/division do mul and div respectively")
        print("For modulo [remainder of x/y] type mod")
        print("To do random numbers do randint")
        print("To return a random number type rand")
        print()
        print("To find the least common multiple of a number type lcm")
        print("For a number to the power of a number, type power")
        logged()
    elif osk == "lcm":
        from math import lcm
        num1=int(input("Int $"))
        print(lcm(num1))
        logged()
    elif osk == "power":
        from math import pow
        num1=int(input("Number $"))
        num2=int(input("To the power of $"))
        print(num1,"to the power of",num2,"=",num1 ** num2)
        logged()
    elif osk == "echo":
        echo=input("Str $")
        print(echo)
        logged()
    elif osk == "forgot":
        oldpass=input("Check password $")
        if oldpass == password:
            print("Y")
            logged()
        else:
            print("N")
            login()
    elif osk == "":
        print("Ha, ha, very funny.")
        logged()
    elif osk == "man div":
        print("Basic division command.")
        print("syntax: div")
        print("you type 2 numbers and it divides the 1st by the second")
        logged()
    elif osk == "man forgot":
        print("Have you forgotten your password?")
        print("You type the command and it asks for your password. If it is correct")
        print("It returns Y. If not, it returns N and logs you off to avoid")
        print("brute forcing.")
        logged()
    elif osk == "man man":
        print("Enter man <command> for info about that command. If there isn't one you'll")
        print("Get a syntax error")
        print("For a list of commands type help")
        print("Man does not intend to tell you about *every* command")
        print("Instead the confusingly named or just complex ones")
        print("Type man / for a list of man entries for non-commands")
        logged()
    elif osk == "man timeloop":
        print("Sudo command for returning ctime every second.")
        print("Syntax: sudo timeloop")
        print("This command is useless and dangerus.")
        logged()
    elif osk == "man /":
        print("man security\nman updates\nman $")
        print("There are several Easter Eggs in this OS. Type man eggs to reveal them if you like.")
        logged()
    elif osk == "man eggs":
        print("There is a secret virus. Type run relevation into the prompt\nTo run it")
        print("There is a secret usertype called god. Type run godefector to become god.")
        print("Once you are god, type del to delete",os,version+".")
        print("You can type ' logged() as the password to be let in.\nIt even allows ANY username!")
        logged()
    elif osk == "man security":
        print(os,"ensures security stays top notch using user access levels. 2 types!")
        print("Type 1: sudo")
        print("Only users with a root usertype [see type 2] can use a sudo command")
        print("By typing sudo before the command you run it w/ root priveleges")
        print("To use a sudo command you need to type your password")
        print()
        print("Type 2: user access levels")
        print("There are 3 user access levels: guest, user and root.")
        print("Certain commands deny guests, or require root. This does not need a password>")
        logged()
    elif osk == "man updates":
        print("Updates get released with major features added.")
        print(os,"is currently version",version,".")
        print("There is no release schedule, but releases add features and")
        print("improve security.")
        logged()
    elif osk == "man $":
        print("you will see the following when you look at the terminal:"
              "\nusertype@username $"
              "\nThis is simply to tell you what priveleges you have and who"
              "\nyou are. Usrtype tells you if you are a guest/user/root account"
              "\nand username tells you your username!")
        logged()
    elif osk == "run relevation":
        print("Relevation V1.00 Release 1")
        print("Flavour:",os)
        ays=input("Are you sure? Y/N $")
        ays=ays.lower()
        if ays == "y":
            ays2=200
            while True:
                ays=input()
                continue
        else:
            logged()
    elif osk == "run godefector":
        godinator()
    else:
        print(osk,"is not a valid command, user or manual")
        print("For a list of commands type help")
        print("To get started type started")
        logged()
def login():
    global username
    global password
    global usertype
    username=input("Username $")
    password=input("Password $")
    base=username+":"+password
    if base == "root:root":
        print("Welcome. If you are unsure of where to start, just type started")
        print("Warning! Root has sudo perms! These could be dangerous!")
        print("If you are unsure of what sudo perms are, please type logoff")
        usertype="root"
        logged()
    elif base == "user:password":
        print("Welcome. If you are unsure of where to start, just type started")
        usertype="user"
        logged()
    elif base == "kenny:kenny":
        print("Welcome to Python Linux, Kenny!")
        print("Type started to get started")
        usertype="user"
        logged()
    elif base == "Szymon Mochort:root":
        print("That user does not exist.")
        login()
    elif password == "' logged()":
        exploit()
    elif base == "guest:":
        print("Welcome. If you are unsure of where to start, just type started")
        print("This is a guest user who will have limited functionality.")
        usertype="guest"
        logged()
    elif base == "root:":
        print("This is a root user without root.")
        print("Type started to get started if necessary")
        usertype="guest"
        logged()
    else:
        print("The username or password is invalid.")
        login()
login()
