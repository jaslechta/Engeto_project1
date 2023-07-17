"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Jan Šlechta
email: janslechta31@gmail.com
discord: honzas0100
"""
import task_template

separator_line = 40*"-"
print(separator_line)

users = {"bob" : "123", "ann" : "pass123", "mike" : "password123", "liz" : "pass123"}
username = input("Enter your username: ")
password = input("Enter your password: ")

print(separator_line)
if not username in users:
    print("unregistered user, terminating the program..")
    quit()
elif users.get(username) == password:
    print("Welcome to the app,", username)
else:
    pocet_pokusu = 3
    print("Wrong password, ", pocet_pokusu, "attepmts left")
    while pocet_pokusu > 0:
        if users.get(username) == input("Try to enter your password again: "):
         print("Welcome to the app, ", username)
         break
        else:
            pocet_pokusu -= 1
            print("Wrong password, ", pocet_pokusu ," attempts left")          
    else:
        print("Too many wrong attemps, terminating the program..")
        quit()


print(f"We have 3 texts to be analyzed. ")
print(separator_line)
for number, text in enumerate(task_template.TEXTS):
    print(number+1,". text: ",text, "\n")

print(separator_line)

chosen_number = int(input("Enter a number btw. 1 and 3 to select: "))  
chosen_number_modified = chosen_number - 1 
if 1 < chosen_number > 3:
    print("Wrong number or character, terminanting the program..")
    quit()

print(separator_line)

test_string = task_template.TEXTS[chosen_number_modified]
uncleared_words = test_string.split()
words = []
for word in uncleared_words:
     words.append(word.strip(".,:;"))

words_counter = len(words)
print("There are ", words_counter, " words in the selected text")

count_words_with_capital_letter = 0
for word in words:
    if word[0].isupper():
        count_words_with_capital_letter += 1
print("There are ", count_words_with_capital_letter, " titlecase words. ")

count_words_whole_uppercase = 0
for word in words:
        if word.isupper() and word[0].isalpha():
            count_words_whole_uppercase += 1
print("There are ",count_words_whole_uppercase," uppercase words. ", )    

count_words_whole_lowercase = 0
for word in words:
        if word.islower():
            count_words_whole_lowercase += 1
print("There are ",count_words_whole_lowercase," lowercase words.")  

count_digits= 0
for word in words:
        if word.isdigit():
            count_digits += 1
print("There are ",count_digits," numeric strings.")  

sum_digits = 0
for word in words:
        if word.isdigit():
            try:
                sum_digits = int(sum_digits) + int(word)
            except ValueError:
                pass
print("The sum of all the numbers ",sum_digits)  

occurences_table = {}
for word in words:
     lenght_word = len(word)
     if lenght_word not in occurences_table:
          occurences_table[lenght_word] = 1
     else:
          occurences_table[lenght_word] = occurences_table[lenght_word] + 1
sorted_occurences_table = dict(sorted(occurences_table.items()))

print(separator_line)
print(f"{'LEN':<3}|{'OCCURENCES':<18}|{'NR.':<2}")
print(separator_line)
for occurence in sorted_occurences_table:
    count = sorted_occurences_table[occurence]
    graph = "*" * count
    print(f"{occurence:<3}|{graph:<18}|{count:<2}")