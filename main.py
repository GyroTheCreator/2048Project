"""
Auteur:     Tiago Da Costa Lourenço
Date:       Février 2023
Version:    1.0
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

grid = [[None,None,None,2], [4,8,16,32], [64,128,256,512], [1024,2048,4096,8192]]
grid_values = [[None,None,None,None],[None,None,None,None],[None,None,None,None],[None,None,None,None]]

grid_width = 100
grid_height = 90

colors = {
    "background": "#311166",
    "background_ampli": "#563F99",
    "empty": "#D3FFDA",
    None: "lightgrey",
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

# FRAME
top_space_frame = Frame(window, background=colors["background"], height=35, width=400)
top_frame = Frame(window, background=colors["background"])
logo_frame = Frame(top_frame, background=colors["background"])
logo_space_score = Frame(top_frame, background=colors["background"], width=40)
score_frame = Frame(top_frame, background=colors["background_ampli"])
space_frame = Frame(top_frame, background=colors["background"], width=10)
top_score_frame = Frame(top_frame, background=colors["background_ampli"])
top_bottom_frame = Frame(window, background=colors["background"])
label_frame = Frame(top_bottom_frame, background=colors["background"])
button_frame = Frame(top_bottom_frame, background=colors["background"])

# LABEL
logo_label = Label(logo_frame, text="2048", font="Arial, 54", fg="white", background=colors["background"])
slide_label = Label(label_frame, text="Slide the numbers and get 2048 to win!", font="Arial, 12", background=colors["background"], fg="white")
score_label = Label(top_score_frame, text="          Score         ", fg="white", background=colors["background_ampli"])
value_score_label = Label(top_score_frame, text=f"         {score}        ", fg="white", background=colors["background_ampli"])
top_label = Label(score_frame, text=f"      Max ★      ", fg="white", background=colors["background_ampli"])
value_top_label = Label(score_frame, text=f"        {maxscore}         ", fg="white", background=colors["background_ampli"])

# BUTTON
new_button = Button(button_frame, text="New game", height=1, width=8)

# PACK
top_space_frame.pack()
top_frame.pack()
logo_frame.pack(side=LEFT)
logo_space_score.pack(side=LEFT)
score_frame.pack(side=RIGHT)
space_frame.pack(side=RIGHT)
top_score_frame.pack(side=RIGHT)
top_bottom_frame.pack(pady=10)
score_label.pack(pady=1)
value_score_label.pack(pady=1)
top_label.pack(pady=1, padx=5)
value_top_label.pack(pady=1, padx=5)
label_frame.pack(side=LEFT)
button_frame.pack(side=RIGHT)
logo_label.pack()
slide_label.pack()
new_button.pack(padx=20)

# ESPACE ENTRE LES DEUX
between = Frame(window, height=20, background=colors["background"])
between.pack()

# FRAMES DU BLOCK DU JEU
alls = Frame(window, height=400, width=415, background=colors["background_ampli"])


# PACKS DU BLOCK DU JEU
alls.pack()

#############
# MAIN CODE #
#############

# GRID DISPLAY
for i in range(len(grid)):
    for j in range(len(grid[i])):
        grid_values[i][j] = Label(alls,text=grid[i][j], width=8, height=3, borderwidth=1, relief="solid", font=("Trajan Pro", 14), fg="white", bg=colors[grid[i][j]])
        grid_values[i][j].place(x=10 + grid_width * j, y=25 + grid_height * i)

##############
# APP LAUNCH #
##############

if __name__ == '__main__':
    window.mainloop()
