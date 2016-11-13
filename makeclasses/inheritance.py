# -*- coding: utf-8 -*-

class Parent():
    def __init__(self,last_name,eye_color):
        print('Parent Constructor Called')
        self.last_name = last_name
        self.eye_color = eye_color
    def show_info(self):
        print('Last Name - ' + self.last_name)
        print('Eye Color - ' + self.eye_color)
        
class Child(Parent):
    def __init__(self,last_name,eye_color,number_of_toys):
        print('Child Constructor Called')
        Parent.__init__(self,last_name,eye_color)
        self.number_of_toys = number_of_toys
    #overriding
    def show_info(self):
        print('Last Name - '+ self.last_name)
        print('Eye Color - ' + self.eye_color)
        print('Number of toy - ' + str(self.number_of_toys))

miley_cyrus = Child('Cyrus','Blue',5)
miley_cyrus.show_info()
#print(miley_cyrus.last_name)
#print(miley_cyrus.number_of_toys)

