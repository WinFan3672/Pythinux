cls()
if os.path.isfile("../LICENSE"):
    with open("../LICENSE") as f:
        div()
        print(f.read())
        div()
else:
    print("ERROR: No license file found.")    