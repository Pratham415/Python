veggies = [
        "Bitter Gourd (Karela)",
        "Bottle Gourd (Lauki)",
        "Ridge Gourd (Turai)",
        "Snake Gourd (Galka)",
        "Pointed Gourd (Parwal)",
        "Drumstick (Moringa)",
        "Taro Root (Arbi)",
        "Elephant Foot Yam (Suran)",
        "Ash Gourd (Petha)",
        "Ivy Gourd (Tindora)",
        "Fenugreek Leaves (Methi)",
        "Amaranth Leaves (Patra)",
        "Colocasia Leaves (Arbi ke Patte)",
        "Beet Greens (Chukandar ke Patte)",
        "Mustard Greens (Sarson)",
        "Radish Greens (Mooli ke Patte)",
        "Spinach (Palak)",
        "Fenugreek Seeds Sprouts (Methi Dana)",
        "Cluster Beans (Gawar Phali)",
        "French Beans",
        "Yardlong Beans (Bora)",
        "Broad Beans (Sem)",
        "Green Peas (Matar)",
        "Corn (Makai)",
        "Bamboo Shoots (Karil)",
        "Jackfruit (Kathal)",
        "Raw Banana (Kachcha Kela)",
        "Green Papaya (Kachcha Papita)",
        "Indian Gooseberry (Amla)",
        "Curry Leaves (Kadi Patta)",
        "Raw Mango (Keri)",
        "Sponge Gourd (Nenua)",
        "Brinjal (Baingan)",
        "Lady Finger (Bhindi)",
        "Cabbage (Patta Gobi)",
        "Cauliflower (Phool Gobi)",
        "Radish (Mooli)",
        "Turnip (Shalgam)",
        "Carrot (Gajar)",
        "Tomato (Tamatar)"
    ]
# 1. Sort by Hindi Names
#  Sort the veggies list based on the Hindi names while keeping the original structure intact.
# for i in veggies:
#     print(i[i.find('('):i.find(')') + 1])

# 2. Extract Only Hindi Names
#  Create a new list that contains only the Hindi names of the vegetables.
# lis = []
# for i in veggies:
#     word = i[i.find('('):i.find(')') + 1]
#     lis.append(word)    
# print(lis)

# 3. Extract Only English Names
#  Create a new list that contains only the English names of the vegetables.
# eng_word = []
# for i in veggies:
#     word = i[0:i.find(" (")]
#     eng_word.append(word)
# print(eng_word)

# 4. Find the Longest and Shortest Vegetable Names
#  Identify and print the longest and shortest vegetable names (English and Hindi separately).
# English :
# max = 0
# name = ""
# for i in eng_word:
#     if len(i) > max:
#         max = len(i)
#         name = i
# print(name)

# min = 100
# name = ""
# for i in eng_word:
#     if len(i) < min:
#         min = len(i)
#         name = i
# print(name)

#  5. Reverse Each Vegetable Name
#  Print a new list where each vegetable name (both English and Hindi) is reversed
# lst = []
# for i in veggies:
#     word = i[::-1]
#     lst.append(word)
# print(lst)

# 6. Find Vegetables Containing a Given Letter
#  Write a function that takes a letter as input and returns all vegetable names (English and Hindi) containing
#  that letter


