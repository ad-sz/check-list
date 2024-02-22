import tkinter as tk
from buttons import create_button_ok_nok

#function for saving the choices
def save_choices():
    choices_list = [choice_1.get(), choice_2.get(), choice_3.get()]
    print("Wybory użytkownika:", choices_list)

#creating main window
tpm_window = tk.Tk()

#setting size of the window
tpm_window.geometry("800x500")

#setting title of the window
tpm_window.title("TPM wytłaczarki")

#create frame for grouping text and buttons
frame = tk.Frame(tpm_window)
frame.pack(padx=10, pady=10)

choice_1 = create_button_ok_nok(frame, what_is_checking="Test 1")
choice_2 = create_button_ok_nok(frame, what_is_checking="Test 2")
choice_3 = create_button_ok_nok(frame, what_is_checking="Test 3")

#buttom "save" for saving choices
save_button = tk.Button(tpm_window, text="Zapisz", command=save_choices, font=('Arial', 16), padx=20, pady=10)
save_button.pack(pady=15)


#showing window
tpm_window.mainloop()