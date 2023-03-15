"""
Auteur:     Tiago Da Costa Lourenço
Date:       Février 2023
Version:    v0.1
Projet:     Jeu du 2048

    Mentions honorables:
    ★ Carlos-Miguel Ferreira Da Silva

"""

#####################
# MODULES IMPORTING #
#####################

from tkinter import *
import random
# from tkinter import messagebox

#############
# VARIABLES #
#############

grid = [[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]]
grid_values = [[None,None,None,None],[None,None,None,None],[None,None,None,None],[None,None,None,None]]

grid_width = 100
grid_height = 90

colors = {
    "background": "#554597",
    "background_ampli": "#16006A",
    0: "#4C3E84",
    2: "#F2006B",
    4: "#F20089",
    8: "#E500A4",
    16: "#DB00B6",
    32: "#D100D1",
    64: "#BC00DD",
    128: "#B100E8",
    256: "#A100F2",
    512: "#8900F2",
    1024: "#6A00F4",
    2048: "#2D00F7",
    4096: "#2500CD",
    8192: "#000000",
}

maxscore = 0
score = 0
chance = 0.80
is2048 = False

###################
# WINDOW CREATION #
###################

window = Tk()

w = 500
h = 630

screenwidth = window.winfo_screenwidth()
screenheight = window.winfo_screenheight()

windowmiddlew = w / 2
windowmiddleh = h / 2

x = (screenwidth / 2) - (w / 2)
y = (screenheight / 2) - (h / 2)

# PARAMETERS
window.title("Jeu du 2048")
window.resizable(False, False)
window.geometry('%dx%d+%d+%d' % (w, h, x, y))
window.iconbitmap("media/icon.ico")
window.config(bg=colors["background"])

##########################
# DESIGN AIDE PAR CARLOS # ★
##########################

# DESIGN FRAME
max_space = Frame(window, background=colors["background"], height=35, width=400)
max_frame = Frame(window, background=colors["background"])

title_frame = Frame(max_frame, background=colors["background"])
title_space = Frame(max_frame, background=colors["background"], width=40)

score_frame = Frame(max_frame, background=colors["background_ampli"])
score_space = Frame(max_frame, background=colors["background"], width=10)

max_score_frame = Frame(max_frame, background=colors["background_ampli"])
max_bottom_frame = Frame(window, background=colors["background"])

label_frame = Frame(max_bottom_frame, background=colors["background"])
button_frame = Frame(max_bottom_frame, background=colors["background"])

# DESIGN LABEL
logo_label = Label(title_frame, text="2048", font="Arial, 54", fg="white", background=colors["background"])
slide_label = Label(label_frame, text="Slide the grid to get 8192 in order to win !", font="Arial, 12", background=colors["background"], fg="white")

score_label = Label(max_score_frame, text="          Score         ", fg="white", background=colors["background_ampli"])
value_score_label = Label(max_score_frame, text=f"         {score}        ", fg="white",
                          background=colors["background_ampli"])

top_label = Label(score_frame, text=f"      Max ★      ", fg="white", background=colors["background_ampli"])
value_top_label = Label(score_frame, text=f"        {maxscore}         ", fg="white", background=colors["background_ampli"])

# DESIGN BUTTON

# PACK ALL THIS
max_space.pack()
max_frame.pack()

title_frame.pack(side=LEFT)
title_space.pack(side=LEFT)

score_frame.pack(side=RIGHT)
score_space.pack(side=RIGHT)

max_score_frame.pack(side=RIGHT)
max_bottom_frame.pack(pady=10)

score_label.pack(pady=1)
value_score_label.pack(pady=1)

top_label.pack(pady=1, padx=5)
value_top_label.pack(pady=1, padx=5)

label_frame.pack(side=LEFT)
button_frame.pack(side=RIGHT)

logo_label.pack()
slide_label.pack()

# SPACE BETWEEN THE GAME
between = Frame(window, height=20, background=colors["background"])
between.pack()

# BLOCK FRAME
alls = Frame(window, height=400, width=415, background=colors["background_ampli"])
alls.pack()

for i in range(len(grid)):
    for j in range(len(grid[i])):
        grid_values[i][j] = Label(alls, text=grid[i][j], width=8, height=3, borderwidth=1, relief="solid",
                                  font=("Comic Sans MS", 14), fg="white", bg=colors[grid[i][j]])
        grid_values[i][j].place(x=10 + grid_width * j, y=25 + grid_height * i)

#############
# MAIN CODE #
#############

# GRID DISPLAY
def display_grid():
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 0:
                grid_values[i][j].config(text="", bg=colors["background"])
            else:
                grid_values[i][j].config(text=grid[i][j], bg=colors[grid[i][j]])

def new_game():
    global grid
    grid = [[0,0,0,0],
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0]]

    [rand_om() for _ in range(2)]
    display_grid()

new_button = Button(button_frame, text="New game", height=1, width=8, command=new_game)
new_button.pack(padx=20)

#[random_spawn() for _ in range(2)]

# PACK FUNCTION
def pack(a, b, c, d):
    global nmove
    nmove = 0

    if c == 0 and d > 0:
        c, d = d, 0
        nmove += 1 # Add +1 to movement list

    if b == 0 and c > 0:
        b, c, d = c, d, 0
        nmove += 1 # Add +1 to movement list

    if a == 0 and b > 0:
        a, b, c, d = b, c, d, 0
        nmove += 1 # Add +1 to movement list

    if a == b and b > 0:
        a, b, c, d = a+b, c, d, 0
        nmove += 1 # Add +1 to movement list

    if b == c and c > 0:
        b, c, d = b+c, d, 0
        nmove += 1 # Add +1 to movement list

    if c == d and d > 0:
        c, d = c+d, 0
        nmove += 1 # Add +1 to movement list

    temp = [a, b, c, d]
    return temp


# FUNCTION FOR MOVE LEFT ACTION

def rand_om():
    randomgrid = random.randint(0, 3)
    randomgrid2 = random.randint(0, 3)

    while grid[randomgrid][randomgrid2] != 0:
          randomgrid = random.randint(0, 3)
          randomgrid2 = random.randint(0, 3)
          if grid[randomgrid][randomgrid2] == 0:
              if random.random() < chance:
                  grid[randomgrid][randomgrid2] = 2
              else:
                  grid[randomgrid][randomgrid2] = 4
              break
    else:
        if random.random() < chance:
            grid[randomgrid][randomgrid2] = 2
        else:
            grid[randomgrid][randomgrid2] = 4
    display_grid()

new_game() # Lance une partie automatiquement

def move_left(event):
    tempmove = 0
    for ligne in range(len(grid)):
        [grid[ligne][0], grid[ligne][1], grid[ligne][2], grid[ligne][3]]= pack(grid[ligne][0],grid[ligne][1],grid[ligne][2],grid[ligne][3])
        tempmove += nmove
    if tempmove != 0:
        rand_om()
    display_grid()


#Déplacer les chiffres à droite
def move_right(event):
    tempmove = 0
    for ligne in range(4):
        [grid[ligne][3], grid[ligne][2], grid[ligne][1], grid[ligne][0]] = pack(grid[ligne][3],
        grid[ligne][2],grid[ligne][1],grid[ligne][0])
        tempmove += nmove
    if tempmove != 0:
        rand_om()
    display_grid()


#Déplacer les chiffres en haut
def move_up(event):
    tempmove = 0
    for ligne in range(4):
        [grid[0][ligne], grid[1][ligne], grid[2][ligne], grid[3][ligne]] = pack(grid[0][ligne],
        grid[1][ligne],grid[2][ligne],grid[3][ligne])
        tempmove += nmove
    if tempmove != 0:
        rand_om()
    display_grid()


#Déplacer les chiffres en bas
def move_down(event):
    tempmove = 0
    for ligne in range(4):
        [grid[3][ligne], grid[2][ligne], grid[1][ligne], grid[0][ligne]] = pack(grid[3][ligne],
        grid[2][ligne],grid[1][ligne],grid[0][ligne])
        tempmove += nmove
    if tempmove != 0:
        rand_om()
    display_grid()

"""
def move_left(event):
    for i in range(len(grid)):
        grid[i] = pack(grid[i][0], grid[i][1], grid[i][2], grid[i][3])
    random_spawn()
    display_grid() # Refresh the game

# FUNCTION FOR MOVE RIGHT ACTION
def move_right(event):
    for i in range(len(grid)):
        grid[i] = pack(grid[i][3], grid[i][2], grid[i][1], grid[i][0])
    random_spawn()
    display_grid()

# FUNCTION FOR MOVE UP ACTION
def move_up(event):
    for i in range(len(grid)):
        grid[i] = pack(grid[0][i], grid[1][i], grid[2][i], grid[3][i])
    random_spawn()
    display_grid()

# FUNCTION FOR MOVE DOWN ACTION
def move_down(event):
    for i in range(len(grid)):
        grid[i] = pack(grid[3][i], grid[2][i], grid[1][i], grid[0][i])
    random_spawn()
    display_grid()"""

# KEYBINDS
window.bind("<w>", move_up)
window.bind("<s>", move_down)
window.bind("<a>", move_left)
window.bind("<d>", move_right)

##############
# APP LAUNCH #
##############

if __name__ == '__main__':
    print("Application lancée avec succès!")
    window.mainloop()
