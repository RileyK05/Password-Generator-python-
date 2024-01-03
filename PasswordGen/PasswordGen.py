import random

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            return
        lastNode = self.head
        while lastNode.next:
            lastNode = lastNode.next
        lastNode.next = newNode
    def getLength(self):
        count = 0
        currentNode = self.head
        while currentNode:
            count += 1
            currentNode = currentNode.next
        return count

lowrCase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

upprCase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
             'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

specChar = ['.', '!', '*', ',', '$', '-', '=']

lowrCaseSize = len(lowrCase)
upprCaseSize = len(upprCase)
numbersSize = len(numbers)
specCharSize = len(specChar)

lenOfPassword = input("How long will the password be: ")
lenOfPassword = int(lenOfPassword)

passwordList = LinkedList()

i = 0
while i < lenOfPassword:
    randOfChoice = random.randint(1, 4)
    if randOfChoice == 1:
        randLetr = lowrCase[random.randint(0, lowrCaseSize - 1)]
        passwordList.append(randLetr)
    elif randOfChoice == 2:
        randULetr = upprCase[random.randint(0, upprCaseSize - 1)]
        passwordList.append(randULetr)
    elif randOfChoice == 3:
        randNum = str(numbers[random.randint(0, numbersSize - 1)])
        passwordList.append(randNum)
    elif randOfChoice == 4:
        randSpecChar = specChar[random.randint(0, specCharSize - 1)]
        passwordList.append(randSpecChar)
    i += 1

password = ""
currentNode = passwordList.head

while currentNode:
    password += str(currentNode.data)
    currentNode = currentNode.next

print(f"Password: {password}")

