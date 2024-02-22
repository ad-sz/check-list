# import tkinter as tk
# from tkinter import ttk

# def move_window(event):
#     tpm_window.geometry(f'+{event.x_root}+{event.y_root}')

# #creating main window
# tpm_window = tk.Tk()

# #hide default title bar
# tpm_window.wm_overrideredirect(True)

# #setting size of the window
# tpm_window.geometry("500x500")

# #custom title bar
# #create frame "Frame" (bg-setting color, relief-style of the frame, bd-settink thick of the border)
# title_bar = tk.Frame(tpm_window, bg='green', relief='raised', bd=2)
# #putting frame "title_bar" in aplication window by use geometry manager "pack", "fill=tk.X" - stretching the frame horizontally, filling the entire available window width
# title_bar.pack(fill=tk.X)
# title_label = tk.Label(title_bar, text="TPM wytłaczarki", bg='green', fg='white', font=('Arial', 12))
# title_label.pack(side=tk.LEFT, padx=10)

# title_bar.bind('<B1-Motion>', move_window)

# #showing window
# tpm_window.mainloop()

import tkinter as tk

def move_window(event):
    tpm_window.geometry(f'+{event.x_root}+{event.y_root}')

def minimize_window():
    tpm_window.iconify()

def close_window():
    tpm_window.destroy()

tpm_window = tk.Tk()
tpm_window.geometry("500x500")
tpm_window.overrideredirect(True)  # Usuwa domyślny pasek tytułowy

title_bar = tk.Frame(tpm_window, bg='grey', relief='raised', bd=2)
title_bar.pack(fill=tk.X)
title_label = tk.Label(title_bar, text="TPM wytłaczarki", bg='grey', fg='white', font=('Arial', 12))
title_label.pack(side=tk.LEFT, padx=10)

minimize_button = tk.Button(title_bar, text='-', command=minimize_window, bg='grey', fg='white', font=('Arial', 10), bd=0, highlightthickness=0)
minimize_button.pack(side=tk.RIGHT, padx=(0, 5))

close_button = tk.Button(title_bar, text='X', command=close_window, bg='grey', fg='white', font=('Arial', 10), bd=0, highlightthickness=0)
close_button.pack(side=tk.RIGHT)

title_bar.bind('<B1-Motion>', move_window)

# Twój pozostały kod UI

tpm_window.mainloop()
