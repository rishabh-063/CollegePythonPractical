
with open("file.txt", "x+t") as f:
    f.write("This is another line.\n")
    f.seek(0)
    print(f.read())


