if args:
    args = " ".join(args)
    if os.path.exists(f"app/{args}.py"):
        os.remove(f"app/{args}.py")
    elif os.path.exists(f"app_high/{args}.py"):
        os.remove(f"app_high/{args}.py")
    else:
        raise OSError(f"Cannot find package '{args}'")
    print(f"Successfully removed {args}.")
else:
    div()
    print("removed <program>")
    div()
    print("Removes an installed program.")
    div()
