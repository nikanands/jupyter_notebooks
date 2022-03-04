# 1. Function for finding Capital Letters (capital_indexs)


from random import randint


def capital_indexes(string):
    capital_letter = []
    letters = []
    for letter in enumerate(string):
        letters.append(letter)

    for let in letters:
        if let[1].isupper():
            capital_letter.append(let[0])

    return capital_letter
# SHORTER VERSION
# from string import uppercase
# def capital_indexes(s):
#     return [i for i in range(len(s)) if s[i] in uppercase]

# 2. Function for finding Middle Letter (mid)


def mid(string):
    if len(string) % 2:
        return string[(len(string) // 2)]
    return ""

# 3. Funtion for finding Online Status from given Dictionary (online_count)


def online_count(dictio):
    count = 0
    for val in dictio.values():
        if val == "online":
            count += 1
    return count
# SHORTER VERSION
# def online_count(people):
#     return len([p for p in people if people[p] == "online"])


# 4. Function for finding random number from 1 to 100 inclusive (random_number)


def random_number():
    return randint(1, 100)

# 5. Function for checking type of given parameter (only_ints)


def only_ints(a, b):
    if type(a) == int and type(b) == int:
        return True
    return False
# SHORTER VERSION
# def only_ints(a, b):
#     return type(a) == int and type(b) == int

# 6. Function for Double Letters Challenge (double_letters)


def double_letters(string):
    letters = []
    for char in string:
        letters.append(char)
    for i in range(len(letters)):
        if string[i] == string[i-1]:
            return True
    return False
# SHORTER VERSION
# def double_letters(string):
#     return any([a == b for a, b in zip(string, string[1:])])

# 7. Function for adding and removing dots from given string (add and remove dots)


def add_dots(string):
    return(".".join(string))


def remove_dots(string):
    return(string.replace(".", ""))


# 8. Function for counting syllables (count)
def count(string):
    return len(string.split("-"))
# DIFFERENT VERSION
# def count(word):
#     return word.count("-") + 1

# 9. Function for finding given strings are Anagrams (is_anagram)


def is_anagram(a, b):
    if len(a) != len(b):
        return False
    elif sorted(a) == sorted(b):
        return True
    return False

# 10. Flatten a multidimensional list (flatten)


def flatten(li):
    return sum(li, [])

# LIST COMPREHENSION METHOD
# def flatten(outer_list):
#     return [
#         item
#         for inner_list in outer_list
#         for item in inner_list
#     ]

# NORMAL METHOD
# def flatten(outer_list):
#     result = []
#     for inner_list in outer_list:
#         for item in inner_list:
#             result.append(item)
#     return result

# 11. Finding difference between Min and Max in a list (largest_difference)


def largest_difference(li):
    return max(li)-min(li)


# 12. Function to find Divisible by 3 (div_3)
def div_3(value):
    return value % 3 == 0


# 13. Function to find row and column from a TiC Tac Toe game (get_row_col)
def get_row_col(string):
    row = ["A", "B", "C"]
    column = ["1", "2", "3"]
    row_col = []
    row_col.append(column.index(string[1]))
    row_col.append(row.index(string[0]))
    return tuple(row_col)

# OTHER SOLUTION
# def get_row_col(choice):
#     translate = {"A": 0, "B": 1, "C": 2}
#     letter = choice[0]
#     number = choice[1]
#     row = int(number) - 1
#     column = translate[letter]
#     return (row, column)


# 14. Function for Palindrome
def palindrome(string):
    return string == string[::-1]


# 15. Function for getting one less and one plus number of given num (up_down)
def up_down(num):
    return (num-1, num+1)


# 16. Function for finding consecutive zeros in given string (consecutive_zeros)
def consecutive_zeros(string):
    return len(max(string.split("1")))


# 17. Function for finding all element of list are equal (al_equal)
def all_equal(li):
    result = all(el == li[0] for el in li)
    if result:
        return True
    return False

# ANOTHER METHOD
# def all_equal(items):
#     for item1 in items:
#         for item2 in items:
#             if item1 != item2:
#                 return False
#     return True


# 18. Function for finding all parameters are True/False (triple_and)
def triple_and(a, b, c):
    if a == True and b == True and c == True:
        return True
    return False

# def triple_and(a, b, c):
#     return a and b and c


# 19. Function for converting list of int into list of string in shortest way (convert)
def convert(li):
    return [str(el) for el in li]


# 20. Custom ZIP function (zap)
def zap(a, b):
    li = []
    for i in range(len(a)):
        li.append((a[i], b[i]))
    return li

# def zap(a, b):
#     return [(a[i], b[i]) for i in range(len(a))]


# 22. Function for finding a param is in other list given as params (list_xor)
def list_xor(a, b, c):
    if a in b and a in c:
        return False
    elif a not in b and a not in c:
        return False
    return True

# def list_xor(n, list1, list2):
#     return (n in list1) ^ (n in list2)


# 23. Function to validate somethings (validate)

# ******************INCOMPLETE*******************
# def validate(args):
#     print(len(args))
#     if "def" not in args:
#         return "missing def"
#     elif ":" not in args:
#         return "missing :"
#     elif "(" not in args and ")" not in args:
#         return "missing paren"
#     elif len(args) == 0:
#         return "missing param"
#     elif "validate" not in args:
#         return "wrong name"
#     elif "return" not in args:
#         return "missing return"


# 23. Finding counting of parameter given to a function (param_count)
def param_count(*args):
    return len(args)


# 24. Function for thousand seprator (format_number)
def format_number(num):
    return (f"{num:,}")


def average(num):
    count = 0
    sum = 0
    li = [1, 2, 3, 5, 6, 7, 8]
    # for i in num:
    #     if
    # print(sum(li))

    # while(count<=10):
    #     count+=1
    #     sum+
    numbers = [1, 2, 3, 4, 5, 1, 4, 5]

# start parameter is not provided
    Sum = sum(numbers)
    return Sum


print(average([1, 2, 3, 5, 6, 7, 8]))


# Web Scraping Script
'''
# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
import time, os

def get_comp_info(symbol):
    url = "https://finance.yahoo.com/quote/"+symbol+"?p="+symbol
    
     
    res = requests.get(url)
     
    res_text = res.text
    
    soup = BeautifulSoup(res_text, features="html.parser")
    
    trs = soup.find_all("tr")
    names=[]
    values=[]
    name_val_dict={}
    
    for i in range(len(trs)):
        for j in range(len(trs[i].contents)):
            if j == 0:
                name = trs[i].contents[j].text
                names.append(name)
            else:
                value = trs[i].contents[j].text
                values.append(value)
                
        name_val_dict[name]= value
        if name == "1y Target Est":
            break
    return names, values
   

def get_comp_list():

    url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
    
    res = requests.get(url)
    res_text = res.text
    soup = BeautifulSoup(res_text, features= "html.parser")
    
    tbody = soup.find_all("tbody")
    symbols= []
    
    
    for i in range(len(tbody[0].contents)):
        if i<2:
            continue
        if i % 2 != 0:
            continue
        #Change 10 to multiple of 2 till 1010 for full result
        if i == 10:
            
            break
        
        symbols.append(tbody[0].contents[i].contents[1].text.strip("\n"))
        

        
    return symbols



for i in range(1):
    print(i)
    start_time = time.time() 
    wait_time = 150
    data = {
            "symbol": [],
            "metric": [],
            "value": []
            }
    
    symbols = get_comp_list()
 
    
    for symbol in symbols:
        names, values = get_comp_info(symbol)
        for j in range(len(names)):
            data["symbol"].append(symbol)
            data["metric"].append(names[j])
            data["value"].append(values[j])
            
        
                   
            
            
    df = pd.DataFrame(data)
    saved_path = "financialData.csv"
    if os.path.isfile(saved_path):
        df.to_csv(saved_path, mode="a", header=False, columns=["symbol", "metric", "value"])
    else:
        df.to_csv(saved_path, columns=["symbol", "metric", "value"])
    
    time_diff = time.time() - start_time
    if wait_time-time_diff > 0:
        time.sleep(15-time_diff)
'''
