# imports
from tkinter import *
from tkinter import messagebox
import datetime


# root screen
root = Tk()
root.title('Tik Tak Toe')
root.iconbitmap('images/logos/my-ic.ico')
root.geometry('400x400')
root.configure(background='#20B2AA')

# creating frames for the launcher window...
header = Frame(root, bg='#20B2AA')
content = Frame(root, bg='#20B2AA')
footer = Frame(root, bg='#20B2AA')

root.columnconfigure(0, weight=1)

root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=8)
root.rowconfigure(2, weight=1)

header.grid(row=0, sticky='news')
content.grid(row=1, sticky='news')
footer.grid(row=2, sticky='news')

# validation label
entry_label = Label(content, bg='#20B2AA')
entry_label.grid(row=3, column=0, columnspan=3)


# my global variables
chance = 0
c = 0
data_matrix = [['-' for i in range(3)]for j in range(3)]


# validation for the player name boxes...
def check_entry():
    global entry_label

    if player1_name.get() and player2_name.get():
        entry_label.destroy()
        my_buttons()
    else:
        entry_label.destroy()
        message = ''
        if (not player1_name.get()) and (not player2_name.get()):
            player1_name.focus_set()
            message = '*Name fields are required'
        elif not player1_name.get():
            player1_name.focus_set()
            message = '*Player 1 Name is also required'
        else:
            player2_name.focus_set()
            message = '*Player 2 Name is also required'
        entry_label = Label(content, text=message, bg='#20B2AA', font=('Helvetica', 10))
        entry_label.grid(row=3, column=0, columnspan=3)


# storing data in a matrix
def data(row, column, text):
    data_matrix[row][column] = text


# resetting game data
def reset_data():
    global data_matrix, c, chance
    c = 0
    chance = 0
    data_matrix = [['-' for i in range(3)]for j in range(3)]
    player1_name.delete(0, END)
    player2_name.delete(0, END)


# conditions for the game
def game_conditions():
    global c
    if (data_matrix[0][0] == data_matrix[0][1]) and (data_matrix[0][0] == data_matrix[0][2]) or \
            (data_matrix[0][0] == data_matrix[1][0]) and (data_matrix[0][0] == data_matrix[2][0]) or \
            (data_matrix[0][0] == data_matrix[1][1]) and (data_matrix[0][0] == data_matrix[2][2]):
        if ((data_matrix[0][0]) != '-' and (data_matrix[0][1]) != '-' and (data_matrix[0][2]) != '-') or \
                ((data_matrix[0][0]) != '-' and (data_matrix[1][0]) != '-' and (data_matrix[2][0]) != '-') or \
                ((data_matrix[0][0]) != '-' and (data_matrix[1][1]) != '-' and (data_matrix[2][2]) != '-'):
            c = 1
    if (data_matrix[2][0] == data_matrix[2][1]) and (data_matrix[2][0] == data_matrix[2][2]) or \
            (data_matrix[2][0] == data_matrix[1][1]) and (data_matrix[2][0] == data_matrix[0][2]):
        if ((data_matrix[2][0]) != '-' and (data_matrix[2][1]) != '-' and (data_matrix[2][2]) != '-') or \
                ((data_matrix[2][0]) != '-' and (data_matrix[1][1]) != '-' and (data_matrix[0][2]) != '-'):
            c = 1
    if (data_matrix[0][2] == data_matrix[1][2]) and (data_matrix[0][2] == data_matrix[2][2]):
        if ((data_matrix[0][2]) != '-') and (data_matrix[1][2] != '-') and (data_matrix[2][2] != '-'):
            c = 1
    if ((data_matrix[1][1] == data_matrix[1][0]) and (data_matrix[1][1] == data_matrix[1][2])) or \
            ((data_matrix[1][1] == data_matrix[0][1]) and (data_matrix[1][1] == data_matrix[2][1])):
        if ((data_matrix[1][1] != '-') and (data_matrix[1][0] != '-') and (data_matrix[1][2] != '-')) or \
                ((data_matrix[1][1] != '-') and (data_matrix[0][1] != '-') and (data_matrix[2][1] != '-')):
            c = 1


#  checking for the game result
def check_result():
    global player_label
    game_conditions()
    message_response = -1
    if c == 1:
        player_label.destroy()
        if chance % 2:
            player_label = Label(game, text=f"{player1_name.get().title()} You Won!!!", bg='#000', fg='#FFF')
            player_label.grid(row=0, column=0, columnspan=2)
            message = f'Congratulations!!! {player1_name.get().title()}\nYou Won\nDo you want to continue?'
            message_response = messagebox.askyesno('Tik Tak Toe Result', message)
        else:
            player_label = Label(game, text=f"{player2_name.get().title()} You Won!!! ", bg='#000', fg='#FFF')
            player_label.grid(row=0, column=0, columnspan=2)
            message = f'Congratulations!!! {player2_name.get().title()}\nYou Won\nDo you want to continue?'
            message_response = messagebox.askyesno('Tik Tak Toe Result', message)
    elif chance == 9:
        message_response = messagebox.askyesno('Tik Tak Toe Result',
                                               'Game Over!!!\nNo Result...\nDo you want to continue?')
    if message_response == 1:
        reset_data()
        game.destroy()
        player1_name.focus_set()
    elif message_response == 0:
        exit()


# updating game screen
def clicked(row, column):
    global chance, player_label
    if not (chance % 2):
        button = Button(game, text='X', padx=30, pady=30, bg='#B22222', fg='#FFF')
        button.grid(row=row+1, column=column, padx=2, pady=2)
        data(row, column, 'X')
        chance += 1
        player_label.destroy()
        player_label = Label(game, text=f"{player2_name.get().title()} it's your turn", bg='#000', fg='#FFF')
        player_label.grid(row=0, column=0, columnspan=2)
        check_result()
    else:
        button = Button(game, text='O', padx=30, pady=30, bg='#B22222', fg='#FFF')
        button.grid(row=row+1, column=column, padx=2, pady=2)
        data(row, column, 'O')
        chance += 1
        player_label.destroy()
        player_label = Label(game, text=f"{player1_name.get().title()} it's your turn", bg='#000', fg='#FFF')
        player_label.grid(row=0, column=0, columnspan=2)
        check_result()


# game screen
def my_buttons():
    global game, player_label
    game = Tk()
    game.title('Tik Tak Toe')
    game.iconbitmap('images/logos/my-ic.ico')
    game.geometry('245x284')
    game.configure(background='#000')
    player_label = Label(game, text=f"{player1_name.get().title()} it's your turn", bg='#000', fg='#FFF')
    player_label.grid(row=0, column=0, columnspan=2)

    button_1 = Button(game, text='   ', padx=30, pady=30, bg='#B22222', fg='#FFF', command=lambda: clicked(0, 0))
    button_1.grid(row=1, column=0, padx=2, pady=2)
    button_2 = Button(game, text='   ', padx=30, pady=30, bg='#B22222', fg='#FFF', command=lambda: clicked(0, 1))
    button_2.grid(row=1, column=1, padx=2, pady=2)
    button_3 = Button(game, text='   ', padx=30, pady=30, bg='#B22222', fg='#FFF', command=lambda: clicked(0, 2))
    button_3.grid(row=1, column=2, padx=2, pady=2)

    button_4 = Button(game, text='   ', padx=30, pady=30, bg='#B22222', fg='#FFF', command=lambda: clicked(1, 0))
    button_4.grid(row=2, column=0, padx=2, pady=2)
    button_5 = Button(game, text='   ', padx=30, pady=30, bg='#B22222', fg='#FFF', command=lambda: clicked(1, 1))
    button_5.grid(row=2, column=1, padx=2, pady=2)
    button_1 = Button(game, text='   ', padx=30, pady=30, bg='#B22222', fg='#FFF', command=lambda: clicked(1, 2))
    button_1.grid(row=2, column=2, padx=2, pady=2)

    button_1 = Button(game, text='   ', padx=30, pady=30, bg='#B22222', fg='#FFF', command=lambda: clicked(2, 0))
    button_1.grid(row=3, column=0, padx=2, pady=2)
    button_1 = Button(game, text='   ', padx=30, pady=30, bg='#B22222', fg='#FFF', command=lambda: clicked(2, 1))
    button_1.grid(row=3, column=1, padx=2, pady=2)
    button_1 = Button(game, text='   ', padx=30, pady=30, bg='#B22222', fg='#FFF', command=lambda: clicked(2, 2))
    button_1.grid(row=3, column=2, padx=2, pady=2)


# launcher
def main():
    global player1_name, player2_name

    # header
    welcome_label = Label(header, text='Welcome to Tik Tak Toe', bg='#20B2AA', font=('Helvetica', 20))
    welcome_label.grid(row=0, column=0, columnspan=3, padx=40, pady=(10, 20))

    # content
    Label(content, text='Player 1 Enter Your Name', bg='#20B2AA').grid(row=0, column=0, padx=25)
    player1_name = Entry(content)
    player1_name.grid(row=0, column=1)
    Label(content, text='Player 2 Enter Your Name', bg='#20B2AA').grid(row=1, column=0, padx=25)
    player2_name = Entry(content)
    player2_name.grid(row=1, column=1)
    player1_name.focus_set()
    game_start_button = Button(content, text='Start The Game', command=check_entry)
    game_start_button.grid(row=2, column=1, pady=(10, 0))

    # footer
    footer_label = Label(footer, text=f'Copyright \u00a9 {datetime.date.today().year} '
                                      f'All rights reserved|Sameer'.encode('latin-1'),
                         bg='#20B2AA', fg='#FFF', font=('Helvetica', 10))
    footer_label.grid(row=0, column=0, columnspan=3, padx=67, pady=(20, 0))


# main method condition
if __name__ == '__main__':
    main()

root.mainloop()
