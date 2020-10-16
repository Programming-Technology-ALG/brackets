import math


def printArr():
    for i in range(math.ceil(len(str1) / 2)):
        print(arr[i])
    return


def checkString():
    chars = set('()?')
    if any((c in chars) for c in str1):
        return 1
    else:
        print("String must contain only such symbols as: (?)")
        return 0


str1 = input("Type a string: ")
if checkString():
    if 0 == len(str1) % 2 and str1[0] != ')':
        arr = [[0] * len(str1) for i in range(math.ceil(len(str1) / 2) + 1)]
        arr[1][0] = 1
        for j in range(1, len(str1)):
            for i in range(math.ceil(len(str1) / 2) + 1):
                if str1[j] == '?':
                    if 0 < i < math.ceil(len(str1) / 2):
                        arr[i][j] = arr[i - 1][j - 1] + arr[i + 1][j - 1]
                    elif i == 0:
                        arr[i][j] = arr[i + 1][j - 1]
                    elif i == math.ceil(len(str1) / 2):
                        arr[i][j] = arr[i - 1][j - 1]
                elif str1[j] == ')' and 0 <= i < math.ceil(len(str1) / 2):
                    arr[i][j] = arr[i + 1][j - 1]
                elif str1[j] == '(' and 0 < i <= math.ceil(len(str1) / 2):
                    arr[i][j] = arr[i - 1][j - 1]
        print(arr[0][len(str1) - 1])
    else:
        print("Problems with string")
