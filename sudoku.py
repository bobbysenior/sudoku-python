""" 
Authors: 
Created the 10/04/2024
"""
import py5
import random
from fonctions_affichage import *
starting_grids = 'Sudoku/Grids_sudoku.txt'

Numbers_dict = {}
Initial_numbers_dict = {}

selected_cell = [None, None]

# Creation d'un dictionnaire de départ
def init_grid():
    grids = []
    with open(starting_grids, 'r') as f:
        lines = py5.load_strings(starting_grids)
        for line in lines:
            grid = [list(map(int, list(row))) for row in line.split()]
            grids.append(grid)
    Inital_grid = (grids[int(random.random() * 50)][0])
    grid_dict = {}

    # Indexation de la grille
    for i in range(81):
        grid_dict[i] = Inital_grid[i]

    return grid_dict
    

def number_selection(number, inital_number):
    global selected_cell
    
    pos_x = (py5.mouse_x // 70)
    pos_y = (py5.mouse_y // 70)
    
    if py5.mouse_x < 630:

        py5.no_stroke()

        if py5.is_mouse_pressed:
            if inital_number[pos_x + (pos_y) * 9] == 0:
                selected_cell = [pos_x, pos_y]


        py5.fill('#9b9b9b')
        py5.square(pos_x * 70, pos_y * 70, 70)
        
    else:    
        py5.no_stroke()

        py5.fill('#C9C062')
        py5.square(pos_x * 70, pos_y * 70, 70)

        if selected_cell != [None, None]:
            if py5.is_mouse_pressed:
                number[selected_cell[0] + (selected_cell[1]) * 9] = pos_y + 1
            
    if selected_cell != [None, None]:
        py5.fill('#5CED73')
        py5.square(selected_cell[0] * 70, selected_cell[1] * 70, 70)


def error(number):
    error_index_list = []

    def is_not_correct(index_list):
        for i in range(1,10):
            count = 0
            value_list = [number[i] for i in index_list]
            for values in value_list:
                if values == i:
                    count = count + 1
            if count > 1:
                return True
        return False
            
     # Fonctions to find numbers of a row
    def find_row(row):
        return [row*9 + i for i in range(9)]
    # Fonctions to find numbers of a collumn
    def find_collumn(collumn):
        return [collumn + i * 9 for i in range(9)]
    # Fonctions to find numbers of a big square
    def find_square(x, y):
        return [x * 3 + y * 3 * 9 + i + j * 9 for j in range(3) for i in range(3)]
        

    for i in range(9):
        if is_not_correct(find_row(i)):
            error_index_list = list(set(error_index_list + find_row(i)))

    for i in range(9):
       if is_not_correct(find_collumn(i)):
            error_index_list = list(set(error_index_list + find_collumn(i)))

    for i in range(3):
        for j in range(3):
            if is_not_correct(find_square(i,j)):
                error_index_list = list(set(error_index_list + find_square(i,j)))

    py5.fill('#FF6666')
    py5.no_stroke()
    for i in error_index_list:
        py5.square(i%9 * 70, i//9 * 70, 70)

    if error_index_list == []:
        return False
    else:
        return True


def win_check(number):
    if error(number) == False:
        if all(value != 0 for value in number.values()):
            return True
    
    return False
   

def draw_win_screen():
        # Set the background color to a deep pink
        py5.stroke(0)  # Set the frame color to black
        py5.fill(255, 102, 204)

        # Draw a rectangle as the background
        py5.rect(0, 0, py5.width, py5.height)

        

        # Draw some confetti to celebrate the win
        py5.no_stroke()
        py5.fill(255, 235, 186)
        py5.ellipse(py5.width/2 + 120, py5.height/2 - 60, 50, 50)
        py5.fill(230, 162, 208)
        py5.ellipse(py5.width/2 - 180, py5.height/2 - 100, 50, 50)
        py5.fill(255, 160, 196)
        py5.ellipse(py5.width/2 + 230, py5.height/2 + 50, 50, 50)
        py5.fill(255, 242, 175)
        py5.ellipse(py5.width/2 + 150, py5.height/2 - 150, 50, 50)
        py5.fill(204, 224, 255)
        py5.ellipse(py5.width/2 - 250, py5.height/2 + 150, 50, 50)
        py5.fill(179, 222, 255)
        py5.ellipse(py5.width/2 - 50, py5.height/2 - 200, 50, 50)
        py5.fill(255, 213, 175)
        py5.ellipse(py5.width/2 - 120, py5.height/2 + 10, 50, 50)

        # Draw the text for the win screen
        py5.text_size(72)
        py5.text_align(py5.CENTER, py5.CENTER)
        py5.fill(0)  # Set the text color to black
        py5.text("You Win!", py5.width/2, py5.height/2)

        # Draw a frame around the text
        py5.stroke_weight(8)
        py5.no_fill()
        py5.stroke(0)  # Set the frame color to black
        py5.rect(py5.width/2 - 150, py5.height/2 - 100, 300, 200)

        py5.no_loop()

def setup():
    global Numbers_dict, Initial_numbers_dict
    py5.size(700,630)
    py5.background(255)
    Initial_numbers_dict = init_grid()
    Numbers_dict = Initial_numbers_dict.copy()
    draw_sudoku_grid()

def draw():
    global Numbers_dict, Initial_numbers_dict
    py5.background(255)

    
    py5.fill("#FBF07B")
    py5.rect(630,0,700,630)

    
    if win_check(Numbers_dict) == True:
        draw_win_screen()
    else:
        number_selection(Numbers_dict, Initial_numbers_dict)
        draw_sudoku_grid()
        draw_numbers(Numbers_dict, Initial_numbers_dict)

py5.run_sketch()
