import os

line = str(input())
a = []
s = ""
current = 0
index = 0

def evaluate(i):
    global a, s, current, index
    if i == "+":
        a[current] += 1
    if i == "-":
        a[current] -= 1
    if i == "_":
        a[current] = 0
    if i == "=":
        s = str(s+chr(a[current]))
    if i == "$":
        s = str(s+str(a[current]))
    if i == "^":
        print(s)
        s = ""
    if i == "#":
        a[current] = int(input())
    if i == "!":
        a[current] = 0
        for i in str(input()):
            a[current] += int(ord(i))
    if i == ">":
        a.append(0)
    if i == "<":
        a.pop()
    if i == "\\":
        if current == len(a):
            current = 0
        else:
            current += 1
    if i == "/":
        if current == 0:
            current = len(a)
        else:
            current -= 1
    if i == ":":
        for i in a:
            print(chr(i))
    if i == "|":
        if a[int(line[index])] == a[int(line[index+1])]:
            for x in line[(index+2):]:
                print(x)
                if x != "~":
                    evaluate(x)
                else:
                    break
    if a[current] != 0:
        if i == "(":
            for x in range(1, a[current]):
                for y in line[index:]:
                    if y != ")":
                        evaluate(y)
                    if y == ")":
                        break
        if i == "[":
            for x in range(1, a[current]**2):
                for y in line[index:]:
                    if y != "]":
                        evaluate(y)
                    if y == "]":
                        break
        if i == "{":
            for x in range(1, a[current]**3):
                for y in line[index:]:
                    if y != "}":
                        evaluate(y)
                    if y == "}":
                        break

for i in line:
    index += 1
    evaluate(i)

input()

os.startfile(__file__)