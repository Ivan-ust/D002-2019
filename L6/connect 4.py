def printcell(cells):
    print("-" * 29)
    for i in range(0, 6):
        for j in range(0, 7):
            print("| %s " % cells[i][j], end="")
        print("|")
        print("-" * 29)



cells = [[' ',' ',' ',' ',' ',' ',' ',' '], [' ',' ',' ',' ',' ',' ',' ',' '],\
         [' ',' ',' ',' ',' ',' ',' ',' '], [' ',' ',' ',' ',' ',' ',' ',' '],\
         [' ',' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' ',' ']]



def check_col(cells):
    for c in range(0,7) :
        for r in range(0,3) :
            if cells[r][c] == cells[r + 1][c] == cells[r + 2][c] == cells[r + 3][c] != ' ' :
                return True
    return False
            


def check_row(cells):
    for r in range(0,6) :
        for c in range(0,4) :
            if cells[r][c] == cells[r][c + 1] == cells[r][c + 2] == cells[r][c + 3] != ' ' :
                return True
    return False
                

               
def check_diagonaltopright(cells) :
    for r in range(3,6) :
       for c in range(0,4) :
            if cells[r][c] == cells[r - 1][c + 1] == cells[r - 2][c + 2] == cells[r - 3][c + 3] != ' ' :
                return True
    return False


                
def check_diagonaltopleft(cells) :
     for r in range(0,3) :
       for c in range(0,4) :
            if cells[r][c] == cells[r + 1][c + 1] == cells[r + 2][c + 2] == cells[r + 3][c + 3] != ' ' :
                return True
     return False



def player2(cells) :
    col2 = int(input("Player2 's turn.Please enter column. From 0 to 6.\t"))
    while col2 < 0 or col2 > 6 :
        print("Invalid input.")
        col2 = int(input("Player2 's turn.Please enter column. From 0 to 6.\t"))
    i = 5
    while cells[i][col2] != ' ' :
        i = i - 1
        if i < 0 :
            print("This line is full.Please put the chip in another row.")
            col2 = int(input("Player2 's turn.Please enter column. From 0 to 6.\t"))
            i = 5
    else :
        cells[i][col2] = 'X'
        printcell(cells)

    
     
def check_win(cells) :
    if check_col(cells) or check_row(cells) or check_diagonaltopright(cells) or check_diagonaltopleft(cells) :
        return True
    return False


        
def check_draw(cells) :
    if cells[0][0] == cells[0][1] == cells[0][2] == cells[0][3] == cells [0][4] == cells[0][5] == cells[0][6] != ' ':
        return True
    return False



printcell(cells)
while True :
    col = int(input("Player1 's turn. Please enter column. From 0 to 6.\t"))
    while col < 0 or col > 6 :
        print("Invalid input.")
        col = int(input("Player1 's turn.Please enter column. From 0 to 6.\t"))
    i = 5
    while cells[i][col] != ' ' :
        i = i - 1
        if i < 0 :
            print("This colimn is full.Please put the chip in another column.")
            col = int(input("Player1 's turn.Please enter column. From 0 to 6.\t"))
            i = 5
    else :
        cells[i][col] = 'O'
        printcell(cells)
        if check_win(cells) == True :
            print("Player1 wins")
            break
        if check_draw(cells) == True :
            print("Draw")
            break
        player2(cells)
        if check_win(cells) == True :
            print("Player2 wins")
            break
        if check_draw(cells) == True :
            print("Draw")
            break
