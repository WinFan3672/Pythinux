#!/usr/bin/python
import os
os.chdir("pythinux")
from pythinux import *
import pythinux
global currentUser, currentGroup, userList
currentGroup = Group("unit", True, True, True, True)
p = hashString("unittest")
currentUser = User(currentGroup, "test", p)
userList = UserList()
userList.add(currentUser)
class Unit(Base):
    def __init__(self, name, command):
        self.name = name
        self.command = command

    def execute(self):
        print(self.command)

class CommandUnit(Unit):
    def execute(self):
        o = pythinux.load_program(self.command, currentUser)
        if o:
            print(o)

class OSUnit(Unit):
    def execute(self):
        os.system(self.command)
class FunctionUnit(Unit):
    def execute(self):
        self.command()
i = 1
def function():
    print(os.getcwd())
def loadAllPrograms():
    i = 1
    c = list_loadable_programs(currentUser)
    for item in c:
        print("    [{}/{}] {}".format(i,len(c),item))
        main(currentUser,item)
        i += 1
units = [
    FunctionUnit("Print Current Directory",function),
    Unit("Test", "Testing..."),
    # CommandUnit("Install StartPKG","pkm install -y startpkg")
    FunctionUnit("Run All Programs",loadAllPrograms)
]
print("Begin...")
for unit in units:
    print("[{}/{}] {}".format(i, len(units), unit.name))
    unit.execute()
    i += 1
print("All unit tests complete.")
