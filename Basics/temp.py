# 7)
# lst = [1,2,3,4,5,6,7,8,9]
# start = int(input("Enter the start number: "))
# end = int(input("Enter the end number: "))
# count = 0
# for i in lst:
#     if i > start and i < end:
#             count += 1
# print(count)
## 8. Create List with Range Concatenation
# - ### Write a Python program to create a list by concatenating a given list with a range from 1 to n.
# ```python
# Sample Input:
#     l1 = ['p', 'q']
#     n = 5
# Sample Output:
#     ['p1', 'q1', 'p2', 'q2', 'p3', 'q3', 'p4', 'q4', 'p5', 'q5']
# ```
# lst = ['p','q']
# l = list()
# n = int(input('Enter a number: '))
# for i in range (n):
#     for j in lst:
#         l.append(j + str(i))
# print(l)

# 9)
# lst = [0,1,2,3,4,5,6,7,8,9]
# for i in range(0,len(lst),2):
#     lst[i] , lst[i+1] = lst[i+1], lst[i]
# print(lst)
# 10
## 10. Remove Consecutive Duplicates
# - ### Write a Python program to remove consecutive (following each other continuously) duplicates (elements) from a given list.
# ```python
# Original list:
#     [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
# After removing consecutive duplicates:
#     [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 4]
# ```
l = list()
lst = [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
# for i in range(0, len(lst) - 1):
#     if lst[i] != lst[i+1]:
#         l.append(lst[i])
# print(l)

## 11. Pack Consecutive Duplicates into Sublists
# - ### Write a Python program to pack consecutive duplicates of a given list of elements into sublists.
# ```python
# Original List:
#     [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
# After packing consecutive duplicates of the said List elements into sublists:
#     [[0, 0], [1], [2], [3], [4, 4], [5], [6, 6, 6], [7], [8], [9], [4, 4]]
# ```
l1 = list([])
for i in lst:
    for j in range(i):
        if lst[i] == lst[j]:
            l1.append(lst[i])
        else:
            l1.append(lst[j])
            print(l1)


