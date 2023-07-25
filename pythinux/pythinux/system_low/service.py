import threading
if args == ["start"]:
    div()
    print("service start '[program]'")
    div()
    print("Starts a program as a service.")
    div()
elif args and args[0] == "kill" and len(args) == 2:
    x = threading.enumerate()[2:]
    x[int(args[1])-1].kill()
    print("Successfully killed process.")    
elif args and args[0] == "start" and len(args) == 2:
    service = createService(args[1],currentUser)
    startService(service,args[0])
elif args == ["list"]:
    if not threading.enumerate()[2:]:
        div()
        print("Error: No running processes.")
        div()
    else:
        x = 1
        div()
        for i in threading.enumerate()[2:]:
            print(f"[{x}] {i.name}")
            x += 1
        div()
elif args == ["kill"]:
    div()
    print("service kill <id>")
    div()
    print("Kill a process based on ID.")
    div()
else:
    div()
    print("service [arguments]")
    print("Service handler.")
    div()
    print("Valid arguments:")
    print("    start: start a process")
    print("    list: lists all running process")
    print("    kill: kills a process")
    div()
