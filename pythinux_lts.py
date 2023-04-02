#!/usr/bin/python
global crashlog
crashlog = []

global functions
functions = []

global data
global consent_mode
consent_mode = 0
import os.path
from platform import uname
from time import strftime as stime

import pickle, inspect

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
from random import randint as rng
import os, sys
from secrets import choice

(
    os_name,
    app_version,
) = "Pythinux LTS", [1, 0, 0]
autologin = 0
import os

global preferences, PREFERENCES

PREFERENCES = {
    "allowDebugMenu": False,
    "pref_format": [1, 7, 0],
    "pref_version": app_version,
    "time_format": "%x %X",
    "div": "--------------------",
    "alias_priority": False,
    "default_prompt": "",
    "banlist": [],
}

preferences = PREFERENCES


def obj_to_dict(obj):
    """
    Recursively convert an object and all its attributes to a dictionary.
    """
    if isinstance(obj, (int, float, bool, str)):
        return obj

    if inspect.isclass(obj):
        try:
            return {"__class__": obj.__name__}
        except:
            pass

    if isinstance(obj, (tuple, list)):
        return [obj_to_dict(x) for x in obj]

    if isinstance(obj, dict):
        return {key: obj_to_dict(value) for key, value in obj.items()}

    obj_dict = {}
    for attr in dir(obj):
        if attr.startswith("__") and attr.endswith("__"):
            continue
        value = getattr(obj, attr)
        obj_dict[attr] = obj_to_dict(value)
    return obj_dict


def get_user_classes():
    import inspect, sys

    ## Returns a list of all user-defined classes in the current module.
    classes = []
    for name, obj in inspect.getmembers(sys.modules[__name__]):
        if inspect.isclass(obj) and obj.__module__ == __name__:
            classes.append(obj)
    return classes


def pprint(obj):
    print(pprint_dict(obj_to_dict(obj)))


def pprint_dict(dic):
    ## Takes a dictionary and returns it as a string with indentation
    import json

    return json.dumps(dic, indent=4)


def list2Dict(lst):
    ## Takes a 2D list and converts it into a dictionary.
    ## Example Usage:

    ## lst = [["hello", "world"]]
    ## dictionary = list2Dict(lst)
    ## print(dictionary)  # Output: {"hello":"world"}

    dictionary = {}
    for sublst in lst:
        if len(sublst) == 2:
            key, value = sublst[0], sublst[1]
            dictionary[key] = value
    return dictionary


def settingsModule():
    global PREFERENCES, preferences
    if preferences["alias_priority"] == True:
        print("[1] Alias Prority [ENABLED]")
    else:
        print("[1] Alias Prority [DISABLED]")
    print('    If this is enabled, aliases can replace system commands such as "help".')
    print("[2] Edit Default Prompt")
    print("[0] Exit")
    ch = input("$")
    if ch == "1":
        if preferences["alias_priority"] == True:
            preferences["alias_priority"] = False
            settingsModule()
        else:
            preferences["alias_priority"] = True
            settingsModule()
    elif ch == 2:
        preferences["default_prompt"] = input("Prompt $")
        settingsModule()
    elif ch == "":
        settingsModule()
    else:
        save_pref(preferences)
        main()


def getIndex(lst, item):
    lst = list(lst)
    return lst.index(item)


def mergeCurlyBrackets(lst):
    merged_lst = []
    i = 0

    while i < len(lst):
        if i < len(lst) - 1 and lst[i] == "{" and lst[i + 1] == "}":
            merged_lst.append("{}")
            i += 2
        else:
            merged_lst.append(lst[i])
            i += 1

    return merged_lst


def get_variable_names():
    # Get the variables in the global and local namespaces
    global_vars = dir(globals())
    local_vars = dir(locals())

    # Return a list of the variable names
    return global_vars + local_vars


def removeItems(lst, check):
    for item in check:
        try:
            lst.remove(item)
        except:
            pass
    return lst


def banCheck(string, check):
    for item in check:
        if item == string or string.startswith(item):
            return item
    return False


def addCommas(n):
    # Convert the number to a string
    s = str(n)

    # Get the length of the string
    l = len(s)

    # Determine the number of commas to insert
    num_commas = (l - 1) // 3

    # Insert the commas
    for i in range(num_commas):
        index = l - (i + 1) * 3
        s = s[:index] + "," + s[index:]

    # Return the modified string
    return s


def doCalc(s):
    global crashlog
    import re

    try:
        s = re.sub(r"[a-zA-Z]", "", s)
        all_variables = get_variable_names()
        for item in all_variables:
            s = s.replace(item, "")
        # Remove all spaces from the string
        s = s.replace(" ", "")
        s = s.replace("^", "**")

        # Evaluate the expression using eval()
        result = eval(s)

        # Check if there is a comparison operator in the expression
        if "==" in s:
            return result == eval(s.split("==")[1])
        elif ">=" in s:
            return result >= eval(s.split(">=")[1])
        elif "<=" in s:
            return result <= eval(s.split("<=")[1])
        elif "!=" in s:
            return result != eval(s.split("!=")[1])
        elif ">" in s:
            return result > eval(s.split(">")[1])
        elif "<" in s:
            return result < eval(s.split("<")[1])
        else:
            return result
    except Exception as e:
        print(f"Error: {e}")
        return None


def removed(filename, return_mode=0):
    if filename == "/":
        print(f"Error: Deleting the {filename} package has been blocked.")
        return None
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
            print('Error: No "program.name" in zip archive".')
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
            print('Error: No "program.info" in zip archive.')
            return False
        try:
            with open("manuals.zip", "rb") as f:
                man = f.read()
                is_man = 1
        except Exception as e:
            crashlog.append(str(e))
            is_man = 0
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
        if is_man == 1:
            with open("manuals.zip", "wb") as f:
                f.write(man)
            with zipfile.ZipFile("manuals.zip", "r") as zip_ref:
                zip_ref.extractall("Custom Manuals")
            os.remove("manuals.zip")
        if is_xx == 1:
            run_script(xx.split("\n"))
        if is_man == 1:
            f = open(f"Installed Manuals/{progname}.cmanpak", "wb")
            f.write(mandata)
            f.close()
        print(f"Successfully installed {progdata[0]}.")
        if is_mp == 1:
            print(f'To run {progdata[0]}, type "run {progname}"')
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


def can_change_dir(path, startpoint):
    abs_path = os.path.abspath(path)
    start_path = os.path.abspath(startpoint)
    return abs_path.startswith(start_path)


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


def remove_user(user):
    import shutil

    global crashlog, data
    print("Removing user...")
    with open(f"System Settings/userlist.pythinux", "r") as f:
        d = f.read()
    d = d.split("/")
    d2 = []
    for i in d:
        d2.append(i.split("|"))
    d = d2
    for i in d:
        if i[0] == user:
            d.remove(i)
            try:
                shutil.rmtree(user)
            except Exception as e:
                crashlog.append(str(e))
    d2 = ""
    for i in d:
        try:
            d2 += f"{i[0]}|{i[1]}|{i[2]}/"
        except Exception as e:
            crashlog.append(str(e))
    with open("System Settings/userlist.pythinux", "w") as f:
        f.write(d2)
    print("Removed User!")
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


def vim_editor(fn="", add=0):
    global crashlog
    global username
    if fn == "":
        fn = input("File Name >>") + ".vimx"
    if add == 1:
        fn = f"Users/{username}/Vim Files/" + fn
    try:
        with open(fn, "a") as f:
            ata = f.read()
        ata = data.split("\n")
        for item in ata:
            print(item)
    except:
        pass
    f = open(fn, "w")
    div()
    print("Press CTRL+C to exit")
    div()
    try:
        while True:
            f.write(f"{input('>>')}\n")
    except:
        f.close()
    main()


def vim(ch=""):
    global crashlog
    if ch == "":
        logo = [
            "# # ### # #",
            "# #  #  ##   ##",
            "# #  #  # # # #",
            "# #  #  #  #  #",
            " #   #   #  # #",
            "  # ##  # #",
            "   #### # #",
        ]
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
            ch = int(input(">"))
        except Exception as e:
            crashlog.append(str(e))
            main()
    else:
        vim_editor(f"Users/{username}/Vim Files/" + ch)
        print("maybe?")
        main()
    div()
    if ch == 1:
        vim_editor(add=1)
    elif ch == 2:
        try:
            f = open(f"Users/{username}/Vim Files/" + input("File Name >>") + ".vimx")
            data = f.read()
            f.close()
            data = data.split("\n")
            for item in data:
                print(item)
            br()
            main()
        except Exception as e:
            crashlog.append(str(e))
            main()
    elif ch == 3:
        try:
            os.remove(f"Users/{username}/Vim Files/" + input("File name >>") + ".vimx")
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
        fn = f"Users/{username}/Vim Files/" + input("File Name >>")
        try:
            f = open(fn + ".vimx", "r")
            dataa = f.read()
            f.close()
            f = open(fn + ".vimbackup", "w")
            f.write(dataa)
            f.close()
            print("Backed up file.")
            main()
        except Exception as e:
            crashlog.append(str(e))
            print("Failed to back up file.")
            main()
    elif ch == 6:
        fn = f"Users/{username}/Vim Files/" + input("File Name >>")
        try:
            f = open(fn + ".vimbackup", "r")
            dataa = f.read()
            f.close()
            f = open(fn + ".vimx", "w")
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
            os.remove(
                f"Users/{username}/Vim Files/" + input("File name >>") + ".vimbackup"
            )
        except Exception as e:
            crashlog.append(str(e))
            pass
        main()
    elif ch == 8:
        path = os.getcwd() + f"/Users/{username}/Vim Files"
        dirlist = os.listdir(path)
        for item in dirlist:
            if item.endswith(".vimx"):
                print(item.replace(".vimx", ""))
        br()
        vim()
    elif ch == 9:
        path = os.getcwd() + f"/Users/{username}/Vim Files"
        dirlist = os.listdir(path)
        for item in dirlist:
            if item.endswith(".vimbackup"):
                print(item.replace(".vimbackup", ""))
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
    res = uname()
    os.system("cls" if res[0] == "Windows" else "clear")


def sha256(text):
    global crashlog
    import hashlib

    hashed_string = hashlib.sha256(text.encode("utf-8")).hexdigest()
    return hashed_string


def cman(manual):
    global crashlog
    if "/" in manual:
        manual = manual.split("/")
        from zipfile import ZipFile

        try:
            with Zipfile("Custom Manuals/" + manual[0] + ".cmanpak", "r") as zip:
                man = zip.read(manual[1] + ".cman")
            man = man.split("\n")
            for item in man:
                item = item.replace("div()", div())
                print(item)
            return True
        except Exception as e:
            crashlog.append(str(e))
            return False
    else:
        f = open("Custom Manuals/" + manual + ".cman", "r")
        man = f.read()
        f.close()
        man = man.split("\n")
        for item in man:
            item = item.replace("div()", div2())
            print(item)


##        return True


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


def crash(reason="CRASH", subreason="GENERIC_CRASH", crash_loop=0):
    global crashlog
    if crash_loop == 1:
        div()
        print("CRASH")
        div()
        print(
            f"The fatal error occured and {os_name} was forced to terminate itself in order to protect the hardware and software from irreversible damage."
        )
        div()
        print(f"{reason}:{subreason}")
        try:
            ch = input("Restart? Y/N $")
        except Exception as e:
            crashlog.append(str(e))
            sleep(2.5)
            crash(reason, subreason, 1)
        if lower(ch) != "n":
            sleep(2.5)
        crash(reason, subreason, 1)
    else:
        div()
        print("CRASH")
        div()
        print(
            f"The fatal error occured and {os_name} was forced to terminate itself in order to protect the hardware and software from irreversible damage."
        )
        div()
        print(f"{reason}:{subreason}")
        try:
            ch = input("Restart? Y/N $")
        except Exception as e:
            crashlog.append(str(e))
            crash(reason, subreason)
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
    elif user_lvl == 2 and auth() == True:
        return True
    else:
        return False


def auth(msg="AUTHENTICATION"):
    global crashlog, user_lvl
    if user_lvl == 3:
        return True
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
    print("--------------------")


def div_double():
    print("----------------------------------------")


def div_double2():
    return "----------------------------------------"


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
    clear_screen()
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
    os.mkdir("Program Data/Tron")
    with open("Program Data/Tron/docs.txt", "w") as f:
        f.writelines(
            [
                "--------------------\n",
                "Tron Documentation\n",
                "--------------------\n",
                "This is the official documentation for the Tron text editor. \n",
                "--------------------\n",
                "1 Introduction\n",
                "--------------------\n",
                "1.1 Table of Contents\n",
                "--------------------\n",
                "1 Introduction\n",
                "1.1 Table of Contents\n",
                "1.2 What Is Tron?\n",
                "1.3 Who Is Tron For?\n",
                "1.4 What Is Tron For?\n",
                "1.5 How To Report Issues\n",
                "1.6 Full, Unabridged Credits\n",
                "\n",
                "2 Using Tron\n",
                "2.1 Functionality\n",
                "2.2 Keyboard Shortcuts\n",
                "2.3 Debugging\n",
                "2.4 Nuances and Quirks\n",
                "\n",
                "3 Getting Help\n",
                "3.1 Official Help\n",
                "3.2 Contact WinFan3672\n",
                "\n",
                "4 How Tron Works\n",
                "5 End\n",
                "\n",
                "--------------------\n",
                "1.2 What Is Tron?\n",
                "--------------------\n",
                "TRON [Text Editor: Reliable, Organised Notes] is a multi-platofrm, GUI-based text editor with basic file editing functionality. It is written in Tkinter based on the Python programming language, a dynamic, high-level, multi-paradigm general-purpose interpreted programming language. \n",
                "\n",
                "Tron is designed to be easy to use, compact and to only use Python's standard library (which is rather extensive, allowing for things like *this* to be made without external modules).\n",
                "\n",
                "--------------------\n",
                "1.3 Who Is Tron For?\n",
                "--------------------\n",
                "Tron is a text editor, designed to edit text files. It is intended to be a Notepad replacement, and is not necessarily a Notepad++ replacement. As such, it is not tailored to developers, but instead average text editors. While you *can* edit code in it, it is not designed for this. \n",
                "\n",
                "--------------------\n",
                "1.4 What Is Tron For?\n",
                "--------------------\n",
                "Tron is designed to read plain text files. It is NOT designed to read or edit anything else, such as PDF's or eBooks.\n",
                "Files it can open:\n",
                "* Text files\n",
                "* Source code files\n",
                "* HTML Files\n",
                "* Markdown documents\n",
                "* Etc.\n",
                "\n",
                "--------------------\n",
                "1.5 How To Report Issues\n",
                "--------------------\n",
                "* Open an issue on its GitHub (https://github.com/WinFan3672/Pythinux/)\n",
                "* Send an email to me (i.am@mildlysucpicio.us)\n",
                "* DM me on Discord (WinFan3672#8705)\n",
                "\n",
                "--------------------\n",
                "1.6 Full, Unabridged Credits\n",
                "--------------------\n",
                "Tron:\n",
                "\n",
                "Written by Szymon Mochort\n",
                "Coded mostly with ChatGPT\n",
                "ChatGPT Made by OpenAI\n",
                "Written in Tkinter\n",
                "Tkinter is a port of TCL/TK\n",
                "TCL/TK (c) https://tcl.tk/\n",
                "Tkinter is written in Python\n",
                "Python (c) 2001-2023 Python Software Foundation\n",
                "\n",
                "--------------------\n",
                "2 Using Tron\n",
                "--------------------\n",
                "This section details how to use Tron.\n",
                "--------------------\n",
                "2.1 Functionality\n",
                "--------------------\n",
                "Tron has a lot of functionality that allows you to manipulate text files. \n",
                "\n",
                "2.1.1 New/Open Files\n",
                "To create a new file, go to File >> New or press CTRL+N. This clears the program data to make a blank file.\n",
                "To open a file, go to File >> Open or press CTRL+O. This opens a file from a file select menu, and allows you to select the file.\n",
                "\n",
                "2.1.2 Save File\n",
                "To save a file, go to File >> Save or press CTRL+S. If the file has not been saved yet, it will open the Save As menu. \n",
                "\n",
                "The Save As menu (File >> Save As/CTRL+SHIFT+S) allows you to save the currently open file to a specific file based on a dropdown menu. \n",
                "\n",
                "2.1.3 Cut/Copy/Paste\n",
                "To select all text, go to Edit >> Select All or press CTRL+A.\n",
                "To copy the selected text, press CTRL+C or go to Edit >> Copy.\n",
                "To paste it, go to Edit >> Paste or press CTRL+V.\n",
                "\n",
                "2.1.4 Undo/Redo\n",
                "To undo the previous action, press CTRL+Z or go to Edit >> Undo.\n",
                "To redo it, press CTRL+Y or Edit >> Redo.\n",
                "\n",
                "2.1.5 GoTo Line\n",
                "To GoTo a particular line, Edit >> Go to Line or press CTRL+G. A dialog box will open. Type the line number you want to go to and press ENTER.\n",
                "\n",
                "--------------------\n",
                "2.2 Keyboard Shortcuts\n",
                "--------------------\n",
                "SHIFT+F1 >> About Tron\n",
                "CTRL+N >> New File\n",
                "CTRL+O >> Open File\n",
                "CTRL+S >> Save File\n",
                "CTRL+SHIFT+S >> Save File As\n",
                "CTRL+Q >> Exit\n",
                "CTRL+A >> Select All Text\n",
                "CTRL+C >> Copy Text\n",
                "CTRL+V >> Paste Text\n",
                "CTRL+G >> GoTo Line\n",
                "CTRL+Z >> Undo\n",
                "CTRL+Y >> Redo\n",
                "\n",
                "--------------------\n",
                "2.3 Debugging\n",
                "--------------------\n",
                "If you find a bug in Tron, here's how you can debug it:\n",
                "* Check the terminal. Any actions performed should have a debug text. \n",
                "--------------------\n",
                "2.4 Nuances and Quirks\n",
                "--------------------\n",
                "* Undo doesn't work.\n",
                "* If you close the app and changes aren't saved, it still happens.\n",
                "\n",
                "--------------------\n",
                "3 Getting Help\n",
                "--------------------\n",
                "This is how you can get help.\n",
                "--------------------\n",
                "3.1 Official Help\n",
                "--------------------\n",
                "There are a few ways you can get help from within Tron. For instance, you can go to Help >> Tron Documentation and open this document. Help >> Help shows very basic help.\n",
                "--------------------\n",
                "3.2 Contact WinFan3672\n",
                "--------------------\n",
                "WinFan3672 is Tron's creator and your best bet for getting help.\n",
                "* Email\n",
                "     * winfan3672@gmail.com\n",
                "* Discord\n",
                "    * WinFan3672#8705\n",
                "* Tron GitHub\n",
                "    * https://github.com/WinFan3672/tron\n",
                "--------------------\n",
                "4 How Tron Works\n",
                "--------------------\n",
                "Tron is a program written in Tkinter. Tkinter is a Python wrapper for Tcl/Tk. \n",
                "Tron is essentially a big function which contains a TronEditor class, which is instanciated to make a new instance of it. Then, it's run() function is called to run it. \n",
                "--------------------\n",
                "5 End\n",
                "--------------------\n",
                "This is the end of the help document.",
            ]
        )
    if un == "admin":
        create_user(un, passw, 2)
    else:
        create_user(un, passw, 1)
    if un != "admin":
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
            print(f'Set up autologin for user "{un}"')
            div()
        else:
            raise Exception
    except Exception as e:
        crashlog.append(str(e))
        div()
    print(f"Successfully set up {os_name}!")
    print("Using the details for your user account, log into the system.")
    print(
        'Note: If you are a beginner (or noobie), when you log in, use the "started" command. It is the official tutorial.'
    )
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


def terminal(ch=""):
    import re

    chh = ""
    global user_type, username, prompt
    if ch == "":
        rm = 0
        if prompt == "":
            ch = input(f"{user_type}@{username} $")
        else:
            ch = input(prompt)
    else:
        rm = 1
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
    elif ch.startswith("include "):
        if main(ch) == False:
            print("TermEmError: Could not run script.")
            print("[-] File does not exist.")
            print("[-] An unhandled exception occured during execution.")
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
    elif ch == "basic-termem":
        print("[NOTE] Basic TermEm is in beta and is not stable.")
        crashlog.append(f"[BASIC-TERMEM] Started process at time {stime('%x %X')}")
        basic_terminal()
    else:
        n = main(ch)
        if n != None:
            if isinstance(n, list) and n != []:
                if (
                    len(n) == 3
                    and isinstance(n[0], int)
                    and isinstance(n[1], int)
                    and isinstance(n[2], int)
                ):
                    print(f"v{n[0]}.{n[1]}.{n[2]}")
                else:
                    div()
                    for i in n:
                        if callable(i):
                            i()
                        else:
                            print(i)
                    div()
            elif isinstance(n, dict):
                print(n)
            else:
                print(n)
    if rm == 0:
        terminal()


def dir_tree(directory_path, isCman=False):
    """
    Create a directory tree of a specified directory and return it as a list.
    """
    directory_tree = []
    for root, dirs, files in os.walk(directory_path):
        level = root.replace(directory_path, "").count(os.sep)
        indent = " " * 4 * (level)
        if level > 0:
            directory_tree.append(f"{indent}{os.path.basename(root)}/")
        subindent = " " * 4 * (level + 1)
        for file in files:
            if isCman:
                file = file.replace(".cman", "")
            directory_tree.append(f"{subindent}{file}")
    return directory_tree


def main(ch=""):
    global functions
    global crashlog, preferences, PREFERENCES
    preferences = refresh_pref()
    global username, password, user_lvl, user_type, data, stdlib, mem, var_data, prompt, packages, dbs
    if ch == "":
        terminal()
    if ch.startswith("while") == False:
        for i in var_data:
            ch = ch.replace("{" + i[0] + "}", i[1])
    import pickle

    if "[{" in ch and "}]" in ch:
        import re

        pattern = r"\[\{\s*(.*?)\s*\}\]"
        matches = re.findall(pattern, ch)
        for match in matches:
            ch = ch.replace("[{" + match + "}]", str(main(match)))
    if " && " in ch:
        ch = ch.split(" && ")
        run_script(ch)
        return None
    banlist = preferences["banlist"]
    if user_lvl < 1:
        n = banCheck(ch, banlist)
        if n != False:
            div()
            print(f'[ERROR] Insufficient priveleges to run command "{n}".')
            print('For a list of commands you can\'t access, use command "banlist".')
            div()
            return None
    ch = ch.replace("$date", strftime("%x"))
    ch = ch.replace("$time", strftime("%X"))
    ch = ch.replace("$user", username)
    ch = ch.replace("$dir", os.getcwd())
    ch = ch.replace("$uuser", username.upper())
    ch = ch.replace("$os", os_name)
    ch = ch.replace("$utype", user_type)
    ch = ch.replace("$version", f"{app_version[0]}.{app_version[1]}.{app_version[2]}")
    import sys

    ch = ch.replace("$exec", sys.executable)
    if "$input2" in ch:
        ch = ch.replace("$input2", input(">"))
    if "$input3" in ch:
        ch = ch.replace("$input3", input(">"))
    if "$input4" in ch:
        ch = ch.replace("$input4", input(">"))
    if "$input5" in ch:
        ch = ch.replace("$input5", input(">"))
    if "$input" in ch:
        ch = ch.replace("$input", input(">"))
    if preferences["alias_priority"] == True:
        try:
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
                        terminal()
        except Exception as e:
            crashlog.append(str(e))
        try:
            with open(f"System Settings/alias.dat", "r") as f:
                d = f.read()
                d = d.split("\n")
                d2 = []
                for i in d:
                    d2.append(i.split("|"))
                for i in d2:
                    if ch == i[0]:
                        terminal(i[1])
                        terminal()
        except Exception as e:
            crashlog.append(str(e))
    if ch == "help":
        lst = [
            "about",
            "add_alias",
            "add_user",
            "alias",
            "banlist",
            "calc",
            "call",
            "cat",
            "cls",
            "cman",
            "cmanls",
            "cmd",
            "div",
            "div()",
            "echf",
            "echo",
            "funct",
            "getdetails",
            "help",
            "include",
            "installd",
            "logoff",
            "ls",
            "pkm",
            "prompt",
            "pwd",
            "qaa",
            "qaag",
            "quit",
            "reinstall",
            "remove_user",
            "removed",
            "return",
            "rng",
            "run",
            "script",
            "settings",
            "sha256",
            "terminal",
            "time",
            "timer",
            "user",
            "user_control",
            "user_editor",
            "var",
            "view_log",
            "vim",
            "wget",
            "xvim",
        ]
        if user_lvl < 1:
            lst = removeItems(lst, banlist)
        return lst
    elif ch == "banlist":
        return sorted(banlist)
    elif ch == "cls":
        clear_screen()
    elif ch.startswith("man "):
        n = man(ch[4:])
        if n != None:
            return n
    elif ch == "cman":
        div()
        print("cman <manual>")
        div()
        print("Custom manual loader.")
        print('For a list of manuals, use the "cmanls" command')
        div()
    elif ch == "cmanls":
        d = dir_tree("Custom Manuals", True)
        if d == []:
            return "No Installed Manuals."
        else:
            return d
    elif ch.startswith("cman "):
        try:
            with open("Custom Manuals/" + ch[5:] + ".cman", "r") as f:
                print(f.read())
        except Exception as e:
            print(e)
    elif ch == "about" or ch == "about -c":
        return f"{os_name} v{app_version[0]}.{app_version[1]}.{app_version[2]}"
    elif ch == "about -cc":
        return app_version
    elif ch == "about -fc":
        return [app_version[0], app_version[1]]
    elif ch == "logout" or ch == "logoff":
        login()
    elif ch == "quit" or ch == "exit":
        exit()
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
            return ch[5:]
    elif ch == "echo":
        print("echo <str>")
    elif ch == "break":
        br()
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
            print(f'Password [Hashed]: {password}')
            print(f"UserLVL: {user_lvl}")
        else:
            print("You need to be root to access this command.")
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
    elif ch == "remove_user":
        if is_root():
            remove_user(input("Username To Remove $"))
        else:
            return (
                f"Error: Only root users and higher can access the REMOVE_USER command"
            )
    elif ch == "userlist_c" or ch == "userlist -c" or ch == "userlist":
        d = []
        if is_root() == True:
            for item in data:
                d.append(item[0])
        else:
            return f"Error: Only root and higher users can access this command"
        return d
    elif ch == "vim":
        div()
        vim()
    elif ch.startswith("vim "):
        vim(ch[4:])
    elif ch == "xvim":
        print("xvim [file]")
        print("Creates a new file called [file] and opens it in Vim.")
    elif ch.startswith("xvim "):
        vim_editor(ch[5:], 0)
    elif ch == "run /" or ch == "pkm list":
        return os.listdir(os.getcwd() + "/Installed Programs")
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
        print('"run /": lists all installed programs')
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
                    data2.append(f"{item[0]} --> {item[1]}")
                except Exception as e:
                    crashlog.append(str(e))
                    pass
            return data2
        except Exception as e:
            crashlog.append(str(e))
            print("Could not perform command; Perhaps no aliases exist.")
    elif ch == "pass":
        return None
    elif ch.startswith("call "):
        for item in functions:
            if item[0] == ch[5:]:
                run_script(item[1])
    elif ch.startswith("funct "):
        if ":" in ch:
            ch = ch[6:]
            ch = ch.split(":")
            for item in functions:
                if item[0] == ch[0]:
                    functions.remove(item)
            try:
                ch[1] = ch[1].split("/")
            except:
                ch[1] = [ch[1]]
            functions.append(ch)
        else:
            print("[ERROR] Invalid Formatting")
    elif ch == "var":
        div()
        print("var [parameter] <var_name> <value>")
        div()
        print("Parameters")
        div()
        print("set <var_name> <value>")
        print("print <var_name>")
        print("list")
        print("del <var_name>")
        print("backup <filename>")
        print("restore <filename>")
        div()
    elif ch == "funct":
        print("funct {function name}:{code}")
        print('Creates a function that can be called using the "call" command')
    elif ch == "call":
        print("call <function>")
        print('Calls a defined function called with "funct".')
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
        print("Quickly adds an alias to the system.")
    elif ch == "qaag":
        print("qaag [alias]|[command]")
        print('Like "qaa" but global.')
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
        print("Version 1.2.0")
        print(f"OS Version: {app_version[0]}.{app_version[1]}.{app_version[2]}")
        print("Build Date: 1 Apr 2023")
        print("(c) 2023 WinFan3672, Some Rights Reserved.")
    elif ch == "pkm version -c":
        print(
            f"PKM Version 1.2.0 : OS Version {app_version[0]}.{app_version[1]}.{app_version[2]}"
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
        main("pkm db clean")
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
            except Exception as e:
                crashlog.append(str(e))
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
    elif ch == "pkm db clean":
        dbs = list(set(dbs))
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
        refresh_data()
        for i in data:
            if i[0] == un and sha256(pw) == i[1]:
                login(un, sha256(pw))
    elif ch == "reinstall":
        if is_god() == True:
            if auth() == True:
                os.chdir("..")
                import shutil

                shutil.rmtree("Pythinux")
                os.mkdir("Pythinux")
                os.chdir("Pythinux")
                setup_wizard()
                login("xm", "xm")
            else:
                print("User operation cancelled.")
                return None
        else:
            print("Requires GOD user priveleges.")
            return None
    elif ch == "stopexec":
        print("[EXEC] Execution Manually Stopped")
        terminal()
    elif ch == "settings":
        settingsModule()
    elif ch == "settings reset":
        if confirmation():
            save_pref(PREFERENCES)
            print("Saved Preferences")
    elif ch == "settings -v":
        return preferences["pref_format"]
    elif ch == "settings --alias-priority true":
        preferences["alias_priority"] = True
        save_pref(preferences)
    elif ch == "settings --alias-priority false":
        preferences["alias_priority"] = False
        save_pref(preferences)
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
                lines = [line.strip() for line in f.readlines()]
                run_script(lines)
                return None
        except Exception as e:
            crashlog.append(str(e))
            return False
    elif ch == "script":
        div()
        print("script [parameter]")
        print("script new [name] - creates a new scipt called [name]")
        print("script list - returns list of installed scripts")
        print("script run [name] - runs a script in your scripts directory")
        div()
    elif ch == "script list":
        n = os.listdir(os.getcwd() + f"/Users/{username}/Scripts")
        index = -1
        for item in n:
            index += 1
            if not item.endswith(".xx"):
                n.remove(item)
            try:
                n[index] = n[index].replace(".xx", "")
            except:
                pass
        return n
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
    elif ch == "ls" or ch == "dir":
        return os.listdir(os.getcwd())
    elif ch == "pwd":
        return os.getcwd()
    elif ch == "settings --export":
        return preferences
    elif ch == "terminal()":
        terminal()
    elif ch == "user":
        div()
        print("user [parameter]")
        div()
        # print("user import <file> - imports a user file")
        print("user export <user> - exports a user to a user file")
        print("user create - creates a user")
        print("user list - creates a user")
        print("user remove <user> - removes a user")
        # print("user disable <user> - disables a user")
        div()
    elif ch == "user create":
        main("add_user")
    elif ch.startswith("user remove "):
        remove_user(ch[12:])
    elif ch == "user list":
        print(main("userlist -c"))
    elif ch.startswith("user export "):
        import shutil

        un = ch[12:]
        try:
            with open(f"Users/{un}/username.pythinux", "w") as f:
                f.write(un)
            with open(f"Users/{un}/pythinux.version", "wb") as f:
                f.write(pickle.dumps(app_version))
            shutil.make_archive(
                input("ZipName $") + ".user_export", "zip", f"Users/{un}"
            )
            print("Exported user.")
        except Exception as e:
            crashlog.append(str(e))
            print(str(e))
        us = ch[12:]
    elif ch == "settings dprompt":
        terminal("prompt", preferences["default_prompt"])
    elif ch.startswith("settings dprompt "):
        ch = ch[17:]
        preferences["default_prompt"] = ch
        save_pref(preferences)
        terminal("prompt " + preferences["default_prompt"])
    elif ch == "ctime":
        return stime(preferences["time_format"])
    elif ch == "cmd":
        print("cmd <command>")
        print("Sends <command> to your OS's terminal.")
        main()
    elif ch == "format":
        print("format <number>")
        print("Returns the number with commas inserted.")
    elif ch.startswith("format "):
        return addCommas(ch[7:])
    elif ch == "calc":
        div()
        print("calc <str>")
        div()
        print("Performs an arithmetic calculation")
        div()
        print("Supported Operations")
        div()
        print("+ Addition")
        print("- Subtraction")
        print("* Multiplication")
        print("/ Division")
        print("// Integer Division (removes decimal)")
        print("% Modulus (returns remainder of division)")
        print("^ or ** indices (10 ** 2 = 10 to the power of 2)")
        div()
        print("Conditional Formatting Support (returns boolean)")
        div()
        print("== is equal to")
        print("!= is not equal to")
        print(">= is greater than/equal to")
        print(">= is less than/equal to")
        print("> greater than")
        print("< less than")
        div()
        print("Examples")
        div()
        print("calc 3/2*(3+2)")
        div()
    elif ch.startswith("calc "):
        return doCalc(ch[5:])
    elif ch.startswith("return "):
        try:
            return eval(ch[7:])
        except Exception as e:
            crashlog.append(str(e))
    elif ch.startswith("type "):
        try:
            return type(eval(ch[5:]))
        except:
            return None
    elif ch == "return":
        print("return <val>")
        print("returns value")
        print("Tip: this can return values in Python memory")
    elif ch == "input":
        print("input <prompt>")
        print("Returns user input with <prompt>")
    elif ch.startswith("input "):
        return input(ch[6:])
    elif ch == "type":
        print("type <eval>")
        print("Returns type(eval(<eval>))")
    else:
        try:
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
                        terminal()
        except Exception as e:
            crashlog.append(str(e))
        try:
            with open(f"System Settings/alias.dat", "r") as f:
                d = f.read()
                d = d.split("\n")
                d2 = []
                for i in d:
                    d2.append(i.split("|"))
                for i in d2:
                    if ch == i[0]:
                        terminal(i[1])
                        terminal()
        except Exception as e:
            crashlog.append(str(e))
        return f'SyntaxError: "{ch}" is not a valid command, manual, alias or program.'


def start(lvl, al, un, pwd):
    global crashlog, user_lvl, user_type, username, password
    username = un
    password = pwd
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
        div()
        print(f"Welcome to {os_name}.")
        print(f"[{os_name} v{app_version[0]}.{app_version[1]}.{app_version[2]}]")
        div()
        if user_lvl == 0:
            print("You are logged in on a guest account.")
            print(
                "Guest accounts have limited access to commands and cannot install/remove programs."
            )
        elif user_lvl == 2:
            print("You are logged in as a root account.")
            print("If you do not know what this means, type LOGOFF right now.")
        elif user_lvl == 3:
            print(
                "Warning! GOD users have very high priveleges and are fully unrestricted."
            )
            print("Exercise caution and common sense when using a God account.")
            print(
                "If you are unaware of the security implications of using a God account, or what any of this means, type LOGOFF right now."
            )
            print("DO NOT USE A GOD ACCOUNT AS YOUR DAILY DRIVER ACCOUNT.")
        div()
    if al == 1:
        main("cls")
        div()
        print("Autologin Security")
        div()
        print("For security, enter your password:")
        while True:
            newpass = getpass.getpass("Password $")
            if sha256(newpass) == password:
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
        if os.path.isfile(os.getcwd() + f"/Users/{username}/startup.xx") == True:
            try:
                with open(f"Users/{username}/startup.xx", "r"):
                    lines = [line.strip() for line in f.readlines()]
                    print(lines)
                    run_script(lines)
            except Exception as e:
                crashlog.append(str(e))
        else:
            crashlog.append("[STARTUP] No User Startup File")
    terminal("prompt " + preferences["default_prompt"])
    terminal()


def login(username="", password=""):
    global data
    if data == []:
        print("Your userfile is corrupt.")
        print("Do you wish to reinstall the OS?")
        ch = input("[y/n] $")
        if ch == "y":
            os.chdir("..")
            shutil.rmtree("Pythinux")
            os.mkdir("Pythinux")
            os.chdir("Pythinux")
            setup_wizard()
            os_init()
        else:
            while True:
                sleep(1)
    if username == "" and password == "":
        al = 0
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
            div()
            for i in data:
                print(i[0])
            login()
        password = sha256(getpass.getpass("Password $"))
    else:
        al = 1
    refresh_data()
    for i in data:
        if i[0] == username and i[1] == password:
            start(int(i[2]), al, username, password)
    login()


def refresh_pref():
    import pickle

    global PREFERENCES
    if os.path.isfile("System Settings/system.preferences") == False:
        save_pref(PREFERENCES)
    with open("System Settings/system.preferences", "rb") as f:
        d = pickle.loads(f.read())
        if d["pref_format"] == PREFERENCES["pref_format"]:
            return d
        else:
            return False


def save_pref(preferences):
    import pickle

    with open("System Settings/system.preferences", "wb") as f:
        f.write(pickle.dumps(preferences))


def os_init():
    global crashlog, preferences, PREFERENCES
    global username, password, user_lvl, user_type, user_type
    global startpoint
    refresh_data()
    preferences = False
    while preferences == False:
        preferences = refresh_pref()
        if preferences == False:
            div()
            print("Preferences Error")
            div()
            print("Error: Preferences File Out of Date.")
            print("Likely caused by system update.")
            print("Preferences will reset and update to latest version.")
            br()
            preferences = PREFERENCES
            with open("System Settings/system.preferences", "wb") as f:
                f.write(pickle.dumps(preferences))
    try:
        f = open("System Settings/autologin.dat")
        aldata = f.read()
        f.close()
        aldata = aldata.split("|")
        login(aldata[0], aldata[1])
    except Exception as e:
        crashlog.append(str(e))
        login(autologin)


try:
    print(os.getcwd())
    os.chdir("Pythinux")
    startpoint = os.getcwd()
except Exception as e:
    crashlog.append(str(e))
    os.mkdir("Pythinux")
    os.chdir("Pythinux")
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
