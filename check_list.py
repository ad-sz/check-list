import tkinter as tk
from tkinter import ttk
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
    users = ["Użytkownik 1", "Użytkownik 2", "Użytkownik 3"]
    selected_user = tk.StringVar()
    user_combobox = ttk.Combobox(login_window, textvariable=selected_user, values=users, state="readonly")
    user_combobox.pack(pady=5)
    user_combobox.current(0)

    tk.Button(login_window, text="Zaloguj", command=lambda: on_login(selected_user.get()), font=('Arial', 12)).pack(pady=20)


#function for saving the choices
def save_choices():
    choices_list = [choice_1.get(), choice_2.get(), choice_3.get()]
    print("Wybory użytkownika:", choices_list)


#initialization of the main Tkinter window
tpm_window = tk.Tk()
tpm_window.withdraw()  #hide main window on start

prepare_main_window()  #prepares the main window, but does not display it yet

#showing login user window
show_login_window()

#starting the Tkinter event loop
tpm_window.mainloop()