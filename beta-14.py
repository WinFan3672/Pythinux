#!/usr/bin/python
global crashlog
crashlog=[]
global data
global consent_mode
consent_mode = 0
import os.path
from platform import uname
from time import strftime as stime
global stdlib
global mem,var_data, prompt
mem=0
var_data=[]
prompt=""
packages=[]
global os_name, app_version, autologin
global username, password, user_lvl, user_type, user_type
import getpass
from time import ctime, strftime, sleep
import os
from secrets import choice

# OS INFORMATION CONTAINED HERE
os_name,app_version,="Pythinux",[0,14,0]
autologin = 0
import os
def removed(filename,return_mode=0):
    try:
        import shutil
        shutil.rmtree("Installed Programs/"+filename)
        if return_mode == 0:
            print(f"Uninstalled {filename}.")
    except Exception as e:
        crashlog.append(str(e))
        if return_mode == 0:
            print("Failed to remove program.")
    if return_mode == 0:
        main()
    else:
        return True
def create_file(filename,data):
    try:
        f=open(filename,"wb")
        f.write(data)
        f.close()
        return True
    except:
        return False
def installd(filename,consent=0):
    try:
        fn=os.path.basename(filename)
        global crashlog
        from zipfile import ZipFile as zf
        try:
            with open(filename,"rb") as f:
                zipdata=f.read()
        except Exception as e:
            crashlog.append(str(e))
        import shutil
        shutil.rmtree("Cached Data")
        os.mkdir("Cached Data")
        os.chdir("Cached Data")
        with open(fn,"wb") as f:
            f.write(zipdata)
            f.close()
        with zf(fn,"r") as zip:
            zip.extractall()
        import sys
        sys.path.insert(0,os.getcwd())
        try:
            f=open("program.name","r")
            progname=f.read()
            f.close()
            progname=progname[:-1]
        except Exception as e:
            crashlog.append(str(e))
            print("Error: No `program.name` in zip archive`.")
            return False
        try:
            f=open("program.info","r")
            progdata=f.read()
            f.close()
            progdata=progdata.split("\n")
            progdata=progdata[0]
            progdata=progdata.split("|")
            progdata[4]=progdata[4].split(".")
            progdata[4][0]=int(progdata[4][0])
            progdata[4][1]=int(progdata[4][1])
            progdata[1]=progdata[1].split(".")
        except Exception as e:
            crashlog.append(str(e))
            print("Error: No `program.info` in zip archive.")
            return False
        
        try:
            with open("program.zip","rb") as f:
                mp=f.read()
                is_mp=1
        except Exception as e:
            crashlog.append(str(e))
            is_mp=0
        try:
            f=open("setup.xx","r")
            xx=f.read()
            f.close()
            is_xx=1
        except Exception as e:
            crashlog.append(str(e))
            is_xx=0
        try:
            f=open("program.deps","r")
            deps=f.read()
            deps=deps.split("\n")
            f.close()
            is_dep=1
        except Exception as e:
            crashlog.append(str(e))
            is_dep=0
        try:
            f=open("manuals.cmanpak","r")
            mandata=f.read()
            f.close()
            is_man=1
        except Exception as e:
            crashlog.append(str(e))
            is_man=0
        if is_dep == 1:
            deps = [dep for dep in deps if dep != ""]
        if consent == 0:
            print(f"Program Name: {progdata[0]}")
            print(f"Version: {progdata[1][0]}.{progdata[1][1]}.{progdata[1][2]}")
            print(f"Released: {progdata[2]}")
            print(f"Author: {progdata[3]}")
            if is_dep == 1:
                print(f"Dependencies: [{len(deps)}]")
                print("Dependency List:",deps)
            print("Install?")
            yn=input("[y/n] >").lower()
            if yn != "y":
                print("User Install Cancelled.")
                return False
        if progdata[4] <= [app_version[0],app_version[1]]:
            pass
        else:
            print(f"Error: OS Version Must be >= {app_version[0]}.{app_version[1]}")
            return False
        if os.path.isfile(os.getcwd()+"/setup.py"):
            import sys
            print("[START] Program Setup")
            print("[NOTICE] If not in terminal, you may not see anything.")
            os.system(f"{sys.executable} setup.py")
            print("[END] Program Setup")
        sys.path.remove(os.getcwd())
        os.chdir("..")
        try:
            import shutil
            shutil.rmtree(f"Installed Programs/{progname}")
            print("[UPGRADE] Removed Old Program")
        except Exception as e:
            crashlog.append(str(e))
        if is_dep == 1:
            for item in deps:
                if item != "":
                    main(f"pkm install -y {item}")
        if is_mp == 1:
            os.mkdir(f"Installed Programs/{progname}")
            f=open(f"Installed Programs/{progname}/program.zip","wb")
            f.write(mp)
            f.close()
        if is_xx == 1:
            run_script(xx.split("\n"))
        if is_man == 1:
            f=open(f"Installed Manuals/{progname}.cmanpak","wb")
            f.write(mandata)
            f.close()
        print(f"Successfully installed {progdata[0]}.")
        if is_mp == 1:
            print(f"To run {progdata[0]}, type `run {progname}`")
        return True
    except Exception as e:
        crashlog.append(str(e))
        print("Install failed.")
        print("Check the following:")
        print("[-] Installer file exists/path was entered correctly")
        print("[-] Installer path typed correctly")
        print("[-] Installer is formatted correctly")
        print("[-] Alternatively, contact the developers of the program to see if this is an issue on your end.")
        return False
def can_change_dir(path, startpoint):
    abs_path = os.path.abspath(path)
    start_path = os.path.abspath(startpoint)
    return abs_path.startswith(start_path)
def create_user(username,passw,ulvl):
    global crashlog
    print("Creating user...")
    os.chdir("Users")
    os.mkdir(username)
    os.chdir(username)
    os.mkdir("Documents")
    os.mkdir("Scripts")
    os.mkdir("User Settings")
    os.mkdir("Programs")
    os.mkdir("Program Data")
    os.mkdir("Vim Files")
    os.chdir("User Settings")
    f=open("os_settings.toml","w")
    f.close()
    f=open(f"alias.dat","w")
    f.close()
    os.chdir("..")
    os.chdir("..")
    os.chdir("..")
    f=open("System Settings/userlist.pythinux","a")
    f.write(f"{username}|{passw}|{ulvl}/")
    f.close()
    print("Created user successfully.")
    refresh_data()
def linux_hub():
    global crashlog
    print("[1] APT Tools")
    print("[2] Pacman Tools")
    print("[0] Exit")
    try:
        ch=int(input(">"))
    except Exception as e:
        crashlog.append(str(e))
        linux_hub()
    if ch == 1:
        print("[1] Install package")
        print("[2] Remove packages")
        print("[3] Update DB")
        print("[4] Update packages")
        print("[5] 3+4")
        print("[0] Exit")
        try:
            ch=int(input(">"))
        except Exception as e:
            crashlog.append(str(e))
            linux_hub()
        if ch == 1:
            os.system(f"sudo apt install {input('Package Name >')} -y")
            main()
        elif ch == 2:
            os.system(f"sudo apt remove {input('Package Name >')} -y")
        elif ch == 3:
            os.system("sudo apt update")
            main()
        elif ch == 4:
            os.system("sudo apt upgrade")
            main()
        elif ch == 5:
            os.system("sudo apt update && sudo apt upgrade")
            main()
        else:
            main()
    elif ch == 2:
        print("[1] Install package")
        print("[2] Remove package")
        print("[3] Update DB")
        print("[4] Update packages")
        print("[0] Exit")
        try:
            ch=int(input(">"))
        except Exception as e:
            crashlog.append(str(e))
            linux_hub()
        if ch == 1:
            os.system(f"sudo pacman -S {input('Package Name >')}")
            main()
        elif ch == 2:
            os.system(f"sudo pacman -R {input('Package Name >')}")
            main()
        elif ch == 3:
            os.system("sudo pacman -Sy")
            main()
        elif ch == 4:
            os.system("sudo pacman -Syu")
            main()
        else:
            main()
    else:
        main()
def ihelp(ch=""):
    global crashlog
    if ch == "":
        ch=input("interactive-help $")
        return_mode=0
    else:
        return_mode=1
    if ch == "help":
        div()
        print("Command List")
        div()
        print("help ihelp mul rand time cls echo started div add sub stopwatch timer getdetails chkroot quit power sysinfo mod userlist timeloop area login pkm ucode installd removed cat wget exit")
        div()
        if return_mode == 0:
            ihelp()
        else:
            return True
    elif ch == "exit":
        main()
    elif ch == "ihelp":
        div()
        print("ihelp is an interactive help application that allows you to learn how commands work.")
        print("Type the name of a supported command and it will help you use the command.")
        print("For instance, if you need to learn how the div command works, type `div`.")
        print("For a list of commands, type `help`.")
        print(f"To return to {os_name}, type `exit`.")
        div()
        if return_mode == 0:
            ihelp()
        else:
            return True
    elif ch == "mul":
        div()
        print("Mul, or MULtiply, is a command that performs basic multiplication.")
        div()
        print("Here's how to use it:")
        print("mul <num1> <num2")
        print("Replace <num1> with a number and <num2> with a number, and it will print <num1> multipled by <num2>.")
        div()
        print("Examples:")
        print("$ mul 45 55")
        print("2475")
        print("$ mul 2 2")
        print("4")
        div()
        if return_mode == 0:
            ihelp()
        else:
            return True
    elif ch == "rand":
        div()
        # print(rng(100 000,1000 000))
        print("Type `rand` and it prints a random number between 100,000 and 1,000,000.")
        div()
        print("Examples")
        div()
        print("$ rand")
        print("123070")
        print("$ rand")
        print("498797")
        div()
        if return_mode == 0:
            ihelp()
        else:
            return True
    elif ch == "time":
        print("The command `time` prints the date and time in the format MONTH/DAY/YEAR HOUR:MINUTE:SECOND.")
        if return_mode == 0:
            ihelp()
        else:
            return True
    elif ch == "cls":
        print("CLS clears the terminal screen. This can be used to get rid of clutter.")
        if return_mode == 0:
            ihelp()
        else:
            return True
    elif ch == "echo":
        div()
        print("ECHO echoes what you feed it.")
        div()
        print("Examples")
        div()
        print("$ echo hello")
        print("hello")
        print("$ echo You have a virus now !!!!111")
        print("You have a virus now !!!!111")
        div()
        if return_mode == 0:
            ihelp()
        else:
            return True
    elif ch == "started":
        print(f"Started, or the Getting Started Guide, is a brief introduction on how to use {os_name}.")
        print("It is currently incomplete.")
        if return_mode == 0:
            ihelp()
        else:
            return True
    elif ch == "div":
        div()
        print("Div is a basic DIVision command.")
        div()
        print("To use it, type `div <num1> <num2>`, replacing <num1> and <num2> with numbers.")
        print("Div will print <num1> divided by <num2>.")
        div()
        print("Examples")
        div()
        print("$ div 12 2")
        print("6.0")
        print("$ div 1 2")
        print("0.5")
        div()
        if return_mode == 0:
            ihelp()
        else:
            return True
    elif ch == "add":
        print("add is an ADdition command.")
        print("To use it, type `add <num1> <num2>`, replacing <num1> and <num2> with numbers.")
        print("add will print <num1> + <num2>.")
        div()
        print("Examples")
        div()
        print("$ add 2 2")
        print("4")
        print("$ add 7 5")
        print("12")
        div()
        if return_mode == 0:
            ihelp()
        else:
            return True
    elif ch == "sub":
        div()
        print("sub is a SUBtraction command.")
        print("To use it, type `sub <num1> <num2>`, replacing <num1> and <num2> with numbers.")
        print("sub will print <num1> - <num2>.")
        div()
        print("Examples:")
        print("$ sub 4 5")
        print("-1")
        div()
        if return_mode == 0:
            ihelp()
        else:
            return True
    elif ch == "stopwatch":
        print("stopwatch is a basic stopwatch.")
        print("It starts at 1 and waits 1 second before incrementing the number and printing it.")
        print("In the stopwatch, press CTRL+C to exit it.")
        if return_mode == 0:
            ihelp()
        else:
            return True
    elif ch == "timer":
        print("Type `timer <number>` and it will count down from <number> to 1 and then exit.")
        ihelp()
    elif ch == "getdetails":
        print("If you are a root user, getdetails prints your username and a censored version of your password.")
        if return_mode == 0:
            ihelp()
        else:
            return True
    elif ch == "chkroot":
        print("This command prints True if you are a root user and False if you are not.")
        if return_mode == 0:
            ihelp()
        else:
            return True
    elif ch == "quit":
        print(f"type `quit` or `exit` to exit {os_name}.")
        ihelp()
    elif ch == "forgot":
        print("The `forgot` utility allows you to confirm if you know your password.")
        print("As a warning, if you type your password incorrectly, you will be logged off, meaning that you will be locked out if you cannot remember your password.")
        if return_mode == 0:
            ihelp()
        else:
            return True
    elif ch == "power":
        print("Usage:\npower <number1> <number2>")
        print("Power prints out <number1> to the power of <number2>.")
        div()
        print("Examples")
        div()
        print("$ power 2 16")
        print("65,536.0")
        print("$ power 10 4")
        print("1,000.0")
        div()
        if return_mode == 0:
            ihelp()
        else:
            return True
    elif ch == "sysinfo":
        print("Sysinfo prints out information about your computer.")
        if return_mode == 0:
            ihelp()
        else:
            return True
    elif ch == "mod":
        div()
        print("Mod is a MODulus [the % operator, which outputs the remainder of division] command.")
        print("To use it, type `mod <num1> <num2>`, replacing <num1> and <num2> with numbers.")
        print("Mod will print <num1> % <num2>")
        div()
        print("Examples")
        div()
        print("$ mod 12 2")
        print("0.0")
        print("$ mod 13 2")
        print("1.0")
        div()
        if return_mode == 0:
            ihelp()
        else:
            return True
    elif ch == "userlist":
        print("`userlist` prints a list of users, grouped by user type.")
        print("`userlist_c` just prints out a list of users.")
        if return_mode == 0:
            ihelp()
        else:
            return True
    elif ch == "timeloop":
        print("timeloop prints the date and time, once per second.")
        print("Once in timeloop, press CTRL+C.")
        if return_mode == 0:
            ihelp()
        else:
            return True
    elif ch == "area":
        print("Area is an interactive command that can be used to calculate the area of a 2D shape.")
        if return_mode == 0:
            ihelp()
        else:
            return True
    elif ch == "login":
        print("Running this command allows you to quickly switch between users.")
        print("Note that typing an incorrect combination still logs you out.")
        if return_mode == 0:
            ihelp()
        else:
            return True
    elif ch == "pkm":
        print("PKM is a package manager. It allows you to install programs.")
        print("It has a detailed guide for how to use and run PKM programs.")
        print("For that, `pkm ?` is your friend.")
        if return_mode == 0:
            ihelp()
        else:
            return True
    elif ch == "ucode":
        print("UCODEs are special codes used in the `qadd` command in the user editor.")
        print("They allow you to paste in the UCODE and quickly create a new user without manually typing in the details.")
        print("To generate a UCODE, use the UCODE command.")
        print("`ucode --generate` allows you to manually fill out the details to make one and `ucode --show` shows the current user's UCODE.")
        print("Do not bother with this if you don't need it/understand what it is.")
        if return_mode == 0:
            ihelp()
        else:
            return True
    elif ch == "installd":
        print("INSTALLD is a command for sideloading applications from SZIP files.")
        print("To use it, type `installd` and paste in the directory for your SZIP file.")
        print("It is mainly used by `pkm` as the backend for installing a downloaded package.")
        if return_mode == 0:
            ihelp()
        else:
            return True
    elif ch == "removed":
        print("Type `removed` followed by the name of a program and it will delete it.")
        print("It is identical to `pkm remove`. Note that it is pronounced \"Remove D\" and not \"Removed\".")
        if return_mode == 0:
            ihelp()
        else:
            return True
    elif ch == "wget" or ch == "cat":
        print("The CAT and WGET commands perform the same functions, except that CAT has another parameter to specify the directory.")
        print("Syntax:")
        print("wget [url]")
        print("cat [url] [filename]")
        print("Both commands download a file from the URL specified.")
        if return_mode == 0:
            ihelp()
        else:
            return True
    elif ch == "view_log":
        print(f"Every time an exception is logged, {os_name} logs it to a variable.")
        print("view_log shows all logged exceptions.")
        print("Note that most exceptions are harmless and are supposed to occur.")
        print(f"It can be useful for working out why {os_name} crashed.")
    else:
        if return_mode == 0:
            print(f"InvalidManual: {ch}")
            ihelp()
        else:
            return True
def tree_demo():
    global crashlog
    ch=input("tree_demo $")
    if ch == "help":
        print("help tree exit")
        tree_demo()
    elif ch == "exit":
        main()
    elif ch == "tree":
        print("Tree of /:")
        print(f"> {os_name}")
        print("   > Users")
        print("      > root")
        print("         > Documents")
        print("         > Scripts")
        print("         > Vim Files")
        print("         > User Settings")
        print("            > os_settings.toml")
        print("         > Programs")
        print("         > Program Data")
        print("      > user")
        print("         > Documents")
        print("         > Scripts")
        print("         > Vim Files")
        print("         > User Settings")
        print("            > os_settings.toml")
        print("         > Programs")
        print("         > Program Data")
        print("      > admin")
        print("         > Documents")
        print("         > Scripts")
        print("         > Vim Files")
        print("         > User Settings")
        print("            > os_settings.toml")
        print("         > Programs")
        print("         > Program Data")
        print("   > Program Files")
        print("   > System Settings")
        print("   > Cached Data")
        print("   > Custom Manuals")
        br()
        tree_demo()
    else:
        tree_demo()
def cman_demo():
    global crashlog
    ch=input("cman_demo %")
    if ch == "cman":
        print("For a list of installed manuals, type `cman /`")
        print("To open a manual, type `cman <manual>")
        cman_demo()
    elif ch == "help":
        print("help cman return")
        cman_demo()
    elif ch == "cman /":
        print("Searching for manuals...")
        div()
        print("Installed Manuals")
        div()
        print("test\ntest2\ntest3")
        div()
        cman_demo()
    elif ch == "cman test":
        print("This is a test manual.")
        cman_demo()
    elif ch == "cman test2" or ch == "cman test3":
        print("This is also a test manual.")
        cman_demo()
    elif ch == "return":
        main()
    else:
        print("Bad command or file name.")
        cman_demo()
def terminal():
    global crashlog
    termin = input(">>>")
    if termin == "%%exit":
        main()
    else:
        os.system(termin)
        terminal()
    terminal()
def is_file(fn,add=0):
    global crashlog
    return os.path.isfile(os.getcwd()+f"/{fn}")
def vim_editor(fn="",add=0):
    global crashlog
    global username
    if fn == "":
        fn = input("File Name >>") + ".vimx"
    if add == 1:
        fn = f"Users/{username}/Vim Files/" + fn
    try:
        f = open(fn,"a")
        ata=f.read()
        f.close()
        ata=data.split("\n")
        for item in ata:
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
def vim(ch=""):
    global crashlog
    if ch == "":
        logo=['# # ### # #', '# #  #  ##   ##', '# #  #  # # # #', '# #  #  #  #  #', ' #   #   #  # #', '  # ##  # #', '   #### # #']
        for l in logo:
            pass
        print("[1] New / Open File")
        print("[2] Read File")
        print("[3] Delete File")
        print("[4] Overwrite File")
        print("[5] Backup File")
        print("[6] Restore Backup")
        print("[7] Delete Backup")
        print("[8] File List")
        print("[9] Backup List")
        print("[10] About Vim")
        print("[0] Exit")
        div()
        try:
            ch=int(input(">"))
        except Exception as e:
            crashlog.append(str(e))
            main()
    else:
        vim_editor(f"Users/{username}/Vim Files/"+ch)
        print("maybe?")
        main()
    div()
    if ch == 1:
        vim_editor(add=1)
    elif ch == 2:
        try:
            f = open(f"Users/{username}/Vim Files/"+input("File Name >>") + ".vimx")
            data=f.read()
            f.close()
            data=data.split("\n")
            for item in data:
                print(item)
            br()
            main()
        except Exception as e:
            crashlog.append(str(e))
            main()
    elif ch == 3:
        try:
            os.remove(f"Users/{username}/Vim Files/"+input("File name >>")+".vimx")
        except Exception as e:
            crashlog.append(str(e))
        main()
    elif ch == 4:
        fn = input("File Name >>") + ".vimx"
        try:
            os.remove(fn)
        except Exception as e:
            crashlog.append(str(e))
            pass
        vim_editor(fn)
    elif ch == 5:
        fn = f"Users/{username}/Vim Files/"+ input("File Name >>")
        try:
            f = open(fn+".vimx","r")
            dataa = f.read()
            f.close()
            f = open(fn+".vimbackup","w")
            f.write(dataa)
            f.close()
            print("Backed up file.")
            main()
        except Exception as e:
            crashlog.append(str(e))
            print("Failed to back up file.")
            main()
    elif ch == 6:
        fn = f"Users/{username}/Vim Files/"+ input("File Name >>")
        try:
            f = open(fn+".vimbackup","r")
            dataa=f.read()
            f.close()
            f = open(fn+".vimx","w")
            f.write(dataa)
            f.close()
            print("Restored file.")
            main()
        except Exception as e:
            crashlog.append(str(e))
            print("Failed to restore file.")
            main()
    elif ch == 7:
        try:
            os.remove(f"Users/{username}/Vim Files/"+input("File name >>")+".vimbackup")
        except Exception as e:
            crashlog.append(str(e))
            pass
        main()
    elif ch == 8:
        path =  os.getcwd() + f"/Users/{username}/Vim Files"
        dirlist = os.listdir(path)
        for item in dirlist:
            if item.endswith(".vimx"):
                print(item.replace(".vimx",""))
        br()
        vim()
    elif ch == 9:
        path=os.getcwd()+f"/Users/{username}/Vim Files"
        dirlist=os.listdir(path)
        for item in dirlist:
            if item.endswith(".vimbackup"):
                print(item.replace(".vimbackup",""))
        br()
        vim()
    elif ch == 10:
        print("Vim Text Editor v3.1.0")
        print("(c) 2022-2023 WinFan3672, some rights reserved.")
        main()
    else:
        main()
def clear_screen():
    global crashlog
    res=uname()
    os.system("cls" if res[0] == "Windows" else "clear")
def sha256(text):
    global crashlog
    import hashlib
    hashed_string = hashlib.sha256(text.encode('utf-8')).hexdigest()
    return hashed_string
def install_stdlib():
    global crashlog
    global stdlib
    try:
        del(stdlib)
    except Exception as e:
        crashlog.append(str(e))
        pass
    try:
        import stdlib
    except Exception as e:
        crashlog.append(str(e))
        pass
def future_features_2():
    global crashlog
    div()
    print("Future Features [Page II]")
    div()
    print("[1] Custom Manual")
    print(f"[2] {os_name} Folder")
    print("[<] Previous Page")
    try:
        ch=input(">")
    except Exception as e:
        crashlog.append(str(e))
        future_features_2()
    if ch == "1":
        man("cman")
        future_features_2()
    elif ch == "2":
        print(f"A {os_name} sub-folder will exist in the current working directory.")
        print("Programs can be installed and run there, documents can be stored and scripts stored as well.")
        div()
        print("Example Directory Structure")
        div()
        print(f"> {os_name}")
        print("   > Users")
        print("      > root")
        print("         > Documents")
        print("         > Scripts")
        print("         > Vim Files")
        print("         > User Settings")
        print("            > os_settings.toml")
        print("            > alias.pythinux")
        print("            > .user_alias_use")
        print("         > Programs")
        print("            > someprogram_helper")
        print("         > Program Data")
        print("   > Program Files")
        print("      > someprogram")
        print("         > settings.data")
        print("         > someprogram.zip")
        print("   > System Settings")
        print("      > .autologin")
        print("      > .startup")
        print("      > userlist.pythinux")
        print("      > aliases.pythinux")
        print("      > .noalias")
        print("      > os_settings.toml")
        print("   > Cached Data")
        print("      > someprogram.cache")
        print("   > Custom Manuals")
        print("      > test.cman")
        print("      > test2.cman")
        print("      > test3.cman")
        div()
        print("This system will allow for a much more organised and efficient system for having multiple users, and allows for much more advanced OS integration.")
        br()
        future_features_2()
    elif ch == "9" or ch == "<":
        future_features()
    else:
        future_features_2()
def future_features(ch="",return_mode = 0):
    global crashlog
    div()
    print("Future Features")
    div()
    print("[1] Scripting Improvements")
    print("[2] WINHUB / LINUXHUB")
    print("[3] Wget")
    print("[4] Standard Library")
    print("[5] RemoveUser Command")
    print("[6] SZIPS improvements")
    print("[7] Interactive Help Hub")
    print("[8] Files Improvements")
    print("[9] Other Additions")
    print("[>] Next Page")
    div()
    if ch == "":
        try:
            ch = input(">")
        except Exception as e:

            main()
    if ch == "1":
        print("[-] FILES and MAN will have full integration with Scripting.")
        print("[-] Infinite Loop Mode will allow for commands underneath the Infinite Loop line to run forever without interruption.")
        print("[-] Variables")
        print("   [-] I can do it, in fact, I have a demo.")
        br()
        if return_mode == 0:
            main()
        else:
            main()
    elif ch == "2":
        print("1 WinHub")
        div()
        print("WinHub is a program that performs various tasks exclusive to Windows:")
        print("[-] Sound playing")
        print("[-] Registry editing")
        print("[-] Clearing DNS resolver cache")
        print("[-] Pinging a server to test Internet")
        print("[-] Shutdown")
        print("[-] etc.")
        div()
        print("2 LinuxHub")
        div()
        print("LinuxHub performs various tasks exclusive to Linux:")
        print("[-] APT installs")
        print("[-] Pacman installs")
        print("[-] Updating packages")
        print("[-] etc.")
        br()
        if return_mode == 0:
            main()
        else:
            return None
    elif ch == "3":
        print("WGET is very similar to CAT, except it automatically works out the file name to use")
        print("WGET requires a URL and saves it to the relevant file.")
        br()
        main()
    elif ch == "4":
        print(f"The {os_name} standard library will add extra functionality to SZIPS programs, which can be taken advantage of.")
        print("To add SZIPS functionality to a program, add:")
        print("from stdlib import *")
        div()
        print("To the top of the file.")
        print("Example features:")
        print("[-] Clear screen")
        print("[-] Change terminal colour")
        print("[-] etc.")
        div()
        print("[Ideas not finalised, so I have little to no idea about what to do.]")
        br()
        if return_mode == 0:
            main()
        else:
            return None
    elif ch == "5":
        print("RemoveUser will list all users inside the userfile and ask you which one to remove.")
        print("You can only remove users with user levels lower than the current logged-in user.")
        br()
        if return_mode == 0:
            main()
        else:
            return None
    elif ch == "6":
        print("[ ] RUN command will be able to use a parameter for a file name")
        print("[-] Standard Library")
        print(f"[-] Potential I/O with {os_name}.")
        print("[-] etc.")
        br()
        if return_mode == 0:
            main()
        else:
            return None
    elif ch == "7":
        div()
        print("Interactive help will be able to provide detailed documentation for every command.")
        print("Entering it will work like this:")
        div()
        print("root@root $ interactive_help")
        print("interactive_help $ ")
        div()
        print("Interactive help will have a terminal-like syntax, where you can type a command and get help on it:")
        div()
        print("interactive_help $ man")
        print("`man` is a manual system that prints out preinstalled manuals on your computer.")
        print("To open a manual, type `man <manual>`, replacing <manual> with the name of the manual.")
        print("A list of manuals is available using the command `man /`.")
        print("`man` is fully compatible with the `xx` scripting system, and is used for documenting complex features.")
        print("interactive_help $ ")
        div()
        print("This will be added in Beta 10.")
        br()
        if return_mode == 0:
            main()
        else:
            return None
    elif ch == "8":
        div()
        print("Future additions to Files:")
        print("[-] Rename command")
        print("[-] Copy/paste commands")
        print("   [-] Copy data from a file, and paste it into a new/existing file.")
        print("[-] View command fix")
        br()
        if return_mode == 0:
            main()
        else:
            return None
    elif ch == "9":
        print("[-] Standard Library 1.0.0")
        print("[-] Compiler")
        print(f"   [-] Compile any Python script to a {os_name}-compatible package.")
        br()
        if return_mode == 0:
            main()
        else:
            return None
    elif ch == "10" or ch == ">":
        future_features_2()
    else:
        if return_mode == 0:
            main()
        else:
            return None
def man(manual, return_mode = 0):
    global crashlog
    if manual == "man":
        print("Man is a manual system that allows for programs")
        print("to create manuals that can be displayed to users.")
        div()
        print("In order to use man, here are some tips:")
        div()
        print("[-] To see a list of installed manuals, type MAN / into the terminal.")
        print(f"[-] To see {os_name}'s changelog, type MAN CHANGES.")
        br()
        if return_mode == 0:
            main()
        else:
            return None
    elif manual == "stdlib":
        print(f"The {os_name} standard library adds extra functionality to SZIPS programs, which can be taken advantage of.")
        print("To add SZIPS functionality to a program, add:")
        print("import stdlib")
        div()
        print("To the top of the file.")
        print("Example features:")
        print("[-] Clear screen")
        print("[-] Change terminal colour")
        print("[-] etc.")
        div()
        print(f"Every {os_name} installation comes with a built-in STDLIB. In order to install it, type INSTALL STDLIB.")
        print("The STDLIB command allows you to test and communicate with the Standard Library.")
        print("Typing stdlib --help shows all STDLIB commands.")
        if return_mode == 0:
            main()
        else:
            return None
    elif manual == "install":
        print(f"{os_name} comes with several programs which are not installed by default. `install` is a command that installs them.")
        print("Type `install <command>` to install <command>, if valid.")
        print("[`install --list` just shows a list]")
        if return_mode == 0:
            main()
        else:
            return None
    elif manual == "removed-man":
        div()
        print("Removed manuals:")
        print("rewrite")
        div()
        print("Manuals to be removed by 1.0:")
        print("removed-man todo deprecated future_features")
    elif manual == "deprecated":
        print("Certain programs have been deprecated [scheduled for removal]* or removed.")
        print("This is a list of programs that have been removed since Beta 5 and programs on the way out.")
        div()
        print("DEPRECATED")
        div()
        print("[N/A]")
        div()
        print("REMOVED")
        div()
        print("vim_legacy tens bytegen scriptux files_legacy ping")
        div()
        print("* That is not what deprecated actually means")
        br()
        if return_mode == 0:
            main()
        else:
            return None
    elif manual == "/":
        div()
        print("MANUAL LIST")
        div()
        print("changes deprecated man / removed_man vim echo scripting todo mem updates template szips future_features stdlib alias startup consent roadmap files2 pkm")
        div()
        if return_mode == 0:
            main()
        else:
            return None
    elif manual == "consent":
        div()
        print("Consent mode is a Scripting feature that allows for elevated functions in a script.")
        print("It allows for:")
        print("[-] Running SZIPS programs")
        print("[-] etc.")
        print("Consent mode requires user consent.")
        print("For a guide for it, type `install consent-guide` into the terminal.")
        div()
        if return_mode == 0:
            main()
        else:
            return None
    elif manual == "alias":
        print("Aliases allow for custom commands.")
        print("An optional file called ALIASES.PYTHINUX contains one alias per line.")
        div()
        print("Format:")
        print("<command_name>|<command>")
        div()
        print("if you type <command_name>, <command> gets executed. Note that built-in commands have priority over aliases.")
        print("Uses:")
        print("[-] Connecting an alias with a script to run that script while looking like a command")
        print("[-] Creating alternate names for commands [for example, turning CLS into CLEAR.")
        print("[-] Downloading files from the Internet with a single command.")
        print("[-] etc.")
        div()
        print("Instructions")
        print("[-] To add an alias, type `add_alias`")
        print("[-] To interact with aliases, type `alias`")
        print("[-] To disable aliases, create a file named .noalias")
        br()
        if return_mode == 0:
            main()
        else:
            return None
    elif manual == "vim":
        div()
        print("Vim is a text editor. It is capable of adding to the end of files.")
        print("While it is basic, it is functional.")
        print("To open it, type VIM.")
        div()
        print("There will be 10 options.")
        div()
        print("Option [1] lets you create or edit files.")
        print("Option [2] lets you view the contents of files.")
        print("Option [3] deletes a file.")
        print("Option [4] opens a file in write mode, not append mode.")
        print("Options [5],[6] and [8] pertain to backups of VIMX files.")
        print("OPtions [7] and [9] pertain to the now-deprecated legacy Vim.")
        print("Option [10] presents you with a nice list of all files in the current directory.")
        br()
        if return_mode == 0:
            main()
        else:
            return None
    elif manual == "files2":
        div()
        print("Files v2 changelog")
        div()
        print("[-] Removed mark command")
        print("[-] Starting directory is now root directory")
        print("[-] Cannot cd above root directory [unfortunately, that means cd .. does not work]")
        print("[-] ver format looks cleaner.")
        print("[-] type ls/dir <keyword> and it is filtered by file name, eg dir test will only show files or folders with `test` in the name")
        print("[-] type ls/dir *.<extension> and it filters by file extension.")
        div()
        main()
    elif manual == "changes":
        div()
        print(f"{os_name} v{app_version[0]}.{app_version[1]}.{app_version[2]} changes")
        div()
        print("[-] Autologin now requires password")
        print("[-] Auth screen now works :)")
        br()
        if return_mode == 0:
            main()
        else:
            return None
    elif manual == "pkm":
        print("PKM is a package manager. It automatically downloads and installs packages from the official database, or a custom one, if you add one.")
        div()
        print("Picking packages")
        div()
        print("To see a list of all packages you can install, the command `pkm all` has you covered.")
        print("It shows the name of the package and its description.")
        print("Once you see a package you like, you need to install it. Speaking of...")
        div()
        print("Installing Packages")
        div()
        print("Once you have a package you want to install, type `pkm install [package name]`, replacing `[package name]` with the package's name.")
        print("The name for the package is given in `pkm all` as the name.")
        div()
        print("Running an installed program")
        div()
        print("Once you have run an installed program, type `run [package name]` to run it. Certain programs may add an alias to do this, so do check your alias list to be sure.")
        print("You can run multiple programs at once as well, which is cool.")
        div()
        print("Removing packages")
        div()
        print("Note: only packages that can be run can be removed. Some packages, such as `essential`, are not runnable since they do not install themselves and just run a setup script.")
        print("To remove a package, type `pkm remove [package name]`.")
        div()
        print("Commands")
        div()
        print("There are some commands that are built into PKM that are useful.")
        print("`pkm all`: lists all packages you can install.")
        print("`pkm db`: manipulates your database list, allowing you to add or remove databases.")
        print("`pkm list`: shows a list of installed packages.")
        print("`pkm update`: refreshes the list of packages. This is done automatically with `pkm install` and `pkm all`, but you may want to do it manually.")
        print("`pkm upgrade`: removes all packages and reinstalls them, essentially upgrading them to their latest version if applicable.")
        br()
        if return_mode == 0:
            main()
        else:
            return None
    elif manual == "echo":
        print(f"In the old {os_name}, you could use functionality in Echo that has not been ported over.")
        print("The functionality allowed for the quick creation of files and the echoing of variable data.")
        div()
        print("This functionality will be added soon.")
        br()
        if return_mode == 0:
            main()
        else:
            return None
    elif manual == "scripting" or manual == "xx":
        div()
        print(f"The scripting system is a new system in {os_name} that allows you to run terminal commands, one at a time.")
        div()
        print("The Concept")
        div()
        print("It is basically the same as Bash in Linux or Batch in Windows. It allows you to run multiple commands at once, automatically, aithout needing to type them out.")
        print("Scripts end in .xx and are in plaintext.")
        div()
        print("Creating a Script")
        div()
        print("[-] Create a new .XX file [In files, do \"vim <filename>.xx\"]")
        print("[-] On each line, enter each command you'd like to run, in the same way as you would type it normally.")
        div()
        print("Running a Script")
        div()
        print("To run a script, type ./[script name]. Replace [script name] with the file name of the XX file. Do not put \".xx\" at the end.")
        div()
        print("Script-Exclusive Stuff")
        div()
        print("[-] div() places a div() element on the screen")
        print("[-] Timer does not show a number in scripts")
        print("[-] Syntax Errors hidden ins scripts.")
        print("[-] cmd [command] sends a command to the host OS's default terminal")
        div()
        print("Status & Limitations")
        div()
        print("The script system is fully experimental, but it will be added to, and new features will have it in mind.")
        print("It is not guaranteed to work, and a lot of commands do not support it.")
        div()
        print("Tips")
        div()
        print("[-] Use echo to print text to the screen")
        br()
        if return_mode == 0:
            main()
        else:
            return None
    elif manual == "custom_manual" or manual =="cman":
        main("cls")
        div()
        print("By 1.0, there will be a Custom Manual System with a full file format.")
        print("For a demo, type `install cman_demo`.")
        div()
        print("Idea")
        div()
        print("A .cman file can be added to the current folder, containing everything in the manual.")
        print("Typing cman / shows every single .cman file in the current directory.")
        print("To choose a man, type cman <manual>.")
        div()
        print("Uses")
        div()
        print("Programs can use CMAN in order to create manuals in a way that is easy to maintain yet still works 100% of the time.")
        print("A program can have a help utility that has easy-to-edit, portable manuals.")
        div()
        print("Name")
        div()
        print("Yes, I am aware. I don't have a better name.")
        div()
        print("Challenges")
        div()
        print("[-] File Format")
        print("[-] Folder Support")
        print("[-] Version identification")
        print("   [-] Could use separate file formats")
        print("[-] etc.")
        br()
        if return_mode == 0:
            main()
        else:
            return None
    elif manual == "todo":
        div()
        print("[-] All future features [MAN FUTURE_FEATURES]")
        print("[-] Proper documentation for every command")
        print("[-] Finish scripting system [MAN TODO_SCRIPTS]")
        print("[-] Fix Standard Library and Startup Script")
        print("[-] Finish IHELP command")
        print("[-] XVIM command")
        print("[-] Change Password")
        div()
        print("MAN TODO_SCRIPTS")
        br()
        if return_mode == 0:
            main()
        else:
            return None
    elif manual == "todo_scripts":
        div()
        print("[-] MEM integration")
        print("[-] File operations")
        print("[-] Consent Mode")
        print("   [-] Enable to allow for extra features")
        print("   [-] User required to allow for it to be turned on")
        print("[-] Direct Python execution")
        br()
        if return_mode == 0:
            main()
        else:
            return None
    elif manual == "mem":
        main("cls")
        div()
        print("MEM is a memory system similar to that of a calculator's M function.")
        div()
        print("MEM Value")
        div()
        print(f"The value of MEM is stored in {os_name}'s memory.")
        print("To view MEM's current value, type `mem --view` or `mem -v`.")
        print("To set it, type `mem --set <value>`, replacing <value> with a number.")
        print("To clear it, type `mem --reset` or `mem -r`.")
        div()
        print("Addition and Subtraction")
        div()
        print("To add a certain value to MEM, type `mem --add <value>`")
        print("To subrtact a certain value to MEM, type `mem --add <value>`")
        div()
        print("Backup/Restore")
        div()
        print("To save MEM to a file, type `mem --backup` or `mem -b`. It will save to a file.")
        print("To restore from the backup, type `mem --restore` or `mem -rs`. It will load the backup.")
        br()
        main()
    elif manual == "updates":
        print(f"{os_name} updates are regularly released. While there is no schedule, they do add features and security improvements.")
        print(f"Current version: v{app_version[0]}.{app_version[1]}.{app_version[2]}")
        br()
        if return_mode == 0:
            main()
        else:
            return None
    elif manual == "template":
        div()
        print(f"Template is a small command that creates files that you can use when writing programs for {os_name}.")
        print("template - create a file called template.zip which contains program.py, which is loaded when SZIPS opens a program.")
        print("template -p - creates a file called template.py, which can be edited and used for SZIPS.")
        print("template -d - Finds and deletes the following files in the current directory:")
        print("[-] template.zip")
        print("[-] template.py")
        print("[-] program.py")
        br()
        if return_mode == 0:
            main()
        else:
            return None
    elif manual == "future_features":
        future_features()
    elif manual == "szips":
        div()
        print("SZIPS [Super Zipped Internal Program System] v2")
        div()
        print("This is a super basic guide on how to create a program compatible with SZIPS v2.")
        print(f"Note that this is not currently doable in {os_name} itself, and must be done in your OS.")
        div()
        print("Build Instructions")
        div()
        print("[-] Create a new folder and open it.")
        print("[-] In that folder, make a file called `program.py` and open it.")
        print("[-] Write your program. Native Python code can be executed :)")
        print("[-] Once you've written your program, use a utility to add `program.py` to a ZIP file called `program.zip`. In Windows, this is achievable by right-clicking and doing \"Send to > Compressed (Zipped) Folder\"")
        print("[-] Create a new file called `program.name` and open it. Type the name of your program [ideally without spaces and all lowercase] and save the file.")
        print("[-] Create a new file called `program.info` and open it. Copy the below string:")
        print(f"Program Name|1.0.0|11 Feb 2023|WinFan3672|{app_version[0]}.{app_version[1]}")
        print("And change the details to be relevant. The order is:")
        print(f"Program name|version|release date|author|minimum {os_name} version")
        print(f"Make sure to format `version` and `minimum {os_name} version` correctly.")
        print("[-] Optionally, you can create a file called `setup.xx` and write a script, but don't worry about that for now.")
        print("[-] Once you're all done, delete `program.py` and confirm that you have the following files ready:")
        print("- program.py")
        print("- program.name")
        print("- program.info")
        print("[-] Once you have confirmed this, add them all to a zip file called `[program name].zip`, changing [program name] to your program's name. Change the file extension from `.zip` to `.szip`.")
        div()
        print(f"Well done, you have now created a program. To install it, copy the path to the .szip file and type `installd [path]` to {os_name}'s console, pasting in the path.")
        print("If you are unaware of how to copy a file path, just Google it.")
        print("You can now install and run your program.")
        br()
        if return_mode == 0:
            main()
        else:
            return None
    elif manual == "cmde":
        print("CMD -E <command>")
        print("Works like bash or batch, you type the name of a file and it runs every line of the file through the OS's default terminal.")
        if return_mode == 0:
            main()
        else:
            return None
    elif manual == "startup":
        print(f"If you reate a file called .startup in the same directory as your {os_name} folder, the contents of it will be run by {os_name}, like a script run on startup. Unlike a script, you can run ./ scripts.")
        print("Startup scripts no longer work :(")
    elif manual == "stdlib_internal":
        if is_stdlib() == True:
            stdlib.help()
        else:
            print("Standard Library not installed.")
        if return_mode == 0:
            main()
        else:
            return None
    elif manual == "roadmap" or manual == "rmap":
        div()
        print("Beta 13")
        print("[-] Proper Consent Mode Integration")
        print("[-] Finish STARTED command")
        print("[-] All Beta 5 features [mainly math]")
        print("[-] Files tree command [install tree_demo]")
        print("[-] Build tools in Files")
        print("[-] IDLE can now be launched 2+ times")
        print("Pre-Releases")
        print("The Pre-Release builds will fix a load of bugs and polish up the OS, particularly with documentation.")
        print("1.0.x")
        print("[-] 1.0 release")
        br()
        main()
    else:
        return True
def cman(manual):
    global crashlog
    if "/" in manual:
        manual=manual.split("/")
        from zipfile import ZipFile
        try:
            with Zipfile("Custom Manuals/"+manual[0]+".cmanpak","r") as zip:
                man=zip.read(manual[1]+".cman")
            man=man.split("\n")
            for item in man:
                item=item.replace("div()",div())
                print(item)
            return True
        except Exception as e:
            crashlog.append(str(e))
            return False
    else:
        f=open("Custom Manuals/"+manual+".cman","r")
        man=f.read()
        f.close()
        man=man.split("\n")
        for item in man:
            item=item.replace("div()",div2())
            print(item)
##        return True
def files(startpoint,start=0,safemode=0,d=None):
    global crashlog
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
    sp=os.getcwd().replace(startpoint,"pythinux")
    sp.replace("//","/")
    prompt = input(f"{sp} >")
    if prompt == "help":
        div()
        print("Command list + description")
        div()
        print("help = Gives you help")
        print("cd <dir> = changes to another directory")
        print("exit = Closes Files.")
        print("startpoint = Change current directory to Startpoint.")
        if safemode == 0:
            print("safemode = enables safe mode [certain commands disabled] [cannot disable]")
        if safemode == 0:
            print("clear = clear a file's contents")
        print("dir = List all files and fodlers in current directory")
        print("pwd = prints current directory")
        print("dir /w = Lists all folders in current directory")
        if safemode == 0:
            print("md <folder> = Create a folder named <folder>")
            print(f"del <file> = Delete <file>")
            print(f"create <file> = Creates a blank file named <file>")
            print("copy <file> = copies contents of <file>")
            print("paste <file> = pastes copies data to <file>")
        print("view <file> = Prints contents of <file>")
        print("cls = clears screen")
        print("ver = prints files version")
        if safemode == 0:
            print("vim <file> = Opens file in Vim")
        br()
        files(startpoint,0,safemode,d)
    elif prompt == "pwd":
        print(os.getcwd())
        files(startpoint,0,safemode,d)
    elif prompt.startswith("copy ") and safemode == 0:
        try:
            f=open(prompt[5:],"rb")
            d=f.read()
            f.close()
        except Exception as e:
            crashlog.append(str(e))
            print("Could not perform action. Perhaps the file does not exist?")
        files(startpoint,0,safemode,d)
    elif prompt.startswith("paste ") and safemode == 0:
        try:
            f=open(prompt[6:],"wb")
            f.write(d)
            f.close()
        except Exception as e:
            print("Could not perform action. Perhaps no file was copied?")
        files(startpoint,0,safemode,d)
    elif prompt == "exit":
        os.chdir(startpoint)
        main()
    elif prompt == "dir" or prompt == "ls":
        div()
        print("TYPE     NAME")
        div()
        for item in os.listdir():
            if os.path.isdir(item):
                item_type = "DIR"
            else:
                item_type = "FILE"
            print("{:7}  {}".format(item_type, item))
        div()
        files(startpoint,0,safemode,d)
    elif prompt == "cls":
        clear_screen()
        files(startpoint,0,safemode,d)
    elif prompt == "safemode" and safemode == 0:
        files(startpoint,1,1)
    elif prompt == "ver":
        print("Files v2.2.0")
        print("(c) 2022-3 WinFan3672, some rights reserved.")
        files(startpoint,0,safemode,d)
    elif "cd " in prompt:
        try:
            if can_change_dir(prompt[3:],startpoint) == True:
                os.chdir(prompt[3:])
            else:
                print("FilesError: Cannot move above root directory.")
        except Exception as e:
            crashlog.append(str(e))
            print("FilesError: Directory Invalid.")
        files(startpoint,0,safemode,d)
    elif prompt == "getsp":
        print(startpoint)
        files(startpoint,0,safemode,d)
    elif prompt == "startpoint" or prompt == "sp":
        os.chdir(startpoint)
        files(startpoint,0,safemode,d)
    elif prompt == "":
        files(startpoint,0,safemode,d)
    elif prompt.startswith("ls *."):
        dirs=os.listdir(os.getcwd())
        d2=[]
        for item in dirs:
            if item.endswith(prompt[5:]):
                d2.append(item)
        for item in d2:
            print(item)
        files(startpoint,0,safemode,d)
    elif prompt.startswith("dir *."):
        dirs=os.listdir(os.getcwd())
        d2=[]
        for item in dirs:
            if item.endswith(prompt[6:]):
                d2.append(item)
        for item in d2:
            print(item)
        files(startpoint,0,safemode,d)
    elif prompt.startswith("dir "):
        dirs=os.listdir(os.getcwd())
        d2=[]
        for item in dirs:
            if prompt[4:] in item:
                d2.append(item)
        for item in d2:
            print(item)
        files(startpoint,0,safemode,d)
    elif prompt.startswith("ls "):
        dirs=os.listdir(os.getcwd())
        d2=[]
        for item in dirs:
            if prompt[3:] in item:
                d2.append(item)
        for item in d2:
            print(item)
        files(startpoint,0,safemode,d)
    elif "clear " in prompt  and safemode == 0:
        try:
            f = open(prompt[6:],"w")
            f.close()
            print("Successfully cleared file.")
        except Exception as e:
            crashlog.append(str(e))
            print("Failed to clear file.")
        print(startpoint)
        files(startpoint,0,safemode,d)
    elif prompt == "dir" or prompt == "ls":
        dirname=os.getcwd()
        filee = os.listdir(dirname)
        for file in filee:
            print(file)
        files(startpoint,0,safemode,d)
    elif "view " in prompt:
        try:
            f=open(prompt[5:],"r")
            data=f.read()
            f.close()
            data=data.split("\n")
            for item in data:
                print(item)
            br()
            files(startpoint,0,safemode,d)
        except Exception as e:
            crashlog.append(str(e))
            files(startpoint,0,safemode,d)
    elif prompt == "dir /w" or prompt == "dir/w" or prompt == "dir /q" or prompt == "dir/q":
        dirname=os.getcwd()
        filee = os.listdir(dirname)
        for file in filee:
            if os.path.isdir(file) == True:
                print(file)
        files(startpoint,0,safemode,d)
    elif "md " in prompt and safemode == 0:
        try:
            os.mkdir(prompt[3:])
        except Exception as e:
            crashlog.append(str(e))
            print("Failed to create directory.")
        files(startpoint,0,safemode,d)
    elif "del " in prompt and safemode == 0:
        unallowed = [".noalias",".no_autologin"]
        for item in unallowed:
            if item == prompt[4]:
                ch="del "
        try:
            os.remove(prompt[4:])
        except Exception as e:
            crashlog.append(str(e))
            print("Could not remove file.")
        files(startpoint,0,safemode,d)
    elif "create " in prompt and safemode == 0:
        try:
            f=open(prompt[7:],"w")
            f.close()
        except Exception as e:
            print("Could not open file.")
            files(startpoint,0,safemode,d)
    elif prompt == "safemode" and safemode == 1:
        print("Safe mode cannot be disabled. Exit Files and re-enter it to disable it, if you have the priveleges to run Files without safe mode.")
        files(startpoint,0,1)
    elif "vim " in prompt and safemode == 0:
       vim_editor(prompt[4:])
       files(startpoint,0,1)
    else:
        print(f"{upper(prompt)} IS NOT A VALID COMMAND OR DIRECTORY.")
        files(startpoint,0,safemode,d)
def remove_userlist():
    global crashlog
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
    global crashlog
    global data
    try:
        f=open("System Settings/userlist.pythinux","r")
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
        f=open("System Settings/userlist.pythinux","w")
        f.write("root|root|2/guest|password|0/user|password|1")
        f.close()
        f=open("System Settings/userlist.pythinux","r")
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
    global crashlog
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
    except Exception as e:
        crashlog.append(str(e))
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
    global crashlog
    if crash_loop == 1:
        div()
        print("CRASH")
        div()
        print(f"The fatal error occured and {os_name} was forced to terminate itself in order to protect the hardware and software from irreversible damage.")
        div()
        print(f"{reason}:{subreason}")
        try:
            ch=input("Restart? Y/N $")
        except Exception as e:
            crashlog.append(str(e))
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
        except Exception as e:
            crashlog.append(str(e))
            crash(reason,subreason)
        if lower(ch) != "n":
            sleep(2.5)
            login()
        else:
            crash(reason, subreason)
def is_god():
    global crashlog
    global user_lvl
    if user_lvl >= 3:
        return True
    else:
        return False
def rng(a,b):
    global crashlog
    # Uses secrets to generate a random number for "true" randomness
    return choice(list(range(a,b+1)))
def auth(msg="AUTHENTICATION"):
    global crashlog
    div()
    print(msg)
    div()
    global password
    newpass=getpass.getpass("Password $")
    if password == sha256(newpass):
        return True
    else:
        return False
def br():
    global crashlog
    div()
    input("Press ENTER to continue.\n")
    return True
def is_root():
    global crashlog
    global user_lvl
    if user_lvl >= 2:
        return True
    elif user_lvl == 1:
        if auth():
            return True
        else:
            return False
    else:
        return False
def is_root_rigid():
    global crashlog
    # The old version of is_root(). Current is_root() allows for standard users to access root-only programs. This one does not.
    global user_lvl
    if user_lvl >= 2:
        return True
    else:
        return False
def div():
    print("--------------------")
def div2():
    return "--------------------"
def upper(inp):
    if isinstance(inp,str) == True:
        return inp.upper()
    else:
        return "[UNDEFINED]"
def is_stdlib():
    try:
        data=stdlib
        return True
    except:
        return False
def lower(inp):
    if isinstance(inp,str) == True:
        return inp.lower()
    else:
        return "[UNDEFINED]"
def userlist():
    global crashlog
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
def confirmation(message="Are you sure you wish to perform this action?"):
    global crashlog
    print(message)
    print("[1] Yes")
    print("[0] No")
    try:
        ch=int(input(">"))
    except Exception as e:
        crashlog.append(str(e))
        return False
    if ch == 1:
        return True
    else:
        return False

def user_editor_v2():
    global crashlog
    ch=input("user-editor-v2 $")
    if ch == "help":
        div()
        print("help - this menu")
        print("create - create a user")
        print("list - lists all users")
        print("delete - delete a user")
        print("lvls - show level code chart")
        print("refresh - refresh user data")
        print("qadd - creates a user from a ucode")
        print("exit - returns to os")
        div()
        user_editor_v2()
    elif ch == "create":
        try:
            un=input("Username >>")
            pw=sha256(getpass.getpass("Password >>"))
            ulvl=int(input("User LVL >>"))
            create_user(un,pw,ulvl)
        except Exception as e:
            crashlog.append(str(e))
            print("Failed to create user.")
        user_editor_v2()
    elif ch == "list":
        lst=os.listdir(os.getcwd()+"/Users")
        if lst != []:
            for item in lst:
                print(item)
        else:
            print(lst)
        user_editor_v2()
    elif ch == "delete":
        unn=input(">")
        try:
            import shutil
            shutil.rmtree(f"Users/{unn}")
        except Exception as e:
            crashlog.append(str(e))
            print("Failed to remove user.")
            user_editor_v2()
        f=open("System Settings/userlist.pythinux","r")
        dat=f.read()
        f.close()
        dat=dat.split("/")
        dat2=[]
        for item in dat:
            dat2.append(item.split("|"))
        for item in dat2:
            if item[0] == unn:
                dat2.remove(item)
        dat=dat2
        dat2=[]
        for item in dat:
            dat2.append("|".join(item))
        dat2="/".join(dat2)
        f=open("System Settings/userlist.pythinux","w")
        f.write(dat2)
        f.close()
        print("Successfully made changes.")
        user_editor_v2()
    elif ch == "refresh":
        refresh_data()
        user_editor_v2()
    elif ch == "qadd":
        print("qadd [ucode]")
        print("Adds a user from a ucode")
        user_editor_v2()
    elif ch.startswith("qadd "):
        ch=ch[5:]
        ch=ch.split("|")
        create_user(ch[0],ch[1],ch[2])
        user_editor_v2()
    elif ch == "lvls":
        print("0 = Guest")
        print("1 = User")
        print("2 = Root")
        print("3 = God")
        user_editor_v2()
    elif ch == "exit":
        main()
    else:
        user_editor_v2()
def user_editor_init():
    global crashlog
    refresh_data()
    buffer_data=data
    user_editor(buffer_data)
def user_editor(buffer_data):
    global crashlog
    ch=input("user-editor $")
    if ch == "help":
        div()
        print("list - lists all users")
        print("list-debug - prints out user editor data")
        print("create - create a new user")
        print("delete <user> - deletes user")
        print("lvls - lists all user levels")
        print("editlvl - edits the userlvl of a particular user")
        print("refresh - os refreshes user data")
        print("clear - deletes all users")
        print("qadd - Creates a user account from a ucode")
        print("exit - exits without saving anything")
        div()
        user_editor(buffer_data)
    elif ch == "delete":
        ch=input("User >>")
        deleted = 0
        for item in buffer_data:
            if item[0] == ch:
                buffer_data.remove(item)
                deleted += 1
        print(f"Deleted {deleted} users.")
        user_editor(buffer_data)
    elif ch == "qadd":
        ucode=input("ucode $")
        ucode=ucode.split("|")
        buffer_data.append(ucode)
        user_editor(buffer_data)
    elif ch.startswith("qadd "):
        ucode=ch[5:]
        ucode=ucode.split("|")
        buffer_data.append(ucode)
        user_editor(buffer_data)
    elif ch == "cls":
        main("cls")
        user_editor(buffer_data)
    elif ch == "refresh":
        refresh_data()
        user_editor(buffer_data)
    elif ch == "editlvl":
        ch=input("User >>")
        bd=[]
        for item in buffer_data:
            if item[0] == ch:
                item[2] = int(input("UserLVL >>"))
                if item[2] > 3:
                    item[2] = 3
                if item[2] < 0:
                    item[2] = 0
            bd.append(item)
        buffer_data=bd
        user_editor(buffer_data)
    elif ch == "lvls":
        print("0 = guest")
        print("1 = user")
        print("2 = root")
        print("3 = god")
        user_editor(buffer_data)
    elif ch == "list":
        for item in buffer_data:
            print(f"{item[0]} = {item[2]}")
        user_editor(buffer_data)
    elif ch == "clear":
        if confirmation() == True:
            buffer_data=[]
            user_editor(buffer_data)
        else:
            user_editor(buffer_data)
    elif ch == "exit":
        main()
    elif ch == "commit":
        if confirmation() == True:
            if auth() == True:
                d2=[]
                for item in buffer_data:
                    i2=[]
                    for i in item:
                        i2.append(str(i))
                    item=i2
                    d2.append("|".join(item))
                d3=""
                for item in d2:
                    d3 += f"{item}/"
                f=open("System Settings/userlist.pythinux","w")
                f.write(d3)
                f.close()
                print("Action performed successfully.")
                user_editor(buffer_data)
        else:
            print("Action canceled.")
            user_editor(buffer_data)
    elif ch == "create":
        un=input("Username >>")
        if un == "":
            user_editor(buffer_data)
            print("Please enter a username.")
        passwd=getpass.getpass("Password >>")
        if passwd == "":
            print("Please enter a password.")
            user_editor(buffer_data)
        try:
            ulvl=int(input("User LVL [0-3] >>"))
        except Exception as e:
            crashlog.append(str(e))
            ulvl=1
        if ulvl > 3:
            ulvl=3
        if ulvl < 0:
            ulvl = 0
        buffer_data.append([un,sha256(passwd),ulvl])
        user_editor(buffer_data)
    elif ch == "list-debug" or ch == "ld":
        for item in buffer_data:
            print(item)
        user_editor(buffer_data)
    else:
        print("Invalid User Editor command:",ch)
        user_editor(buffer_data)
def user_control():
    global crashlog
    div()
    print("[0] Return")
    print("[1] User List")
    print("[2] User Editor")
    print("[3] Clear Userlist")
    print("[4] Refresh Userlist Data")
    print("[5] Set Autologin Details")
    print("[6] Delete Autologin File")
    div()
    try:
        ch=int(input(">"))
    except Exception as e:
        crashlog.append(str(e))
        user_control()
    if ch == 4:
        refresh_data()
        div()
        print("Refreshed user list.")
        user_control()
    elif ch == 2:
        user_editor_v2()
    elif ch == 3:
        try:
            if confirmation() == True and auth() == True:
                f=open("System Settings/userlist.pythinux","w")
                f.close()
            else:
                raise KeyboardInterrupt
        except Exception as e:
            crashlog.append(str(e))
            print("Failed to complete action.")
        user_control()
    elif ch == 1:
        main("userlist",return_mode=0)
        user_control()
    elif ch == 5:
        try:
            f=open(f"System Settings/autologin.dat","w")
            un=input("Username >>")
            un=un.replace("|","")
            pw=sha256(getpass.getpass("Password >>"))
            f.write(f"{un}|{pw}")
            f.close()
            div()
            print("Completed action successfully.")
            print("Login username:",un)
        except Exception as e:
            crashlog.append(str(e))
            div()
            print("Failed to complete action.")
        user_control()
    elif ch == 6:
        try:
            os.remove("System Settings/autologin.dat")
            print("Action completed successfully.")
        except Exception as e:
            crashlog.append(str(e))
            print("Could not complete action.")
        main()
    else:
        main()
    main()
def setup_wizard():
    global crashlog
    global crashlog
    print(f"Welcome to {os_name}.")
    print("This is the Setup Wizard.")
    print("Enter your username:")
    un=input("$")
    print("Enter your password:")
    print("[Make it strong!]")
    passw=sha256(getpass.getpass("$"))
    os.mkdir("Users")
    os.mkdir("Program Data")
    os.mkdir("System Settings")
    os.mkdir("Custom Manuals")
    os.mkdir("Installed Programs")
    os.mkdir("Cached Data")
    f=open("System Settings/alias.dat","w")
    f.close()
    f=open("System Settings/userlist.pythinux","w")
    f.close()
    create_user(un,passw,1)
    print("The system will now create an administrator account.")
    print("Protect the password for this account at all costs.")
    print("Enter an admin password:")
    passw2=sha256(getpass.getpass("$"))
    create_user("admin",passw2,2)
    div()
    print("Do you want to set up autologin?")
    print("[1] Yes")
    print("[0] No")
    try:
        ch=int(input(">"))
        if ch == 1:
            f=open("System Settings/autologin.dat","w")
            f.write(f"{un}|{passw}")
            f.close()
            print(f"Set up autologin for user `{un}`")
            div()
        else:
            raise Exception
    except Exception as e:
        crashlog.append(str(e))
        div()
    print(f"Successfully set up {os_name}!")
    print("Using the details for your user account, log into the system.")
    br()
def run(ch):
    global crashlog
    try:
        os.chdir(f"Installed Programs/{ch}")
        import sys
        from zipfile import ZipFile as zf
        with zf("program.zip","r") as zip:
            zip.extractall()
        os.system(f"{sys.executable} program.py")
    except Exception as e:
        print(e)
        crashlog += str(e)
        return False
    os.chdir(startpoint)
    main()
def run_script(things):
    global crashlog
    things = [dep for dep in things if dep != ""]
    if isinstance(things,list) == False:
        things=things.split("\n")
    for item in things:
        if "<input>" in item:
            item = item.replace("<input>",input())
        if "<input2>" in item:
            item = item.replace("<input2>",input())
        if "<input3>" in item:
            item = item.replace("<input3>",input())
        if "<input4>" in item:
            item = item.replace("<input4>",input())
        if "<input5>" in item:
            item = item.replace("<input5>",input())
        main(item)
    return True
def main(ch="",allow_script=0,return_mode=-1):
    global crashlog
    global username, password, user_lvl, user_type, data, stdlib, mem, var_data, prompt, packages, dbs
    if return_mode == -1:
        if ch == "":
            return_mode = 0
        else:
            return_mode = 1
    if ch == "":
        if prompt == "":
            ch=input(f"{user_type}@{username} $")
        else:
            ch=input(prompt)
    if " && " in ch:
        ch=ch.split(" && ")
        for item in ch:
            main(item)
        main()
    for item in var_data:
        ch=ch.replace("{"+item[0]+"}",item[1])
    ch=ch.replace("$date",strftime("%x"))
    ch=ch.replace("$time",strftime("%X"))
    ch=ch.replace("$user",username)
    ch=ch.replace("$dir",os.getcwd())
    ch=ch.replace("$uuser",username.upper())
    ch=ch.replace("$os",os_name)
    ch=ch.replace("$utype",user_type)
    ch=ch.replace("$version",f"{app_version[0]}.{app_version[1]}.{app_version[2]}")
    if ch.startswith("pkm") or ch.startswith("installd") or ch.startswith("removed"):
        if not is_root():
            print("Installing and uninstalling programs is only performable by ROOT users or administrators.")
            main()
    if "%input2" in ch:
        ch=ch.replace("%input2",input(">"))
    if "%input3" in ch:
        ch=ch.replace("%input3",input(">"))
    if "%input4" in ch:
        ch=ch.replace("%input4",input(">"))
    if "%input5" in ch:
        ch=ch.replace("%input5",input(">"))
    if "%input" in ch:
        ch=ch.replace("%input",input(">"))
    if ch.startswith("alias") and is_root_rigid() == False:
        print("Access denied.")
        if return_mode == 0:
            main()
        else:
            return True
    if ch.startswith("cman"):
        print("CMAN has been disabled.")
        main()
    if ch == "help":
        div()
        print(f"Command List [Split By Space]")
        div()
        print(f"about help logoff author mul rand rng time cls login censor")
        print(f"echo started div add sub stopwatch timer getdetails chkroot")
        print(f"quit forgot power sysinfo mod userlist timeloop sqrt area add_user")
        print(f"admin_panel man userlist_c vim run cat update terminal view_log qaag")
        print(f"idle-launch jit install stdlib alias add_alias user_control pkm reinstall")
        print("var mem ihelp prompt wget echf linuxhub user_editor ucode qaa installd removed")
        div()
        if return_mode == 0:
            main()
        else:
            return True
    elif ch == "ihelp":
        ihelp()
    elif ch.startswith("ihelp "):
        ihelp(ch[6:])
        main()
    elif ch == "ucode":
        div()
        print("ucode [parameter]")
        print("Parameters:")
        print("--show : shows current user's ucode")
        print("--generate : generates new ucode")
        print("--usage : explain what ucodes are used for")
        div()
        main()
    elif ch == "ucode --show":
        print(f"{username}|{password}|{user_lvl}")
        main()
    elif ch == "ucode --generate":
        unn=input("Username >>")
        pswd=sha256(getpass.getpass("Password >>"))
        ulvl=input("UserLVL >>")
        print(f"{unn}|{pswd}|{ulvl}")
        main()
    elif ch == "cman":
        print("cman [manual]")
        print("Like man, but reads custom manuals from CMAN files.")
        main()
    elif ch.startswith("cman "):
        cman(ch[5:])
        main()
    elif ch == "ucode --usage":
        print("ucodes are used in several commands, most notably the user editor's qadd command.")
        print("ucodes are used to quickly spin up a user account with specific parameters.")
        main()
    elif ch == "jit" and return_mode == 0:
        print("JIT [COMMAND]")
        print("Sends [command] to main().")
        main()
    elif ch.startswith("jit "):
        main(ch[4:])
        main()
    elif ch == "about -c":
        print(f"{os_name} v{app_version[0]}.{app_version[1]}.{app_version[2]}")
        if return_mode == 0:
            main()
        else:
            return True
    elif ch == "is_stdlib":
        print(is_stdlib())
        if return_mode == 0:
            main()
        else:
            return True
    elif ch == "about":
        div()
        print(f"{upper(os_name)} v{app_version[0]}.{app_version[1]}.{app_version[2]}")
        div()
        print(f"{os_name} is (c) 2022 WinFan3672, some rights reserved.")
        print(f"{os_name} is distributed under the MIT license, a flexible license that gives you\nfull control over the source code and no warranty.")
        div()
        if return_mode == 0:
            main()
        else:
            return True
    elif ch == "logoff":
        main("prompt ")
        login()
    elif ch == "author":
        div()
        print(f"{os_name} was written by WinFan3672.")
        print(f"WinFan3672 is a British developer making stupid things like this.")
        div()
        if return_mode == 0:
            main()
        else:
            return True
    elif ch.replace(" ","") == "":
        if return_mode == 0:
            main()
        else:
            return True
    elif ch == "mul":
        print("Syntax:")
        print("mul [int] [int]")
        if return_mode == 0:
            main()
        else:
            return True
    elif ch.startswith("mul "):
        try:
            ch=ch.split(" ")
            if len(ch) == 3:
                try:
                    print(int(ch[1])*int(ch[2]))
                except Exception as e:
                    crashlog.append(str(e))
                    print("Invalid use of command.")
                    print("Correct use: mul [int] [int]")
            else:
                print("MUL requires [2] parameters, and [2] parameters only.")
        except Exception as e:
            crashlog.append(str(e))
            print("Invalid use of command.")
            print("Correct use: mul [int] [int]")
            if return_mode == 0:
                main()
            else:
                return True
        if return_mode == 0:
            main()
        else:
            return True
    elif ch == "time":
        print(strftime("%x %X"))
        if return_mode == 0:
            main()
        else:
            return True
    elif ch == "rand":
        print(rng(100000,1000000))
        if return_mode == 0:
            main()
        else:
            return True
    elif ch == "rng":
        print("RNG generates a random number from [1st parameter] to [2nd parameter]")
        div()
        print("Correct syntax:")
        print("rng [int] [int]")
        if return_mode == 0:
            main()
        else:
            return True
    elif ch.startswith("rng ") == True:
        ch=ch.split(" ")
        if len(ch) == 3:
            try:
                print(rng(int(ch[1]),int(ch[2])))
            except Exception as e:
                crashlog.append(str(e))
                print("Only INT numbers are accepted.")
                if return_mode == 0:
                    main()
                else:
                    return True
        else:
            base=[]
            for item in ch:
                if item != "":
                    base.append(item)
            ch=base
            print(f"RNG requires [2] parameters, got [{len(ch)-1}].")
        if return_mode == 0:
            main()
        else:
            return True
    elif ch == "cls":
        clear_screen()
        if return_mode == 0:
            main()
        else:
            return True
    elif ch.startswith("echo "):
        if " > " in ch:
            ch=ch[5:]
            ch=ch.split(" > ")
            if len(ch) == 2:
                f=open(ch[1],"w")
                f.write(ch[0])
                f.close()
                if return_mode == 0:
                    main()
                else:
                    return True
            else:
                print(ch)
                if return_mode == 0:
                    main()
                else:
                    return True
        else:
            print(ch[5:])
            if return_mode == 0:
                main()
            else:
                return True
    elif ch == "echo":
        print("echo <str>")
        if return_mode == 0:
            main()
        else:
            return True
    elif ch == "started":
        div()
        print("GETTING STARTED GUIDE")
        div()
        print("In order to enter a list of commands, type HELP.")
        print("In order to log off, type LOGOFF.")
        div()
        print(f"{os_name} has a buit-in help system known as man.")
        print(f"In order to use it, type `man man` for help on how to use it, and `man /` for a list of pre-installed manuals.")
        div()
        print(f"To continue the tutorial, type `started -e`")
        if return_mode == 0:
            main()
        else:
            return True
    elif ch == "started -e":
        div()
        print("First Things First")
        div()
        print(f"You have already installed and set up {os_name}. Great!")
        print(f"You now need to understand {os_name}'s mechanics, starting with the console.")
        div()
        print(f"You type commands into the console, which looks something like this by default:")
        print("root@username $")
        print("This is where you type commands in. There are 3 parts to the default prompt:")
        div()
        print("root - this refers to the current user's user type [for a guide on how users work, type `started -u`]")
        print("username - this is your username. What a shock.")
        print("$ - this is the separator between the prompt and what you type, to make it easier to see what you're doing, particularly in a command line.")
        div()
        print("When you type commands into this, this should never change, unless you use the `prompt` command to change it.")
        print(f"In order to use {os_name}, you need to understand what its commands do, and, thankfully there are several commands that help with that.")
        print("To learn about that, type `started -h`.")
        br()
        if return_mode == 0:
            main()
        else:
            return True
    elif ch == "started -h":
        div()
        print(f"Certain commands are \"documentation commands\". They are designed to help you understand the complexities of {os_name}.")
        div()
        print(f"First off is the `started` command. This command is the initial tutorial command, that allows you to get started with the basics of using {os_name}.")
        div()
        print(f"Second is `help`. This is a complete list of *all* commands in {os_name}. Note that each command's name is split by a space.")
        div()
        print(f"`man` is a command that reads preinstalled manuals, of which there are a number of.")
        print(f"To use man, type `man man` and it will open the manpage for man, which will teach you how to use it.")
        div()
        print(f"Then there's `ihelp`, your best friend. While it is currently incomplete, it allows you to type the name of a command and it will explain how it works in detail.")
        print(f"Just type `ihelp` to run it, after which you will open the Interactive Help program. In `ihelp`, type `exit` to leave, `help` for a list of manuals and `ihelp` on how to use ihelp.")
        div()
        print(f"This is the end of the official tutorial, however, there are more installed. To see a list, type `started /`.")
        br()
        if return_mode == 0:
            main()
        else:
            return True
    elif ch == "started /":
        print("started: the initial tutorial")
        print("started -e: tutorial pt. 2")
        print("started -h: how to read documentation")
        print("started -u: how the user system works")
        print("started -p: how to install and run programs.")
        if return_mode == 0:
            main()
        else:
            return True
    elif ch == "started -p":
        main("man pkm")
        if return_mode == 0:
            main()
        else:
            return True
    elif ch == "started -u":
        div()
        print("There are several different user types built-in, all with different permissisons.")
        print("First off is the `user` usertype, which has a user level of 1.")
        print("This one can access almost all commands but may require you to type your password in order to use certain commands.")
        print("The `root` user type, or 2, is identical to the `user` usertype, except that no password is needed for running commands.")
        print("The `guest` user type, or 0, has very few priveleges and cannot run a lot of commands.")
        print("The `god` user type, or 3, is identical to root, but it can use god mode commands, such as `reinstall`.")
        div()
        print("The user editor, or `user_editor`, is a command that allows you to intuitively create and remove users.")
        print("It contains a `help` command that should get you started.")
        div()
        print("For a list of tutorials, type `started /`")
        br()
        if return_mode == 0:
            main()
        else:
            return True
    elif ch == "div":
        print("Correct syntax:")
        print("div [int] [int]")
        if return_mode == 0:
            main()
        else:
            return True
    elif ch.startswith("div "):
        ch=ch.split(" ")
        if len(ch) == 3:
            try:
                print(int(int(ch[1])/int(ch[2])) if int(ch[1]) % int(ch[2]) == 0 else int(ch[1])/int(ch[2]))
            except Exception as e:
                crashlog.append(str(e))
                print("Incorrect syntax.")
        else:
            base=[]
            for item in ch:
                if item != "":
                    base.append(item)
            ch=base
            print(f"RNG requires [2] parameters, got [{len(ch)-1}].")
        if return_mode == 0:
            main()
        else:
            return True
    elif ch == "add":
        print("Correct syntax:")
        print("add [int] [int]")
        if return_mode == 0:
            main()
        else:
            return True
    elif ch.startswith("add "):
        ch=ch.split(" ")
        if len(ch) == 3:
            try:
                print(int(ch[1])+int(ch[2]))
            except Exception as e:
                crashlog.append(str(e))
                print("Incorrect syntax.")
        else:
            base=[]
            for item in ch:
                if item != "":
                    base.append(item)
            ch=base
            print(f"RNG requires [2] parameters, got [{len(ch)-1}].")
        if return_mode == 0:
            main()
        else:
            return True
    elif ch == "sub":
        print("Correct syntax:")
        print("sub [int] [int]")
        main()
    elif ch.startswith("sub "):
        ch=ch.split(" ")
        if len(ch) == 3:
            try:
                print(int(ch[1])-int(ch[2]))
            except Exception as e:
                crashlog.append(str(e))
                print("Incorrect syntax.")
        else:
            base=[]
            for item in ch:
                if item != "":
                    base.append(item)
            ch=base
            print(f"RNG requires [2] parameters, got [{len(ch)-1}].")
        if return_mode == 0:
            main()
        else:
            return True
    elif ch == "timer":
        print("Correct syntax:")
        print("timer [seconds(int)]")
        if return_mode == 0:
            main()
        else:
            return True
    elif ch.startswith("timer "):
        ch=int(ch[6:])
        while ch > 0:
            if return_mode == 0:
                print(ch)
            sleep(1)
            ch -= 1
        if return_mode == 0:
            main()
        else:
            return True
    elif ch == "stopwatch":
        print("[Press CTRL+C To Exit]")
        i = 1
        try:
            while True:
                print(i)
                i += 1
                sleep(1)
        except Exception as e:
            crashlog.append(str(e))
            if return_mode == 0:
                main()
            else:
                return True
    elif ch == "getdetails -h":
        if is_root() == True:
            print(password)
        else:
            newpass=""
            for item in password:
                newpass.append("*")
            print(newpass)
        main()
    elif ch == "getdetails":
        if is_root() == True:
            print(f"Username: {username}")
            print(f"Password [Hashed]: [`getdetails -h` to reveal]")
            print(f"UserLVL: {user_lvl}")
            if return_mode == 0:
                main()
            else:
                return True
        else:
            print("You need to be root to access this command.")
            if return_mode == 0:
                main()
            else:
                return True
    elif ch == "linuxhub":
        linux_hub()
    elif ch == "chkroot":
        print(is_root())
        if return_mode == 0:
            main()
        else:
            return True
    elif ch == "quit" or ch == "exit" and return_mode == 0:
        if return_mode == 0:
            exit()
        else:
            main()
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
        except Exception as e:
            crashlog.append(str(e))
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
    elif ch.startswith("power "):
        ch=ch.split(" ")
        if len(ch) == 3:
            try:
                print(str("{:,}".format(float(ch[1]) ** float(ch[2]))))
            except Exception as e:
                crashlog.append(str(e))
                print("ERROR.")
        else:
            base=[]
            for item in ch:
                if item != "":
                    base.append(item)
            ch=base
            print(f"POWER requires [2] parameters, got [{len(ch)-1}].")
        if return_mode == 0:
            main()
        else:
            return True
    elif ch == "sysinfo":
        import platform
        print(platform.system(),platform.uname()[2])
        print("OS:",platform.platform())
        try:
            import tkinter as tk
            root = tk.Tk()
        except Exception as e:
            crashlog.append(str(e))
            root = "N/A"
        try:
            screen_width = root.winfo_screenwidth()
            screen_height = root.winfo_screenheight()
        except Exception as e:
            crashlog.append(str(e))
            screen_width = "N/A"
            screen_height = "N/A"
        try:
            root.withdraw()
        except Exception as e:
            crashlog.append(str(e))
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
        if return_mode == 0:
            main()
        else:
            return True
    elif ch == "auth":
        print(auth())
        main()
    elif ch == "debug" and return_mode == 0:
        if is_root_rigid() == True and auth() == True:
            debug_menu()
        else:
            div()
            print("An error occured:")
            print("[-] You are not a ROOT user")
            print("OR:")
            print("[-] You entered an incorrect password.")
            div()
            if return_mode == 0:
                main()
            else:
                return True
    elif ch == "mod":
        div()
        print("mod [num1] [num2]")
        print("Outputs [num] % [num2]")
        if return_mode == 0:
            main()
        else:
            return True
    elif ch.startswith("mod "):
        ch=ch.split(" ")
        if len(ch) == 3:
            try:
                print(str("{:,}".format(float(ch[1]) % float(ch[2]))))
            except Exception as e:
                crashlog.append(str(e))
                print("An error occured.")
        else:
            base=[]
            for item in ch:
                if item != "":
                    base.append(item)
            ch=base
            print(f"MOD requires [2] parameters, got [{len(ch)-1}].")
        if return_mode == 0:
            main()
        else:
            return True
    elif ch == "userlist":
        if is_root() == True and return_mode == 0:
            userlist()
        else:
            print("Only ROOT users can access this menu.")
            if return_mode == 0:
                main()
            else:
                return True
    elif ch == "timeloop":
        print("Enter CTRL+C to exit.")
        while True:
            try:
                print(strftime("%x %X"))
                sleep(1)
            except Exception as e:
                crashlog.append(str(e))
                main()
    elif ch == "sqrt":
        print("sqrt [float]")
        print("Does sqare root of [float].")
        if return_mode == 0:
            main()
        else:
            return True
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
        except Exception as e:
            crashlog.append(str(e))
            main()
        if ch == 1:
            try:
                print(int(input("Base $")) * int(input("Height $")))
            except Exception as e:
                crashlog.append(str(e))
                print("@ERROR")
            main()
        elif ch == 2:
            try:
                print(int(input("Base $")) * int(input("Height $")) / 2)
            except Exception as e:
                crashlog.append(str(e))
                print("@ERROR")
            main()
        elif ch == 3:
            from math import pi
            try:
                print((int(input("Radius $")) ** 2) * pi)
            except Exception as e:
                crashlog.append(str(e))
                print("@ERROR")
            main()
        else:
            main()
    elif ch.startswith("sqrt "):
        ch=ch.split(" ")
        try:
            from math import sqrt
            print(sqrt(float(ch[1])))
        except Exception as e:
            crashlog.append(str(e))
            print("An error occured.")
        main()
    elif ch == "user_control" and is_root() == 1:
        user_control()
    elif ch == "add_user":
        if is_root() == True:
            f=open("System Settings/userlist.pythinux","r")
            d=f.read()
            f.close()
            f=open("System Settings/userlist.pythinux","w")
            base1=input("Username $")
            base2=sha256(getpass.getpass("Password $"))
            base3=input("UserLVL  $")
            try:
                if int(base3) > user_lvl:
                    base3 = str(user_lvl)
                    print(f"[To prevent privelege escalation, {os_name} has automatically reduced the user level you chose.]")
            except Exception as e:
                crashlog.append(str(e))
            f.write(d+f"/{base1}|{base2}|{base3}")
            f.close()
            refresh_data()
            print("Added to userlist.")
            if return_mode == 0:
                main()
            else:
                return True
        else:
            print("You must be a ROOT user to access this.")
            if return_mode == 0:
                main()
            else:
                return True
    elif ch == "admin_panel":
        if is_root() == True and return_mode == 0:
            div()
            print("Admin Control Panel")
            div()
            print("[1] Regenerate Userlist And Log Out")
            div()
            try:
                ch=int(input(">"))
            except Exception as e:
                crashlog.append(str(e))
                main()
            div()
            if ch == 1:
                os.remove("System Settings/userlist.pythinux")
                login()
            else:
                print("Could not remove userlist.")
                main()
        else:
            print("Only ROOT users can do this!")
            if return_mode == 0:
                main()
            else:
                return True
    elif ch == "man":
        print("man [manual]")
        print("For manual list, type man /")
        print("For help with man, type man man")
        if return_mode == 0:
            main()
        else:
            return True
    elif ch.startswith("man "):
        man(ch[4:],return_mode)
        if return_mode == 1:
            main()
        print(f"{upper(ch)} IS NOT A VALID COMMAND, PROGRAM OR MANUAL.")
        main()
    elif ch == "userlist_c" or ch == "userlist -c":
        if is_root() == True:
            div()
            for item in data:
                print(item[0])
            div()
            if return_mode == 0:
                main()
            else:
                return True
        else:
            print("Only ROOT users can use this command.")
            if return_mode == 0:
                main()
            else:
                return True
    elif ch == "update" and return_mode == 0:
        if isinstance(app_version[2],str) == True:
            print("Unable to check for updates.")
            main()
        import urllib.request

        url = "http://winfan3672.000webhostapp.com/version_check/pythinux.version"
        print("Checking for updates...")
        print(
            f"Current Version: v{app_version[0]}.{app_version[1]}.{app_version[2]}"
        )
        try:
            urllib.request.urlretrieve(url, "pythinux.version")
        except Exception as e:
            crashlog.append(str(e))
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
            if return_mode == 0:
                main()
            else:
                return True
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
        if return_mode == 0:
            main()
        else:
            return True
    elif "vim " in ch:
        vim(ch[4:])
    elif ch == "vim" and return_mode == 0:
        div()
        vim()
    elif ch == "files" and return_mode == 0:
        if is_root() == True:
            os.chdir(os.getcwd())
            files(os.getcwd(),1)
        else:
            files(os.getcwd(),1,1)
    elif ch == "run":
        div()
        print("run [program name]")
        print("Runs an installed SZIPS program.")
        div()
        print("Custom launch options:")
        print("`run /`: lists all installed programs")
        div()
        main()
    elif ch == "run /":
        print(os.listdir(os.getcwd()+"/Installed Programs"))
        main()
    elif ch.startswith("run ") and return_mode == 0:
        ch=ch[4:]
        if run(ch) == False:
            print("Failed to run program.")
            print("Try:")
            print("[-] Checking that the program is spelt correctly")
            print("[-] Rebooting the OS")
            print("[-] Reinstalling the program")
            print("[-] Reinstalling the OS")
            print("[-] Contacting the program developer")
        os.chdir(startpoint)
        main()
    elif ch == "./" and return_mode == 0:
        print("./[name of .xx file]")
        print("For instructions, type MAN SCRIPTING or MAN XX")
        main()
    elif "./" in ch and return_mode == 0 or allow_script == 1:
        consent_mode = 0
        try:
            f=open(f"Users/{username}/Scripts/"+ch[2:]+".xx","r")
            data=f.read()
            f.close()
            run_script(data.split("\n"))
            consent_mode = 0
            main()
        except Exception as e:
            crashlog.append(str(e))
            print("Could not run script.")
            consent_mode = 0
            main()
        if return_mode == 0:
            main()
        else:
            return True
    elif ch == "div()" and return_mode == 1:
        div()
        return True
    elif ch == "cat" and return_mode == 0:
        print("CAT [url] [filename]")
        print("Downloads [url] and saves it to [filename]")
        main()
    elif ch.startswith("cat "):
        ch=ch.split(" ",2)
        if len(ch) == 3:
            try:
                import urllib.request
                url = ch[1]
                saveas=ch[2]
                print("Downloading...")
                try:
                    urllib.request.urlretrieve(url, saveas)
                    print("Downloaded.")
                except Exception as e:
                    crashlog.append(str(e))
                    raise Exception
            except Exception as e:
                crashlog.append(str(e))
                print("FAILED.")
        else:
            if return_mode == 0:
                print("Invalid parameters.")
        if return_mode == 0:
            main()
        else:
            return True
    elif ch == "terminal" and return_mode == 0:
        print("To exit the TERMINAL, type %%exit")
        terminal()
    elif ch.startswith("cmd -e "):
        try:
            f=open(ch[7:],"r")
            data=f.read()
            f.close()
            data=data.split("\n")
            for item in data:
                os.system(item)
        except Exception as e:
            crashlog.append(str(e))
            print("Failed to run script.")
        main()
    elif ch.startswith("cmd ") and return_mode == 1:
        os.system(ch[4:])
        return True
    elif ch == "stdlib" and return_mode == 0:
        div()
        print(f"STDLIB Installed: {is_stdlib()}")
        if is_stdlib() == True:
            print(f"Version: {stdlib.app_version_str}")
        if is_stdlib == False:
            print("To install Standard Library, type INSTALL STDLIB")
        div()
        print("STDLIB --HELP for help")
        main()
    elif ch == "stdlib --help" and return_mode == 0:
        print("STDLIB <parameter>")
        print("<only supports 1 parameter at a time")
        print("Valid parameters:")
        print("--help = Displays help")
        print("--help-stdlib = Shows stdlib.help()")
        print("--console = Opens STDLIB console")
        print("--install = Installs STDLIB from stdlib.py")
        print("--remove = Uninstalls Standard library")
        main()
    elif ch == "stdlib --help-stdlib" and return_mode == 0:
        if is_stdlib() == True:
            main("cls")
            stdlib.help()
            main()
        else:
            print("Standard Library not installed.")
            main()
    elif ch == "stdlib --install" and return_mode == 0:
        try:
            try:
                del(stdlib)
            except Exception as e:
                crashlog.append(str(e))
                pass
            import stdlib
            print("Installed successfully.")
            print(f"Version: {stdlib.app_version_str}")
        except Exception as e:
            crashlog.append(str(e))
            print("Could not install Standard library.")
        main()
    elif ch == "install consent_guide" and return_mode == 0:
        div()
        print("Consent Mode Guide")
        div()
        print("In a script, certain functions are disallowed for security reasons.")
        print("However, there may be genuine reasons for using said functions.")
        print("This is where Consent Mode comes in.")
        print("In a `xx` script, you can call `consent_mode` and a Consent Mode screen will appear.")
        div()
        print("#Example script")
        print("echo This is now the script")
        print("consent_mode")
        div()
        print("If you run the code, a Consent Mode message appears, asking the user to type `YES` in order to allow for extended functionality.")
        print("In order to prevent breaking your program, `consent_check` can be called. If no consent is given, an error is thrown and the script ends.")
        print("To revoke consent, call `revoke_consent`. This is automatically done when the script ends.")
        br()        
        main()
    elif ch == "install numpy":
        try:
            import numpy
            print("Numpy already installed.")
            if return_mode == 0:
                main()
            else:
                return True
        except Exception as e:
            crashlog.append(str(e))
            os.system("pip install numpy")
            os.system("pip3 install numpy")
            try:
                import numpy
                del(numpy)
                print("Successfully installed numpy.")
            except Exception as e:
                crashlog.append(str(e))
                print("Failed to install numpy.")
            if return_mode == 0:
                main()
            else:
                return True
    elif ch == "install cman_demo":
        print("Custom Manual Demo")
        print("Command list: help")
        print("To exit: return")
        cman_demo()
    elif ch == "install tree_demo":
        print("To see the demo, type TREE.")
        print("To exit, type EXIT.")
        tree_demo()
    elif ch == "install" and return_mode == 0:
        print("install <program>")
        print("Installs <program> and imports it.")
        div()
        print("Valid programs:")
        print("stdlib numpy consent_guide cman_demo tree_demo")
        main()
    elif ch == "install --help" and return_mode == 0:
        print("install <program> OR install <parameter>")
        print("For a list of installable programs, type install --list.")
        div()
        print("Parameters [Use one at a time]:")
        print("--help = Shows this menu")
        print("--list = Lists all installable programs")
        main()
    elif ch == "install --list" and return_mode == 0:
        print("stdlib numpy consent_guide cman_demo tree_demo")
        main()
    elif ch == "stdlib --remove" and return_mode == 0:
        try:
            del(stdlib)
        except Exception as e:
            crashlog.append(str(e))
            pass
        main()
    elif ch == "stdlib --console" and return_mode == 0:
        install_stdlib()
        print("Type %%exit to exit STDLIB console")
        while True:
            ch=input(">")
            if ch == "%%exit":
                break
            stdlib.console(ch)
        main()
    elif ch == "cls -s":
        install_stdlib()
        stdlib.cls()
        if return_mode == 0:
            main()
        else:
            return True
    elif ch == "install stdlib":
        print("Installing Standard Library v0.0.1...")
        import base64
        f=open("stdlib.py","wb")
        f.write(base64.b64decode("'aW1wb3J0IG9zDQpmcm9tIHBsYXRmb3JtIGltcG9ydCB1bmFtZQ0KaW1wb3J0IGJhc2U2NA0KYXBwX3ZlcnNpb24gPSBbMCwwLDFdDQphcHBfdmVyc2lvbl9zdHIgPSAiMC4wLjEiDQoNCiMgUHl0aGludXggU3RhbmRhcmQgTGlicmFyeQ0KZGVmIGhlbHAoKToNCiAgICBwcmludCgiVGhlIFB5dGhpbnV4IFN0YW5kYXJkIExpYnJhcnkgYWxsb3dzIHlvdSB0byBhY2Nlc3MgY29vbCBBUEkgc3R1ZmYuXG4iKQ0KICAgIHByaW50KCIxIEltcGxlbWVudGluZyBJbiBQcm9ncmFtIikNCiAgICBwcmludCgiSW4gb3JkZXIgdG8gYWRkIHRoZSBTVERMSUIgaW50byB5b3VyIHByb2dyYW0sIHBsYWNlIHRoZSBmb2xsb3dpbmcgbGluZSBhdCB0aGUgdG9wIG9mIHlvdXIgY29kZToiKQ0KICAgIHByaW50KCJcbmltcG9ydCBzdGRsaWIiKQ0KICAgIHByaW50KCJcblRoaXMgd2lsbCBhbGxvdyB5b3UgdG8gYWNjZXNzIGV2ZXJ5IGZ1bmN0aW9uIG9mIHN0ZGxpYi4iKQ0KZGVmIHZlcnNpb25fY2hlY2sodmVyLGlzX3N0cj0xKToNCiAgICAjIElmIGlzX3N0ciA9IDAgaXQgY2hlY2tzIGFnYWluc3QgYXBwX3ZlcnNpb24sIGlmIDEgaXQgY2hlY2tzIGFnYWluc3QgYXBwX3ZlcnNpb25fc3RyICAgIA0KICAgIGlmIGlzX3N0ciA9PSAwIGFuZCB2ZXIgPT0gYXBwX3ZlcnNpb246DQogICAgICAgIHJldHVybiBUcnVlDQogICAgZWxpZiBpc19zdHIgPT0gMSBhbmQgdmVyID09IGFwcF92ZXJzaW9uX3N0cjoNCiAgICAgICAgcmV0dXJuIFRydWUNCiAgICBlbHNlOg0KICAgICAgICByZXR1cm4gRmFsc2UNCmRlZiBjbHMoKToNCiAgICByZXM9dW5hbWUoKQ0KICAgIG9zLnN5c3RlbSgiY2xzIiBpZiByZXNbMF0gPT0gIldpbmRvd3MiIGVsc2UgImNsZWFyIikNCmRlZiBjb25zb2xlKGNtZCk6DQogICAgaWYgY21kID09ICJoZWxwIjoNCiAgICAgICAgcHJpbnQoImhlbHAgPSB0aGlzIG1lbnUiKQ0KICAgICAgICBwcmludCgiY2xzID0gY2xzKCkiKQ0KICAgICAgICBwcmludCgiaGVscCAtLXN0ZGxpYiA9IGhlbHAoKSIpDQogICAgICAgIHByaW50KCJnZmQgPGZpbGVuYW1lPiA9IFByaW50IGZpbGUgZGF0YSBvZiA8ZmlsZW5hbWU+IikNCiAgICAgICAgcmV0dXJuIE5vbmUNCiAgICBlbGlmIGNtZCA9PSAiY2xzIjoNCiAgICAgICAgY2xzKCkNCiAgICBlbGlmIGNtZC5zdGFydHN3aXRoKCJnZmQgIik6DQogICAgICAgIHByaW50KGdldF9maWxlX2RhdGEoY21kWzQ6XSkpDQogICAgZWxpZiBjbWQgPT0gImhlbHAgLS1zdGRsaWIiOg0KICAgICAgICBoZWxwKCkNCmRlZiBnZXRfZmlsZV9kYXRhKGZuLG1vZGU9InIiKToNCiAgICB0cnk6DQogICAgICAgIGY9b3Blbihmbixtb2RlKQ0KICAgICAgICBkYXRhPWYucmVhZCgpDQogICAgICAgIGYuY2xvc2UoKQ0KICAgICAgICByZXR1cm4gZGF0YQ0KICAgIGV4Y2VwdDoNCiAgICAgICAgcmV0dXJuIE5vbmUNCmRlZiBiNjRlKGRhdGEpOg0KICAgIHJldHVybiBiYXNlNjQuYjY0ZW5jb2RlKGRhdGEpLmRlY29kZSgiYXNjaWkiKQ0KZGVmIGI2NGQoZGF0YSk6DQogICAgcmV0dXJuIGJhc2U2NC5iNjRkZWNvZGUoZGF0YSkNCmRlZiBpc2ZpbGUoZm4pOg0KICAgIHJldHVybiBvcy5wYXRoLmlzZmlsZShmbikNCg=='"))
        f.close()
        install_stdlib()
        print("Successfully installed standard library.")
        if return_mode == 0:
            main()
        else:
            return True
    elif ch == "revoke_consent":
        consent_mode = 0
        if return_mode == 0:
            main()
        else:
            return True
    elif ch.startswith("#") and return_mode == 1:
        return True
    elif ch == "consent_mode" and return_mode == 1:
        print("The current program is asking for elevated priveleges.")
        print("In order to allow these priveleges, type YES [exactly as I put ut]")
        if input("$") == "YES":
            consent_mode = 1
        else:
            consent_mode = 0
            print("Consent not provided.")
        return True
    elif ch == "consent_check" and return_mode == 1:
        print(consent_mode)
        if consent_mode == 1:
            return True
        else:
            print("The program has requested elevated priveleges.")
            print("Due to a lack of elevated priveleges, it cannot run.")
            main()
    elif ch == "add_alias" and return_mode == 0:
        if os.path.isfile(f"Users/{username}/User Settings/alias.dat") == False:
            f=open(f"Users/{username}/User Settings/alias.dat","w")
            f.close()
        f=open(f"Users/{username}/User Settings/alias.dat","a")
        inp1=input("Alias >>")
        inp1=inp1.replace("|","")
        inp2=input("Command >>")
        inp2=inp2.replace("|","")
        f.write(f"{inp1}|{inp2}\n")
        f.close()
        main()
    elif ch == "alias --add-global" and return_mode == 0:
        if os.path.isfile(f"System Settings/alias.dat") == False:
            f=open(f"System Settings/alias.dat","w")
            f.close()
        f=open(f"System Settings/alias.dat","a")
        inp1=input("Alias >>")
        inp1=inp1.replace("|","")
        inp2=input("Command >>")
        inp2=inp2.replace("|","")
        f.write(f"{inp1}|{inp2}\n")
        f.close()
        main()
    elif ch == "alias" and return_mode == 0:
        div()
        print("alias <parameter>")
        print("Only 1 parameter at a time")
        div()
        print("Parameters:")
        print("--list = Lists all aliases")
        print("--list-plus = Lists all aliases and all their respective commands")
        print("--remove = Remove a local alias")
        print("--clear = Remove all aliases")
        print("--list-global = Lists all global aliases")
        print("--add-global = adds a global alias")
        print("--remove-global = removes a global alias")
        div()
        print("man alias to learn more about aliases")
        main()
    elif ch =="alias --clear":
        f=open(f"Users/{username}/User Settings/alias.dat","w")
        f.close()
        if return_mode == 0:
            main()
        else:
            return True
    elif ch == "alias --remove":
        try:
            f=open(f"Users/{username}/User Settings/alias.dat","r")
            aliases=f.read()
            f.close()
            aliases=aliases.split("\n")
            a2=[]
            for item in aliases:
                a2.append(item.split("|"))
            ch=input("Alias >>")
            for item in a2:
                if item[0] == ch:
                    a2.remove(item)
                if item == [""]:
                    a2.remove(item)
            a3=[]
            for item in a2:
                a3.append("|".join(item))
            a4=""
            for item in a3:
                a4 += f"{item}\n"
            f=open(f"Users/{username}/User Settings/alias.dat","w")
            f.write(a4)
            f.close()
            print(f"Successfully deleted alias {ch}.")
        except Exception as e:
            crashlog.append(str(e))
            print("Could not perform deletion operation.")
        main()
    elif ch == "alias --remove-global":
        try:
            f=open(f"System Settings/alias.dat","r")
            aliases=f.read()
            f.close()
            aliases=aliases.split("\n")
            a2=[]
            for item in aliases:
                a2.append(item.split("|"))
            ch=input("Alias >>")
            for item in a2:
                if item[0] == ch:
                    a2.remove(item)
                if item == [""]:
                    a2.remove(item)
            a3=[]
            for item in a2:
                a3.append("|".join(item))
            a4=""
            for item in a3:
                a4 += f"{item}\n"
            f=open(f"System Settings/alias.dat","w")
            f.write(a4)
            f.close()
            print(f"Successfully deleted alias {ch}.")
        except Exception as e:
            crashlog.append(str(e))
            print("Could not perform deletion operation.")
        main()
    elif ch == "alias --list" and return_mode == 0:
        try:
            f=open(f"Users/{username}/User Settings/alias.dat","r")
            data=f.read()
            f.close()
            data=data.split("\n")
            data2=[]
            for item in data:
                if item != "":
                    item=item.split("|")
                    data2.append(item[0])
            for item in data2:
                print(item)
            main()
        except Exception as e:
            crashlog.append(str(e))
            print("Could not perform command; Perhaps no aliases exist.")
            main()
    elif ch == "alias --list-global" and return_mode == 0:
        try:
            f=open(f"System Settings/alias.dat","r")
            data=f.read()
            f.close()
            data=data.split("\n")
            data2=[]
            for item in data:
                if item != "":
                    item=item.split("|")
                    data2.append(item[0])
            for item in data2:
                print(item)
            main()
        except Exception as e:
            crashlog.append(str(e))
            print("Could not perform command; Perhaps no aliases exist.")
            main()
    elif ch == "alias --list-plus" and return_mode == 0:
        try:
            f=open(f"Users/{username}/User Settings/alias.dat","r")
            data=f.read()
            f.close()
            data=data.split("\n")
            data2=[]
            for item in data:
                try:
                    item=item.split("|")
                    data2.append(f"{item[0]} = {item[1]}")
                except Exception as e:
                    crashlog.append(str(e))
                    pass
            for item in data2:
                print(item)
            main()
        except Exception as e:
            crashlog.append(str(e))
            print("Could not perform command; Perhaps no aliases exist.")
            main()    
    elif ch == "idle-launch":
        try:
            import idlelib.idle
            import sys
            del sys.modules["idlelib.idle"]
        except Exception as e:
            crashlog.append(str(e))
            print("Could not launch IDLE:")
            print("[-] IDLE is not installed by default on your system")
            print("[-] You do not have a graphics driver installed.")
        if return_mode == 0:
            main()
        else:
            return True
    elif ch == "mem --help":
        man("mem")
    elif ch == "mem --backup" or ch == "mem -b":
        try:
            f=open("mem.pythinux","w")
            f.write(str(mem))
            f.close()
        except Exception as e:
            crashlog.append(str(e))
            print("Could not save MEM.")
        if return_mode == 0:
            main()
        else:
            return None
    elif ch == "mem --restore" or ch == "mem -rs":
        try:
            f=open("mem.pythinux","r")
            mem=float(f.read())
            f.close()
        except Exception as e:
            crashlog.append(str(e))
            print("Could not restore MEM. Does a backup exist?")
        if return_mode == 0:
            main()
        else:
            return None
    elif ch == "mem":
        div()
        print("mem <parameter>")
        div()
        print("Parameters")
        div()
        print("--help\n--view -v\n--set\n--reset -r\n--add\n--sub\n--backup -b\n--restore -rs")
        div()
        if return_mode == 0:
            main()
        else:
            return None
    elif ch == "mem --view" or ch == "mem -v":
        print(mem)
        if return_mode == 0:
            main()
        else:
            return None
    elif ch.startswith("mem --add ") == True:
        try:
            mem += float(ch[10:])
        except Exception as e:
            crashlog.append(str(e))
            print("Failed to set MEM.")
        if return_mode == 0:
            main()
        else:
            return None
    elif ch.startswith("mem --sub "):
        try:
            mem -= float(ch[10:])
        except Exception as e:
            crashlog.append(str(e))
            print("Failed to set MEM.")
        if return_mode == 0:
            main()
        else:
            return None
    elif ch == "mem --set":
        print("mem --set <float>")
        print("sets mem to <float>")
        if return_mode == 0:
            main()
        else:
            return None
    elif ch == "mem --reset" or ch == "mem -r":
        mem=0
        if return_mode == 0:
            main()
        else:
            return None
    elif ch.startswith("mem --set ") == True:
        try:
            mem = float(ch[10:])
        except Exception as e:
            crashlog.append(str(e))
            print("Failed to set.")
        if return_mode == 0:
            main()
        else:
            return None
    elif ch.startswith("prompt "):
        prompt=ch[7:]
        if return_mode == 0:
            main()
        else:
            return True
    elif ch == "prompt":
        print("Prompt <str>")
        print("Replace prompt with <str>")
        print("To reset the prompt, type `prompt `.")
        if return_mode == 0:
            main()
        else:
            return True
    elif ch == "var":
        print("var [parameter] <var_name> <value>")
        print("Parameters:")
        print("set <var_name> <value>")
        print("print <var_name>")
        print("list")
        print("del <var_name>")
        print("backup <filename>")
        print("restore <filename>")
        if return_mode == 0:
            main()
        else:
            return True
    elif ch == "var list":
        print(var_data)
        if return_mode == 0:
            main()
        else:
            return True
    elif ch.startswith("var set "):
        ch=ch.split(" ",3)
        ch=ch[2:]
        if len(ch) == 2:
            var_data2=[]
            for item in var_data:
                if item[0] == ch[0]:
                    continue
                else:
                    var_data2.append(item)
            var_data=var_data2
            del(var_data2)
            var_data.append([ch[0],ch[1]])
        else:
            print("NO")
        if return_mode == 0:
            main()
        else:
            return True
    elif ch.startswith("var print "):
        ch=ch[10:]
        is_find = 0
        for item in var_data:
            if item[0] == ch:
                print(item[1])
                is_find=1
                break
        if is_find == 0:
            print(f"Could not find variiable {ch[0]}")
        if return_mode == 0:
            main()
        else:
            return True
    elif ch.startswith("var del "):
        ch=ch[8:]
        for item in var_data:
            if item[0] == ch:
                var_data.remove(item)
                print(f"Removed {ch}")
        if return_mode == 0:
            main()
        else:
            return True
    elif ch.startswith("var backup "):
        try:
            import pickle
            f=open(ch[11:]+".vbkp","wb")
            pickle.dump(var_data,f)
            f.close()
            print("Successful Backup.")
        except Exception as e:
            crashlog.append(str(e))
            print("Backup Failed.")
        if return_mode == 0:
            main()
        else:
            return True
    elif ch.startswith("var restore "):
        try:
            f=open(ch[12:]+".vbkp","rb")
            import pickle
            var_data=pickle.load(f)
            f.close()
            print("Restore successful.")
        except Exception as e:
            crashlog.append(str(e))
            print("Failed to restore.")
        if return_mode == 0:
            main()
        else:
            return True
    elif ch == "echf":
        print("echf [filename] [text]")
        print("Saves [text] to [filename]")
        main()
    elif ch.startswith("echf "):
        try:
            ch=ch.split(" ",2)
            f=open(ch[1],"w")
            f.write(ch[2])
            f.close()
        except Exception as e:
            crashlog.append(str(e))
            print("Write failed.")
        main()
    elif ch == "wget":
        print("wget [url]")
        print("Wget downloads the file from [url] and saves it, picking the filename automatically.")
        main()
    elif ch.startswith("wget "):
        try:
            import urllib.request
            url=ch[5:]
            saveas=url.split("/")
            s2=[]
            for item in saveas:
                if item != "":
                    s2.append(item)
            saveas=s2
            saveas=saveas[len(saveas)-1]
            print("Downloading...")
            urllib.request.urlretrieve(url, saveas)
            print(f"Download successful, saved as {saveas}.")
        except Exception as e:
            crashlog.append(str(e))
            print("Failed to download file.")
        main()
    elif ch =="user_editor" and is_root() == True:
        user_editor_v2()
    elif ch == "qar" and return_mode == 0:
        print("qar <alias>")
        print("Removes all instances of <alias> from your aliases.")
        main()
    elif ch.startswith("qar "):
        ch=ch[4:]
        try:
            f=open(f"Users/{username}/User Settings/alias.dat","r")
            d=f.read()
            d=d.split("\n")
            f.close()
            d2=[]
            for i in d:
                d2.append(i.split("|"))
            d2 = [x for x in d2 if x[0] != ch]
            d2.remove([""])
            d3=[]
            for i in d2:
                d3.append("|".join(i))
            f=open(f"Users/{username}/User Settings/alias.dat","w")
            for i in d3:
                f.write(i+"\n")
            f.close()
            if return_mode == 0:
                main()
            else:
                return True
        except Exception as e:
            crashlog.append(str(e))
            main()
    elif ch == "qaa":
        print("qaa [alias]|[command]")
        print("Quickly adds alias to the system.")
        main()
    elif ch == "qaag":
        print("qaag [alias]|[command]")
        print("Like `qaa` but global.")
        main()
    elif ch.startswith("qaa "):
        ch=ch[4:]
        chh=ch.split("|")
        print(f"[ALIAS] {chh[0]} --> {chh[1]}")
        if os.path.isfile(f"Users/{username}/User Settings/alias.dat") == False:
            f=open(f"Users/{username}/User Settings/alias.dat","w")
            f.close()
        f=open(f"Users/{username}/User Settings/alias.dat","a")
        f.write(f"{ch}\n")
        f.close()
        if return_mode == 0:
            main()
        else:
            return True
    elif ch.startswith("qaag "):
        ch=ch[5:]
        if os.path.isfile(f"System Settings/alias.dat") == False:
            f=open(f"System Settings/alias.dat","w")
            f.close()
        f=open(f"Users/{username}/User Settings/alias.dat","a")
        f.write(f"{ch}\n")
        f.close()
        if return_mode == 0:
            main()
        else:
            return True
    elif ch == "removed":
        print("Removed [installed program]")
        print("Uninstalls an installed SZIPS v2 program.")
        if return_mode == 0:
            main()
        else:
            return True
    elif ch.startswith("removed "):
        removed(ch[8:])
        if return_mode == 0:
            main()
        else:
            return True
    elif ch == "installd":
        print("installd [/path/to/installer]")
        print("Installs a program from a .szip file.")
        main()
    elif ch.startswith("installd "):
        if ch.endswith(".szip") == False:
            installd(ch[9:]+".szip")
        else:
            installd(ch[9:])
        if return_mode == 0:
            main()
        else:
            return True
    elif ch.startswith("pkm remove "):
        main(f"removed {ch[11:]}")
        if return_mode == 0:
            main()
        else:
            return True
    elif ch == "pkm version":
        print("PKM Package Manager")
        print("Version 1.1.0")
        print(f"OS Version: {app_version[0]}.{app_version[1]}.{app_version[2]}")
        print("Build Date: 11 Feb 2023")
        print("(c) 2023 WinFan3672, Some Rights Reserved.")
        if return_mode == 0:
            main()
        else:
            return True
    elif ch == "pkm version -c":
        print(f"PKM Version 1.1.0 : OS Version {app_version[0]}.{app_version[1]}.{app_version[2]}")
        if return_mode == 0:
            main()
        else:
            return True
    elif ch == "pkm":
        div()
        print("pkm [parameter]")
        div()
        print("Parameters:")
        print("install <program>: installs <program>")
        print("search <program>: searches for <program>")
        print("remove <program>: uninstalls installed <program>")
        print("list: lists all installed programs")
        print("all: lists all installable and installed packages")
        print("update: refreshes package list from DB's")
        print("upgrade: updates all packages")
        print("db: manipulates installed DB's.")
        print("version: displays version information about pkm")
        print("version -c: shows less detailed information about pkm")
        print("?: opens pkm's manpage")
        div()
        if return_mode == 0:
            main()
        else:
            return True
    elif ch == "pkm ?":
        main("man pkm")
        main()
    elif ch == "pkm upgrade":
        main("pkm update")
        ip=os.listdir(os.getcwd()+"/Installed Programs")
        for i in ip:
            main(f"pkm install -y {i}")
        print("Package upgrade finished.")
        main()
    elif ch.startswith("pkm search "):
        term=ch[11:]
        results=[]
        for item in packages:
            if term in item[0]:
                results.append(item)
        if results == []:
            print("Found no results.")
        else:
            print(f"Found [{len(results)}] result[s]:")
            div()
            for item in results:
                print(item[0])
                print("    "+item[1])
                div()
        if return_mode == 0:
            main()
        else:
            return True
    elif ch.startswith("pkm install -y "):
        term=ch[15:]
        for item in packages:
            if item[0] == term:
                if item[2] == "about:blank":
                    print("Error: Program does not have a download link.")
                    if return_mode == 0:
                        main()
                    else:
                        return True
                print(f"[DOWNLOAD] {item[2]}")
                import urllib.request
                try:
                    try:
                        os.remove("Cached Data/pkm.szip")
                    except Exception as e:
                        crashlog.append(str(e))
                        pass
                    urllib.request.urlretrieve(item[2],"Cached Data/pkm.szip")
                    installd("Cached Data/pkm.szip",1)
                    if return_mode == 0:
                        main()
                    else:
                        return True
                except Exception as e:
                    crashlog.append(str(e))
                    print(f"[FAIL] Download {item[2]}")
                    if return_mode == 0:
                        main()
                    else:
                        return True
        print(f"Could not find package {term}.")
        if return_mode == 0:
            main()
        else:
            return True
        main()
    elif ch.startswith("pkm install "):
        main("pkm update")
        term=ch[12:]
        for item in packages:
            if item[0] == term:
                if item[2] == "about:blank":
                    print("Error: Program does not have a download link.")
                    if return_mode == 0:
                        main()
                    else:
                        return True
                print("Downloading program...")
                print(f"[DOWNLOAD] {item[2]}")
                import urllib.request
                try:
                    try:
                        os.remove("Cached Data/pkm.szip")
                    except Exception as e:
                        crashlog.append(str(e))
                        pass
                    urllib.request.urlretrieve(item[2],"Cached Data/pkm.szip")
                    main("installd Cached Data/pkm.szip")
                    if return_mode == 0:
                        main()
                    else:
                        return True
                except Exception as e:
                    crashlog.append(str(e))
                    print(f"[FAIL] Download {item[2]}")
                    if return_mode == 0:
                        main()
                    else:
                        return True
        print(f"Could not find package {term}.")
        if return_mode == 0:
            main()
        else:
            return True
    elif ch == "pkm search":
        print("pkm search <term>")
        print("Searches all installable packages and returns a list")
        if return_mode == 0:
            main()
        else:
            return True
    elif ch == "pkm list":
        ip=os.listdir(os.getcwd()+"/Installed Programs")
        for i in ip:
            print(f"[-] {i}")
        if return_mode == 0:
            main()
        else:
            return True
    elif ch == "pkm update":
        packages=[]
        print("Updating packages...")
        import urllib.request
        for item in dbs:
            url=item
            print(f"[DOWNLOAD] {url}")
            try:
                urllib.request.urlretrieve(url, "Cached Data/pkm.pkm")
                f=open("Cached Data/pkm.pkm","r")
                d=f.read()
                f.close()
                d=d.split("\n")
                for item in d:
                    packages.append(item.split("|"))
            except:
                print(f"[FAIL] Download data from {item}")
        print("Updated packages.")
        if return_mode == 0:
            main()
        else:
            return True
    elif ch == "pkm db":
        div()
        print("pkm db [parameter]")
        div()
        print("Parameters:")
        print("add <url>: Adds <url> to DB's")
        print("list: lists all DB's")
        print("remove <url>: remove <url> from DB's.")
        print("save: saves DB list to OS.")
        print("load: retreives DB list from OS.")
        print("reset: resets DB list to OS default")
        div()
        print("Note: If you save the database list, it is loaded on startup")
        div()
        if return_mode == 0:
            main()
        else:
            return True
    elif ch == "pkm db list":
        print(dbs)
        main()
    elif ch == "pkm db save":
        import pickle
        f=open("System Settings/pkm.db","wb")
        f.write(pickle.dumps(dbs))
        f.close()
        main()
    elif ch == "pkm db reset":
        dbs=["https://winfan3672.000webhostapp.com/pkm/official.pkm"]
        main()
    elif ch == "pkm db load":
        import pickle
        try:
            f=open("System Settings/pkm.db","rb")
            dbs=pickle.loads(f.read())
            f.close()
            main()
        except Exception as e:
            crashlog.append(str(e))
            print("FAIL")
    elif ch.startswith("pkm db add "):
        ch=ch[11:]
        dbs.append(ch)
        main()
    elif ch.startswith("pkm db remove "):
        ch=ch[14:]
        dbs.remove(ch)
        main()
    elif ch == "pkm all":
        main("pkm update")
        div()
        for item in packages:
            print(item[0])
            print("    "+item[1])
            div()
        if return_mode == 0:
            main()
        else:
            return True
    elif ch == "censor":
        main("prompt [$utype] $")
        main()
    elif ch == "view_log":
        if crashlog == []:
            print("No errors.")
        else:
            print("Errors:")
            for item in crashlog:
                print(item)
        if return_mode == 0:
            main()
        else:
            return True
    elif ch == "login":
        un=input("Username $")
        pw=getpass.getpass("Password $")
        login(2,un,sha256(pw))
    elif ch == "reinstall" and return_mode == 0:
        if is_god() == True:
            if auth() == True:
                os.chdir("..")
                import shutil
                shutil.rmtree("Pythinux")
                os.mkdir("Pythinux")
                os.chdir("Pythinux")
                setup_wizard()
                os_init()
            else:
                print("User operation cancelled.")
                main()
        else:
            print("Requires GOD user priveleges.")
            main()
    else:
        if return_mode == 0:
            f=open("System Settings/alias.dat","r")
            dat=f.read()
            f.close()
            dat += "\n"
            ff=open(f"Users/{username}/User Settings/alias.dat","r")
            dat+=ff.read()
            ff.close()
            dat=dat.split("\n")
            data2=[]
            for item in dat:
                item=item.split("|")
                data2.append(item)
            dat=data2
            for item in dat:
                if ch == item[0]:
                    main(item[1],0,0)
                    main()
        if return_mode == 0:
            print(f"{upper(ch)} IS NOT A VALID COMMAND, PROGRAM, ALIAS, SCRIPT OR MANUAL.")
            if is_stdlib() == False:
                print("NOTE: STANDARD LIBRARY NOT INSTALLED.")
            if os.path.isfile(os.getcwd()+"/.noalias") == True:
                print("NOTE: ALIASES HAVE BEEN DISABLED BY YOUR ADMINISTRATOR.")
        if return_mode == 0:
            main()
        else:
            return True
        
def start(lvl,al,alpassword=""):
    global crashlog
    global username, password, user_lvl, user_type
    password=sha256(password)
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
    if al == 0:
        print(f"Welcome to {os_name}.")
        print(f"[{os_name} v{app_version[0]}.{app_version[1]}.{app_version[2]}]")
        div()
        if user_lvl == 0:
            print("You are logged in on a guest account.")
            print("Guest accounts have limited access to commands and cannot install/remove programs.")
        elif user_lvl == 1:
            pass
        elif user_lvl == 2:
            print("You are logged in as a root account.")
            print("If you do not know what this means, type LOGOFF right now.")
            print("DO NOT USE A ROOT ACCOUNT AS YOUR DAILY DRIVER ACCOUNT.")
        elif user_lvl == 3:
            print("Warning! GOD users have very high priveleges and are fully unrestricted.")
            print("Exercise caution and common sense when using a God account.")
            print("If you are unaware of the security implications of using a God account, or what any of this means, type LOGOFF right now.")
            print("DO NOT USE A GOD ACCOUNT AS YOUR DAILY DRIVER ACCOUNT.") 
    if al == 1:
        main("cls")
        div()
        print("Autologin Security")
        div()
        print("For security, enter your password:")
        while True:
            newpass=getpass.getpass("Password $")
            if sha256(sha256(newpass)) == password:
                password=sha256(newpass)
                break
        main("cls")
    if user_lvl >= 1:
        if os.path.isfile(os.getcwd()+"/System Settings/.startup") == True:
            try:
                f=open("System Settings/.startup","r")
                sdata=f.read()
                f.close()
                sdata=sdata.split("\n")
                for item in sdata:
                    main(item,1)
            except Exception as e:
                crashlog.append(str(e))
                pass  
    main()
def login(al=0,al_username="root",al_password="root"):
    global crashlog
    global username, password, user_lvl, user_type, autologin, data
    if data == []:
        div()
        print("[Your user file is corrupt. Please delete it.]")
        div()
        data = [[]]
    if al == 1:
        base=f"{al_username}:{al_password}"
        sh_base = f"{al_username}:{sha256(al_password)}"
        username,password=f"{al_username}",f"{al_password}"
    elif al == 2:
        base=f"{al_username}:{al_password}"
        for item in data:
            if base == f"{item[0]}:{item[1]}":
                username,password=al_username,al_password
                main()
    else:
        al_password=""
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
        if username == "//ul":
            l=[]
            for item in data:
                l.append(item[0])
            print(l)
            login()
        password=getpass.getpass("Password $")
        div()
        base=f"{username}:{password}"
        sh_base=f"{username}:{sha256(password)}"
    for item in data:
        try:
            if base == f"{item[0]}:{item[1]}":
                start(int(item[2]),al,al_password)
            elif sh_base == f"{item[0]}:{item[1]}":
                start(int(item[2]),al,al_password)
        except Exception as e:
            crashlog.append(str(e))
            continue
    print("Username or password is invalid.")
    login()
def os_init():
    global crashlog
    global username, password, user_lvl, user_type, user_type
    global startpoint
    refresh_data()
    try:
        f=open("System Settings/autologin.dat")
        aldata=f.read()
        f.close()
        aldata=aldata.split("|")
        login(1,aldata[0],aldata[1])
    except Exception as e:
        crashlog.append(str(e))
        login(autologin)
try:
    print(os.getcwd())
    os.chdir("Pythinux")
    startpoint=os.getcwd()
except Exception as e:
    crashlog.append(str(e))
    print("did")
    os.mkdir("Pythinux")
    os.chdir("Pythinux")
    setup_wizard()
try:
    f=open("System Settings/userlist.pythinux","r")
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
except Exception as e:
    crashlog.append(str(e))
    f=open("System Settings/userlist.pythinux","w")
    f.close()
    f=open("System Settings/userlist.pythinux","r")
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
try:
    f=open("System Settings/pkm.db","rb")
    import pickle
    dbs=pickle.loads(f.read())
    f.close()
except Exception as e:
    crashlog.append(str(e))
    dbs=["https://winfan3672.000webhostapp.com/pkm/official.pkm"]
os_init()
