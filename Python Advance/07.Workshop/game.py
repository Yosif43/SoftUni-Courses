import tkinter as tk
from tkinter import messagebox
from functools import partial

app_config = {
    'board': [[None] * 3 for _ in range(3)],
    'buttons': [[None] * 3 for _ in range(3)],
    'sign': 'X',
    'X': None,
    'O': None
}


def rebuild_window(window):
    window.destroy()
    window = tk.Tk()
    window.geometry('280x280')
    window.title('Tic Tac Toe')
    return window


def is_row_win(board_):
    for row_ in board_:
        if len(set(row_)) == 1 and set(row_) != {None}:
            return True
    return False


def is_column_win(board_, current_sign_):
    for col_ in range(len(board_)):
        current_column = []
        for row_ in range(len(board_)):
            current_column.append(board_[row_][col_] == current_sign_)
        if all(current_column):
            return True
    return False


def is_diagonal_win(board_, current_sign_):
    diagonal_1, diagonal_2 = [], []
    for inx in range(len(board_)):
        diagonal_1.append(board_[inx][inx] == current_sign_)
        diagonal_2.append(board_[inx][len(board_) - 1 - inx] == current_sign_)
    return all(diagonal_1) or all(diagonal_2)


def is_win(board_, current_sign_):
    return any([is_row_win(board_), is_column_win(board_, current_sign_), is_diagonal_win(board_, current_sign_)])


def is_row_win_possible(board_):
    if all(['X' in row_ and 'O' in row_ for row_ in board_]):
        return False
    return True


def is_col_win_possible(board_):
    columns = []
    for col_ in range(len(board_)):
        current_column = []
        for row_ in range(len(board_)):
            current_column.append(board_[row_][col_])
        columns.append(current_column)
    if all(['X' in col_ and 'O' in col_ for col_ in columns]):
        return False
    return True


def is_diagonal_win_possible(board_):
    diagonal_1, diagonal_2 = [], []
    for inx in range(len(board_)):
        diagonal_1.append(board_[inx][inx])
        diagonal_2.append(board_[inx][len(board_) - 1 - inx])
    if 'X' in diagonal_1 and 'O' in diagonal_1 and 'X' in diagonal_2 and 'O' in diagonal_2:
        return False
    return True


def is_draw(board_):
    if any([is_row_win_possible(board_), is_col_win_possible(board_), is_diagonal_win_possible(board_)]):
        return False
    return True


def get_content(row, col, window):
    if app_config['board'][row][col] is None:
        app_config['board'][row][col] = app_config['sign']
        app_config['buttons'][row][col].config(text=app_config['board'][row][col])
        if is_win(app_config['board'], app_config['sign']):
            window = rebuild_window(window)
            tk.Label(window, text=f"Player {app_config[app_config['sign']]} won!").pack()
            # messagebox.showinfo("Win", f"Player {app_config[app_config['sign']]} won!")
        if is_draw(app_config['board']):
            window = rebuild_window(window)
            tk.Label(window, text="Draw!").pack()
            # messagebox.showinfo("Draw!", "Draw!")
        app_config['sign'] = 'X' if app_config['sign'] == 'O' else 'O'


def render_board(window):
    grid_frame = tk.Frame(master=window)
    grid_frame.pack(padx=10, pady=10)
    for row in range(3):
        for col in range(3):
            gc = partial(get_content, row, col, window)
            app_config['buttons'][row][col] = tk.Button(
                master=grid_frame,
                command=gc,
                text=app_config['board'][row][col] if app_config['board'][row][col] else ' ',
                width=5,
                height=4
            )
            app_config['buttons'][row][col].grid(row=row, column=col)


def start_game(window, player_one, player_two, player_one_sign, player_two_sign):
    window = rebuild_window(window)

    app_config['sign'] = player_one_sign
    app_config[player_one_sign] = player_one
    app_config[player_two_sign] = player_two

    render_board(window)


def start_screen():
    window = tk.Tk()
    window.geometry('240x240')
    window.title('Tic Tac Toe')

    tk.Label(window, text='First player name: ').pack()
    player_one = tk.Entry(window)
    player_one.pack()
    p_one_sign = tk.StringVar()
    p_one_sign.set('X')
    tk.Label(window, text='Choose sign for player one:').pack()
    tk.Radiobutton(window, text='X', variable=p_one_sign, value='X').pack()
    tk.Radiobutton(window, text='O', variable=p_one_sign, value='O').pack()
    tk.Label(window, text='Second player name: ').pack()
    player_two = tk.Entry(window)
    player_two.pack()

    tk.Button(window, text='Start game', command=lambda: start_game(window,
                                                                    player_one.get(),
                                                                    player_two.get(),
                                                                    p_one_sign.get(),
                                                                    'X' if p_one_sign.get() == 'O' else 'O')
              ).pack()

    window.mainloop()


if __name__ == '__main__':
    start_screen()
