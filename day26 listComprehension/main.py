# list comprehension (remember: [<new item> for <item> in <list>]
# we can work with strings also
# eg: name = "alan"
# list = [letter for letter in name] output: list = ['a','l','a','n']
#  we can use this with list, range, string, tuple
# conditional list comprehention remember: [<new item> for <item> in <list> if <test>]
import random

# Dictionary comprehension


# new_dict = {<new_key:new_value> for <item> in <list>}
# another syntax -# new_Dict = {<new_key:new value> for (key,value) in dict.items() if <test>}
# eg:
# names = ["alan", "saji", "malan", "sheeja", "atul", "siya"]
#
# random_score = {name: random.randint(1, 100) for name in names}
# print(random_score)
#
# passed_students = {name:mark for (name,mark ) in random_score.items() if mark > 60}
# print(passed_students)
#
#
#working with pandas dataframes
#{new_key: new_value for (index,row) in df.iterrows()}
# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
#TODO 1. Create a dictionary in this format:
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

word = input("Enter a word: ").upper()
output_list = [phonetic_dict[letter] for letter in word]
print(output_list)
