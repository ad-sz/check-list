import tkinter as tk
from tkinter import ttk
import csv
from buttons import create_button_ok_nok

#function for preparing main window
def prepare_main_window():
    #setting size of the window
    tpm_window.geometry("800x500")
    #setting title of the window
    tpm_window.title("TPM wytłaczarki")
    
    #create frame for grouping text and buttons
    frame = tk.Frame(tpm_window)
    frame.pack(padx=10, pady=10)

    global choice_1, choice_2, choice_3
    choice_1 = create_button_ok_nok(frame, what_is_checking="Test 1")
    choice_2 = create_button_ok_nok(frame, what_is_checking="Test 2")
    choice_3 = create_button_ok_nok(frame, what_is_checking="Test 3")

    #buttom "save" for saving choices
    save_button = tk.Button(tpm_window, text="Zapisz", command=save_choices, font=('Arial', 16), padx=20, pady=10)
    save_button.pack(pady=15)

#function called after login that shows the main window
def on_login(username):
    login_window.destroy()
    tpm_window.deiconify() #showing main window after login

#function showing login window
def show_login_window():
    global login_window
    login_window = tk.Toplevel(tpm_window)
    login_window.title("Logowanie")

    tk.Label(login_window, text="Wybierz użytkownika:", font=('Arial', 12)).pack(pady=10)

    #create users list
    users = ["Adam Nowak", "Jan Kowalski", "Adam Ul"]
    global selected_user
    selected_user = tk.StringVar()
    user_combobox = ttk.Combobox(login_window, textvariable=selected_user, values=users, state="readonly")
    user_combobox.pack(pady=5)
    user_combobox.current(0)

    tk.Button(login_window, text="Zaloguj", command=lambda: on_login(selected_user.get()), font=('Arial', 12)).pack(pady=20)


#function for saving the choices
def save_choices():
    choices_list = [selected_user.get().lower(), choice_1.get(), choice_2.get(), choice_3.get()]
    filename = "D:/python_data/projekt/check_lista/check-list/records.csv"
    with open(filename, mode="a", newline="") as records_csv:
        new_records_csv = csv.writer(records_csv, delimiter=";")
        new_records_csv.writerow(choices_list)

    #only for checking if saving works
    print("Wybory użytkownika:", choices_list)

    #hide main window(logging out after put "save" button)
    tpm_window.withdraw()

    #reset variables in aplication
    reset_app_state()

    #showilng loggin window again
    show_login_window()


#function for reset aplication
def reset_app_state():
    global selected_user, choice_1, choice_2, choice_3
    selected_user.set("")
    choice_1.set("")
    choice_2.set("")
    choice_3.set("")


#initialization of the main Tkinter window
tpm_window = tk.Tk()
tpm_window.withdraw()  #hide main window on start

prepare_main_window()  #prepares the main window, but does not display it yet

#showing login user window
show_login_window()

#starting the Tkinter event loop
tpm_window.mainloop()