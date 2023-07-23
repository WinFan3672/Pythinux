User = User
if arguments == ["list"]:
    for item in userList:
        div()
        print(f"Username: {item.username}")
        print(f"Password: {item.password}")
        print(f"LVL: {item.lvl}")
    div()
elif arguments == ["add"]:
    div()
    print("user add <username> <password> [lvl]")
    div()
    print("LVL Guide:")
    print("0 - Guest")
    print("1 - User")
    print("2 - Root")
    print("3 - God")
    div()
elif "add" in arguments and len(arguments) >= 3:
    if len(arguments) == 3:
        arguments.append(1)
    u = User(arguments[1],arguments[2],int(arguments[3]))
    userList = createUser(userList,u)
    saveUserList(userList)
elif arguments == ["remove"]:
    div()
    print("user remove <user>")
    div()
    print("Removes <user> from system.")
    div()
elif "remove" in args and len(args) == 2:
    for i in userList:
        if i.username == args[1]:
            removeUser(userList,i)
else:
    div()
    print("user [args]")
    print("Program for creating and managing users.")
    div()
    print("Arguments:")
    print("    add: adds a user")
    print("    list: lists all users")
    print("    remove: removes a user")
    div()
