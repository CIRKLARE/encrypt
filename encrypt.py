#!/bin/python3
path = input("path to your file : ")
password = int(input("password : "))
fin = open(path, "rb")
file = fin.read()
fin.close()
file = bytearray(file)

for index, values in enumerate(file):
    file [index] = values ^ password
    
fin = open(path, "wb")

fin.write(file)
fin.close()
print("Done")
