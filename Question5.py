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

def assign_random_places_to_students():
    dic_seats = {}
    for s, p in zip(shuffle_students(), create_places()):
        dic_seats[s] = p
    return dic_seats

def not_in_window(student, dic_places):
    #windos are the seats ending in 2
    if(dic_places[student][-1] == '2'):
        old_seat = dic_places[student]
        new_seat = dic_places[student][:-1] + '1'
        for key in dic_places:
            if(dic_places[key] == new_seat):
                dic_places[key] = old_seat
                dic_places[student] = new_seat
    return dic_places

def not_in_back(student, dic_places):
    #windos are the seats ending in 3
    if(int(dic_places[student][1]) == 2):
        old_seat = dic_places[student]
        new_seat = dic_places[student][0] + '1' + dic_places[student][2:]
        for key in dic_places:
            if(dic_places[key] == new_seat):
                dic_places[key] = old_seat
                dic_places[student] = new_seat
    return dic_places

#do the magic
def seat_arrange(s_not_window ='', s_not_in_back=''):
    assign = assign_random_places_to_students()
    assign = not_in_back(s_not_in_back, assign)
    assign = not_in_window(s_not_window, assign)
    return assign

sa = seat_arrange(s_not_window='Carl', s_not_in_back='Malin')

for key in sa:
    print(key + ' seated ' +sa[key])
