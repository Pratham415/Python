# Problem 1: Find the Unique Elements in Multiple Lists
# Problem Statement:
# You are given a list of lists, where each list contains numbers. Find all the unique elements across all the lists
# using sets.
# Sample Input:
# list_of_lists = [[1, 2, 3], [3, 4, 5], [5, 6, 7]]
# Sample Output:
# {1, 2, 3, 4, 5, 6, 7}
# lst = [[1, 2, 3], [3, 4, 5], [5, 6, 7]]
# s = set([j for i in lst for j in i])
# print(s)

# Problem 2: Find the Common Elements Between Two Lists
# Problem Statement:
# Given two lists, use a set to find the common elements between them and print the result.
# Sample Input:
# list1 = [1, 2, 3, 4, 5]
# list2 = [3, 4, 5, 6, 7]
# Sample Output:
# {3, 4, 5}
# s = list()
# for i in list1:
#     for j in list2:
#         if i == j:
#           s.append(i)
# print(set(s))

# Problem 3: Remove Duplicates from a List
# Problem Statement:
# Given a list with duplicates, remove the duplicates using sets and print the resulting list.
# Sample Input:
list = [1, 2, 2, 3, 3, 4, 5, 5]
# Sample Output:
# [1, 2, 3, 4, 5]

