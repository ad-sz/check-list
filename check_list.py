import tkinter as tk
from tkinter import ttk

# Przygotowanie funkcji dla głównego okna, ale jeszcze bez jego wyświetlania
def prepare_main_window():
    # Ustawienie rozmiaru okna, tytułu itd.
    root.geometry("800x500")
    root.title("TPM wytłaczarki")

    # Tworzenie ramki i elementów w głównym oknie
    frame = tk.Frame(root)
    frame.pack(padx=10, pady=10)

    # Przykładowe wywołanie funkcji tworzącej przyciski (tutaj tylko placeholder)
    # choice_1 = create_button_ok_nok(frame, what_is_checking="Test 1")
    # Powtórzyć dla choice_2 i choice_3

    # Przycisk "Zapisz" do zapisywania wyborów
    save_button = tk.Button(root, text="Zapisz", command=save_choices, font=('Arial', 16), padx=20, pady=10)
    save_button.pack(pady=15)

# Funkcja wywołana po zalogowaniu się, która pokazuje główne okno
def on_login(username):
    login_window.destroy()
    root.deiconify()  # Pokazuje główne okno po zalogowaniu

# Funkcja pokazująca okno logowania
def show_login_window():
    global login_window
    login_window = tk.Toplevel(root)
    login_window.title("Logowanie")

    tk.Label(login_window, text="Wybierz użytkownika:", font=('Arial', 12)).pack(pady=10)

    # Lista użytkowników
    users = ["Użytkownik 1", "Użytkownik 2", "Użytkownik 3"]
    selected_user = tk.StringVar()
    user_combobox = ttk.Combobox(login_window, textvariable=selected_user, values=users, state="readonly")
    user_combobox.pack(pady=5)
    user_combobox.current(0)

    tk.Button(login_window, text="Zaloguj", command=lambda: on_login(selected_user.get()), font=('Arial', 12)).pack(pady=20)

# Funkcja do zapisywania wyborów użytkownika (jako placeholder)
def save_choices():
    # Tutaj logika zapisywania wyborów
    print("Wybory użytkownika zapisane.")

# Inicjalizacja głównego okna Tkinter
root = tk.Tk()
root.withdraw()  # Ukrywa główne okno na start

prepare_main_window()  # Przygotowuje główne okno, ale jeszcze nie wyświetla

# Pokazuje okno logowania
show_login_window()

# Rozpoczęcie pętli zdarzeń Tkinter
root.mainloop()


# import tkinter as tk
# from buttons import create_button_ok_nok

# #function for saving the choices
# def save_choices():
#     choices_list = [choice_1.get(), choice_2.get(), choice_3.get()]
#     print("Wybory użytkownika:", choices_list)

# #creating main window
# tpm_window = tk.Tk()

# #setting size of the window
# tpm_window.geometry("800x500")

# #setting title of the window
# tpm_window.title("TPM wytłaczarki")

# #create frame for grouping text and buttons
# frame = tk.Frame(tpm_window)
# frame.pack(padx=10, pady=10)

# choice_1 = create_button_ok_nok(frame, what_is_checking="Test 1")
# choice_2 = create_button_ok_nok(frame, what_is_checking="Test 2")
# choice_3 = create_button_ok_nok(frame, what_is_checking="Test 3")

# #buttom "save" for saving choices
# save_button = tk.Button(tpm_window, text="Zapisz", command=save_choices, font=('Arial', 16), padx=20, pady=10)
# save_button.pack(pady=15)


# #showing window
# tpm_window.mainloop()