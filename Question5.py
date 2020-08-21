# where you write a code that randomly places each of 
# the 9 data analytics candidates in a random seat in the classroom. 
# Add extra requirements and corresponding logic:-One of the candidates do not have glasses and cannot sit in the back row (pick who you want this to be). 
# -One of the candidates get distracted by what going on outside the window and should not sit next to the windows (pick who you want this to be).

import random
#Create the sitting places
def create_places():
    places_keys = []
    for i in range(3):
        for j in range(3):
            places_keys.append('R' + str(i) + 'S' + str(j))
    return places_keys

#Shuffle the students
def shuffle_students():
    students = ['Camila', 'Malin', 'Lene', 'Helene', 'Kaja', 'Martin', 'Osama', 'Salam', 'Carl']
    random.shuffle(students)
    return students

#do the magic
def assign_random_places_to_students():
    dic_seats = {}
    for s, p in zip(shuffle_students(), create_places()):
        dic_seats[p] = s
    return dic_seats



print(assign_random_places_to_students())