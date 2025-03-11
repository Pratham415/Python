#1)Extract all odd numbers from a nested list and square them
# nested_numbers = [[10, 15, 21], [33, 40, 45], [50, 60, 75]]
# odd = [j**2 for i in nested_numbers for j in i if j%2 != 0]
# print(odd) 

#2)Flatten a matrix and keep only the prime numbers.
# matrix = [[4, 3, 8], [5, 6, 7], [9, 11, 13]]
# flatten = [j for i in matrix for j in i]
# print(flatten)

# 3)Find all words that are palindromes inside a nested word list.
# words_list = [["madam", "level", "python"], ["racecar", "wow", "data"]] 
# test = [j for i in words_list for j in i if j[::-1] == j]
# print(test)

#4)Filter out words with less than 4 letters and return a flattened list.
# words_list = [["madam", "level", "python"], ["racecar", "wow", "data"]]
# filter = [j for i in words_list for j in i if len(j) <= 4]
# print(filter)

#5)Generate a new list containing the sum of corresponding elements in two nested lists.

#6)Extract unique vowels from all words in a nested list.
# words_list = [["madam", "level", "python"], ["racecar", "wow", "data"]]
# vowel = [char for i in words_list for j in i for char in j if char in ['a','e','i','o','u']]
# print(vowel)

#7)Find all numbers in a nested list that are divisible by both 3 and 5.
# numbers_list = [[10, 20, 30], [1, 2, 3], [5, 15, 25]] 
# num = [j for i in numbers_list for j in i if j % 5 == 0 and j % 3 == 0]
# print(num)

#8)Convert a nested list of words into their lengths but only for words longer than 3 letters.
# words_list = [["madam", "level", "python"], ["racecar", "wow", "data"]]
# word = [len(j) for i in words_list for j in i if len(j) > 3]
# print(word)

# 9)Create a list of coordinate pairs from a 3x3 grid representation.
grid = [[(x, y) for y in range(3)] for x in range(3)]
print(grid)

#10 Reverse each word in a nested list, but only if it starts with a vowel.
# sentence_list = [["Python", "is", "fun"], ["AI", "rocks", "comprehension"]]
# rev = [j for i in sentence_list for j in i if j[0] in ['a','i','e','o','u','A','I','O','U','E']]
# print(rev)