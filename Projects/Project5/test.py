try:
    x="x"
    print(int(x))
    print(x)
except ValueError:
    print("lol")
except Exception:
    print("lol 2")
    raise