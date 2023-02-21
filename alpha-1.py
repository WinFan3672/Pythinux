os="Python Linux"
version="Alpha 1"
print("Welcome to",os,version)
def logged():
    osk=input("$")
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
        print("help, div, about, ping, randint, author, mod, chngpass, rand, mul, quit, logoff")
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
        if oldpass != "root":
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
    else:
        print(osk,"is not a valid command")
        logged()
def login():
    username=input("Username $")
    password=input("Password $")
    base=username+":"+password
    if base != "root:root":
        print("The username or password is invalid.")
        login()
    else:
        logged()

login()
