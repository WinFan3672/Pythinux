cls()
if os.path.isfile("../helptopics/License"):
    with open("../helptopics/License") as f:
        div()
        print(f.read())
        div()
else:
    print("ERROR: No license file found.")    