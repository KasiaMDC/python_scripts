# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 21:23:16 2024

@author: Kasia
"""
import random

def display_board(board):
    for i in range(len(board)):
        
        print('+-------'*3, '+')
        print('|       '*3, '|')
        
        for j in range(len(board[i])):
            print('|   ', end = '')
            print(board[i][j], end = '')
            print('   ', end = '')
        else: 
            print(' |')

        print('|       '*3, '|')    
    else:
        print('+-------'*3, '+')


# The function accepts the board's current status, asks the user about their move, 
# checks the input, and updates the board according to the user's decision.
def enter_move(board):
    global draw_again
    draw_again = True
    while draw_again:
        try:
            users_move = int(input("What's your next move...?"))
            list_of_free_fields = make_list_of_free_fields(board)
            i = (users_move - 1) // 3   
            j = (users_move -1) % 3
            
            if users_move < 1 or users_move > 9:
                print("Insert a free field from the board as a number2")   
                continue
            if (i,j) not in list_of_free_fields:
                print("this field is already taken. Please choose a free field")
                continue
            else:
                draw_again = False
        except ValueError:
            print("Insert a free field from the board as a number")
    
    board[i][j] = 'O'
       
    return board;


 # The function browses the board and builds a list of all the free squares; 
 # the list consists of tuples, while each tuple is a pair of row and column numbers.
def make_list_of_free_fields(board):
    list_of_free_fields = []
    
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] != 'X' and board[i][j] != 'O':
                tuple = (i, j)
                list_of_free_fields.append(tuple)
                
    return list_of_free_fields


# The function analyzes the board's status in order to check if 
# the player using 'O's or 'X's has won the game
def victory_for(board, sign):
    victory_list = [sign, sign, sign]
    
    for item in board:
        if item == victory_list:
            return sign
        
    vertical_list = [] 
    j = 0
    for i in range(len(board)):
        vertical_list.append(board[i][j])
        if len(vertical_list) == 3 and vertical_list == victory_list:
            return sign
        else: j +=1
    
    if(sign == 'X'):
        if board[0][0] == 'X' and board[2][2] == 'X':
            return sign
        elif board[0][2] == 'X' and board[2][0] == 'X':
            return sign
    
    list_of_free_fields = make_list_of_free_fields(board)
    if len(list_of_free_fields) == 0:
        print("ënd of the game! Try again!")
        global game_not_won
        game_not_won = False
    

 # The function draws the computer's move and updates the board.
def draw_move(board):    
    list_of_free_fields = make_list_of_free_fields(board)            
                 
    computer_choice = random.choice(list_of_free_fields)
   
    board[computer_choice[0]][computer_choice[1]] = 'X'
    
    return board


def main():
    
    board = [[1,2,3],[4,'X',6],[7,8,9]]
    game_not_won = True
    
    while game_not_won:
        display_board(board)
        board  = enter_move(board)
        victory = victory_for(board, 'O')
        if victory != None:
            print("the winner is O")
            break
        display_board(board)
        board = draw_move(board)
        victory = victory_for(board, 'X')
        if victory != None:
            print("the winner is X")
            break
    
    display_board(board)

if __name__ == '__main__':
    main()