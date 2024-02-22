import tkinter as tk

#creating main window
tpm_window = tk.Tk()

#setting size of the window
tpm_window.geometry("800x500")

#setting title of the window
tpm_window.title("TPM wytłaczarki")

#create frame for grouping text and buttons
frame = tk.Frame(tpm_window)
frame.pack(padx=10, pady=10)

#setting variable for user choice
choice = tk.StringVar(value="none")

#create and placing text in the frame
label = tk.Label(frame, text="Sprawdzenie zaworów", font=('Arial', 18))
label.pack(side=tk.LEFT, padx=8)

#create frame for buttons
radio_frame = tk.Frame(frame)
radio_frame.pack(side=tk.RIGHT)

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

#showing window
tpm_window.mainloop()
