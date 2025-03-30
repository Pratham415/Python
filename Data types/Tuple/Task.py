# > #### Ordering tuple by list
# Input:
# ```python
# tupList = [('l', 5), ('k', 2), ('a', 1), ('e', 6)]
# sortList = ['l', 'a', 'k', 'e']
# ```
# Output:
# ```python
# [('l', 5), ('a', 1), ('k', 2), ('e', 6)]
# ```
# for i in tupList:
#     for j in sortList:
#         print(list(i))

# 1)
# count = 0
# list =  ['abc', 'xyz', 'aba', '1221']
# for i in list:
#     if i[0] == i[-1]:
#         count+=1

# list(set([10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40])) 
## 4. Find Words Longer Than n
# - ### Write a Python program to find the list of words that are longer than n from a given list of words.
# ```python
#     Sample Input:
#         input_str = "The quick brown fox jumps over the lazy dog"
#         n = 3
#     Expected Result: ['quick', 'brown', 'jumps', 'over', 'lazy']
#  
# ```
list = list()
input_str = "The quick brown fox jumps over the lazy dog"
imp = int(input("Enter the number : ")) 
# for i in input_str.split():
#     if len(i) > imp:
#         list.append(i)
# print(list)
list = [i for i in input_str.split() if len(i) > imp]
print(list)
    