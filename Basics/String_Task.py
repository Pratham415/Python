# 1. Count the number of occurrences of a specific character in a string.

#    Input: sentence = "Hello, how are you?", character = 'o'

#    Output: Count of 'o' in sentence: 3
str = input("Enter the string : ")
print(str.count('o'))

# ---------------------------------------------------------
# 2. Check if a string starts with a given substring.

#    Input: text = "Python programming"

#    Output: 
   
#    Does the string start with 'Python'? True
#    Does the string start with 'java'? False
# text = input("Enter the starting char : ")
# print(f"Does string start with the {text} ?{str.startswith(text)}")
   
#---------------------------------------------------------------
# 3. Find the index of the first occurrence of a substring within a string.

#    Input: text = "Hello, how are you?", substring = "how"

#    Output: Index of 'how' in text: 7
# substr = input("Enter the substring : ")
# print(f"Index of '{substr}' text is : {str.index(substr)}")

#---------------------------------------------------------------
# 4. Replace all occurrences of a substring with another substring in a string.

#    Input: text = "I like ice cream and ice cream likes me.", old = "ice cream", new = "gelato"

#    Output: "I like gelato and gelato likes me."


# 5. Convert all characters in a string to uppercase.

#    Input: text = "Hello, World!"

#    Output: "HELLO, WORLD!"

# 6. Convert all characters in a string to lowercase.

#    Input: text = "Hello, World!"

#    Output: "hello, world!"

# 7. Capitalize the first character of each word in a string.

#    Input: text = "hello world"

#    Output: "Hello World"

# 8. Check if a string consists only of alphanumeric characters.

#    Input: text = "Hello123"

#    Output: Is 'Hello123' alphanumeric? True

# 9. Remove leading and trailing whitespace characters from a string.

#    Input: text = "   Hello, World!   "

#    Output: "Hello, World!"

# 10. Split a string into substrings based on a delimiter.

#     Input: text = "apple,banana,orange"

#     Output: ['apple', 'banana', 'orange']

# 11. Join a list of strings into a single string with a delimiter.

#     Input: words = ['apple', 'banana', 'orange'], delimiter = ', '

#     Output: "apple, banana, orange"

# 12. Swap the cases of all characters in a string.

#     Input: text = "Hello, World!"

#     Output: "hELLO, wORLD!"

# 13. Check if a string ends with a specified suffix.

#     Input: text = "Hello, World!", suffix = "World!"

#     Output: Does 'Hello, World!' end with 'World!'? True

# 14. Reverse a string.

#     Input: text = "Hello, World!"

#     Output: "!dlroW ,olleH"

# 15. Strip characters from the left side of a string.

#     Input: text = "   Hello, World!   "

#     Output: "Hello, World!   "

# 16. Strip characters from the right side of a string.

#     Input: text = "   Hello, World!   "

#     Output: "   Hello, World!"

# 17. Check if a string contains only numeric characters.

#     Input: text = "12345"

#     Output: Is '12345' numeric? True

# 18. Find the position of the last occurrence of a substring in a string.

#     Input: text = "Hello, World, World!", substring = "World"

#     Output: Last occurrence of 'World' starts at index: 13

# 19. Extract digits from a string.

#     Input: text = "Hello 123 World 456!"

#     Output: "123456"

# 20. Count the number of words in a string.

#     Input: text = "Hello, how are you?"

#     Output: Number of words in text: 4

# More Added:

# 1. Problem Statement 1:
#    Given a sentence, return a new string where the first letter of each word is capitalized and the rest of the letters are in lowercase.
#    - Sample Input: "hello WORLD"
#    - Sample Output: "Hello World"
# print(str.title())

# 2. Problem Statement 2:
#    Given a paragraph of text, count the number of times the word "data" appears, regardless of its case.
#    - Sample Input: "Data is the new oil. Many companies analyze data to gain insights. DATA science is a growing field."
#    - Sample Output: 3
# print(str.casefold().count("data"))

# 3. Problem Statement 3:
#    Given a string containing a mixture of letters, numbers, and special characters, encode the string using UTF-8 encoding and return the encoded result.
#    - Sample Input: "Café ☕"
#    - Sample Output: b'Caf\xc3\xa9 \xe2\x98\x95'
# print(str.encode(encoding="ASCII",errors="backslashreplace"))

# 4. Problem Statement 4:
#    Write a function that checks if a given string starts with the substring "Hello" and ends with the substring "World".
#    - Sample Input: "Hello, beautiful World"
#    - Sample Output: True
#    - Sample Input: "Hi there, World"
#    - Sample Output: False


# 5. Problem Statement 5:
#    Given a list of words separated by commas in a string, return a new string where each word is surrounded by square brackets.
#    - Sample Input: "apple,banana,cherry"
#    - Sample Output: "[apple],[banana],[cherry]"

# 6. Problem Statement 6:
#    Write a function that takes a file path as a string and extracts the file extension (e.g., "document.pdf" should return "pdf").
#    - Sample Input: "report.final.docx"
#    - Sample Output: "docx"

# 7. Problem Statement 7:
#    Given a sentence, return the index of the first occurrence of the word "Python". If the word is not found, return -1.
#    - Sample Input: "I am learning Python programming."
#    - Sample Output: 14
#    - Sample Input: "I love coding."
#    - Sample Output: -1

# 8. Problem Statement 8:
#    Write a function that takes a string and a character, and returns the string with all occurrences of the character replaced by an asterisk (*).
#    - Sample Input: "hello world", "o"
#    - Sample Output: "hell* w*rld"

# 9. Problem Statement 9:
#    Given a string with tab-separated values, convert it to a string with comma-separated values.
#    - Sample Input: "name\tage\tcity"
#    - Sample Output: "name,age,city"

# 10. Problem Statement 10:
#     Write a function that takes a multiline string and returns a list of strings, where each string is a single line from the original multiline string.
#     - Sample Input:
#       ```
#       Hello world
#       This is a test
#       Python is fun
#       ```
#     - Sample Output: ["Hello world", "This is a test", "Python is fun"]