import tkinter as tk

from numpy import place
from hangman_utils import random_word, check_word, check_occured
from tkinter import *
from PIL import ImageTk, Image

root = tk.Tk()
root.geometry("1000x600")
root.resizable(width=0, height=0)

select_word = ""
heart = 8
word_corrected = 0
passed_char = []

data = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
        'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


def main():
    pass


def start_game():
    global select_word
    global root
    global img

    rows = 0
    columns = 0
    select_word = random_word()

    root.destroy()  # Removes everything currently inside root.
    root = tk.Tk()
    root.geometry("1000x600")
    root.resizable(width=0, height=0)
    root.title('hangman')

    img = ImageTk.PhotoImage(Image.open(
        "2.jpg").resize((1000, 600), Image.ANTIALIAS))
    background_label = tk.Label(root, image=img)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    for i, char in enumerate(data):
        if i == 13:
            rows = 1
            columns = 0
            columns += 1
        else:
            columns += 1

        if i < 13:
            tk.Button(root, text=char, bg="#DCD0FF", height=2, width=8, command=Callback(
                char_click, char)).grid(
                row=rows, column=columns, sticky=tk.S, padx=5, pady=(510, 0))
        else:
            tk.Button(root, text=char, bg="#DCD0FF", height=2, width=8, command=Callback(
                char_click, char)).grid(
                row=rows, column=columns, sticky=tk.S, padx=5, pady=(5, 0))

    create_char(root)

    print(select_word)


root.title('HANGMAN')
n_word = len(select_word)

img = ImageTk.PhotoImage(Image.open(
    "1.jpg").resize((1000, 600), Image.ANTIALIAS))

background_label = tk.Label(root, image=img)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

tk.Button(text='START', bg="#3D3935", fg='white', height=3, width=18,
          command=start_game).place(x=430, y=400)


def try_again():
    global img
    global select_word
    global heart

    heart = 8
    rows = 0
    columns = 0

    select_word = random_word()

    print(select_word)

    img = ImageTk.PhotoImage(Image.open(
        "2.jpg").resize((1000, 600), Image.ANTIALIAS))
    background_label = tk.Label(root, image=img)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    for i, char in enumerate(data):
        if i == 13:
            rows = 1
            columns = 0
            columns += 1
        else:
            columns += 1

        if i < 13:
            tk.Button(root, text=char, bg="#DCD0FF", height=2, width=8, command=Callback(
                char_click, char)).grid(
                row=rows, column=columns, sticky=tk.S, padx=5, pady=(510, 0))
        else:
            tk.Button(root, text=char, bg="#DCD0FF", height=2, width=8, command=Callback(
                char_click, char)).grid(
                row=rows, column=columns, sticky=tk.S, padx=5, pady=(5, 0))

    create_char(root)


def create_char(input_root):

    data_char = data

    rows = 0
    columns = 0

    for i, char in enumerate(data_char):
        if i == 13:
            rows = 1
            columns = 0
            columns += 1
        else:
            columns += 1

        for passed in passed_char:
            passed = passed.upper()

            if passed == char:
                if i < 13:
                    tk.Button(input_root, text=char, bg="#DCD0FF", height=2, width=8, command=Callback(
                        char_click, char), state=DISABLED).grid(
                        row=rows, column=columns, sticky=tk.S, padx=5, pady=(510, 0))
                    break

                else:
                    tk.Button(input_root, text=char, bg="#DCD0FF", height=2, width=8, command=Callback(
                        char_click, char), state=DISABLED).grid(
                        row=rows, column=columns, sticky=tk.S, padx=5, pady=(5, 0))
                    break

            else:
                if i < 13:
                    tk.Button(input_root, text=char, bg="#DCD0FF", height=2, width=8, command=Callback(
                        char_click, char)).grid(
                        row=rows, column=columns, sticky=tk.S, padx=5, pady=(510, 0))
                else:
                    tk.Button(input_root, text=char, bg="#DCD0FF", height=2, width=8, command=Callback(
                        char_click, char)).grid(
                        row=rows, column=columns, sticky=tk.S, padx=5, pady=(5, 0))


class Callback:
    def __init__(self, func, *args, **kwargs):
        self.func = func
        self.args = args
        self.kwargs = kwargs

    def __call__(self):
        self.func(*self.args, **self.kwargs)


def char_click(char):
    global root
    global heart
    global word_corrected
    global passed_char
    global img
    global T

    if word_corrected == (len(select_word) - 1):

        word_corrected = 0
        passed_char = []

        root.destroy()  # Removes everything currently inside root.

        root = tk.Tk()
        root.geometry("1000x600")
        root.resizable(width=0, height=0)
        root.title('hangman')

        img = ImageTk.PhotoImage(Image.open(
            "12.jpg").resize((1000, 600), Image.ANTIALIAS))
        background_label = tk.Label(root, image=img)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        tk.Button(text='TRY AGAIN', bg="#3D3935", fg='white', height=3, width=18,
                  command=try_again).place(x=430, y=400)

    else:
        print(f"Button '{char}' pressed.")

        change_heart, change_corrected, change_passed = check_word(
            select_word, heart, char, word_corrected, passed_char)
        heart = change_heart
        word_corrected = change_corrected
        passed_char = change_passed

        if heart == 8:

            img = ImageTk.PhotoImage(Image.open(
                "3.jpg").resize((1000, 600), Image.ANTIALIAS))
            background_label = tk.Label(root, image=img)
            background_label.place(x=0, y=0, relwidth=1, relheight=1)

            create_char(root)

        if heart == 7:

            img = ImageTk.PhotoImage(Image.open(
                "3.jpg").resize((1000, 600), Image.ANTIALIAS))
            background_label = tk.Label(root, image=img)
            background_label.place(x=0, y=0, relwidth=1, relheight=1)

            create_char(root)

        if heart == 6:

            img = ImageTk.PhotoImage(Image.open(
                "4.jpg").resize((1000, 600), Image.ANTIALIAS))
            background_label = tk.Label(root, image=img)
            background_label.place(x=0, y=0, relwidth=1, relheight=1)

            create_char(root)

        if heart == 5:

            img = ImageTk.PhotoImage(Image.open(
                "5.jpg").resize((1000, 600), Image.ANTIALIAS))
            background_label = tk.Label(root, image=img)
            background_label.place(x=0, y=0, relwidth=1, relheight=1)

            create_char(root)

        if heart == 4:

            img = ImageTk.PhotoImage(Image.open(
                "6.jpg").resize((1000, 600), Image.ANTIALIAS))
            background_label = tk.Label(root, image=img)
            background_label.place(x=0, y=0, relwidth=1, relheight=1)

            create_char(root)

        if heart == 3:

            img = ImageTk.PhotoImage(Image.open(
                "7.jpg").resize((1000, 600), Image.ANTIALIAS))
            background_label = tk.Label(root, image=img)
            background_label.place(x=0, y=0, relwidth=1, relheight=1)

            create_char(root)

        if heart == 2:

            img = ImageTk.PhotoImage(Image.open(
                "8.jpg").resize((1000, 600), Image.ANTIALIAS))
            background_label = tk.Label(root, image=img)
            background_label.place(x=0, y=0, relwidth=1, relheight=1)

            create_char(root)

        if heart == 1:

            img = ImageTk.PhotoImage(Image.open(
                "9.jpg").resize((1000, 600), Image.ANTIALIAS))
            background_label = tk.Label(root, image=img)
            background_label.place(x=0, y=0, relwidth=1, relheight=1)

            create_char(root)

        if heart == 0:

            img = ImageTk.PhotoImage(Image.open(
                "10.jpg").resize((1000, 600), Image.ANTIALIAS))
            background_label = tk.Label(root, image=img)
            background_label.place(x=0, y=0, relwidth=1, relheight=1)

            create_char(root)

    if heart < 0:

        word_corrected = 0
        passed_char = []

        root.destroy()  # Removes everything currently inside root.

        root = tk.Tk()
        root.geometry("1000x600")
        root.resizable(width=0, height=0)
        root.title('hangman')

        img = ImageTk.PhotoImage(Image.open(
            "11.jpg").resize((1000, 600), Image.ANTIALIAS))
        background_label = tk.Label(root, image=img)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        tk.Button(text='TRY AGAIN', bg="#3D3935", fg='white', height=3, width=18,
                  command=try_again).place(x=430, y=400)

    return word_corrected, passed_char


root.mainloop()

if __name__ == "__main__":
    main()
