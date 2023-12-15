import random

def criateList():
    numberList = []
    def addNumberInList():
        if len(numberList) != 6:
            numberList.append(random.randint(1, 50))
            addNumberInList()

    addNumberInList()
    return numberList

def addListInList():
    listNumberList = []
    def addnumberListinList():
        if len(listNumberList) != 6:
            listNum = criateList()
            listNumberList.append(listNum)
            addnumberListinList()

    addnumberListinList()
    return listNumberList


def enterList(num2, listNum):
    if num2 != 6:
        if num2 == 5:
            print(listNum[num2])
        else:
            print(listNum[num2], end=' ')
        num2 += 1
        enterList(num2, listNum)

def enterListNumber(num, listNumber):
    if num != 6:
        listNum = listNumber[num]
        num += 1
        enterList(0, listNum)
    enterListNumber(num, listNumber)


def printListNumber():
    listNumber = addListInList()
    print(listNumber)
    enterListNumber(0, listNumber)
#hi
#hi
printListNumber()
