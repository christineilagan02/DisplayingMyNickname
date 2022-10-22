# Assignment 1:
# Create a program that will print your nickname using only asterisk character (*)

import sys

def intro():
    str1 = "TINE"
    print_T = [[" " for i in range(5)] for j in range(5)]
    print_I = [[" " for i in range(5)] for j in range(5)]
    print_N = [[" " for i in range(5)] for j in range(5)]
    print_E = [[" " for i in range(5)] for j in range(5)]

    # code for T
    for row in range(5):
        for col in range(5):
            if row==0 or col==2:
                print_T[row][col]= "\033[1m\033[92m*\033[0m"   
                
    # code for I
    for row in range(5):
        for col in range(5):
            if row==0 or col==2 or row==4:
                print_I[row][col]= "\033[1m\033[92m*\033[0m"

    # code for N
    for row in range(5):
        for col in range(5):
            if ((col==0 or col==4) or row==col):
                print_N[row][col]= "\033[1m\033[92m*\033[0m"
                
    # code for E
    for row in range(5):
        for col in range(5):
            if ((col==0 or row==4) or (col==0 or row==0) or (row==2 and (col!=3 and col!=4))):
                print_E[row][col]= "\033[1m\033[92m*\033[0m"  
                
    for i in range(5):
        print(end="    ")
        for j in range(5):
            print(print_T[i][j], end=" ")
        print(end="  ")
        for j in range(5):
            print(print_I[i][j], end=" ")
        print(end="  ")
        for j in range(5):
            print(print_N[i][j], end=" ")
        print(end="  ")
        for j in range(5):
            print(print_E[i][j], end=" ")
        print()
        
def effect():
    from time import sleep
    string = ("\t\t\33[1m  This is my Nickname  \33[0m")
    for letter in string:
        sleep(0.15)
        sys.stdout.write(letter)
        sys.stdout.flush()  
    string = ("\n\t\t\33[3m  short for Christine  \33[0m\n\n")
    for letter in string:
        sleep(0.15)
        sys.stdout.write(letter)
        sys.stdout.flush()  
        
def design():
    print("\n\33[1m\33[33moOo\33[0m---+---+---+------+---\33[1m\33[33moOo\33[0m---+------+---+---+---\33[1m\33[33moOo\33[0m\n")
    
def menu():
    design()
    effect()
    intro()
    design()
    print("\n\n")
    
menu()