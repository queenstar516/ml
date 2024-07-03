def printStrContent(str):
    [print(i) for i in str]

def revStr(str):
    i = len(str) - 1
    while i >= 0:
        print(str[i])
        i -= 1


revStr(input())