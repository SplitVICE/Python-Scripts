i = input("Enter input: ")
iL = i.lower()
l = ["a", "b", "c", "d", "e", "f", "g", "h",
     "i", "j", "k", "l", "m", "n", "o", "p",
     "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
o = ""

for x in iL:
    try:
        o += str(l.index(x) + 1)
    except:
        o += str(0)

print(o)
