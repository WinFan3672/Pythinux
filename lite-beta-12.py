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
global os_name, app_version, autologin
global username, password, user_lvl, user_type, user_type
import getpass
from time import ctime, strftime, sleep
import os
from secrets import choice

# OS INFORMATION CONTAINED HERE
os_name,app_version,="Pythinux Lite",[0,12,0]
autologin = 0
import os
def installd(filename):
    from zipfile import ZipFile as zf
    try:
        with zf(filename,"r") as zip:
            # zip.printdir()
            prog_name=str(zip.read("program.name"))
            prog_name=prog_name[2:]
            prog_name=prog_name[:-3]
            progdata=str(zip.read("program.info"))
            progdata=progdata[2:]
            progdata=progdata[:-3]
            progdata=progdata.split("|")
            progdata[1]=progdata[1].split(".")
            progdata[4]=progdata[4].split(".")
            progdata[4][0]=int(progdata[4][0])
            progdata[4][1]=int(progdata[4][1])
            try:
                main_program=zip.read("program.zip")
                is_mp=1
            except:
                is_mp = 0
            try:
                mandata=[zip.read("manuals.cmanpak"),str(zip.read("manual.name"))]
                mandata[1]=mandata[1][2:]
                mandata[1]=mandata[1][:-3]
                is_man = 1
            except:
                is_man = 0
            try:
                setupxx=zip.read("setup.xx")
                is_xx=1
            except:
                is_xx=0
            try:
                setuppy=zip.read("setup.py")
                is_py=1
            except:
                is_py=0
        print(f"Program Name: {progdata[0]}")
        print(f"Version: {progdata[1][0]}.{progdata[1][1]}.{progdata[1][2]}")
        print(f"Released: {progdata[2]}")
        print(f"Author: {progdata[3]}")
        print("Install?")
        yn=input("[y/n] >").lower()
        if yn == "y":
            print(f"Installing {progdata[0]}...")
            if progdata[4] <= [0,12]:
                if is_mp == 1:
                    try:
                        os.mkdir(f"Installed Programs/{prog_name}")
                    except:
                        print("Error: Program already installed.")
                        print("`installd` does not currently support upgrades.")
                        main()
                    f=open(f"Installed Programs/{prog_name}/program.zip","wb")
                    f.write(main_program)
                    f.close()
                if is_man == 1:
                    f=open(f"Custom Manuals/{mandata[1]}.cmanpak","wb")
                    f.write(mandata[0])
                    f.close()
                if is_xx == 1:
                    f=open("Cached Data/setup.xx","wb")
                    f.write(setupxx)
                    f.close()
                    f=open("Cached Data/setup.xx","r")
                    xx=f.read()
                    f.close()
                    run_script(xx.split("\n"))
                if is_py == 1:
                    f=open("Cached Data/setup.py","wb")
                    f.write(setuppy)
                    f.close()
                    os.chdir("Cached Data")
                    import setup
                    os.chdir("..")
                print(f"Installed program {progdata[0]}.")
                print(f"To run {progdata[0]}, type `run {prog_name}`.")
                main()
                    
            else:
                print(f"Incompatible {os_name} version!")
                print(f"Requires OS version >= {progdata[4][0]}.{progdata[4][1]}.x")
                print(f"Please update to a new version of {os_name}.")
                main()
            
        else:
            print("Install cancelled.")
            main()
    except:
        print("Failed to install program.")
        print("Check the following:")
        print("[-] Installer file exists")
        print("[-] Installer path typed correctly")
        print("[-] Installer is formatted correctly")
        print("[-] Alternatively, contact the developers of the program to see if this is an issue on your end.")
    return None
def can_change_dir(path, startpoint):
    abs_path = os.path.abspath(path)
    start_path = os.path.abspath(startpoint)
    return abs_path.startswith(start_path)
def create_user(username,passw,ulvl):
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
def is_file(fn,add=0):
    return os.path.isfile(os.getcwd()+f"/{fn}")
def vim_editor(fn="",add=0):
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
    return True
def clear_screen():
    res=uname()
    os.system("cls" if res[0] == "Windows" else "clear")
def sha256(text):
    import hashlib
    hashed_string = hashlib.sha256(text.encode('utf-8')).hexdigest()
    return hashed_string
def install_stdlib():
    global stdlib
    try:
        del(stdlib)
    except:
        pass
    try:
        import stdlib
    except:
        pass
def cman(manual):
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
        except:
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
def remove_userlist():
    # https://www.geeksforgeeks.org/python-os-remove-method/
    import os
    # File name
    file = 'System Settings/userlist.pythinux'
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
def is_god():
    global user_lvl
    if user_lvl >= 3:
        return True
    else:
        return False
def auth(msg="AUTHENTICATION"):
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
    div()
    input("Press ENTER to continue.\n")
    return True
def is_root():
    global user_lvl
    if user_lvl >= 2:
        return True
    elif user_lvl == 1:
        print("In order to perform this function, you need to enter your password.")
        if auth() == True:
            return True
        else:
            return False
    else:
        return False
def is_root_rigid():
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
    print(message)
    print("[1] Yes")
    print("[0] No")
    try:
        ch=int(input(">"))
    except:
        return False
    if ch == 1:
        return True
    else:
        return False

def user_editor_v2():
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
            create_user(un,pw,uvlv)
        except:
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
        except:
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
def user_control():
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
    except:
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
        except:
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
        except:
            div()
            print("Failed to complete action.")
        user_control()
    elif ch == 6:
        try:
            os.remove("System Settings/autologin.dat")
            print("Action completed successfully.")
        except:
            print("Could not complete action.")
        main()
    else:
        main()
    main()
def setup_wizard():
    print(f"Welcome to {os_name}.")
    print("This is the Setup Wizard.")
    print("Enter your username:")
    un=input("$")
    print("Enter your password:")
    print("[Make it strong!]")
    passw=sha256(getpass.getpass("$"))
    os.mkdir("Users")
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
    passw2=sha256(getpass.getpass(">"))
    create_user("admin",passw2,2)
    div()
    print("Do you want to set up autologin? Not recommended.")
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
    except:
        div()
    print(f"Successfully set up {os_name}!")
    print("Using the details for your user accoint, log into the system.")
    br()
    login()
def run(ch):
    try:
        os.chdir(f"Installed Programs/{ch}")
        import sys
        sys.path.insert(0,"program.zip")
        try:
            import importlib
            importlib.reload(program)
        except:
            import program
    except:
        return False
    try:
        sys.path.remove("program.zip")
        del sys.modules["program"]
        sys.path.remove("program.zip")
        os.chdir(startpoint)
        main()
        return True
    except:
        return True
def run_script(things):
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
def main(ch="",allow_script=0,return_mode=-1):
    global username, password, user_lvl, user_type, data, stdlib, mem, var_data, prompt
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
        run_script(ch)
        main()
    for item in var_data:
        ch=ch.replace("{"+item[0]+"}",item[1])
    ch=ch.replace("%date",strftime("%x"))
    ch=ch.replace("%time",strftime("%X"))
    ch=ch.replace("%user",username)
    ch=ch.replace("%os_name",os_name)
    ch=ch.replace("%os_version",f"{app_version[0]}.{app_version[1]}.{app_version[2]}")
    if ch.startswith("build-prog"):
        print("This command has been disabled due to bugs.")
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
    if ch == "help":
        div()
        print(f"Command List")
        div()
        print(f"about help logoff cls echo timer getdetails")
        print(f"quit userlist admin_panel run cat")
        print(f"jit stdlib alias add_alias user_control")
        print("var mem prompt wget echf user_editor ucode qaa")
        print(f"installd removed")
        div()
        if return_mode == 0:
            main()
        else:
            return True
    elif ch == "ihelp":
        ihelp()
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
    elif ch == "jit" and return_mode == 0:
        print("JIT [COMMAND]")
        print("Sends [command] to main().")
        main()
    elif ch.startswith("jit "):
        main(ch[4:])
        main()
    elif ch == "about":
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
    elif ch == "logoff":
        login()
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
    elif ch == "cls":
        clear_screen()
        if return_mode == 0:
            main()
        else:
            return True
    elif ch.startswith("echo "):
        ch=ch.replace("$date",stime("%x"))
        ch=ch.replace("$time",stime("%X"))
        ch=ch.replace("$user",username)
        ch=ch.replace("$uuser",username.upper())
        ch=ch.replace("$os",os_name)
        ch=ch.replace("$version",f"{app_version[0]}.{app_version[1]}.{app_version[2]}")
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
    elif ch == "getdetails":
        if is_root() == True:
            print(f"Username: {username}")
            print(f"Password [Hashed]: {password}")
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
    elif ch == "quit" or ch == "exit" and return_mode == 0:
        import sys
        sys.exit()
    elif ch == "userlist":
        if is_root() == True and return_mode == 0:
            userlist()
        else:
            print("Only ROOT users can access this menu.")
            if return_mode == 0:
                main()
            else:
                return True
    elif ch == "user_control" and is_root() == 1:
        user_control()
    elif ch == "admin_panel":
        if is_root() == True and return_mode == 0:
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
    elif "vim " in ch:
        vim(ch[4:])
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
        except:
            print("Could not run script.")
            consent_mode = 0
            main()
    elif ch == "div()" and return_mode == 1:
        div()
        return True
    elif ch == "cat" and return_mode == 0:
        print("CAT [url] [filename]")
        print("Downloads [url] and saves it to [filename]")
        main()
    elif ch.startswith("cat "):
        ch=ch.split(" ")
        if len(ch) == 3:
            try:
                import urllib.request
                url = ch[1]
                saveas=ch[2]
                print("Downloading...")
                try:
                    urllib.request.urlretrieve(url, saveas)
                    print("Downloaded.")
                except:
                    raise Exception
            except:
                print("FAILED.")
        else:
            if return_mode == 0:
                print("Invalid parameters.")
        if return_mode == 0:
            main()
        else:
            return True
    elif ch.startswith("cmd -e "):
        try:
            f=open(ch[7:],"r")
            data=f.read()
            f.close()
            data=data.split("\n")
            for item in data:
                os.system(item)
        except:
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
            except:
                pass
            import stdlib
            print("Installed successfully.")
            print(f"Version: {stdlib.app_version_str}")
        except:
            print("Could not install Standard library.")
        main()
    elif ch == "stdlib --remove" and return_mode == 0:
        try:
            del(stdlib)
        except:
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
    elif ch == "revoke_consent":
        consent_mode = 0
        if return_mode == 0:
            main()
        else:
            return True
    elif ch.startswith("#") or ch.startswith("//") and return_mode == 1:
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
    elif ch == "alias --clear":
        f=open(f"Users/{username}/User Settings/alias.dat","w")
        f.close()
        main()
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
        except:
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
        except:
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
        except:
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
        except:
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
                except:
                    pass
            for item in data2:
                print(item)
            main()
        except:
            print("Could not perform command; Perhaps no aliases exist.")
            main()
    elif ch == "mem --help":
        man("mem")
    elif ch == "mem --backup" or ch == "mem -b":
        try:
            f=open("mem.pythinux","w")
            f.write(str(mem))
            f.close()
        except:
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
        except:
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
        except:
            print("Failed to set MEM.")
        if return_mode == 0:
            main()
        else:
            return None
    elif ch.startswith("mem --sub "):
        try:
            mem -= float(ch[10:])
        except:
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
        except:
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
        except:
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
        except:
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
        except:
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
        except:
            print("Failed to download file.")
        main()
    elif ch =="user_editor" and is_root() == True:
        user_editor_v2()
    elif ch == "qaa":
        print("qaa [alias]|[command]")
        print("Quickly adds alias to the system.")
        main()
    elif ch.startswith("qaa "):
        ch=ch[4:]
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
    elif ch == "removed":
        print("Removed [installed program]")
        print("Uninstalls an installed SZIPS v2 program.")
        if return_mode == 0:
            main()
        else:
            return True
    elif ch.startswith("removed "):
        try:
            import shutil
            shutil.rmtree("Installed Programs/"+ch[8:])
            print(f"Uninstalled {ch[8:]}.")
        except:
            print("Failed to remove program.")
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
            print(f"Invalid command: {ch}")
        if return_mode == 0:
            main()
        else:
            return True
        
def start(lvl,al):
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
    if al == 1:
        main("cls")            
    if user_lvl >= 1:
        if os.path.isfile(os.getcwd()+"/.startup") == True:
            try:
                f=open(".startup","r")
                sdata=f.read()
                f.close()
                sdata=sdata.split("\n")
                for item in sdata:
                    main(item,1)
            except:
                pass
    main()
def login(al=0,al_username="root",al_password="root"):
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
        if username == "//ul":
            l=[]
            for item in data:
                l.append(item[0])
            print(l)
        password=getpass.getpass("Password $")
        div()
        base=f"{username}:{password}"
        sh_base=f"{username}:{sha256(password)}"
    for item in data:
        try:
            if base == f"{item[0]}:{item[1]}":
                start(int(item[2]),al)
            elif sh_base == f"{item[0]}:{item[1]}":
                start(int(item[2]),al)
        except:
            continue
    print("Username or password is invalid.")
    login()
def os_init():
    global username, password, user_lvl, user_type, user_type
    global startpoint
    try:
        os.chdir("PythinuxLite")
        startpoint=os.getcwd()
    except:
        os.mkdir("PythinuxLite")
        os.chdir("PythinuxLite")
        setup_wizard()
        os.chdir("..")
        os_init()
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
    refresh_data()
    try:
        f=open("System Settings/autologin.dat")
        aldata=f.read()
        f.close()
        aldata=aldata.split("|")
        login(1,aldata[0],aldata[1])
    except:
        login(autologin)
os_init()
