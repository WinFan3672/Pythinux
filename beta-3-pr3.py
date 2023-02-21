global mem
global bmem
mem=1
bmem=1 #backup mem used by mem command

###
global os,version
os="Pythinux"
version="Beta 3 [Prerelease 3]"
###
try:
    '''for those reading this, this os is not secure in any way
    it is not really an os
    most of the logins are stored in plaintext in sc
    and the rest are hashed so they might be secure idk
    so dont change them
    '''
    global crashloop
    global crashloop_r
    crashloop=0
    crashloop_r="NaN"

    from time import sleep
    print("Loading...")
    ##sleep(1.5)
    def man(manual):
        if manual == "/":
            print("To see a manual, type man <manual>")
            print("Each manual name is split using a space")
            print()
            print("updates $ man todo / sudo manlist")
            godcheck()
        elif manual == "updates":
            print("\nUpdates get released with major features added.")
            print(os,"is currently version",version,".")
            print()
            print("There is no release schedule, but releases add features and")
            print("improve security.")
            print()
            print("Press ENTER to continue.")
            wer=input()
            print()
            godcheck()
        elif manual == "%vim%":
            print("\nVIM future updates:")
            print("[1] Fix #2")
            print("[2]Allow the .vimx to change into anything by editing source")
            print("[3]Make it inside of a VIM > Backup / File folder!")
            print("\nAccess legacy vim by typing in vim_legacy")
            print("This is the old vim from beta 1 and earlier")
            print()
            print("Press ENTER to continue.")
            wer=input()
            print()
            godcheck()
        elif manual == "vim":
            print("\nVim is a text editor.")
            print("It uses a VIMX file format which is actually plaintext")
            print("Viewable in Notepad or other text editor.")
            print("It has no syntax.")
            print("Type vim to open it.")
            print("When you load it, you have 5 options")
            print()
            print("Press ENTER to continue.")
            fileformat=".vimx" #change this is u want a different format!
            backupformat="_backup.bak" #puts _backup on the end of filename
            #and sets a BAK file type
            wer=input()
            print()
            print("OPTION 1\n")
            print("This option allows you to create a new file, or load ")
            print("an existing one and add lines to it")
            print("1 line at a time")
            print("It lets you type the line and then adds it to the file.")
            print("Type CTRL+C to exit vim")
            print()
            print("Press ENTER to continue.")
            wer=input()
            print()
            print("Option 2\n")
            print("You can type in the name of a file and its contents will be displayed")
            print("Sadly, thanks to Python, there are a lot of line breaks that should not be there")
            print()
            print("Press ENTER to continue.")
            wer=input()
            print()
            print("Option 3\n")
            print("This allows you to empty a file by entering it in")
            print("The erase is not secure, but it does empty its contents")
            print()
            print("Press ENTER to continue.")
            wer=input()
            print()
            print("OPtion 4\n")
            print("This allows you to replace the ENTIRE text of a file.")
            print()
            print("Press ENTER to continue.")
            wer=input()
            print()
            print("The 5th option is to exit.")
            print("That's it. Rudimentary text editor.")
            print()
            print("Press ENTER to continue.")
            wer=input()
            print()
            godcheck()
        elif manual == "$":
            print("\nYou will see the following when you look at the terminal:"
                  "\nusertype@username $"
                  "\nThis is simply to tell you what priveleges you have and who"
                  "\nyou are. Usertype tells you if you are a guest/user/root account"
                  "\nand username tells you your username!")
            print()
            print("Press ENTER to continue.")
            wer=input()
            print()
            godcheck()
        elif manual == "man":
            print("\nEnter man <command> for info about that command. If there isn't one you'll")
            print("Get a syntax error")
            print("For a list of commands type help")
            print("Man does not intend to tell you about *every* command")
            print("Instead the confusingly named or just complex ones")
            print("Type man / for a list of pre-installed manuals")
            print()
            print("Press ENTER to continue.")
            wer=input()
            print()
            print("Every manual uses the following terms and symbols to explain syntax:")
            print()
            print("[type is not required]")
            print("<type is required>")
            print("int = integer = whole number")
            print("float = floating point number = number with decimal point optional")
            print("str = string = text")
            print("dir = directory = folder")
            print("file = file path = location of a file i.e:")
            print("\documents\mydocs\docs\moredocs\myfile.txt")
            print()
            print("Press ENTER to continue.")
            wer=input()
            print()
            print("Some example syntax:")
            print("command <int> [str] [dir]")
            print("Note: 99% of commands have NO syntax and look like this:")
            print("command")
            print()
            print("Press ENTER to continue.")
            wer=input()
            print()
            godcheck()
        elif manual == "todo":
            print("\nTo-do list for",os)
            print("[1] MEM variable for maths- allows you to save and load")
            print("float numbers in every math command. Type man %mem% for info")
            print("[2] Revamping help and UI")
            print("[3] Adding more math stuff")
            print("[4] Adding environment variables [see man %env_var%]")
            print("[5] Vim upgrade")
            print("[6] Overhaul bytegen")
            print("[7] Add files program [see %files%]")
            print("[8] Python editor")
            print()
            print("Press ENTER to continue.")
            wer=input()
            print()
            godcheck()
        elif manual == "%files%":
            print("\nUpcoming feature: Files")
            print("This allows for the user to use commands like cd and md")
            print("to make and edit files on their computer!")
            print("\nTo see a list of commands that I will add, go to %files_l%")
            print()
            print("Scheduled: Beta 4")
            print()
            print("Press ENTER to continue.")
            wer=input()
            print()
            godcheck()
        elif manual == "%files_l%":
            print("\ncd= change directory")
            print("You can change to a specific directory or a folder in the cwd")
            print("Supports both \\ and /")
            print("cwd=shows current working directory")
            print("C:/Windows/System32")
            print("md=create a folder")
            print("Folder TEST created.")
            print("vimx=convert a file to VIMX")
            print("Converted test.txt --> test.vimx")
            print("startpoint=return to initial directory")
            print("clear=clear a file's contents")
            print("del= delete a file")
            print("dir=list all files")
            print("safemode=disables all commands that write data")
            print("exit=exit files app")
            print()
            print("Press ENTER to continue.")
            wer=input()
            print()
            godcheck()
        elif manual == "%env_var%":
            print("\nUpcoming feature: Environment variables")
            print("Preinstalled software may have an environment variable")
            print("This is a set of up to 12 symbols it can use")
            print("When refering to manuals or parts of the program")
            print("For instance, Audacity could have á as an env_var")
            print("And audacity-related manuals and references")
            print("Would need it, such as the manual áaudacityá")
            print("You can have up to 12 characters!")
            print("EG: !£$%^&*()!£$")
            print("This would mean our manual ref would be !£$%^&*()!£$audacity!£$%^&*()!£$)")
            print()
            print("Scheduled: N/A")
            print()
            godcheck()
        elif manual == "sudo":
            print("\nSome commands require you to put sudo in front of them")
            print("For example:\nsudo timeloop")
            print("Sudo performs 2 checks before allowing")
            print("The command to run:")
            print("[1] The usertype is root")
            print("[2] You need to enter your password correctly")
            print()
            print("Press ENTER to continue.")
            wer=input()
            print()
            godcheck()
        elif manual == "manlist":
            print("\nThis is a list of all commands with a manual:")
            print("cls div forgot tens timeloop run")
            godcheck()
        elif manual == "%%":
            print("\nSome pre-installed manuals would like to be hidden from the preinstalled manual list")
            print("As a result, the man command has been updated to allow hidden manuals")
            print("The manual names must be wrapped in % symbols to be ignored, such as %mem%")
            print("This is useful for software that uses the",os,"API to call man to")
            print("display manuals")
            print()
            print("Press ENTER to continue.")
            wer=input()
            print()
            godcheck()
        elif manual == "%mem%":
            print("\nUpcoming feature: MEM")
            print("This is similar to the M function on most calculators")
            print()
            print("You can launch a math command using <math command> mem")
            print("and load mem into the command")
            print("For instance, sqrt mem would do the square root of the contents of mem")
            print()
            print("Scheduled: Beta 3")
            print()
            print("Current supported commands: sqrt")
            print()
            print("Press ENTER to continue.")
            wer=input()
            print()
            godcheck()
        elif manual == "tens":
            print("\nThis command multiplies a number by 10 a set number of times")
            print("Syntax:")
            print("tens")
            print()
            print("After you enter the command, you type in <int_1>, press ENTER")
            print("and type in <int_2>. <int_1> will be multiplied by 2 <int_2> times")
            print()
            print("Press ENTER to continue.")
            wer=input()
            print()
            godcheck()
        elif manual == "forgot":
            print("Have you forgotten your password?")
            print("You type the command and it asks for your password. If it is correct")
            print("It returns Y. If not, it returns N and logs you off to avoid")
            print("brute forcing.")
            godcheck()
        elif manual == "div":
            print("Basic division command.")
            print("syntax: div")
            print("you type 2 numbers and it divides the 1st by the second")
            godcheck()
        elif manual == "cls":
            print("Syntax:")
            print("cls [int]")
            godcheck()
        elif manual == "timeloop":
            print("Sudo command for returning ctime every second.")
            print("Syntax: sudo timeloop")
            print("This command is useless.")
            godcheck()
        elif manual == "run":
            print("Run lets you run a program installed to",os+".")
            print("Typing run on its own lists all the programs")
            print("Typing run <program> runs that program")
            godcheck()
        else:
            print(manual,"is not a valid manual!")
            godcheck()
    def godcheck():
        if usertype=="god":
            crash("PRIVELEGE_ESCALATION","GOD")
            #this subroutine checks if your usertype is "god" and if it is, it'll crash your system.
            #this is done because the god usertype was meant to be a joke and unobtainable
            #so, the owner of the os found out it was obtainable and added safeguards.
        else:
            logged()

    def startsystem():
        global usertype, os, version
        global userlvl
        if usertype == "guest":
            userlvl=0
            print("Welcome to",os,version)
            print("Guest users have limited privleges.")
            print("Type started if you are unsure of how to start")
        elif usertype == "user":
            userlvl=1
            print("Welcome to",os,version)
            print("As a user, you have access to most system files, but not all.")
            print("Type started if you are unsure of how to start")
        elif usertype == "root":
            userlvl=2
            print("Welcome to",os,version)
            print("Root users have escalated priveleges")
            print("If you are unsure of what that is, type logoff")
            print("It is not safe to use root users as your main account")
            print("Type started if you are unsure of how to start")
        elif usertype == "god":
            userlvl=3
        else:
            godcheck()
        godcheck()
    def injector():
        print("General purpose injector.")
        print("[1] God mode")
        print("[2] Root mode")
        print("[3] Random Username")
        print("[4] Lock Out Mode")
        print("[5] Change Username")
        choice=int(input("$"))
        if choice == 5:
            usernamechange() # i need a sub because of an error grr
        elif choice == 1:
            godmodeme()
        elif choice == 2:
            exploit()
        elif choice == 3:
            global username
            from random import randint
            username=randint(1,1000000000)
            username=str(username)
            godcheck()
        elif choice == 4:
            global usertype
            usertype="locked-out-mode"
            godcheck()
        else:
            godcheck()

    def usernamechange():
        global username
        username=input("New Username $")
        godcheck()

    def chngpass():
        global password
        newpass=input("New password $")
        if newpass == password:
            godcheck()
        else:
            password=newpass
            godcheck()
            
    def godmodeme():
        global usertype
        global username
        from random import randint
        usertype="god"
        logged()
        
    def servermode():
        try:
            global bitcoin
            global servertype
            global update_speed
            #just pretends to be a resource manager and server.
            from time import sleep
            from random import randint
            if servertype == 9:
                cpu=randint(12,15)
            else:
                cpu=randint(44,100)
            ram=randint(33,67)
            if servertype==9:
                gpu=randint(98,100)
            else:
                gpu=randint(0,1)
            net=randint(89,100)
            net=str(net)
            cpu=str(cpu)
            ram=str(ram)
            gpu=str(gpu)
            #ints converted to strings to avoid issues with adding strings and integers
            if servertype == 9:
                print(bitcoin,"BTC")
                bitcoin=bitcoin+0.01
            print("CPU:",cpu+"% RAM:",ram+"% GPU:",gpu+"% NETWORK",net+"%")
            sleep(update_speed) #to "update" twice a second
            servermode()
        except KeyboardInterrupt:
            godcheck()
    def bootloop():
        from time import sleep
        sleep(1.5)
        try:
            while True:
                print("Loading...")
                sleep(2.5)
        except:
            bootloop()
    def server():
        global bitcoin
        bitcoin=0.1
        global update_speed
        #checks for correct usertype and password, asks for a server type and goes to servermode()
        #that way, debug can bypass all of this and launch the server directly
        global usertype
        global servertype
        if usertype != "root":
            print("Insufficient priveleges.")
            godcheck()
        else:
            global password
            try:
                testpass=input("Password $")
            except:
                godcheck()
            if testpass == password:
                print("[1] Web")
                print("[2]",os)
                print("[3] Minecraft")
                print("[4] Tor Node")
                print("[5] I2P Node")
                print("[6] Factorio")
                print("[7] Torrent Tracker")
                print("[8] Torrent Seeder")
                print("[9] Bitcoin Miner")
                print("[10] Urban VPN*")
                print("*I DO NOT ENDORSE OR RECOMMEND IT STAY FAR AWAY")
                try:
                    servertype=int(input("$"))
                except:
                    godcheck()
                print("Enter update speed [seconds]")
                try:
                    update_speed=float(input(">"))
                    if update_speed < 0.25:
                        update_speed=0.25
                    servermode()
                except KeyboardInterrupt:
                    godcheck()
                except:
                    update_speed=1
                    servermode()
            else:
                crash("SECURITY","FAILED_TO_AUTHENTICATE_PASSWORD")
    def blankpass():
        #this is used by the debug command to initiate a blank password crash (option 4)
        global password
        password=""
        godcheck()
    def doit():
        global usertype
        usertype="god"
        godcheck()
        #this sub sets your usertype as god and checks for god. this is for the debug cmd
        #since python will complain about "variable referenced before assignment" unless i make it inside a sub.
    def exitvs():
        quit()
    def crash(reason,subreason):
        try:
            global crashloop
            global crashloop_r
            #this crashes the os in the format OS:Subreason.
            print("A fatal exception occured and",os,"crashed.")
            print("Reason:",reason+":"+subreason)
            restart=input("Restart? Y/N $")
            restart=restart.lower()
            #if i make y and n lowercase it saves code since i do not have to do if statements for Y, N, y and n.
            #surely you know this, but I'm meant to explain why something is here.
            if restart == "y":
                from time import sleep
                sleep(1.5)
                #sleep emulates restarting os
                if crashloop == 1:
                    crash("CRASH",crashloop_r)
                else:
                    login()
            else:
                import sys
                sys.exit()
        except KeyboardInterrupt:
            crashloop=1
            crashloop_r="ATTEMPTEDESCAPE"
            crash("CRASH","ATTEMPTEDESCAPE")
    def godinator():
        modier=1.35
        #this is used as a way of slowing down the speed to make is seem
        #as if the OS kernel is more bloated
        #a personal touch ;)
        print("Unloading kernel...")
        global usertype
        from time import sleep
        sleep(2*modier)
        crash("KERNEL_MISSING_OR_CORRUPT","MISSING")
        print("Writing kernel to memory...")
        sleep(8*modier)
        print("Searching for godmode status indicator...")
        sleep(0.225*modier)
        print("Writing data to memory...")
        sleep(0.225*modier)
        print("Compiling kernel...")
        sleep(7.5*modier)
        print("Saving kernel to [\system\kernel\kernel.krn]...")
        sleep(5.5*modier)
        print("Starting kernel...")
        sleep(8*modier)
        usertype="god"
        print("God mode access granted.")
        godcheck()
    def exploit():
        #forces you to have root and does a godcheck.
        global usertype
        usertype="root"
        godcheck()
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
            godcheck()
        elif ask == 2:
            usertype="root"
            godcheck()
        elif ask == 3:
            usertype="user"
            godcheck()
        elif ask == 4:
            usertype="guest"
            godcheck()
        elif ask == 5:
            from random import randint
            defin=randint(1,256245256)
            defin=str(defin)
            usertype=defin
            godcheck()
        else:
            print("FAIL")
            godcheck()
    def timeloop():
        try:
            if usertype == "root" or usertype == "god":
                try:
                    delay=float(input("Enter Delay [seconds] >"))
                except:
                    delay=0.5
                from time import sleep
                from time import ctime
                while True:
                    print(ctime())
                    sleep(delay)
            else:
                print("You are not root!")
                godcheck()
        except KeyboardInterrupt:
            godcheck()
    print("Welcome to",os,version)
    print("For a guest account, username=guest and password=password")
    def logged():
        global mem
        global os, version
        global bmem
        global userlvl
        if password == "":
            crash("AUTHENTICATION_BYPASS","NO_PASSWORD_GOD_EXPLOIT")
            #the system immediately assumes that blank passwords = a god mode exploit. This kills the *secret* root account with no password.
        elif password == "' logged()":
            crash("EXPLOIT_PREVENTION","LOGIN_EXPLOIT")
            #an exploit that used to occur where typing ' logged() as the password logged you in as a root user, bypassing the user check.
            #it was patched in alpha 6 but protection against it was added for future-proofing
        osk=input(usertype+"@"+username+" $")
        if osk == "about":
            print(os,version)
            godcheck()
        elif osk == "div":
            num1=int(input("Int $"))
            num2=int(input("Int $"))
            print(num1/num2)
            godcheck()
        elif osk == "help":
            print("For help on a particular command, enter man [command]")
            print("help, div, about, ping, randint, author, mod, global, rand,")
            print("mul, quit, logoff, userlist, getdetails")
            print("ctime, chkroot, timeloop, vim, pytho, sqrt, forgot, echo, power")
            print("reset, run, cls, bytegen, date, time, stopwatch, timer, area,")
            print("circumference, tens")
            godcheck()
        elif osk =="randint":
            from random import randint
            num1=int(input("Int $"))
            num2=int(input("Int $"))
            num3=randint(num1,num2)
            print("Random number between",num1,"and",num2,"=",num3)
            godcheck()
        elif osk == "ping":
            print("pong")
            godcheck()
        elif osk == "date":
            from time import strftime
            time=strftime("%A %d %B %Y")
            print(time)
            godcheck()
        elif osk == "run bloop":
            bootloop()
        elif osk == "timer":
            timer=int(input("Time [seconds] >"))
            try:
                while timer > 0:
                    print(timer)
                    from time import sleep
                    sleep(1)
                    timer=timer-1
            except:
                godcheck()
            godcheck()
        elif osk == "stopwatch":
            timer=1
            print("Press CTRL+C to exit")
            try:
                while True:
                    print(timer)
                    timer=timer+1
                    from time import sleep
                    sleep(1)
            except:
                godcheck()
        elif osk == "time":
            from time import strftime
            time=strftime("%H:%M:%S")
            print(time)
            godcheck()
        elif osk == "manapi":
            man("YESY")
        elif osk == "rand" or osk == "ran":
            from random import randint
            ans=randint(1,100000)
            print(ans)
            godcheck()
        elif osk == "chngpass":
            print("This change is NOT permanent.\nOnce you end this session or log off, you will revert to your old password")
            oldpass=input("Old password $")
            if oldpass != password:
                print("Failed to authenticate user.")
                godcheck()
            else:
                chngpass()
        elif osk == "mul":
            num1=int(input("Int $"))
            num2=int(input("Int $"))
            print(num1,"*",num2,"=",num1*num2)
            godcheck()
        elif osk == "mod":
            num1=int(input("Int $"))
            num2=int(input("Int $"))
            print(num1%num2)
            godcheck()
        elif osk == "run godforcemode":
            print("Warning! This skips the godcheck, but you WILL crash if you're not careful")
            print("[1] Continue")
            print("[2] Exit")
            choice=int(input("$"))
            if choice == 1:
                godmodeme()
            else:
                godcheck()
        elif osk == "hang":
            hang=int(input("Seconds $"))
            from time import sleep
            sleep(hang)
            godcheck()
        elif osk == "run":
            print("Installed programs:")
            print("relevation godefector godforcemode injector subs gradeaundera")
            print("Every program name is split by a space.")
            print("To run a program, type run <program>")
            godcheck()
        elif osk == "run gradeaundera":
            print("AT ALLLLLLL!")
            godcheck()
        elif osk == "run run":
            global crashloop
            global crashloop_r
            crashloop=1
            crashloop_r="ATTEMPTED_OVERWRITE_VARIABLE"
            crash("CRASH","ATTEMPTED_OVERWRITE_VARIABLE")
        elif osk == "run crash":
            a=input("Enter Reason >")
            if a == "":
                a="CRASH"
            b=input("Enter subreason>")
            if b == "":
                b="GENERAL_EXCEPTION"
            crash(a,b)
        elif osk == "author":
            print(os,version,"was created by WinFan3672. (c)2022 WinFan3672,\nall rights reserved.")
            godcheck()
        elif osk == "run injector":
            injector()
        elif osk == "quit" or osk == "exit":
            quit()
        elif osk == "area":
            print("[1] Square")
            print("[2] Triangle")
            print("[3] Circle")
            choice=int(input(">"))
            if choice == 1:
                try:
                    length=float(input("Length >"))
                except:
                    length=12
                try:
                    width=float(input("Width >"))
                except:
                    width=length
                area=length*width
                if area % 1 == 0:
                    area=int(area)
                print("The square is",area,"units square.")
                godcheck()
            elif choice == 2:
                try:
                    length=float(input("Length >"))
                except:
                    length=12
                try:
                    width=float(input("Width >"))
                except:
                    width=length
                area=length*width
                area=area/2
                if area % 1 == 0:
                    area=int(area)
                print("The triangle is",area,"units square.")
                godcheck()
            elif choice == 3:
                from math import pi
                print("[1] From Radius")
                print("[2] From Diameter")
                choice=int(input(">"))
                if choice == 1:
                    try:
                        radius=float(input("Radius >"))
                    except:
                        radius=12
                    radius=radius*radius
                    area=pi*radius
                    print("Area:",area,"units squared")
                    godcheck()
                elif choice == 2:
                    try:
                        diameter=float(input("Diameter >"))
                    except:
                        diameter=12
                    radius=diameter/2
                    radius=radius*radius
                    area=pi*radius
                    print("Area:",area,"units squared")
                    godcheck()
                else:
                    godcheck()
            else:
                godcheck()
        elif osk == "logoff":
            print("You have logged off.")
            print()
            print("==========")
            print()
            login()
        elif osk == "osk" or osk ==  "oske" or osk == "logged" or osk == "youknowwhoiam" or osk == "reserved0707" or osk == "reserved0708" or osk == "\n" or osk == "\r\n" or osk == "\f" or osk == "%%":
            if osk == "%%":
                crashloop=1
                crashloop_r="%%"
            debug=osk
            debug=debug.upper()
            crash("RESERVED_VARIABLE",debug)
            godcheck()
        elif osk == "debug":
            print("[1]God mode")
            print("[2]Crash")
            print("[3]Kernel Panic")
            print("[4]Blank Password Crash")
            print("[5]Force Start Server")
            print("[6]Man API")
            choice=int(input(">"))
            if choice == 1:
                doit()
            elif choice == 2:
                crash("GENERIC_CRASH","GENERIC")
            elif choice == 3:
                crash("KERNEL_MISSING_OR_CORRUPT","MISSING")
            elif choice == 4:
                blankpass()
            elif choice == 5:
                servermode()
            elif choice == 6:
                man("TEST")
            else:
                godcheck()
        elif osk == "userlist":
            if userlvl >= 1:
                print("God Mode Users: Szymon Mochort")
                if userlvl >= 2:
                    print("Admin users: root")
                print("Normal users: user, ibxtoycat, testaccount1")
                print("Guest users: guest, root")
                print()
                print("current user:",username)
            else:
                print("This command is unavailable for guest users.")
            godcheck()
        elif osk == "started" or osk == "?":
            print()
            print("Welcome to",os+".")
            print()
            print(os,"is a 'Linux' distro that uses a")
            print("combination of DOS and Linux syntax.")
            print()
            print("To use a command, type it into the prompt.")
            print("All commands available are listed in the help")
            print("Command. To see this list, type help.")
            print()
            print("To see the actual info about each individual")
            print("Command, type man <command>, where <command> is")
            print("the command you want to execute.")
            print()
            print("Press ENTER to continue.")
            wer=input()
            print()
            print("There are several math commands available.")
            print("To see all you need to know about math in",os)
            print("type mhelp or math_help")
            print()
            print("Press ENTER to continue.")
            wer=input()
            print()
            print("General, useful commands:")
            print("To log out of your user, type logoff")
            print("For proper help on using the man command, type man man")
            print("To refer back to this guide, type started or ?")
            print()
            print("Press ENTER to continue.")
            wer=input()
            print()
            print("The man command has a lot of preinstalled manuals")
            print("To see these preinstalled manuals, type man /")
            print()
            print("Press ENTER to continue.")
            wer=input()
            print()
            print("Software:")
            print("Some preinstalled software exists on")
            print("your install of",os)
            print("To see a list type run")
            print("To run a program, type run <program>")

            print()
            print("Press ENTER to continue.")
            wer=input()
            print()
            
            rel=open("secrets.txt","w")
            rel.write("I hid a virus inside of the OS\n")
            rel.write("And to run it type run relevation into\n")
            rel.write("The console")
            rel.write("-MasterCardX")
            rel.write("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            rel.write("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nthis is a secret")
            rel.close()
            godcheck()
        elif "cls " in osk:
            lines=osk[4:]
            try:
                lines=int(lines)
            except:
                print("Syntax error.")
                print("Command syntax:")
                print("cls <int>")
                print("Your syntax:")
                print(osk)
                godcheck()
            for i in range (lines):
                print()
            godcheck()
        elif "man " in osk:
            manuale=osk[4:]
            man(manuale)
        elif osk == "mem":
            print("\nMEM:",mem)
            print("BMEM:",bmem)
            print("[1] Set MEM")
            print("[2] Reset MEM")
            print("[3] Backup MEM to BMEM + clear MEM")
            print("[4] Restore MEM using BMEM")
            print("[5] Reset BMEM")
            print("[6] Initialise ALL")
            print("Press ENTER to exit.\n")
            try:
                ans=int(input(">"))
                if ans == 1:
                    mem=int(input(">"))
                elif ans == 2:
                    mem=1
                elif ans == 3:
                    bmem=mem
                    mem=1
                elif ans == 4:
                    mem=bmem
                elif ans == 5:
                    bmem=1
                elif ans == 6:
                    mem=1
                    bmem=1
                else:
                    godcheck()
                godcheck()
            except:
                godcheck()
        elif osk == "getdetails":
            if userlvl < 2:
                print("Insufficient Priveleges")
                godcheck()
            else:
                print("Username:",username)
                hashes=len(password)
                hashes=str(hashes)
                hash_f="*"
                hash_fa=""
                theone=len(password)
                for i in range(theone):
                    hash_fa=hash_fa+hash_f
                print("Password:",hash_fa)
                godcheck()
        elif osk == "chkroot":
            if username =="root":
                print("Root=1")
                godcheck()
            else:
                print("Root=0")
                godcheck()
        elif osk == "ctime":
            from time import ctime
            print(ctime())
            godcheck()
        elif osk == "timeloop":
            print("To exit the command, press CTRL+C"
                  "\nOtherwise, the command runs forever")
            timeloop()
        elif osk == "sudo":
            print("This is for ROOT to access superuser commands. Most commands do not have a sudo version.")
            godcheck()
        elif osk == "bytegen":
            print("[1] print")
            print("[2] Save to bytegen.txt")
            print("[3] Save to [choice].txt")
            print("[4] Option 3 but as hex [EXPERIMENTAL]")
            print("[5] Export bytegen.txt to bytegen.vimx")
            try:
                choice = int(input(">"))
            except:
                godcheck()
            if choice == 1:
                bytes=int(input("How many bytes to generate $"))
                for i in range(bytes):
                    from random import randint
                    b1=randint(0,1)
                    b2=randint(0,1)
                    b3=randint(0,1)
                    b4=randint(0,1)
                    b5=randint(0,1)
                    b6=randint(0,1)
                    b7=randint(0,1)
                    b8=randint(0,1)
                    print(b1,b2,b3,b4,b5,b6,b7,b8)
                godcheck()
            elif choice == 2:
                bytes=int(input("How many bytes to generate $"))
                for i in range(bytes):
                    from random import randint
                    b1=randint(0,1)
                    b1=str(b1)
                    b2=randint(0,1)
                    b2=str(b2)
                    b3=randint(0,1)
                    b3=str(b3)
                    b4=randint(0,1)
                    b4=str(b4)
                    b5=randint(0,1)
                    b5=str(b5)
                    b6=randint(0,1)
                    b6=str(b6)
                    b7=randint(0,1)
                    b7=str(b7)
                    b8=randint(0,1)
                    b8=str(b8)
                    thing=b1+b2+b3+b4+b5+b6+b7+b8+"\n"
                    thing=str(thing)
                    file=open("bytegen.txt","a")
                    file.write(thing)
                    file.close()
                print("Write successful.")
                godcheck()
            elif choice == 3:
                filename=input("File name >")
                filename=filename+".txt"
                bytes=int(input("How many bytes to generate $"))
                for i in range(bytes):
                    from random import randint
                    b1=randint(0,1)
                    b1=str(b1)
                    b2=randint(0,1)
                    b2=str(b2)
                    b3=randint(0,1)
                    b3=str(b3)
                    b4=randint(0,1)
                    b4=str(b4)
                    b5=randint(0,1)
                    b5=str(b5)
                    b6=randint(0,1)
                    b6=str(b6)
                    b7=randint(0,1)
                    b7=str(b7)
                    b8=randint(0,1)
                    b8=str(b8)
                    thing=b1+b2+b3+b4+b5+b6+b7+b8+"\n"
                    thing=str(thing)
                    file=open(filename,"a")
                    file.write(thing)
                    file.close()
                print("Write successful.")
                godcheck()
            elif choice == 4:
                filename=input("File name >")
                filename=filename+".txt"
                bytes=int(input("How many bytes to generate $"))
                for i in range(bytes):
                    from random import randint
                    b1=randint(0,1)
                    b1=hex(b1)
                    b2=randint(0,1)
                    b2=hex(b2)
                    b3=randint(0,1)
                    b3=hex(b3)
                    b4=randint(0,1)
                    b4=hex(b4)
                    b5=randint(0,1)
                    b5=hex(b5)
                    b6=randint(0,1)
                    b6=hex(b6)
                    b7=randint(0,1)
                    b7=hex(b7)
                    b8=randint(0,1)
                    b8=hex(b8)
                    b1=str(b1)
                    b2=str(b2)
                    b3=str(b3)
                    b4=str(b4)
                    b5=str(b5)
                    b6=str(b6)
                    b7=str(b7)
                    b8=str(b8)
                    thing=b1+b2+b3+b4+b5+b6+b7+b8
                    thing=thing+"\n"
                    file=open(filename,"a")
                    file.write(thing)
                    file.close()
                print("Write successful.")
                godcheck()
            elif choice == 5:
                file=open("bytegen.txt","r")
                for line in file:
                    file=open("bytegen.vimx","a")
                    file.write(line)
                    file.close()
                file.close()
                print("Write successful.")
                godcheck()
        elif osk == "htop":
            if usertype == "root" or usertype == "god":
                print("1% CPU 1% MEM 0% GMEM 0% VIRTMEM")
                godcheck()
            else:
                print("You are not root.")
                godcheck()
        elif osk == "sudo help":
            print("These commands must have sudo in front of them:")
            print("These commands could be dangerous!")
            print("timeloop")
            godcheck()
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
            godcheck()
        elif osk == "sqrt":
            from math import sqrt
            num1=int(input("Int $"))
            num2=sqrt(num1)
            print("sqrt",num1,"=",num2)
            print("Save to MEM? Y/N")
            choice=input(">")
            choice=choice.lower()
            if choice == "y":
                mem=num2
                godcheck()
            else:
                godcheck()
            godcheck()
        elif osk == "sqrt mem":
            try:
                from math import sqrt
                eem=sqrt(mem)
                print(eem)
                print("Save to MEM? Y/N")
                choice=input(">")
                choice=choice.lower()
                if choice == "y":
                    mem=eem
                    godcheck()
                else:
                    godcheck()
                godcheck()
            except:
                print("MATH ERROR")
                godcheck()
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
            godcheck()
        elif osk == "cls":
            for i in range(39):
                print()
            godcheck()
        elif osk == "vim":
            if usertype != "guest":
                print("[1] New / Load File")
                print("[2] Print File")
                print("[3] Clear Contents of File")
                print("[4] Overwrite File")
                print("[5] Backup File")
                print("[6] Restore Backup")
                print("[7] Migrate Legacy Vim File To VIMX")
                print("[8] Clear Backup")
                print("[9] Backup Backup <must manually restore>")
                print("[10]Clear legacy vim file")
                print("[11] Exit")
                try:
                    choice=int(input(">"))
                except:
                    godcheck()
                if choice == 1:
                    filename=input("File name  $")
                    filename=filename+".vimx"
                    print(filename)
                    print("Press CTRL+C to exit")
                    while True:
                        try:
                            file=open(filename,"a")
                            nextline=input(">")
                            file.write(nextline+"\n")
                            file.close()
                        except:
                            godcheck()
                elif choice == 2:
                    try:
                        filename=input("File >")
                        filename=filename+".vimx"
                        file=open(filename,"r")
                        for line in file:
                            print(line)
                        file.close()
                        godcheck()
                    except:
                        print("Bad file name.")
                        godcheck()
                elif choice == 3:
                    try:
                        filename=input(">>")
                        filename=filename+".vimx"
                        file=open(filename,"w")
                        file.write("")
                        file.close()
                        print("Contents deleted. File is not deleted")
                        godcheck()
                    except:
                        print("ERROR")
                        godcheck()
                elif choice == 4:
                    filename=input(">")
                    oldname=filename
                    filename=filename+".vimx"
                    file=open(filename,"w")
                    string=input("What to put?")
                    file.write(string)
                    file.close()
                    godcheck()
                elif choice == 5:
                    try:
                        print("It is recommended you backup your backup")
                        print("before proceeding, if you have one")
                        print("If you need to do so,")
                        print("Press CTRL+C")
                        try:
                            filename=input("VIMX File Name>")
                            oldname=filename
                        except KeyboardInterrupt:
                            godcheck()
                        backupname=filename+"_backup.bak"
                        filename=filename+".vimx"
                        try:
                            file=open(backupname,"w")
                            file.write("")
                            file.close()
                        except:
                            meme=1
                        file=open(filename,"r")
                        for line in file:
                            file=open(backupname,"a")
                            file.write(line)
                            file.close()
                        print("Backup complete. Restore as",oldname)
                        godcheck()
                    except:
                        print("Backup complete. Restore as",oldname)
                        godcheck()
                elif choice == 6:
                    try:
                        filename=input("Backup name>")
                        restorename=filename
                        restorename=restorename+".vimx"
                        filename=filename+"_backup.bak"
                        file=open(filename,"r")
                        for line in file:
                            file=open(restorename,"a")
                            file.write(line)
                            file.close()
                        file.close()
                        print("Complete.")
                        godcheck()
                    except:
                        print("Bad file name.")
                        godcheck()
                elif choice == 7:
                    try:
                        filename=input("Name of migrated file >")
                        oldname=filename
                        filename=filename+".vimx"
                        file=open("vim.txt","r")
                        for line in file:
                            file=open(filename,"a")
                            file.write(line)
                            file.close()
                        file.close()
                        print("Migrated to",filename)
                        print("Load as",oldname)
                        godcheck()
                    except:
                        print("An unexpected error has occured.")
                        print("Maybe vim.txt does not exist?")
                        godcheck()
                elif choice == 8:
                    try:
                        bname=input("Backup name >")
                        bname=bname+"_backup.bak"
                        file=open(bname,"w")
                        file.write("")
                        file.close()
                        print("Backup cleared. You can't recover it.")
                        godcheck()
                    except:
                        print("An error occured.")
                        godcheck()
                elif choice == 9:
                    bname=input("Enter backup name >")
                    openname=bname+"_backup.bak"
                    from time import strftime
                    strf=strftime("_%Y_%m_%d_%H.%M")
                    newname=bname+strf+".bak"
                    print(newname)
                    import os
                    startpoint=os.getcwd()
                    startpoint=startpoint.replace("\\","/")
                    print(startpoint)
                    import os
                    os.chdir(startpoint)
                    try:
                        file=open(openname,"r")
                        for line in file:
                            import os
                            try:
                                os.makedirs("pythinux_backups_backups")
                                file=open(newname,"a")
                                file.write(line)
                                file.close()
                                os.chdir(startpoint)
                            except OSError as error:
                                os.chdir("pythinux_backups_backups")
                                file=open(newname,"a")
                                file.write(line)
                                file.close()
                                os.chdir(startpoint)
                        print("Success!")
                        print("Backed up as",newname)
                    except:
                        print("Unexpected error. Perhaps",openname,"does not exist?")
                    godcheck()
                elif choice == 10:
                    print("Warning! Deleting your old vim file will wipe")
                    print("its contents!")
                    print()
                    print("It is highly recommended you migrate it to a VIMX file first!")
                    print("[1] Delete VIM file")
                    print("[0] Cancel")
                    vimer=int(input(">"))
                    if vimer == 1:
                        file=open("vim.txt","w")
                        file.write("")
                        file.close
                        print("VIM file wiped. You might not be able to recover its data")
                        godcheck()
                    else:
                        godcheck()
                else:
                    godcheck()
            else:
                print("Guests cannot access vim!")
                godcheck()
        elif osk == "vim_legacy":
            if usertype != "guest":
                print("\n**********")
                print("Note: This version of vim is depreceated!")
                print("**********\n")
                print("Type 'quit' as the text to quit\n")
                while True:
                    txt=input("Text to add to vim.txt $")
                    if txt != "quit":
                        saveto=open("vim.txt","a")
                        saveto.write(txt+"\n")
                        saveto.close()
                    elif txt == "":
                        godcheck()
                    else:
                        godcheck()
            else:
                print("Guest accounts cannot access this.")
                godcheck()
        elif osk == "del os" or osk == "del":
            if usertype== "god":
                print("Deleting OS...")
                from time import sleep
                sleep(7.5)
                print(os,version,"has been deleted!")
                print("You are not supposed to do this...How???")
                import sys
                sys.exit()
            else:
                print("You need GOD priveleges to access this command")
                print("This is not assigned to a proper user")
                print("The only way to run a command like this is to change your usertype\nto god in source")
                print("OR to simply type godme")
                godcheck()
        elif osk == "sudo setpriveleges":
            currpass=input("Password $")
            if currpass == password:
                if usertype != "user" or usertype != "guest":
                    setter()
                else:
                    godcheck()
            else:
                print("User authentication FAILED")
                godcheck()
        elif osk == "godme" or osk == "gimmegod":
            print("godme is not a valid command or user")
            godcheck()
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
            godcheck()
        elif osk == "vim /debuglogs/readme.txt":
            print("The logs are being stored and sent to a random database online. IDK where.")
            print("The IP is invalid so it goes nowhere. I wanted to scare paranoid ppl")
            godcheck()
        elif osk == username:
            print(username,"is a user not a command")
            godcheck()
        elif osk == "sysdbg":
            if usertype != "root" or usertype != "god":
                print("You do not have root perms")
                godcheck()
            else:
                print(username)
                print(usertype)
                print("The above is debug info for development purposes only.")
                godcheck()
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
            print()
            print("To find the area of various shapes, do area")
            print("To find the circumference of a circle, do circumference")
            print()
            print("Press ENTER to continue.")
            wer=input()
            godcheck()
        elif osk == "lcm":
            from math import lcm
            num1=int(input("Int $"))
            print(lcm(num1))
            godcheck()
        elif osk == "power":
            from math import pow
            num1=int(input("Number $"))
            num2=int(input("To the power of $"))
            print(num1,"to the power of",num2,"=",num1 ** num2)
            godcheck()
        elif osk == "echo":
            echo=input("Str $")
            print(echo)
            godcheck()
        elif osk == "forgot":
            oldpass=input("Check password $")
            if oldpass == password:
                print("Y")
                godcheck()
            else:
                print("N")
                login()
        elif osk == "":
            print("Ha, ha, very funny.")
            godcheck()
        elif osk == "tens":
            number=int(input("Enter a number>"))
            tens=int(input("How many times to x10 >"))
            for i in range(tens):
                number=number*10
            print(number)
            print()
            godcheck()
        elif osk == "crash":
            if usertype == "god" or usertype == "root":
                reason=input("Enter reason $")
                if reason == "":
                    reason="GENERIC_CRASH"
                subreason2=input("Enter subreason $")
                subreason=subreason2
                if subreason=="":
                    subreason="ERROR"
                if reason == "666" and subreason == "DONT_DEAL_WITH_DEVIL":
                    crash("I AM WATCHING YOU","YOU CANNOT HIDE")
                    godcheck()
                else:
                    crash(reason,subreason)
            else:
                print("You are not root.")
                godcheck()
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
                godcheck()
        elif osk == "run subs":
            print("[1] Timeloop")
            print("[2] Godcheck")
            print("[3] Injector")
            print("[4] GodModeMe")
            print("[5] Crash")
            print("[6] Logged")
            print("[7] Login")
            choice=int(input("$"))
            if choice == 1:
                timeloop()
            elif choice == 2:
                godcheck()
            elif choice == 3:
                injector()
            elif choice == 4:
                godmodeme()
            elif choice == 5:
                crash("GENERIC","GENERIC")
            elif choice == 6:
                logged()
            elif choice == 7:
                login()
        elif osk == "run godefector":
            godinator()
        elif osk == "server":
            print("You need to run this program with sudo")
            godcheck()
        elif osk == "xyzzy":
            from random import randint
            rng=randint(1,3)
            if rng == 1:
                print("The shadow knows!")
            elif rng == 2:
                print("You are a real rascal!")
            elif rng == 3:
                print("EJECT PC")
            godcheck()
        elif osk == "sudo server":
            server()
        else:
            print(osk,"is not a valid command, user or directory.")
            print("For a list of commands type help")
            print("To get started using",os,version,"type started")
            print("For help on a particular command type man <command>")
            godcheck()
    def login():
        global username
        global password
        global usertype
        username=input("Username $")
        if username == "e" or username == "":
            quit()
            #this quits on the login screen bc of vscode being dumb and pasting in a powershell command when i press run
            #meaning i would have to log in and then exit
            #so i made THIS
            #this check occurs before the login to avoid me from typing a password
        password=input("Password $")
        base=username+":"+password
        import hashlib
        hashed_string = hashlib.sha256(base.encode('utf-8')).hexdigest()
        if base == "root:root":
            usertype="root"
            startsystem()
        elif base == "user:password":
            usertype="user"
            startsystem()
        elif hashed_string == "ca2a533a8edc8ba4855ed44bc3dc7318c70dec0324bbd559435b403ffc4753e0":
            usertype="user"
            startsystem()
        elif base == "kenny:kennyeeee":
            usertype="user"
            startsystem()
        elif base == "Szymon Mochort:root" or base == "ibxtoycat:toycat_is_yes":
            print("That user does not exist.")
            #easter egg number 1
            login()
        elif base == "guest:password":
            usertype="guest"
            startsystem()
        elif hashed_string == "f098f8ddf8905b85d27166522c1db538cdcd63e66d2e063cc7cddf8d12e632bc":
            usertype="user"
            startsystem()
        elif base == "root:password":
            usertype="guest"
            crash("CONFLICT","USERNAME")
            startsystem()
        else:
            print("The username or password is invalid.")
            login()
    login()
except KeyboardInterrupt:
    if crashloop == 1:
        crashloop=1
        crashloop_r="YOUWILLNOTESCAPECRASHLOOP"
        crash("CRASH","CRASH")
    try:
        crash("GENERAL","KEYBOARDINTERRUPT")
    except:
        crashloop=1
        crashloop_r="EVASI0N"
        crash("CRASH","EVASI0N")
        login()
##except:
##    crash("CRASH","GENERAL")
##
