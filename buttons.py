import tkinter as tk


def create_button_ok_nok(frame, what_is_checking):
    #setting variable for user choice
    choice = tk.StringVar(value="none")

    #create and placing text in the frame
    label = tk.Label(frame, text=what_is_checking, font=('Arial', 18))
    label.pack(side=tk.TOP, padx=8, pady=(0, 20))

    #create frame for buttons
    radio_frame = tk.Frame(frame)
    radio_frame.pack(side=tk.TOP)

    #define style for radio buttons
    radiobutton_style = ('Arial', 20)

    #define buttom size
    radiobutton_width = 10

    #define space around buttoms
    padx_pady = 8

    #create frame for buttons
    radiobutton_ok = tk.Radiobutton(radio_frame, text="OK", variable=choice, value="ok", font=radiobutton_style, indicatoron=0, width=radiobutton_width, padx=padx_pady, pady=padx_pady, anchor='n')
    radiobutton_ok.pack(side=tk.LEFT)

    radiobutton_nok = tk.Radiobutton(radio_frame, text="NOK", variable=choice, value="nok", font=radiobutton_style, indicatoron=0, width=radiobutton_width, padx=padx_pady, pady=padx_pady, anchor='n')
    radiobutton_nok.pack(side=tk.RIGHT)

    return choice