import os
#nova verzija
print(os.getcwd())

os.chdir("/home/natasa/Desktop/python")

fajl = open("test3Fajl.txt", "w")
fajl.write("fajl je upravo napravljen\n")
fajl.close()

fajl = open("test3Fajl.txt","a")
fajl.write("prvi dodat red\n")
fajl.write("drugi dodat red\n")
fajl.close()


with open("test3Fajl.txt","r") as f:
    for linija in f:
        print(linija.strip())
