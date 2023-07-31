import os
import importlib
import zipfile
import traceback
import shutil
pkm = silent(lambda:load_program("pkm",currentUser))
def filterDeps(deps):
    filtered_deps = [x for x in deps if x not in pkm.list_app()]
    return filtered_deps, deps
PackageInf = pkm.PackageInf
class InstallerError(Exception):
    def __init__(self,message="Could not install program"):
        self.msg = message
    def __str__(self):
        return self.msg
def installd(path,yesMode=False,depMode=False,upgradeMode=False):
    try:
        with open(path,"rb") as f:
            x = f.read()
        clearTemp()
        os.chdir("tmp")
        with open("program.szip3","wb") as f:
            f.write(x)
        with open("program.szip3","rb") as f:
            with zipfile.ZipFile(f,"r") as zf:
                with zf.open("program.name") as f:
                    name = f.read().decode("utf-8")
                try:
                    with zf.open("requirements.txt") as f:
                        deps = f.read().decode("utf-8").split("\n")
                        os.chdir("..")
                        deps, originalDeps = filterDeps(deps)
                        os.chdir("tmp")
                except:
                    deps, originalDeps = [], []
                with zf.open("program.info") as f:
                    info = f.read().decode("utf-8").split("|")
                    for item in info:
                        item.strip()
                    for item in info:
                        item.strip()
                if "manuals.zip" in zf.namelist():
                    manualsMode = True
                    zf.extract("manuals.zip")
                else:
                    manualsMode = False
                if "library.zip" in zf.namelist():
                    libMode = True
                    zf.extract("library.zip")
                else:
                    libMode = False
                if "program.py" in zf.namelist():
                    with zf.open("program.py") as f:
                        program = f.read()
                else:
                    program = None
                if "rscript.xx" in zf.namelist():
                    with zf.open("rscript.xx") as f:
                        rscript = f.read().decode("utf-8")
                if "desktop.entry" in zf.namelist():
                    with zf.open("desktop.entry") as f:
                        with open("icon/{}.entry".format(name),"wb") as g:
                            g.write(f.read())
                if "icon.svg" in zf.namelist():
                    with zf.open("icon.svg") as f:
                        with open("icon/{}.svg".format(name),"wb") as g:
                            g.write(f.read())
                else:
                    rscript = False
                if "setup.py" in zf.namelist():
                    setupMode=True
                    with zf.open("setup.py","r") as f:
                        setupCode=f.read().decode("utf-8")
                else:
                    setupMode=False
                if "SYSTEM" in zf.namelist():
                    system=True
                else:
                    system=False
        name = name.replace(" ","")
        name=name.replace("\n","")
        if not yesMode:
            cls()
            div()
            print("Install Program?")
            div()
            print(f"Name: {info[0]}")
            print(f"Version: {info[1]}")
            print(f"Release Date: {info[2]}")
            print(f"Author: {info[3]}")
            print("Dependencies: {}".format("; ".join(deps) if deps else "None"))
            div()
            ch = input("[y/n] $").lower()
        else:
            ch = "y"
        if ch != "y":
            return None
        else:
            os.chdir("..")
            if upgradeMode:
                return info
            dd = "|".join(originalDeps)
            cmd = "pkm register '{}' '{}' '{}' {} '{}' '{}'".format(name,info[1],dd if originalDeps else [],1 if program else 0,info[0],info[2])
            load_program(cmd,currentUser,shell="installd")
            no = 1
            for item in deps:
                print(f"({no}/{len(deps)}) Installing '{item}' (dependency of '{name}')...")
                main(currentUser,f"pkm install -d {item}")
                no += 1
            if setupMode and not yesMode:
                if input("Review setup script? [y/n]").lower() == "y":
                    cls()
                    print(setupCode)
                    br()
                print(setupCode)
                exec(setupCode)
            try:
                v = info[4]
                v = v.split(".")
                z = []
                for i in v:
                    z.append(int(i))
                v = z
                if v > [version[0],version[1]]:
                    raise InstallerError(f"Package requires newer OS version: {v[0]}.{v[1]}")
            except Exception as e:
                raise InstallerError(str(e))
            if libMode:
                with zipfile.ZipFile("tmp/library.zip") as f:
                    f.extractall("tmp/libtmp")
                if os.path.exists("tmp/libtmp/lib.name"):
                    with open("tmp/libtmp/lib.name") as f:
                        libName=f.read().replace("\n","")
                    if os.path.exists("tmp/libtmp/lib.ver"):
                        with open("tmp/libtmp/lib.ver") as f:
                            libVer=f.read().replace("\n","")
                        shutil.make_archive("lib/lib", 'zip', "tmp/libtmp/lib")
                        if not os.path.isdir("lib/{}/{}".format(libName,libVer)):
                            if not os.path.isdir("lib/{}".format(libName)):
                                os.mkdir("lib/{}".format(libName))
                            if not os.path.isdir("lib/{}".format(libVer)):
                                os.mkdir("lib/{}/{}".format(libName,libVer))
                            with zipfile.ZipFile("lib/lib.zip") as f:
                                f.extractall("lib/{}/{}".format(libName,libVer))
                            os.remove("lib/lib.zip")
                    else:
                        print("Error: No 'lib.ver' provided.")
                else:
                    print("Error: No 'lib.name' provided.")
            if system:
                fn = f"app_high/{name}.py"
            else:
                fn = f"app/{name}.py"
            if rscript:
                with open(f"rscript/{name}.xx","w") as f:
                    f.write(rscript)
            if program:                
                with open(fn,"wb") as f:
                    f.write(program)
            if manualsMode:
                os.mkdir(f"man/{name}")
                zip_path = os.getcwd()+"/tmp/manuals.zip"
                os.chdir(f"man/{name}")
                with open(zip_path,"rb") as f:
                    with zipfile.ZipFile(f,"r") as zip:
                        zip.extractall()
                os.chdir(cdir)
            if os.path.isfile("tmp/setup.xx"):
                if depMode:
                    silent(lambda:main(currentUser,f"script tmp/setup.xx"))
                else:
                    main(currentUser,f"script tmp/setup.xx")
        if not depMode:
            print(f"Successfully installed '{name}'.")
        else:
            print("Dependency '{}' installed.".format(name))
    except Exception as e:
        print(traceback.format_exc())
if arguments:
    if "-y" in arguments:
        arguments.remove("-y")
        yesMode=True
    else:
        yesMode=False
    if "-d" in arguments:
        arguments.remove("-d")
        yesMode=True
        depMode=True
    else:
        depMode=False
    if "-u" in args:
        args.remove("-u")
        upMode=True
    else:
        upMode=False
    installd(" ".join(arguments),True,depMode,upMode)
else:
    div()
    print("installd <path/to/installer.szip3>")
    print("Installs an SZIPS3 program.")
    div()
    print("Optional positional arguments:")
    print("    -y: installs without confirmation")
    div()
