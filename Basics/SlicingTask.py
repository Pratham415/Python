# Paragraph:
a = "Indian cuisine offers a rich and diverse array of vegetarian dishes, reflecting the country's cultural and regional variations. Staples like lentils, rice, and a variety of fresh vegetables form the foundation of many meals. Dishes such as dal (lentil stew), sabzi (vegetable curry), and roti (unleavened bread) are commonplace. Spices play a crucial role, with ingredients like turmeric, cumin, coriander, and garam masala imparting unique flavors. South Indian cuisine features dishes like dosa (fermented crepe), idli (steamed rice cakes), and sambar (spicy lentil soup). North Indian cuisine is famous for dishes like paneer tikka (grilled cheese), chole (chickpea curry), and aloo gobi (potato and cauliflower curry). Street foods such as samosas, bhel puri, and pav bhaji are popular across the country. Many Indian sweets, including gulab jamun, jalebi, and barfi, are also vegetarian. Each region offers its own specialties, ensuring a vast and exciting culinary landscape for vegetarians to explore."

# > Maggie Tasks:
# Extract the first sentence of the paragraph.
# print(a[0:a.find(". ")+1])
# print(len(a))
# Extract the last sentence of the paragraph.
# sent = a.rsplit(". ")
# print(sent[-1])
# Extract the word "lentils" from the paragraph.
# print(a[len(a)-1:-3])
# Extract the first five words of the paragraph.
# word = a.split()
# print(" ".join(word[:5]))
# Extract the last five words of the paragraph.
# word = a.rsplit()
# print(" ".join(word[-5:]))
# Extract the phrase "South Indian cuisine features dishes like dosa".
# print(a[450:496])
# Extract all the words between "coriander" and "idli".
# print(a[405:516])
# print(a.find("idli"))
# Extract the name of three North Indian dishes.
# print(a[492:a.find(".")])
# Extract the names of all South Indian dishes mentioned.

# Extract the name of the first street food mentioned.
# Extract the phrase "unique flavors" from the paragraph.
# Extract the names of all spices mentioned in the paragraph.
# Extract the phrase "Indian sweets, including gulab jamun, jalebi, and barfi".
# Extract the phrase "North Indian cuisine is famous for dishes".
# Extract the phrase "foundation of many meals".
# Extract the first mention of the word "curry".
# Extract the phrase "reflecting the country's cultural and regional variations".
# Extract the phrase "North Indian cuisine is famous for dishes like paneer tikka".
# Extract the phrase "spices play a crucial role".
# Extract the phrase "Each region offers its own specialties".

# > 56-Bhog Tasks:
# Extract the first sentence without using the split method.
# print(a[0:a.find(". ")+1])
# Extract the last sentence without using the split method.
# Extract the phrase "rich and diverse" from the first sentence.
# Extract the phrase "lentil stew" without using the find method.
# Extract the word "lentils" in reverse order.
# str = a[a.find("lentils"):a.find("lentils")+7]
# print(str[::-1])
# Extract every second word in the paragraph.
# wordCount = 0
# for i in a.split():
#     wordCount+=1
#     if wordCount%2 == 0:
#         print(i, end=', ')
# Extract the first word of each sentence in the paragraph.
# for i in a.split():
#     if i.istitle():
#         print("".join(i) , end=", ")
# Extract the last word of each sentence in the paragraph.
# for i in a.split():
#     if i.endswith("."):
#         print("".join(i) , end = ", ")
# Extract the paragraph in reverse order.
# print(a[::-1])
# Extract every third character from the paragraph.
# count = 0
# for i in a.split():
#     count = count + 1
#     if count%3 == 0:
#         print("".join(i),end=" , ")
# Extract the first and last word of the paragraph.
# b = a.split()
# print(b[0])
# print(b[-1]) 
# Extract all words containing the letter 'e'.
# for i in a.split():
#     if i.__contains__('e'):
#         print("".join(i),end=" , ")
# Extract the paragraph without the first and last word.
# i = 1
# for i in a.split():
# Extract all occurrences of the word "Indian" and reverse them.
##
# Extract the phrase "dal (lentil stew), sabzi (vegetable curry), and roti" without using the split or find method.
# Extract the names of dishes that contain the letter 'a'.
# Extract the first and last sentence, and join them into a new string.
# first = a[0:a.find(". ")]
# last = a.rsplit(". ")
# print("".join(first),end=" ")
# print("".join(last[-1]) , end="")
# Extract the words "fresh vegetables form" and reverse the order of these words.
# Extract every word that starts with a consonant.
# for i in a.split():
#     if not(i.startswith('A' or 'a') and i.startswith('E' or 'e') and i.startswith('I' or 'i')) and i.startswith('O' or 'o') and i.startswith('U' or 'u'):
#         print(i) 
# Extract all the capital letters in the paragraph.
for i in a:
    if i.isupper():
        print("".join(i),end=", ")