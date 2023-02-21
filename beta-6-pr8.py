global data
import os.path
from platform import uname
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
    f.write("root|root|2/guest|password|0/user|password|1")
    f.close()
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
global os_name, app_version, autologin
global username, password, user_lvl, user_type, user_type
import getpass
from time import ctime, strftime, sleep
import os
from secrets import choice
os_name,app_version,="Pythinux",[0,6,"PR8"]
autologin = 1
def vim_editor(fn=""):
    if fn == "":
        fn = input("File Name >>") + ".vimx"
    try:
        f = open(fn,"r")
        data=f.read()
        f.close()
        data=data.split("\n")
        for item in data:
            print(item)
    except:
        pass
    f = open(fn,"w")
    div()
    print("Press CTRL+C to exit")
    div()
    try:
        while True:
            f.write(input(">>"))
            f.write("\n")
    except:
        f.close()
    main()
def vim():
    logo = ['# ##### # ', '# # # ##   ## ', '# # # # # # # ', '# # # #  #  # ', ' #   #  # # # ', '  # #   # # # ', '   #   #### # ']
    for l in logo:
        pass
    print("[1] New / Open File")
    print("[2] Read File")
    print("[3] Delete File")
    print("[4] Overwrite File")
    print("[5] Backup File")
    print("[6] Restore Backup")
    print("[7] Migrate vim.txt to VIMX")
    print("[8] Delete Backup")
    print("[9] Delete vim.txt")
    print("[10] File List")
    print("[0] Exit")
    div()
    try:
        ch=int(input(">"))
    except:
        main()
    div()
    if ch == 1:
        vim_editor()
    elif ch == 2:
        try:
            f = open(input("File Name >>") + ".vimx")
            data=f.read()
            f.close()
            data=data.split("\n")
            for item in data:
                print(item)
            br()
            main()
        except:
            main()
    elif ch == 3:
        try:
            os.remove(input("File name >>")+".vimx")
        except:
            pass
        main()
    elif ch == 4:
        fn = input("File Name >>") + ".vimx"
        try:
            os.remove(fn)
        except:
            pass
        vim_editor(fn)
    elif ch == 5:
        fn = input("File Name >>")
        try:
            f = open(fn+".vimx","r")
            data = f.read()
            f.close()
            f = open(fn+".vimbackup","w")
            f.write(data)
            f.close()
            print("Backed up file.")
            main()
        except:
            print("Failed to back up file.")
            main()
    elif ch == 6:
        fn = input("File Name >>")
        try:
            f = open(fn+".vimbackup","r")
            data=f.read()
            f.close()
            f = open(fn+".vimx","w")
            f.write(data)
            f.close()
            print("Restored file.")
            main()
        except:
            print("Failed to restore file.")
            main()
    elif ch == 7:
        try:
            f=open("vim.txt","r")
            data=f.read()
            f.close()
            f=open("vim_legacy.vimx","w")
            f.write(data)
            f.close()
            print("To load, open \"vim_legacy\"")
        except:
            print("Failed to load VIM.TXT")
        main()
    elif ch == 8:
        try:
            os.remove(input("File name >>")+".vimbackup")
        except:
            pass
        main()
    elif ch == 9:
        try:
            os.remove("vim.txt")
        except:
            pass
        main()
    elif ch == 10:
        path = os.getcwd()
        dirlist = os.listdir(path)
        for item in dirlist:
            isFile = os.path.isfile(item)
            if isFile == True and item.endswith(".vimx"):
                item = item.replace(".vimx", "")
                print(item)
            else:
                continue
        br()
        vim()
    else:
        main()
def clear_screen():
    res=uname()
    os.system("cls" if res[0] == "Windows" else "clear")
def man(manual):
    if manual == "man":
        print("Man is a manual system that allows for programs")
        print("to create manuals that can be displayed to users.")
        div()
        print("In order to use man, here are some tips:")
        div()
        print("[-] To see a list of installed manuals, type MAN / into the terminal.")
        print(f"[-] To see {os_name}'s changelog, type MAN CHANGES.")
        br()
        main()
    elif manual == "rewrite":
        div()
        print(f"{os_name} was made in early 2022.")
        print(f"It was the first major project I ever worked on, while I was still learning the basics of Python.")
        print(f"One day, I decided to work on {os_name}, and the first thing I noticed was how messy my code was.")
        print(f"Compared to my modern code, it was a mess.")
        print(f"I knew a rewrite was in order.")
        print(f"I had already started rewriting my previous stuff, and decided to get on with it.")
        print(f"The rewrite will have a much better UI and code.")
        print(f"Hopefully, this isn't something I end up regretting :)")
        br()
        main()
    elif manual == "deprecated":
        print("Certain programs have been deprecated [scheduled for removal] or removed.")
        div()
        print("DEPRECATED")
        div()
        print("bytegen scriptux")
        div()
        print("REMOVED")
        div()
        print("vim_legacy")
        br()
        main()
    elif manual == "/":
        div()
        print("MANUAL LIST")
        div()
        print("changes deprecated man / rewrite")
        br()
        main()
    elif manual == "changes":
        print(f"{os_name} v{app_version[0]}.{app_version[1]}.{app_version[2]} changes:")
        div()
        print("[-] Complete rewrite of the codebase and software.")
        print("[-] A lot of programs upgraded/downgraded/removed, most notably Vim.")
        print("[-] Creation of custom users possible with new add_user command")
        print("[-] Overhauled manuals")
        print("[-] Certain software deprecated [MAN DEPRECATED]")
        print("[-] Files has been upgraded [the old version is available since not all features have been ported over]")
        div()
        print("Note: This is a pre-release build, so a lot of changes have not been implemented yet.")
        div()
        br()
        main()
    else:
        return True
def files(startpoint,start=0,safemode=0):
    if start == 1:
        div()
        print("Files")
        div()
        print("For help, type HELP.")
        div()
        print("Files is a command-line file explorer.")
        print("It is similar to CMD in Windows.")
        if safemode == 1:
            print("Safe mode is on. Certain commands do not work.")
        div()
    prompt = input(f"{os.getcwd()} />")
    if prompt == "help":
        div()
        print("Command list + description")
        div()
        print("help = Gives you help")
        print("cd <dir> = changes to another directory")
        print("exit = Closes Files.")
        if safemode == 0:
            print("mark = Set current directory as Startpoint.")
        print("startpoint = Change current directory to Startpoint.")
        if safemode == 0:
            print("safemode = enables safe mode [certain commands disabled] [cannot disable]")
        if safemode == 0:
            print("clear = clear a file's contents")
        print("dir = List all files and fodlers in current directory")
        print("dir /w = Lists all folders in current directory")
        if safemode == 0:
            print("md <folder> = Create a folder named <folder>")
            print(f"del <file> = Delete <file>")
            print(f"create <file> = Creates a blank file named <file>")
        br()
        files(startpoint,0,safemode)
    elif prompt == "exit":
        os.chdir(startpoint)
        main()
    elif prompt == "safemode" and safemode == 0:
        files(startpoint,1,1)
    elif "cd " in prompt:
        try:
            os.chdir(prompt[3:])
        except:
            pass
        files(startpoint,0,safemode)
    elif prompt == "cd..":
        os.chdir("..")
        files(startpoint,0,safemode)
    elif prompt == "startpoint":
        os.chdir(startpoint)
        files(startpoint,0,safemode)
    elif prompt == "":
        files(startpoint,0,safemode)
    elif prompt == "mark" and safemode == 0:
        files(os.getcwd())
    elif "clear " in prompt  and safemode == 0:
        try:
            f = open(prompt[6:],"w")
            f.close()
            print("Successfully cleared file.")
        except:
            print("Failed to clear file.")
        print(startpoint)
        files(startpoint,0,safemode)
    elif prompt == "dir" or prompt == "ls":
        dirname=os.getcwd()
        filee = os.listdir(dirname)
        for file in filee:
            print(file)
        files(startpoint,0,safemode)
    elif "view " in prompt:
        try:
            f=open(prompt[5:],"r")
            data=f.read()
            f.close()
            data=data.split("\n")
            for item in data:
                print(item)
            br()
            files(startpoint,0,safemode)
        except:
            files(startpoint,0,safemode)
    elif prompt == "dir /w" or prompt == "dir/w" or prompt == "dir /q" or prompt == "dir/q":
        dirname=os.getcwd()
        filee = os.listdir(dirname)
        for file in filee:
            if os.path.isdir(file) == True:
                print(file)
        files(startpoint,0,safemode)
    elif "md " in prompt and safemode == 0:
        try:
            os.mkdir(prompt[3:])
        except:
            print("Failed to create directory.")
        files(startpoint,0,safemode)
    elif "del " in prompt and safemode == 0:
        try:
            os.remove(prompt[4:])
        except:
            print("Could not remove file.")
        files(startpoint,0,safemode)
    elif "create " in prompt and safemode == 0:
        try:
            f=open(prompt[7:],"w")
            f.close()
        except:
            print("Could not open file.")
        files(startpoint,0,safemode)
    elif prompt == "safemode" and safemode == 1:
        print("Safe mode cannot be disabled. Exit Files and re-enter it to disable it, if you have the priveleges to run Files without safe mode.")
        files(startpoint,0,1)
    else:
        print(f"{upper(prompt)} IS NOT A VALID COMMAND OR DIRECTORY.")
        files(startpoint,0,safemode)
def files_legacy():
        import os
        safemode=0
        startpoint=os.getcwd()
        while True:
            import os
            prompt=input(str(os.getcwd()+" />"))
            if prompt == "help":
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
                print("dir=list all files and folders")
                print("dir /w = list all folders")
                print("mark=make this the startpoint")
                print("safemode=disables all commands that write data")
                print("create= create a blank file with a name")
                print("create file.txt\n")
                print("view=show the contents of a file")
                print("cls=clear the screen")
                print("cd.. = parent directory")
                print("edit=edit a file")
                print("exit=exit files app")
                print()
                print("Press ENTER to continue.")
                wer=input()
                print()
            elif prompt == "cls":
                clear_screen()
                main()
            elif prompt == "exit":
                os.chdir(startpoint)
                main()
            elif prompt == "cwd" or prompt == "cd":
                cwd=os.getcwd()
                print(cwd)
            elif prompt == "dir":
                dirname=os.getcwd()
                files = os.listdir(dirname)
                temp = map(lambda name: os.path.join(dirname, name), files)
                for file in temp:
                    print(file)
            elif prompt == "startpoint" or prompt == "sp":
                os.chdir(startpoint)
            elif prompt == "cd..":
                os.chdir("..")
            elif prompt == "safemode":
                if safemode==0:
                    safemode=1
                    print("Safemode enabled")
                else:
                    safemode=0
                    print("Safemode disabled.")
            elif "create " in prompt and safemode == 0:
                create=prompt[7:]
                try:
                    file=open(create,"a")
                    file.close()
                    print("Success!")
                except:
                    print("Error!")
            elif "clear " in prompt and safemode == 0:
                clear=prompt[6:]
                try:
                    file=open(clear,"w")
                    file.write("")
                    file.close()
                    print("Success!")
                except:
                    ("Error! Perhaps",clear,"does not exist?")
            elif "vimx " in prompt:
                dirold=os.getcwd()
                vimx=prompt[5:]
                vimx2=vimx.split(".")
                vimx2.pop(1)
                vimx2 = ','.join(str(x) for x in vimx2)
                vimx2=vimx2+".vimx"
                
                try:            
                    file=open(vimx,"r")
                    for line in file:
                        os.chdir(startpoint)
                        file=open(vimx2,"a")
                        file.write(line)
                        file.close()
                        os.chdir(dirold)
                    print("Success! Saved file!")
                    print("Load as",vimx)
                except:
                    print("Bad file name.")
            elif "view " in prompt:
                view=prompt[5:]
                try:                                        
                    file=open(view,"r")
                    for line in file:
                        print(line)
                    file.close()                    
                except:
                    print("Bad file name.")                    
            elif "cd " in prompt:
                dir2ch=prompt[3:]
                try:
                    os.chdir(dir2ch)
                except:
                    print("Bad file name.")
            elif "md " in prompt and safemode == 0:
                newdir=prompt[3:]
                try:
                    os.makedirs(newdir)
                    print("Directory",newdir,"made.")
                except:
                    print("Error. Perhaps",newdir,"already exists>?")
            elif prompt == "mark" and safemode == 0:
                print("[1] Confirm")
                print("[0] Cancel")
                choice=int(input(">"))
                if choice == 1:
                    newdir=os.getcwd()
                    startpoint=newdir
            elif "del " in prompt and safemode == 0:
                file2=prompt[4:]
                print("[1] Confirm\n[0] Cancel")
                choice=int(input(">"))
                if choice == 1:
                    try:
                        os.remove(file2)
                    except:
                        print(file2)
                        print("Error. Perhaps there is no file.")
        
            elif prompt == "dir /w" or prompt == "dir/w" or "dir/q" or "dir /q":
                dirname=os.getcwd()
                dirfiles = os.listdir(dirname)

                fullpaths = map(lambda name: os.path.join(dirname, name), dirfiles)

                dirs = []
                files = []

                for file in fullpaths:
                    if os.path.isdir(file): dirs.append(file)

                for file in dirs:
                    print(file)
            else:
                print("Bad command or file name.")
                if safemode == 1:
                    print("Some commands are disabled in safe mode!")
def remove_userlist():
    # https://www.geeksforgeeks.org/python-os-remove-method/
    import os
    # File name
    file = 'userlist.pythinux'
    # File location
    location = str(os.getcwd())
    # Path
    path = os.path.join(location, file)
    # Remove the file
    # 'file.txt'
    os.remove(path)
    refresh_data()
    login()
def refresh_data():
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
        f.write("root|root|2/guest|password|0/user|password|1")
        f.close()
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
    return ""
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
        crash(upper(input("Reason $").replace(" ","_")),upper(input("Subreason $")).replace(" ","_"))
    elif ch == 3:
        crash("CRASH","GENERIC_CRASH",1)
    elif ch == 4:
        crash(upper(input("Reason $")),upper(input("Subreason $")),1)
    elif ch == 5:
        autologin = 1
        login(1,input("Username $"),input("Password $"),1)
    else:
        main()
def crash(reason="CRASH",subreason="GENERIC_CRASH",crash_loop=0):
    if crash_loop == 1:
        div()
        print("CRASH")
        div()
        print(f"The fatal error occured and {os_name} was forced to terminate itself in order to protect the hardware and software from irreversible damage.")
        div()
        print(f"{reason}:{subreason}")
        try:
            ch=input("Restart? Y/N $")
        except:
            sleep(2.5)
            crash(reason,subreason,1)
        if lower(ch) != "n":
            sleep(2.5)
        crash(reason,subreason,1)
    else:
        div()
        print("CRASH")
        div()
        print(f"The fatal error occured and {os_name} was forced to terminate itself in order to protect the hardware and software from irreversible damage.")
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
def god_check():
    if user_lvl >= 3:
        crash("SECURITY","INVALID_PRIVELEGE")
    else:
        return True
def userlist():
    global data
    div()
    print("GOD USERS")
    div()
    has_god = 0
    has_root = 0
    has_regular = 0
    has_guest = 0
    for item in data:
        if item[2] == "3":
            has_god = 1
            print(item[0])
    if has_god == 0:
        print("N/A")
    div()
    print("ROOT USERS")
    div()
    for item in data:
        if item[2] == "2":
            has_root = 1
            print(item[0])
    if has_root == 0:
        print("N/A")
    div()
    print("NORMAL USERS")
    div()
    for item in data:
        if item[2] == "1":
            has_regular = 1
            print(item[0])
    if has_regular == 0:
        print("N/A")
    div()
    print("GUEST USERS")
    div()
    for item in data:
        if item[2] == "0":
            has_guest = 1
            print(item[0])
    if has_guest == 0:
        print("N/A")
    br()
    main()
def scriptux():
    global os, app_version
    div()
    print("DeprecationWarning")
    div()
    print("This command will be deprecated and removed soon; please do not use it unless you HAVE to.")
    div()
    print("[1] Use Tool")
    print("[0] Exit")
    try:
        ch = input(">>")
    except:
        main()
    if ch != "1":
        main()
    vali=0 #used to validate if the version was declared
    hasdebug=0
    endmsg=""
    file=input("Filename >")
    if file == "about:scriptux":
        print("Scriptux")
        print("Version 1a")
        print("(c) 2022 WinFan3672, all rights reserved.")
        main()
    else:
        file=file+".pyth"
        try:
            file=open(file,"r")
        except:
            print("FILE ERROR")
            main()
            import sys
            sys.exit()
        for line in file:
            if "print " in line and vali == 1:
                printf=line[6:]
                print(printf)
            elif "var input " in line and vali == 1:
                linx=line[10:]
                var=input(linx)
            elif "var print" in line and vali == 1:
                try:
                    print(var)
                except:
                    print("VARIABLE ERROR! Var not assigned")
            elif "var clear" in line and vali == 1:
                var=""
            elif "about os" in line and vali == 1:
                print(os_name)
            elif "about version" in line and vali == 1:
                print(version)
            elif "about scriptux" in line and vali == 1:
                print("Scriptux v1")
            elif "about manual" in line  and vali == 1:
                print("Scriptux is a scripting langauge for Pythinux written in the")
                print("Python programming language.")
                print("There isn't a manual yet. Just wait for one if ur lazy")
                print("Or you could read the code!")
            elif "nl" in line and vali == 1:
                print("\n")
            elif "endmsg " in line and vali == 1:
                endmsg=line[7:]
            elif "version=" in line:
                if "version=1" in line and vali == 0:
                    vali=1
                    continue
                else:
                    print("Version Error! Script is for older/newer version")
                    print("The version line in your script:")
                    print(line)
                    vali=2
                    break
            elif "end" in line and vali == 1:
                vali=4
                break
            else:
                continue
        file.close()
        if vali == 1:
            print("Program ended.")
        elif vali == 2:
            print("Program terminated with errors.")
        elif vali == 4:
            if endmsg == "":
                print("Program terminated using END command.")
                #Using the end command at the end of the program is not necessary, but it does allow for custom end messages!
            else:
                print(endmsg)
        else:
            print("Your program didn't provide a version!")
            print("On line 1, you need to include version=1 in order for it to work")
            scriptux()
        main()            
def main():
    global username, password, user_lvl, user_type, data
    god_check()
    ch=lower(input(f"{user_type}@{username} $"))
    if ch == "help":
        div()
        print(f"Command List")
        div()
        print(f"about help logoff author mul rand rng time cls")
        print(f"echo started div add sub stopwatch timer getdetails bytegen chkroot")
        print(f"quit forgot power sysinfo mod userlist timeloop sqrt area add_user")
        print(f"scriptux admin_panel files_legacy man userlist_c vim run")
        div()
        main()
    elif ch == "about":
        div()
        print(f"{upper(os_name)} v{app_version[0]}.{app_version[1]}.{app_version[2]}")
        div()
        print(f"{os_name} is (c) 2022 WinFan3672, some rights reserved.")
        print(f"{os_name} is distributed under the MIT license, a flexible license\nthat gives full control over source code and no warranty.")
        div()
        main()
    elif ch == "logoff":
        login()
    elif ch == "ping":
        print("Pong")
        main()
    elif ch == "author":
        div()
        print(f"{os_name} was written by WinFan3672.")
        print(f"WinFan3672 is a British developer making stupid things like this.")
        main()
    elif ch.replace(" ","") == "":
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
        exit()
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
    elif ch == "mod":
        div()
        print("mod [num1] [num2]")
        print("Outputs [num] % [num2]")
        main()
    elif "mod " in ch:
        ch=ch.split(" ")
        if len(ch) == 3:
            try:
                print(str("{:,}".format(float(ch[1]) % float(ch[2]))))
            except:
                print("An error occured.")
        else:
            base=[]
            for item in ch:
                if item != "":
                    base.append(item)
            ch=base
            print(f"MOD requires [2] parameters, got [{len(ch)-1}].")
        main()
    elif ch == "userlist":
        if is_root() == True:
            userlist()
        else:
            print("Only ROOT users can access this menu.")
            main()
    elif ch == "timeloop":
        print("Enter CTRL+C to exit.")
        while True:
            try:
                print(strftime("%x %X"))
                sleep(1)
            except:
                main()
    elif ch == "sqrt":
        print("sqrt [float]")
        print("Does sqare root of [float].")
        main()
    elif ch == "area":
        div()
        print("Area Menu")
        div()
        print("[1] Rectangle")
        print("[2] Triangle")
        print("[3] Circle")
        div()
        try:
            ch=int(input(">"))
        except:
            main()
        if ch == 1:
            try:
                print(int(input("Base $")) * int(input("Height $")))
            except:
                print("@ERROR")
            main()
        elif ch == 2:
            try:
                print(int(input("Base $")) * int(input("Height $")) / 2)
            except:
                print("@ERROR")
            main()
        elif ch == 3:
            from math import pi
            try:
                print((int(input("Radius $")) ** 2) * pi)
            except:
                print("@ERROR")
            main()
        else:
            main()
    elif "sqrt " in ch:
        ch=ch.split(" ")
        try:
            from math import sqrt
            print(sqrt(float(ch[1])))
        except:
            print("An error occured.")
        main()
    elif ch == "add_user":
        if is_root() == True:
            f=open("userlist.pythinux","r")
            d=f.read()
            f.close()
            f=open("userlist.pythinux","w")
            base1=input("Username $")
            base2=input("Password $")
            base3=input("UserLVL  $")
            try:
                if int(base3) > user_lvl:
                    base3 = str(user_lvl)
                    print(f"[To prevent privelege escalation, {os_name} has automatically reduced the user level you chose.]")
            except:
                pass
            f.write(d+f"/{base1}|{base2}|{base3}")
            f.close()
            refresh_data()
            print("Added to userlist.")
            main()
        else:
            print("You must be a ROOT user to access this.")
            main()
    elif ch == "scriptux":
        if is_root() == True:
            scriptux()
        else:
            print("Only ROOT users can access this.")
            main()
    elif ch == "admin_panel":
        if is_root() == True:
            div()
            print("Admin Control Panel")
            div()
            print("[1] Regenerate Userlist And Log Out")
            div()
            try:
                ch=int(input(">"))
            except:
                main()
            div()
            if ch == 1:
                os.remove("userlist.pythinux")
                login()
            else:
                print("Could not remove userlist.")
                main()
        else:
            print("Only ROOT users can do this!")
            main()
    elif ch == "files_legacy":
        if is_root() == True:
            div()
            print("FILES")
            div()
            print("DeprecationWarning")
            div()
            print("This version of Files only exists in order to allow you to use commands that have not been ported over.")
            print("The new Files can be accessed by exiting and typing FILES into the terminal.")
            print("This old version of files is buggy and poorly written. Use at own risk.")
            print("In order to exit this version of Files, type EXIT.")
            print("For a command list, type HELP.")
            br()
            div()
            files_legacy()
        else:
            print("Only ROOT users can use this command.")
            main()
    elif ch == "man":
        print("man [manual]")
        print("For manual list, type man /")
        print("For help with man, type man man")
        main()
    elif "man " in ch:
        man(ch[4:])
        print(f"{upper(ch)} IS NOT A VALID COMMAND, PROGRAM OR MANUAL.")
        main()
    elif ch == "userlist_c":
        if is_root() == True:
            div()
            for item in data:
                print(item[0])
            div()
            main()
        else:
            print("Only ROOT users can use this command.")
            main()
    elif ch == "update":
        print(f"{upper(ch)} IS NOT A VALID COMMAND, PROGRAM OR MANUAL.")
        # Not working oops
        main()
        import urllib.request

        url = "http://winfan3672.000webhostapp.com/version_check/pythinux.version"
        print("Checking for updates...")
        print(
            f"Current Version: {app_version[0]}.{app_version[1]}.{app_version[2]}"
        )
        try:
            urllib.request.urlretrieve(url, "pythinux.version")
        except:
            div()
            print("Failed to check for updates.")
            div()
            print("You could try:")
            print("[-] Checking that you are connected to the Internet.")
            print(
                "[-] Checking that winfan3672.000webhostapp.com is still up, since that is the server that provides the version check information."
            )
            print(
                "[-] Checking that http://winfan3672.000webhostapp.com/version_check/openlife.versio exists, since it may have been deleted."
            )
            print(
                "[-] Checking that your antivirus or firewall is not blocking winfan3672.000webhostapp.com/"
            )
            print("[-] On Windows, deleting your DNS resolver cache.")
            main()
        div()
        f = open("pythinux.version", "r")
        data = f.read()
        data = data.split("|")
        data = [int(data[0]), int(data[1]), int(data[2])]
        not_update_text = f"An update for {os_name} [{data[0]}.{data[1]}.{data[2]}] is available.\nNo download available"
        if data[0] > app_version[0]:
            print(not_update_text)
        else:
            if data[1] > app_version[1]:
                print(not_update_text)
            else:
                if data[2] > app_version[2]:
                    print(not_update_text)
                else:
                    print(f"You are on the latest version of {os_name}.")
        main()
    elif ch == "vim":
        div()
        vim()
    elif ch == "files":
        if is_root() == True:
            files(os.getcwd(),1)
        else:
            files(os.getcwd(),1,1)
    elif ch == "run":
        prog=input(">>")
        if ".zip" not in prog:
            prog+=".zip"
        try:
            import sys
            sys.path.insert(0,prog)
            import program
            program.p_start()
        except:
            print("FileError: The file",prog,"does not exist.")
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
    print(f"Welcome to {os_name}.")
    print(f"[{os_name} v{app_version[0]}.{app_version[1]}.{app_version[2]}]")
    div()
    if user_lvl == 0:
        print("You are logged in on a guest account.")
        print("Guest accounts have limited access to commands and cannot run programs.")
    elif user_lvl == 1:
        pass
    elif user_lvl == 2:
        print("You are logged in as a root account.")
        print("If you do not know what this means, type LOGOFF right now.")
        print("DO NOT USE A ROOT ACCOUNT AS YOUR DAILY DRIVER ACCOUNT.")
    elif user_lvl == 3:
        pass
    else:
        print("[Error: The account type is invalid.]")
        login()
    main()
def login(al=0,al_username="root",al_password="root"):
    global username, password, user_lvl, user_type, autologin, data
    if data == []:
        div()
        print("[Your user file is corrupt. Please delete it.]")
        div()
        data = [["root","root","2"],["user","password","1"],["guest","password","0"]]
    if al == 1:
        base=f"{al_username}:{al_password}"
        username,password=f"{al_username}",f"{al_password}"
        autologin = 0
    else:
        div()
        print(f"{upper(os_name)} LOGIN SYSTEM")
        div()
        print("Enter your login details.")
        print("If they are valid, you will be logged in.")
        print(f"There are [{len(data)}] users on your machine.")
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
    print("Username or password is invalid.")
    login()
login(autologin)
