## 5. Find List with Max and Min Lengths
# - ### Write a Python program to find a list with maximum and minimum lengths.
# ```python
# Original list:
#     [[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
# List with maximum length of lists:
#     (3, [13, 15, 17])
# List with minimum length of lists:
#     (1, [0])
# Original list:
#     [[0], [1, 3], [5, 7], [9, 11], [3, 5, 7]]
# List with maximum length of lists:
#     (3, [3, 5, 7])
# List with minimum length of lists:
#     (1, [0])
# Original list:
#     [[12], [1, 3], [1, 34, 5, 7], [9, 11], [3, 5, 7]]
# List with maximum length of lists:
#     (4, [1, 34, 5, 7])
# List with minimum length of lists:
#     (1, [12])
# ```
lst = [[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
cout = 0
# a = [j for i in lst for j in i ]
for i in lst:
    if i.count(lst) < cout:
        cout = i.count() 
print(cout) 

## 6. Check if Nested List Is Subset
# - ### Write a Python program to check if a nested list is a subset of another nested list.
# ```python
# Original list:
#     [[1, 3], [5, 7], [9, 11], [13, 15, 17]]
#     [[1, 3], [13, 15, 17]]
# If the one of the said list is a subset of another.: True
# Original list:
#     [[[1, 2], [2, 3]], [[3, 4], [5, 6]]]
#     [[[3, 4], [5, 6]]]
# If the one of the said list is a subset of another.: True
# Original list:
#     [[[1, 2], [2, 3]], [[3, 4], [5, 7]]]
#     [[[3, 4], [5, 6]]]
# If the one of the said list is a subset of another.: False
# `
# ``
st = [[1, 3], [5, 7], [9, 11], [13, 15, 17]]
st1 = [[1, 3], [13, 15, 17]]          
for i in st1:
    sub = i in st
print(sub)
