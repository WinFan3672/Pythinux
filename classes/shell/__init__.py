from classes import desktopenv
import pythinux
def startShell():
    manager = desktopenv.WindowManager()
    base = manager.create_base_window("Pythinux {} (Unstable Pre-Release)".format(".".join([str(x) for x in pythinux.version])), 1600, 900)
    manager.start()