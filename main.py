"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Jan Šlechta
email: janslechta31@gmail.com
discord: honzas0100
"""
import task_template

users = {"lopol" : "password", "gogo" : "aaa"}
username = input("zadej prosim svoje prihlasovaci jmeno: ")
password = input("zadej svoje heslo: ")


if not username in users:
    print("spatny user")
elif users.get(username) == password:
    print("Vitej v analyzatoru ", username)
else: 
    print("spatne heslo")