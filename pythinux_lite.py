#!/usr/bin/python
global crashlog
crashlog = []
global data
global consent_mode
consent_mode = 0
import os.path
from platform import uname
from time import strftime as stime

global stdlib
global mem, var_data, prompt
mem = 0
var_data = []
prompt = ""
packages = []
global os_name, app_version, autologin
global username, password, user_lvl, user_type, user_type
import getpass
from time import ctime, strftime, sleep
import os
from secrets import choice

(
    os_name,
    app_version,
) = "Pythinux Lite", [0, 15, 1]
autologin = 0
import os

global preferences
preferences = {
    "pref_format": [1, 0, 0],
    "pref_version": app_version,
    "time_format": "%x %X",
    "div": "--------------------",
    "terminal_debug_output":"n"
}


def removed(filename, return_mode=0):
    try:
        import shutil

        shutil.rmtree("Installed Programs/" + filename)
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


def create_file(filename, data):
    try:
        f = open(filename, "wb")
        f.write(data)
        f.close()
        return True
    except:
        return False


def installd(filename, consent=0):
    try:
        fn = os.path.basename(filename)
        global crashlog
        from zipfile import ZipFile as zf

        try:
            with open(filename, "rb") as f:
                zipdata = f.read()
        except Exception as e:
            crashlog.append(str(e))
        import shutil

        shutil.rmtree("Cached Data")
        os.mkdir("Cached Data")
        os.chdir("Cached Data")
        with open(fn, "wb") as f:
            f.write(zipdata)
            f.close()
        with zf(fn, "r") as zip:
            zip.extractall()
        import sys

        sys.path.insert(0, os.getcwd())
        try:
            f = open("program.name", "r")
            progname = f.read()
            f.close()
            progname = progname[:-1]
        except Exception as e:
            crashlog.append(str(e))
            print("Error: No `program.name` in zip archive`.")
            return False
        try:
            f = open("program.info", "r")
            progdata = f.read()
            f.close()
            progdata = progdata.split("\n")
            progdata = progdata[0]
            progdata = progdata.split("|")
            progdata[4] = progdata[4].split(".")
            progdata[4][0] = int(progdata[4][0])
            progdata[4][1] = int(progdata[4][1])
            progdata[1] = progdata[1].split(".")
        except Exception as e:
            crashlog.append(str(e))
            print("Error: No `program.info` in zip archive.")
            return False

        try:
            with open("program.zip", "rb") as f:
                mp = f.read()
                is_mp = 1
        except Exception as e:
            crashlog.append(str(e))
            is_mp = 0
        try:
            f = open("setup.xx", "r")
            xx = f.read()
            f.close()
            is_xx = 1
        except Exception as e:
            crashlog.append(str(e))
            is_xx = 0
        try:
            f = open("program.deps", "r")
            deps = f.read()
            deps = deps.split("\n")
            f.close()
            is_dep = 1
        except Exception as e:
            crashlog.append(str(e))
            is_dep = 0
        try:
            f = open("manuals.cmanpak", "r")
            mandata = f.read()
            f.close()
            is_man = 1
        except Exception as e:
            crashlog.append(str(e))
            is_man = 0
        if is_dep == 1:
            deps = [dep for dep in deps if dep != ""]
        if consent == 0:
            print(f"Program Name: {progdata[0]}")
            print(f"Version: {progdata[1][0]}.{progdata[1][1]}.{progdata[1][2]}")
            print(f"Released: {progdata[2]}")
            print(f"Author: {progdata[3]}")
            if is_dep == 1:
                print(f"Dependencies: [{len(deps)}]")
                print("Dependency List:", deps)
            print("Install?")
            yn = input("[y/n] >").lower()
            if yn != "y":
                print("User Install Cancelled.")
                return False
        if progdata[4] <= [app_version[0], app_version[1]]:
            pass
        else:
            print(f"Error: OS Version Must be >= {app_version[0]}.{app_version[1]}")
            return False
        if os.path.isfile(os.getcwd() + "/setup.py"):
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
            f = open(f"Installed Programs/{progname}/program.zip", "wb")
            f.write(mp)
            f.close()
        if is_xx == 1:
            run_script(xx.split("\n"))
        if is_man == 1:
            f = open(f"Installed Manuals/{progname}.cmanpak", "wb")
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
        print(
            "[-] Alternatively, contact the developers of the program to see if this is an issue on your end."
        )
        return False
def create_user(username, passw, ulvl):
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
    f = open("os_settings.toml", "w")
    f.close()
    f = open(f"alias.dat", "w")
    f.close()
    os.chdir("..")
    os.chdir("..")
    os.chdir("..")
    f = open("System Settings/userlist.pythinux", "a")
    f.write(f"{username}|{passw}|{ulvl}/")
    f.close()
    print("Created user successfully.")
    refresh_data()
def os_terminal():
    global crashlog
    termin = input(">>>")
    if termin == "%%exit":
        main()
    else:
        os.system(termin)
        os_terminal()
    os_terminal()
def is_file(fn, add=0):
    global crashlog
    return os.path.isfile(os.getcwd() + f"/{fn}")
def clear_screen():
    global crashlog
    res = uname()
    os.system("cls" if res[0] == "Windows" else "clear")


def sha256(text):
    global crashlog
    import hashlib

    hashed_string = hashlib.sha256(text.encode("utf-8")).hexdigest()
    return hashed_string
def remove_userlist():
    global crashlog
    # https://www.geeksforgeeks.org/python-os-remove-method/
    import os

    # File name
    file = "userlist.pythinux"
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
        f = open("System Settings/userlist.pythinux", "r")
        data = f.read()
        f.close()
        data = data.split("/")
        data2 = []
        for item in data:
            data2.append(item.split("|"))
        data = data2
        data2 = []
        for item in data:
            if len(item) == 3:
                data2.append(item)
        data = data2
    except:
        f = open("System Settings/userlist.pythinux", "w")
        f.write("root|root|2/guest|password|0/user|password|1")
        f.close()
        f = open("System Settings/userlist.pythinux", "r")
        data = f.read()
        f.close()
        data = data.split("/")
        data2 = []
        for item in data:
            data2.append(item.split("|"))
        data = data2
        data2 = []
        for item in data:
            if len(item) == 3:
                data2.append(item)
    return ""

def is_god():
    global crashlog
    global user_lvl
    if user_lvl >= 3:
        return True
    else:
        return False


def rng(a, b):
    global crashlog
    # Uses secrets to generate a random number for "true" randomness
    return choice(list(range(a, b + 1)))


def auth(msg="AUTHENTICATION"):
    global crashlog
    div()
    print(msg)
    div()
    global password
    newpass = getpass.getpass("Password $")
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
    global preferences
    print(preferences["div"])


def div2():
    global preferences
    print(preferences["div"])
    return "--------------------"


def upper(inp):
    if isinstance(inp, str) == True:
        return inp.upper()
    else:
        return "[UNDEFINED]"


def is_stdlib():
    try:
        data = stdlib
        return True
    except:
        return False


def lower(inp):
    if isinstance(inp, str) == True:
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
        ch = int(input(">"))
    except Exception as e:
        crashlog.append(str(e))
        return False
    if ch == 1:
        return True
    else:
        return False


def user_editor_v2():
    global crashlog
    ch = input("user-editor-v2 $")
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
            un = input("Username >>")
            pw = sha256(getpass.getpass("Password >>"))
            ulvl = int(input("User LVL >>"))
            create_user(un, pw, ulvl)
        except Exception as e:
            crashlog.append(str(e))
            print("Failed to create user.")
        user_editor_v2()
    elif ch == "list":
        lst = os.listdir(os.getcwd() + "/Users")
        if lst != []:
            for item in lst:
                print(item)
        else:
            print(lst)
        user_editor_v2()
    elif ch == "delete":
        unn = input(">")
        try:
            import shutil

            shutil.rmtree(f"Users/{unn}")
        except Exception as e:
            crashlog.append(str(e))
            print("Failed to remove user.")
            user_editor_v2()
        f = open("System Settings/userlist.pythinux", "r")
        dat = f.read()
        f.close()
        dat = dat.split("/")
        dat2 = []
        for item in dat:
            dat2.append(item.split("|"))
        for item in dat2:
            if item[0] == unn:
                dat2.remove(item)
        dat = dat2
        dat2 = []
        for item in dat:
            dat2.append("|".join(item))
        dat2 = "/".join(dat2)
        f = open("System Settings/userlist.pythinux", "w")
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
        ch = ch[5:]
        ch = ch.split("|")
        create_user(ch[0], ch[1], ch[2])
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
        ch = int(input(">"))
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
                f = open("System Settings/userlist.pythinux", "w")
                f.close()
            else:
                raise KeyboardInterrupt
        except Exception as e:
            crashlog.append(str(e))
            print("Failed to complete action.")
        user_control()
    elif ch == 1:
        main("userlist", return_mode=0)
        user_control()
    elif ch == 5:
        try:
            f = open(f"System Settings/autologin.dat", "w")
            un = input("Username >>")
            un = un.replace("|", "")
            pw = sha256(getpass.getpass("Password >>"))
            f.write(f"{un}|{pw}")
            f.close()
            div()
            print("Completed action successfully.")
            print("Login username:", un)
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
    global crashlog, preferences
    import pickle

    print(f"Welcome to {os_name}.")
    print("This is the Setup Wizard.")
    print("Enter your username:")
    un = input("$")
    print("Enter your password:")
    print("[Make it strong!]")
    passw = sha256(getpass.getpass("$"))
    os.mkdir("Users")
    os.mkdir("Program Data")
    os.mkdir("System Settings")
    f = open("System Settings/startup.xx", "w")
    f.close()
    os.mkdir("Custom Manuals")
    os.mkdir("Installed Programs")
    os.mkdir("Cached Data")
    f = open("System Settings/alias.dat", "w")
    f.close()
    f = open("System Settings/userlist.pythinux", "w")
    f.close()
    f = open("System Settings/system.preferences", "wb")
    f.write(pickle.dumps(preferences))
    f.close()
    create_user(un, passw, 1)
    print("The system will now create an administrator account.")
    print("Protect the password for this account at all costs.")
    print("Enter an admin password:")
    passw2 = sha256(getpass.getpass("$"))
    create_user("admin", passw2, 2)
    div()
    print("Do you want to set up autologin?")
    print("[1] Yes")
    print("[0] No")
    try:
        ch = int(input(">"))
        if ch == 1:
            f = open("System Settings/autologin.dat", "w")
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

        with zf("program.zip", "r") as zip:
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
    if isinstance(things, list) == False:
        things = things.split("\n")
    for item in things:
        if "<input>" in item:
            item = item.replace("<input>", input())
        if "<input2>" in item:
            item = item.replace("<input2>", input())
        if "<input3>" in item:
            item = item.replace("<input3>", input())
        if "<input4>" in item:
            item = item.replace("<input4>", input())
        if "<input5>" in item:
            item = item.replace("<input5>", input())
        terminal(item)
    return True


def main(ch=""):
    global crashlog, preferences
    global username, password, user_lvl, user_type, data, stdlib, mem, var_data, prompt, packages, dbs
    if ch == "":
        terminal()
    for i in var_data:
        ch = ch.replace("{" + i[0] + "}", i[1])
    ch = ch.replace("$date", strftime("%x"))
    ch = ch.replace("$time", strftime("%X"))
    ch = ch.replace("$user", username)
    ch = ch.replace("$dir", os.getcwd())
    ch = ch.replace("$uuser", username.upper())
    ch = ch.replace("$os", os_name)
    ch = ch.replace("$utype", user_type)
    ch = ch.replace("$version", f"{app_version[0]}.{app_version[1]}.{app_version[2]}")
    if ch == "help":
        return [
            "about",
            "help",
            "logoff",
            "rand",
            "rng",
            "time",
            "cls",
            "login",
            "censor",
            "echo",
            "timer",
            "getdetails",
            "quit",
            "userlist",
            "add_user",
            "userlist_c",
            "run",
            "cat",
            "terminal",
            "view_log",
            "qaag",
            "alias",
            "add_alias",
            "user_control",
            "pkm",
            "var",
            "prompt",
            "wget",
            "user_editor",
            "ucode",
            "qaa",
            "installd",
            "removed",
            "stime",
            "include",
            "script",
            "sha256",
            "div()",
            "cmd"
        ]
    elif ch == "cls":
        clear_screen()
    elif ch == "ucode":
        div()
        print("ucode [parameter]")
        print("Parameters:")
        print("--show : shows current user's ucode")
        print("--generate : generates new ucode")
        print("--usage : explain what ucodes are used for")
        div()
    elif ch == "ucode --show":
        print(f"{username}|{password}|{user_lvl}")
    elif ch == "ucode --generate":
        unn = input("Username >>")
        pswd = sha256(getpass.getpass("Password >>"))
        ulvl = input("UserLVL >>")
        print(f"{unn}|{pswd}|{ulvl}")
    elif ch == "about -c" or ch == "about":
        return f"{os_name} v{app_version[0]}.{app_version[1]}.{app_version[2]}"
    elif ch == "about -cc":
        return app_version
    elif ch == "logout" or ch == "logoff":
        login()
    elif ch == "quit" or ch == "exit":
        exit()
    elif ch == "time":
        print(strftime("%x %X"))
    elif ch == "rand":
        return rng(100000, 1000000)
    elif ch == "rng":
        print("RNG generates a random number from [1st parameter] to [2nd parameter]")
        div()
        print("Correct syntax:")
        print("rng [int] [int]")
    elif ch.startswith("rng ") == True:
        ch = ch.split(" ")
        if len(ch) == 3:
            try:
                return rng(int(ch[1]), int(ch[2]))
            except Exception as e:
                crashlog.append(str(e))
                print("Only INT numbers are accepted.")
                return None
        else:
            base = []
            for item in ch:
                if item != "":
                    base.append(item)
            ch = base
            print(f"RNG requires [2] parameters, got [{len(ch)-1}].")
        return None
    elif ch.startswith("echo "):
        if " > " in ch:
            ch = ch[5:]
            ch = ch.split(" > ")
            if len(ch) == 2:
                f = open(ch[1], "w")
                f.write(ch[0])
                f.close()
                return None
            else:
                print(ch)
                return None
        else:
            print(ch[5:])
            return None
    elif ch == "echo":
        print("echo <str>")
    elif ch == "timer":
        print("Correct syntax:")
        print("timer [seconds(int)]")
    elif ch.startswith("timer "):
        ch = int(ch[6:])
        while ch > 0:
            sleep(1)
            ch -= 1
    elif ch == "getdetails":
        if is_root() == True:
            print(f"Username: {username}")
            print(f"Password [Hashed]: {password}")
            print(f"UserLVL: {user_lvl}")
        else:
            print("You need to be root to access this command.")
    elif ch == "chkroot":
        return is_root()
    elif ch == "userlist":
        if is_root() == True:
            userlist()
        else:
            print("Only ROOT users can access this menu.")
    elif ch == "user_control" and is_root() == 1:
        user_control()
    elif ch == "add_user":
        if is_root():
            un = input("Username $")
            pw = sha256(getpass.getpass("Password $"))
            try:
                ul = int(input("User LVL $"))
            except Exception as e:
                print(str(e))
                return None
            if ul > 3:
                ul = 3
            if ul < 0:
                ul = 0
            create_user(un, pw, ul)
        else:
            return f"Error: Only root users and higher can access the ADD_USER command"
    elif ch == "admin_panel":
        if is_root() == True:
            div()
            print("Admin Control Panel")
            div()
            print("[1] Delete Userlist And Log Out")
            div()
            try:
                ch = int(input(">"))
            except Exception as e:
                crashlog.append(str(e))
                main()
            div()
            if ch == 1:
                os.remove("System Settings/userlist.pythinux")
                login()
            else:
                print("Could not remove userlist.")
                return None
        else:
            print("Only ROOT users can do this!")
            return None
    elif ch == "userlist_c" or ch == "userlist -c":
        d = []
        if is_root() == True:
            for item in data:
                d.append(item[0])
        else:
            return f"Error: Only root and higher users can access this command"
        return d
    elif ch == "run /":
        print(os.listdir(os.getcwd() + "/Installed Programs"))
        main()
    elif ch.startswith("run "):
        ch = ch[4:]
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
    elif ch == "run":
        div()
        print("run [program name]")
        print("Runs an installed SZIPS program.")
        div()
        print("Custom launch options:")
        print("`run /`: lists all installed programs")
        div()
    elif ch == "div()":
        div()
    elif ch == "cat":
        print("CAT [url] [filename]")
        print("Downloads [url] and saves it to [filename]")
    elif ch.startswith("cat "):
        ch = ch.split(" ", 2)
        if len(ch) == 3:
            try:
                import urllib.request

                url = ch[1]
                saveas = ch[2]
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
            print("Invalid parameters.")
    elif ch == "terminal":
        print("To exit, type %%exit")
        os_terminal()
    elif ch.startswith("cmd "):
        os.system(ch[4:])
        return True
    elif ch.startswith("#"):
        return None
    elif ch == "add_alias":
        if os.path.isfile(f"Users/{username}/User Settings/alias.dat") == False:
            f = open(f"Users/{username}/User Settings/alias.dat", "w")
            f.close()
        f = open(f"Users/{username}/User Settings/alias.dat", "a")
        inp1 = input("Alias >>")
        inp1 = inp1.replace("|", "")
        inp2 = input("Command >>")
        inp2 = inp2.replace("|", "")
        f.write(f"{inp1}|{inp2}\n")
        f.close()
    elif ch == "alias --add-global":
        if os.path.isfile(f"System Settings/alias.dat") == False:
            f = open(f"System Settings/alias.dat", "w")
            f.close()
        f = open(f"System Settings/alias.dat", "a")
        inp1 = input("Alias >>")
        inp1 = inp1.replace("|", "")
        inp2 = input("Command >>")
        inp2 = inp2.replace("|", "")
        f.write(f"{inp1}|{inp2}\n")
        f.close()
    elif ch == "alias":
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
    elif ch == "alias --clear":
        f = open(f"Users/{username}/User Settings/alias.dat", "w")
        f.close()
    elif ch == "alias --remove":
        try:
            f = open(f"Users/{username}/User Settings/alias.dat", "r")
            aliases = f.read()
            f.close()
            aliases = aliases.split("\n")
            a2 = []
            for item in aliases:
                a2.append(item.split("|"))
            ch = input("Alias >>")
            for item in a2:
                if item[0] == ch:
                    a2.remove(item)
                if item == [""]:
                    a2.remove(item)
            a3 = []
            for item in a2:
                a3.append("|".join(item))
            a4 = ""
            for item in a3:
                a4 += f"{item}\n"
            f = open(f"Users/{username}/User Settings/alias.dat", "w")
            f.write(a4)
            f.close()
            print(f"Successfully deleted alias {ch}.")
        except Exception as e:
            crashlog.append(str(e))
            print("Could not perform deletion operation.")
    elif ch == "alias --remove-global":
        try:
            f = open(f"System Settings/alias.dat", "r")
            aliases = f.read()
            f.close()
            aliases = aliases.split("\n")
            a2 = []
            for item in aliases:
                a2.append(item.split("|"))
            ch = input("Alias >>")
            for item in a2:
                if item[0] == ch:
                    a2.remove(item)
                if item == [""]:
                    a2.remove(item)
            a3 = []
            for item in a2:
                a3.append("|".join(item))
            a4 = ""
            for item in a3:
                a4 += f"{item}\n"
            f = open(f"System Settings/alias.dat", "w")
            f.write(a4)
            f.close()
            print(f"Successfully deleted alias {ch}.")
        except Exception as e:
            crashlog.append(str(e))
            print("Could not perform deletion operation.")
    elif ch == "alias --list":
        try:
            f = open(f"Users/{username}/User Settings/alias.dat", "r")
            data = f.read()
            f.close()
            data = data.split("\n")
            data2 = []
            for item in data:
                if item != "":
                    item = item.split("|")
                    data2.append(item[0])
            return data2
        except Exception as e:
            crashlog.append(str(e))
            print("Could not perform command; Perhaps no aliases exist.")
    elif ch == "alias --list-global":
        try:
            f = open(f"System Settings/alias.dat", "r")
            data = f.read()
            f.close()
            data = data.split("\n")
            data2 = []
            for item in data:
                if item != "":
                    item = item.split("|")
                    data2.append(item[0])
            return data2
        except Exception as e:
            crashlog.append(str(e))
            print("Could not perform command; Perhaps no aliases exist.")
    elif ch == "alias --list-plus":
        try:
            f = open(f"Users/{username}/User Settings/alias.dat", "r")
            data = f.read()
            f.close()
            data = data.split("\n")
            data2 = []
            for item in data:
                try:
                    item = item.split("|")
                    data2.append(f"{item[0]} = {item[1]}")
                except Exception as e:
                    crashlog.append(str(e))
                    pass
            return data2
        except Exception as e:
            crashlog.append(str(e))
            print("Could not perform command; Perhaps no aliases exist.")
    elif ch == "var":
        print("var [parameter] <var_name> <value>")
        print("Parameters:")
        print("set <var_name> <value>")
        print("print <var_name>")
        print("list")
        print("del <var_name>")
        print("backup <filename>")
        print("restore <filename>")
    elif ch == "var list":
        return var_data
    elif ch.startswith("var set "):
        ch = ch.split(" ", 3)
        ch = ch[2:]
        if len(ch) == 2:
            var_data2 = []
            for item in var_data:
                if item[0] == ch[0]:
                    continue
                else:
                    var_data2.append(item)
            var_data = var_data2
            del var_data2
            var_data.append([ch[0], ch[1]])
        else:
            print("NO")
    elif ch.startswith("var print "):
        ch = ch[10:]
        is_find = 0
        for item in var_data:
            if item[0] == ch:
                print(item[1])
                is_find = 1
                break
        if is_find == 0:
            print(f"Could not find variiable {ch[0]}")
    elif ch.startswith("var del "):
        ch = ch[8:]
        for item in var_data:
            if item[0] == ch:
                var_data.remove(item)
                print(f"Removed {ch}")
    elif ch.startswith("var backup "):
        try:
            import pickle

            f = open(ch[11:] + ".vbkp", "wb")
            pickle.dump(var_data, f)
            f.close()
            print("Successful Backup.")
        except Exception as e:
            crashlog.append(str(e))
            print("Backup Failed.")
    elif ch.startswith("var restore "):
        try:
            f = open(ch[12:] + ".vbkp", "rb")
            import pickle

            var_data = pickle.load(f)
            f.close()
            print("Restore successful.")
        except Exception as e:
            crashlog.append(str(e))
            print("Failed to restore.")
    elif ch == "echf":
        print("echf [filename] [text]")
        print("Saves [text] to [filename]")
    elif ch.startswith("echf "):
        try:
            ch = ch.split(" ", 2)
            f = open(ch[1], "w")
            f.write(ch[2])
            f.close()
        except Exception as e:
            crashlog.append(str(e))
            print("Write failed.")
    elif ch == "wget":
        print("wget [url]")
        print(
            "Wget downloads the file from [url] and saves it, picking the filename automatically."
        )
    elif ch.startswith("wget "):
        try:
            import urllib.request

            url = ch[5:]
            saveas = url.split("/")
            s2 = []
            for item in saveas:
                if item != "":
                    s2.append(item)
            saveas = s2
            saveas = saveas[len(saveas) - 1]
            print("Downloading...")
            urllib.request.urlretrieve(url, saveas)
            print(f"Download successful, saved as {saveas}.")
        except Exception as e:
            crashlog.append(str(e))
            print("Failed to download file.")
    elif ch == "user_editor" and is_root() == True:
        user_editor_v2()
    elif ch.startswith("qar "):
        ch = ch[4:]
        try:
            f = open(f"Users/{username}/User Settings/alias.dat", "r")
            d = f.read()
            d = d.split("\n")
            f.close()
            d2 = []
            for i in d:
                d2.append(i.split("|"))
            d2 = [x for x in d2 if x[0] != ch]
            d2.remove([""])
            d3 = []
            for i in d2:
                d3.append("|".join(i))
            f = open(f"Users/{username}/User Settings/alias.dat", "w")
            for i in d3:
                f.write(i + "\n")
            f.close()
        except Exception as e:
            crashlog.append(str(e))
    elif ch == "qaa":
        print("qaa [alias]|[command]")
        print("Quickly adds alias to the system.")
    elif ch == "qaag":
        print("qaag [alias]|[command]")
        print("Like `qaa` but global.")
    elif ch.startswith("qaa "):
        ch = ch[4:]
        chh = ch.split("|")
        print(f"[ALIAS] {chh[0]} --> {chh[1]}")
        if os.path.isfile(f"Users/{username}/User Settings/alias.dat") == False:
            f = open(f"Users/{username}/User Settings/alias.dat", "w")
            f.close()
        f = open(f"Users/{username}/User Settings/alias.dat", "a")
        f.write(f"{ch}\n")
        f.close()
    elif ch.startswith("qaag "):
        ch = ch[5:]
        if os.path.isfile(f"System Settings/alias.dat") == False:
            f = open(f"System Settings/alias.dat", "w")
            f.close()
        f = open(f"Users/{username}/User Settings/alias.dat", "a")
        f.write(f"{ch}\n")
        f.close()
    elif ch == "removed":
        print("Removed [installed program]")
        print("Uninstalls an installed SZIPS v2 program.")
    elif ch.startswith("removed "):
        removed(ch[8:])
    elif ch == "installd":
        print("installd [/path/to/installer]")
        print("Installs a program from a .szip file.")
    elif ch.startswith("installd "):
        if ch.endswith(".szip") == False:
            installd(ch[9:] + ".szip")
        else:
            installd(ch[9:])
    elif ch.startswith("pkm remove "):
        main(f"removed {ch[11:]}")
    elif ch == "pkm version":
        print("PKM Package Manager")
        print("Version 1.1.0")
        print(f"OS Version: {app_version[0]}.{app_version[1]}.{app_version[2]}")
        print("Build Date: 11 Feb 2023")
        print("(c) 2023 WinFan3672, Some Rights Reserved.")
    elif ch == "pkm version -c":
        print(
            f"PKM Version 1.1.0 : OS Version {app_version[0]}.{app_version[1]}.{app_version[2]}"
        )
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
    elif ch == "pkm ?":
        main("man pkm")
    elif ch == "pkm upgrade":
        main("pkm update")
        ip = os.listdir(os.getcwd() + "/Installed Programs")
        for i in ip:
            main(f"pkm install -y {i}")
        print("Package upgrade finished.")
    elif ch.startswith("pkm search "):
        main("pkm update")
        term = ch[11:]
        results = []
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
                print("    " + item[1])
                div()
    elif ch.startswith("pkm install -y "):
        term = ch[15:]
        for item in packages:
            if item[0] == term:
                if item[2] == "about:blank":
                    print("Error: Program does not have a download link.")
                    return None
                print(f"[DOWNLOAD] {item[2]}")
                import urllib.request

                try:
                    try:
                        os.remove("Cached Data/pkm.szip")
                    except Exception as e:
                        crashlog.append(str(e))
                        pass
                    urllib.request.urlretrieve(item[2], "Cached Data/pkm.szip")
                    installd("Cached Data/pkm.szip", 1)
                    return None
                except Exception as e:
                    crashlog.append(str(e))
                    print(f"[FAIL] Download {item[2]}")
                    return None
        print(f"Could not find package {term}.")
    elif ch.startswith("pkm install "):
        main("pkm update")
        term = ch[12:]
        for item in packages:
            if item[0] == term:
                if item[2] == "about:blank":
                    print("Error: Program does not have a download link.")
                    return None
                print("Downloading program...")
                print(f"[DOWNLOAD] {item[2]}")
                import urllib.request

                try:
                    try:
                        os.remove("Cached Data/pkm.szip")
                    except Exception as e:
                        crashlog.append(str(e))
                        pass
                    urllib.request.urlretrieve(item[2], "Cached Data/pkm.szip")
                    main("installd Cached Data/pkm.szip")
                    return None
                except Exception as e:
                    crashlog.append(str(e))
                    print(f"[FAIL] Download {item[2]}")
                    return None
        print(f"Could not find package {term}.")
    elif ch == "pkm update":
        packages = []
        print("Updating packages...")
        import urllib.request

        for item in dbs:
            url = item
            print(f"[DOWNLOAD] {url}")
            try:
                urllib.request.urlretrieve(url, "Cached Data/pkm.pkm")
                f = open("Cached Data/pkm.pkm", "r")
                d = f.read()
                f.close()
                d = d.split("\n")
                for item in d:
                    packages.append(item.split("|"))
            except:
                print(f"[FAIL] Download data from {item}")
        print("Updated packages.")
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
    elif ch == "pkm db list":
        return dbs
    elif ch == "pkm list":
        ip = os.listdir(os.getcwd() + "/Installed Programs")
        for i in ip:
            print(f"[-] {i}")
    elif ch == "pkm db save":
        import pickle

        f = open("System Settings/pkm.db", "wb")
        f.write(pickle.dumps(dbs))
        f.close()
    elif ch == "pkm db reset":
        dbs = ["https://winfan3672.000webhostapp.com/pkm/official.pkm"]
    elif ch == "pkm db load":
        import pickle

        try:
            f = open("System Settings/pkm.db", "rb")
            dbs = pickle.loads(f.read())
            f.close()
            return None
        except Exception as e:
            crashlog.append(str(e))
            print("FAIL")
    elif ch.startswith("pkm db add "):
        ch = ch[11:]
        dbs.insert(0, ch)
    elif ch.startswith("pkm db remove "):
        ch = ch[14:]
        dbs.remove(ch)
    elif ch == "censor":
        terminal("prompt [$utype] $")
    elif ch == "pkm all":
        main("pkm update")
        div()
        for item in packages:
            print(item[0])
            print("    " + item[1])
            div()
    elif ch == "view_log":
        return crashlog
    elif ch == "login":
        un = input("Username $")
        pw = getpass.getpass("Password $")
        login(2, un, sha256(pw))
    elif ch == "stopexec":
        print("[EXEC] Execution Manually Stopped")
        terminal()
    elif ch == "stime":
        print("stime [str]")
        print("Returns string handled by Python's time.strftime")
    elif ch.startswith("stime "):
        return stime(ch[6:])
    elif ch == "True":
        return True
    elif ch == "False":
        return False
    elif ch == "None":
        return None
    elif ch == "var int":
        print("var int [var name]")
        print("converts [var name] to an integer")
    elif ch.startswith("var int "):
        ch = ch[8:]
        index = 0
        print(var_data)
        for i in var_data:
            print(i)
            if i[0] == ch:
                print("yos")
                try:
                    var_data[index][1] = int(var_data[index][1])
                except Exception as e:
                    print(str(e))
            else:
                print(i[0], ch)
            index += 1
    elif ch == "include":
        return f"include [dir]\nRuns a .xx file in [dir]\nThe new ./ command"
    elif ch.startswith("include "):
        try:
            with open(ch[8:] + ".xx", "r") as f:
                run_script(f.readlines())
                return True
        except Exception as e:
            crashlog.append(str(e))
            return False
    elif ch == "script":
        print("script [parameter]")
        print("script new [name] - creates a new scipt called [name]")
        print("script list - returns list of installed scripts")
        print("script run [name] - runs a script in your scripts directory")
    elif ch == "script list":
        return os.listdir(os.getcwd() + f"/Users/{username}/Scripts")
    elif ch == "script run":
        print("Script run [file]")
        print("runs a file in your Users/[username]/Scripts folder")
    elif ch.startswith("script run "):
        ch = ch[11:]
        n = main(f"include Users/{username}/Scripts/{ch}")
        return n
    elif ch == "script new":
        print("script new [name]")
        print("Makes a new script in your Scripts folder and opens it in Vim")
    elif ch.startswith("script new "):
        vim_editor(f"Users/{username}/Scripts/{ch[11:]}.xx")
    elif ch == "sha256":
        print("sha256 [str]")
        print("Returns the SHA256 hash of [str]")
    elif ch.startswith("sha256 "):
        return sha256(ch[7:])
    else:
        with open(f"Users/{username}/User Settings/alias.dat", "r") as f:
            d = f.read()
            d = d.split("\n")
            d2 = []
            for i in d:
                if i != "":
                    d2.append(i.split("|"))
            d = d2
            del d2
            for i in d:
                if ch == i[0]:
                    terminal(i[1])
        with open(f"System Settings/alias.dat", "r") as f:
            d = f.read()
            d = d.split("\n")
            d2 = []
            for i in d:
                d2.append(i.split("|"))
            for i in d2:
                if ch == i[0]:
                    terminal(i[1])
        return f'SyntaxError: "{ch}" is not a valid command, manual, alias or program.'


def terminal(ch=""):
    import re

    chh = ""
    pattern = r"\[[{](.*?)[}]]"
    global user_type, username, prompt
    if ch == "":
        rm = 0
        if prompt == "":
            ch = input(f"{user_type}@{username} $")
        else:
            ch = input(prompt)
    else:
        rm = 1
    if "[{" in ch and "}]" in ch:
        chh = re.findall(pattern, ch)
        chh = chh[0]
        ch = ch.replace("[{" + chh + "}]", str(main(chh)))
    if " && " in ch:
        ch=ch.split(" && ")
        run_script(ch)
    if ch == "help":
        div()
        print("Command List")
        div()
        n = main("help")
        n = sorted(n)
        n2 = [n[i : i + 10] for i in range(0, len(n), 10)]
        for item in n2:
            print(" ".join(item))
        div()
        terminal()
    elif ch.startswith("prompt "):
        ch = ch.replace("$date", strftime("%x"))
        ch = ch.replace("$time", strftime("%X"))
        ch = ch.replace("$user", username)
        ch = ch.replace("$dir", os.getcwd())
        ch = ch.replace("$uuser", username.upper())
        ch = ch.replace("$os", os_name)
        ch = ch.replace("$utype", user_type)
        ch = ch.replace(
            "$version", f"{app_version[0]}.{app_version[1]}.{app_version[2]}"
        )
        prompt = ch[7:]
        terminal()
    else:
        n = main(ch)
        if n != None:
            if isinstance(n,list) and n != []:
                if len(n) == 3 and isinstance(n[0],int) and isinstance(n[1],int) and isinstance(n[2],int):
                    print(f"v{n[0]}.{n[1]}.{n[2]}")
                else:
                    div()
                    for i in n:
                        if callable(i):
                            i()
                        else:
                            print(i)
                    div()
            else:
                print(n)
        if rm == 0:
            terminal()


def start(lvl, al, alpassword=""):
    global crashlog
    global username, password, user_lvl, user_type
    password = sha256(password)
    user_lvl = lvl
    if user_lvl == 0:
        user_type = "guest"
    elif user_lvl == 1:
        user_type = "user"
    elif user_lvl == 2:
        user_type = "root"
    elif user_lvl == 3:
        user_type = "god"
    else:
        user_type = "[INVALIDUSER]"
    if al == 0:
        print(f"Welcome to {os_name}.")
        print(f"[{os_name} v{app_version[0]}.{app_version[1]}.{app_version[2]}]")
        div()
        if user_lvl == 0:
            print("You are logged in on a guest account.")
            print(
                "Guest accounts have limited access to commands and cannot install/remove programs."
            )
        elif user_lvl == 1:
            pass
        elif user_lvl == 2:
            print("You are logged in as a root account.")
            print("If you do not know what this means, type LOGOFF right now.")
            print("DO NOT USE A ROOT ACCOUNT AS YOUR DAILY DRIVER ACCOUNT.")
        elif user_lvl == 3:
            print(
                "Warning! GOD users have very high priveleges and are fully unrestricted."
            )
            print("Exercise caution and common sense when using a God account.")
            print(
                "If you are unaware of the security implications of using a God account, or what any of this means, type LOGOFF right now."
            )
            print("DO NOT USE A GOD ACCOUNT AS YOUR DAILY DRIVER ACCOUNT.")
    if al == 1:
        main("cls")
        div()
        print("Autologin Security")
        div()
        print("For security, enter your password:")
        while True:
            newpass = getpass.getpass("Password $")
            if sha256(sha256(newpass)) == password:
                password = sha256(newpass)
                break
        main("cls")
    if user_lvl >= 1:
        if os.path.isfile(os.getcwd() + "/System Settings/startup.xx") == True:
            try:
                f = open("System Settings/startup.xx", "r")
                sdata = f.read()
                f.close()
                sdata = sdata.split("\n")
                for item in sdata:
                    main(item)
            except Exception as e:
                crashlog.append(str(e))
                pass
    terminal()


def login(al=0, al_username="root", al_password="root"):
    global crashlog
    global username, password, user_lvl, user_type, autologin, data
    if data == []:
        div()
        print("[Your user file is corrupt. Please delete it.]")
        div()
        data = [[]]
    if al == 1:
        base = f"{al_username}:{al_password}"
        sh_base = f"{al_username}:{sha256(al_password)}"
        username, password = f"{al_username}", f"{al_password}"
    elif al == 2:
        base = f"{al_username}:{al_password}"
        for item in data:
            if base == f"{item[0]}:{item[1]}":
                username, password = al_username, al_password
                main()
    else:
        al_password = ""
        div()
        print(f"{upper(os_name)} LOGIN SYSTEM")
        div()
        print("Enter your login details.")
        print("If they are valid, you will be logged in.")
        print(f"There are [{len(data)}] users on your machine.")
        div()
        print("Username = guest\nPassword = password\nFor a guest account")
        div()
        username = input("Username $")
        if username == "//ul":
            l = []
            for item in data:
                l.append(item[0])
            print(l)
            login()
        password = getpass.getpass("Password $")
        div()
        base = f"{username}:{password}"
        sh_base = f"{username}:{sha256(password)}"
    for item in data:
        try:
            if base == f"{item[0]}:{item[1]}":
                start(int(item[2]), al, al_password)
            elif sh_base == f"{item[0]}:{item[1]}":
                start(int(item[2]), al, al_password)
        except Exception as e:
            crashlog.append(str(e))
            continue
    print("Username or password is invalid.")
    login()


def refresh_pref():
    import pickle

    with open("System Settings/system.preferences", "rb") as f:
        return pickle.loads(f.read())


def os_init():
    global crashlog, preferences
    global username, password, user_lvl, user_type, user_type
    global startpoint
    refresh_data()
    preferences = refresh_pref()
    try:
        f = open("System Settings/autologin.dat")
        aldata = f.read()
        f.close()
        aldata = aldata.split("|")
        login(1, aldata[0], aldata[1])
    except Exception as e:
        crashlog.append(str(e))
        login(autologin)


try:
    print(os.getcwd())
    os.chdir("Pythinux Lite")
    startpoint = os.getcwd()
except Exception as e:
    crashlog.append(str(e))
    print("did")
    os.mkdir("Pythinux Lite")
    os.chdir("Pythinux Lite")
    setup_wizard()
try:
    f = open("System Settings/userlist.pythinux", "r")
    data = f.read()
    f.close()
    data = data.split("/")
    data2 = []
    for item in data:
        data2.append(item.split("|"))
    data = data2
    data2 = []
    for item in data:
        if len(item) == 3:
            data2.append(item)
    data = data2
except Exception as e:
    crashlog.append(str(e))
    f = open("System Settings/userlist.pythinux", "w")
    f.close()
    f = open("System Settings/userlist.pythinux", "r")
    data = f.read()
    f.close()
    data = data.split("/")
    data2 = []
    for item in data:
        data2.append(item.split("|"))
    data = data2
    data2 = []
    for item in data:
        if len(item) == 3:
            data2.append(item)
    data = data2
try:
    f = open("System Settings/pkm.db", "rb")
    import pickle

    dbs = pickle.loads(f.read())
    f.close()
except Exception as e:
    crashlog.append(str(e))
    dbs = ["https://winfan3672.000webhostapp.com/pkm/official.pkm"]
os_init()
