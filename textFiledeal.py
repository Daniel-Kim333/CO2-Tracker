"""import os
if os.path.exists("2.txt"):
    os.remove("2.txt")
else:
    print("The file does not exist")"""


def readFile(filename):
    try:
        with open(filename, "r") as f:
            print(f.read())
    except FileNotFoundError:
        print(f"file {filename} is not found")


def funprintline():
    print("==="*15)


readFile("1.txt")
print("\n"*3)
readFile("2.txt")
print("*"*30)
readFile("3.txt")
print(funprintline())
readFile("4.txt")

# gets grav details from file
qbfile = open("2.txt", "r")
print("ALl good")


x = 0
t = []
for aline in qbfile:
    values = aline.split()  # split puts an item in a list
    t.append(values)

print(type(values))
print(t)
qbfile.close()

funprintline()
w = open("3.txt", "w")  # run this code with a mode
str = ["Login#password\n", "user1#pswd1\n", "user2#pswd2\n", "user3#pswd3\n", "user4#pswd4"]
w.writelines(str)
w.close()

