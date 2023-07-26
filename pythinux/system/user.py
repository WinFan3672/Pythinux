User = User
if args == ["list"]:
    for item in userList:
        if not item.hidden:
            div()
            print(f"Username: {item.username}")
            print(f"Password: {item.password}")
            print(f"LVL: {item.lvl}")
    div()
elif args == ["add"]:
    div()
    print("user add <username> <password> <group_name>")
    div()
    print("For a list of groups:")
    print("group list")
    div()
elif "add" in args and len(args) == 4:
    gl = loadGroupList()
    g = gl.byName(args[3])
    u = User(g, args[1],args[2])
    userList = createUser(userList,u)
    saveUserList(userList)
elif args == ["remove"]:
    div()
    print("user remove <user>")
    div()
    print("Removes <user> from system.")
    div()
elif "remove" in args and len(args) == 2:
    for i in userList:
        if i.username == args[1]:
            removeUser(userList,i)
elif args == ["info"]:
    div()
    print("user info <username>")
    div()
    print("Lists info about a user.")
    div()
elif "info" in args and len(args) == 2:
    u = userList.byName(args[1])
    pprint(u)
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
