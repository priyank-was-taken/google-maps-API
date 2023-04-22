# # tech = ['a', 'b', 'c']
# # newtech = ['a', 'b', 'c']
# # retech = newtech
# # print(retech is newtech)

# # mylist = [17, 7, 5, 3, 4]
# # yourlist = mylist[1:-1]
# # print(yourlist)

# # mylist = [0, 1, 2, 3, 4]
# # mylist[0], mylist[4] = mylist[4], mylist[0]
# # mylist[1], mylist[3] = mylist[3], mylist[1]
# # print(mylist)

# # print(7//2*4)
# # print(7/2*4)

# # def xobinChars(st):
# #     if len(st) > 256:
# #         return False
# #     char_set = [False] * 128
# #     for i in range(0, len(st)):
# #         val = ord(st[i])
# #         if char_set[val]:
# #             return False
# #         char_set[val] = True
# #     return True
# # st = "xobin"
# # print(xobinChars(st))    

# # class Solution:
# #     def intToRoman(self, num: int) -> str:
# #         # Creating Dictionary for Lookup
# #         num_map = {
# #             1: "I",
# #             5: "V",    4: "IV",
# #             10: "X",   9: "IX",
# #             50: "L",   40: "XL",
# #             100: "C",  90: "XC",
# #             500: "D",  400: "CD",
# #             1000: "M", 900: "CM",
# #         }

# #         # Result Variable
# #         r = ''


# #         for n in [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]:
# #             # If n in list then add the roman value to result variable
# #             while n <= num:
# #                 r += num_map[n]
# #                 num-=n
# #         return r

# # obj = Solution()
# # print(obj.intToRoman(2222))    

# # for i in range(6):
# #     for x in range(i):
# #         print("*", end=" ")
# #     print()    
# class Node:
#     def __init__(self, value=None):
#         self.value = value
#         self.next = None


# class singlylinkedlist:
#     def __init__(self):
#         self.head = None
#         self.tail = None
#         self.count = 0

#     def __iter__(self):
#         node = self.head
#         while node:
#             yield node
#             node = node.next

#     def createSLL(self, value):
#         node = Node(value)
#         self.head = node
#         self.tail = node
#         self.count += 1

#     def appendSLL(self, value):
#         newNode = Node(value)
#         if self.head is None:
#             self.head = newNode
#             self.tail = newNode
#         else:
#             self.tail.next = newNode
#             self.tail = newNode
#         self.count += 1

#     def deleteDuplicates(self, head):
#         temp = self.head
#         while (temp and temp.next):
#             if (temp.next.val == temp.val):
#                 temp.next = temp.next.next
#                 continue
#             temp = temp.next
#         return head

# # x = [1,2,2,5,1]    

# # print(sol.deleteDuplicates(x)) 
# SLinkedList = singlylinkedlist()
# SLinkedList.createSLL(1)
# SLinkedList.appendSLL(2)
# SLinkedList.appendSLL(2)
# SLinkedList.appendSLL(5)
# SLinkedList.appendSLL(1)
# print([node.value for node in SLinkedList])
# SLinkedList.deleteDuplicates()

# ----------------------------------------------------------------

# unique_coins: [2, 3, 9, 4, 7, 1]   cost = 9

# output: True
# Explanation: 2+7 = 9

# if cost = 15
# output: False
# Explanation: there are no two coins sum is equal to 15


# x = [2, 3, 9, 4, 7, 1]
# cost = 13

# for i in range(len(x)):
#     for j in range(1, len(x)):
#         # print("(",x[i],x[j],")")
#         if x[i] + x[j] == cost:
#             print(True)
#             print("(",x[i],x[j],")")
#             break
#     if i == len(x)-1:
#         print(False)    

# x = [7,1,5,3,6,4]
# v = 0
# for i in range(0, len(x)):
#     for j in range(i+1, len(x)):
#         if x[j] - x[i] > v:
#             v = x[j] - x[i]
# #
# #
# #
# print(v)

# def maxProfit(prices):
#     l, r = 0, 1
#     maxP = 0
#
#     while r < len(prices):
#         if prices[l] < prices[r]:
#             profit = prices[r] - prices[l]
#             maxP = max(maxP, profit)
#         else:
#             l = r
#         r += 1
#     return maxP
#
#
# prices = [7,1,5,3,6,4]
# print(maxProfit(prices))


# def isPalindrome(s):
#     n = ''.join(e for e in s if e.isalnum()).lower()
#     v = ""
#     for i in n:
#         v = i + v
#     if n == v:
#         return True
#     return False
#
#
# string = "A man, a plan, a canal: Panama"
# print(isPalindrome(string))
from random import randint


class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None
        self.head = None

    def __iter__(self):
        currentNode = self.head
        while currentNode:
            yield currentNode
            currentNode = currentNode.next

    def __str__(self):
        values = [str(x.value) for x in self]
        return ' -> '.join(values)

    def __len__(self):
        node = self.head
        result = 0
        while node:
            result += 1
            node = node.next
        return result

    def add(self, value):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = self.tail.next

    def generate(self, n, min_value, max_value):
        self.head = None
        self.tail = None
        for i in range(n):
            self.add(randint(min_value, max_value))
        return self


def intersection(llA, llB):
    if llA.tail is not llB.tail:
        return False

    lenA = len(llA)
    lenB = len(llB)

    shorter = llA if lenA < lenB else llB
    longer = llB if lenA < lenB else llA

    diff = len(longer) - len(shorter)
    longerNode = longer.head
    shorterNode = shorter.head

    for i in range(diff):
        longerNode = longerNode.next

    while shorterNode is not longerNode:
        shorterNode = shorterNode.next
        longerNode = longerNode.next

    return shorterNode


# add the same node to linked list
def sameNode(llA, llB, value):
    tempNode = Node(value)
    llA.tail.next = tempNode
    llA.tail = tempNode
    llB.tail.next = tempNode
    llB.tail = tempNode


llA = LinkedList()
llA.generate(4, 0, 10)

llB = LinkedList()
llB.generate(3, 0, 10)

sameNode(llA, llB, 11)
sameNode(llA, llB, 32)

print(intersection(llA, llB))

print(llA)
print(llB)
