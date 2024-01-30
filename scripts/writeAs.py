f = open("testfileA", "w")
for x in range(1000000):
    f.write("A")
f.close()
