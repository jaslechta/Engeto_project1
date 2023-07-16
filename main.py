"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Jan Šlechta
email: janslechta31@gmail.com
discord: honzas0100
"""
import task_template

users = {"bob" : "123", "ann" : "pass123", "mike" : "password123", "liz" : "pass123"}
username = input("zadej prosim svoje prihlasovaci jmeno: ")
password = input("zadej svoje heslo: ")


if not username in users:
    print("unregistered user, terminating the program..")
    quit()
elif users.get(username) == password:
    print("Vitej v analyzatoru, ", username)
else:
    pocet_pokusu = 3
    print("spatne heslo, zbyvaji ", pocet_pokusu, "pokusy")
    while pocet_pokusu > 0:
        if users.get(username) == input("zkus zadat heslo znova: "):
         print("Vitej v analyzatoru, ", username)
         break
        else:
            pocet_pokusu -= 1
            print("znova spatne heslo, zbyvaji", pocet_pokusu ,"pokusy")          
    else:
        print("bohuzel jsi vycerpal pocet pokusu, program se ukonci")
        quit()


#print(f"Mame na vyber ze tri textu: ", task_template.TEXTS[0], task_template.TEXTS[1],task_template.TEXTS[2], sep = "\n\n")
print(f"Mame na vyber ze tri textu: ")
for number, text in enumerate(task_template.TEXTS):
    print(number+1,". text: ",text, "\n")

chosen_number = int(input("zadej cislo textu, ktery chces dale zpracovavat z rozsahu 1-3: "))  
chosen_number_modified = chosen_number - 1 
if 1 < chosen_number > 3:
    print("zadane cislo textu je mimo rozsah, nebo to neni platna ciselna hodnota, program se nyni ukonci")
    quit()

test_string = task_template.TEXTS[chosen_number_modified]
uncleared_words = test_string.split()
words = []
for word in uncleared_words:
     words.append(word.strip(".,:;"))

words_counter = len(words)
print("pocet slov vybraneho textu je: ", words_counter)

count_words_with_capital_letter = 0
for word in words:
    if word[0].isupper():
        count_words_with_capital_letter += 1
print("Pocet slov s velkym pismenem je: ", count_words_with_capital_letter)

count_words_whole_uppercase = 0
for word in words:
        if word.isupper() and word[0].isalpha():
            count_words_whole_uppercase += 1
print("Pocet slov napsanych velkym pismenem je: ", count_words_whole_uppercase)    

count_words_whole_lowercase = 0
for word in words:
        if word.islower():
            count_words_whole_lowercase += 1
print("Pocet slov napsanych velkym pismenem je: ", count_words_whole_lowercase)  

count_digits= 0
for word in words:
        if word.isdigit():
            count_digits += 1
print("Pocet cisel: ", count_digits)  

sum_digits = 0
for word in words:
        if word.isdigit():
            try:
                sum_digits = int(sum_digits) + int(word)
            except ValueError:
                pass
print("Pocet cisel: ", sum_digits)  

occurences_table = {}
for word in words:
     lenght_word = len(word)
     if lenght_word not in occurences_table:
          occurences_table[lenght_word] = 1
     else:
          occurences_table[lenght_word] = occurences_table[lenght_word] + 1
sorted_occurences_table = dict(sorted(occurences_table.items()))
print(sorted_occurences_table)

graph_occurences = []
for occurence in sorted_occurences_table:
    count = sorted_occurences_table[occurence]
    graph = "*" * count
    print(f"{occurence:<2}|{graph:<15}|{count:<2}")