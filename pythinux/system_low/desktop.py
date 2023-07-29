manager = Desktop.WindowManager()
base = manager.create_base_window("Pythinux {} (Unstable Pre-Release)".format(".".join([str(x) for x in version])), 1600, 900)
manager.start()