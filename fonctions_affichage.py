import py5

def draw_sudoku_grid():
    py5.stroke_weight(2)  # Set the stroke weight for grid lines
    py5.stroke(0)  # Set the stroke color to black

    # Draw vertical lines
    for x in range(10):
        if x % 3 == 0:
            py5.stroke_weight(6)  # Set thicker stroke weight for bold lines
        else:
            py5.stroke_weight(2)  # Set regular stroke weight for thin lines
        py5.line(x * 70, 0, x * 70, 700)

    # Draw horizontal lines
    for y in range(10):
        if y % 3 == 0:
            py5.stroke_weight(6)  # Set thicker stroke weight for bold lines
        else:
            py5.stroke_weight(2)  # Set regular stroke weight for thin lines
        py5.line(0, y * 70, 800, y * 70)

def mouse_highlight():
    pos_x = (py5.mouse_x // 70) * 70
    pos_y = (py5.mouse_y // 70) * 70

    py5.no_stroke()

    py5.fill('#9b9b9b')
    py5.square(pos_x, pos_y, 70)

def draw_numbers(number, inital_number):

    #Draw numbers in the grid
    for x in range(9):
        for y in range(9):
            if number[x + y * 9] == 0:
                continue

            if inital_number[x + y*9] == 0:
                py5.fill('#0000ff')
            else:
                py5.fill('#000000')

            py5.text_size(30)
            py5.text_align(py5.CENTER)
            py5.text(number[x + y * 9], 35+x*70, 45+y*70)
    
    #Draw the number selection
    
    py5.fill('#000000')
    py5.text_size(30)
    py5.text_align(py5.CENTER)
    for i in range(9):
        py5.text(f"{i+1}", 665, i*70 + 45)