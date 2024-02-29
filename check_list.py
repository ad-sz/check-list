import tkinter as tk
from tkinter import ttk
from tkinter import Canvas, Scrollbar, Frame
import csv
import tkinter.messagebox
from PIL import Image, ImageTk
from buttons import create_button_ok_nok

#function for verify user
def verify_user(barcode):   #variable "barcode" store scanned user's barcode for logging
    try:   #using "try" method for checking if file can be opened
        with open('D:/python_data/projekt/check_lista/check-list/users.csv', mode='r') as users_csv:   #open csv file with user's id with mode for reading (mode='r')
            reader = csv.DictReader(users_csv, delimiter=';')   #csv.DictReade convert every row in dict
            for row in reader:
                if row['id'] == barcode:   #searching user's id according to scanned barcode
                    return row['name'], row['surname']   #if user's id is found, function return tuple name and surname of the user
    except Exception as e:
        print(f"Wystąpił wyjątek: {e}")
    return None, None   #if user's id is not found, function return tuple None, None

#function for using mouse scroll
def on_mousewheel(event):
    canvas.yview_scroll(int(-1*(event.delta/120)), "units")

#function for preparing main window
def prepare_main_window():
    tpm_window.geometry("480x600")   #setting size of the window
    tpm_window.title("TPM wytłaczarki")   #setting title of the window

    #create canvas and scrollbar
    global canvas
    canvas = Canvas(tpm_window)
    scrollbar = Scrollbar(tpm_window, orient='vertical', command=canvas.yview, width=40)

    #packing canvas and scrollbar
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(30, 20))
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    #canvas configuration
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    
    #create frame inside canvas where elements can be add
    frame = Frame(canvas)

    #adding frame to canvas window
    canvas.create_window((0, 0), window=frame, anchor="nw")

    #create variables storing the user's choices as global 
    global choice_1, choice_2, choice_3

    #variables for storing choices of the user, create radiobuttons by using function
    choice_1 = create_button_ok_nok(frame, what_is_checking="Test 1", image_file_path='D:/python_data/projekt/check_lista/check-list/sample_1.jpg')
    choice_2 = create_button_ok_nok(frame, what_is_checking="Test 2", image_file_path='D:/python_data/projekt/check_lista/check-list/sample_2.jpg')
    choice_3 = create_button_ok_nok(frame, what_is_checking="Test 3", image_file_path='D:/python_data/projekt/check_lista/check-list/sample_3.jpg')

    #buttom "save" for saving choices
    save_button = tk.Button(frame, text="Zapisz", command=save_choices, font=('Arial', 16), padx=25, pady=15)
    save_button.pack(pady=15)

    #assigning mouse scroll event
    tpm_window.bind_all("<MouseWheel>", on_mousewheel)

#function called after login that shows the main window
def on_login(barcode): 
    global current_user_name, current_user_surname   #create variables storing the user's name and surname as global
    current_user_name = ""
    current_user_surname = ""
    name, surname = verify_user(barcode)   #variable for storage user's name and surname after veryfication
    if name and surname:   #checking the result of the user veryfication
        current_user_name = name   #if veryfication is correct, assigns name value to global variable 
        current_user_surname = surname   #if veryfication is correct, assigns name value to global variable
        login_window.destroy()   #closing login window
        tpm_window.deiconify()   #showing main window after logging
    else:
        tk.messagebox.showerror("Błąd", "Brak użytkownika")   #if user's id is not found, showing error
        barcode_entry.delete(0, tk.END)    #cleaning field for entering barcode
        barcode_entry.focus()    #set focus on field for entering barcode

#function showing login window
def show_login_window():
    global login_window   #create global variable for storage login window references
    login_window = tk.Toplevel(tpm_window)   #create login window which is subordinate to the main window
    login_window.title("Logowanie")   #setting title of the login window

    tk.Label(login_window, text="Zeskanuj kod kreskowy w celu zalogowania", font=('Arial', 12)).pack(pady=10)   #putting label on window regarding what user should do

    #create field to introduce bar code
    global barcode_entry   #create global variable for storage login field references
    barcode_entry = tk.Entry(login_window, font=('Arial', 12))   #create field for entering barcode
    barcode_entry.pack(pady=5)
    barcode_entry.focus_force()   #set focus on field for entering barcode 

    #create button for logging
    tk.Button(login_window, text="Zaloguj", command=lambda: on_login(barcode_entry.get()), font=('Arial', 12)).pack(pady=20)

    #auxiliary function which is invoked when the "enter" key is pressed
    def on_barcode_scan(event):
        username = barcode_entry.get()
        #only for checking if scanning works
        print(f"Zeskanowano kod: {username}")
        #forward scanning value to login function
        on_login(username)

    #after entering the barcode and pressing 'enter' key, the login process is automatically initiated
    barcode_entry.bind("<Return>", on_barcode_scan)

#function for saving the choices
def save_choices():
    choices_list = [current_user_name, current_user_surname, choice_1.get(), choice_2.get(), choice_3.get()]
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
    global choice_1, choice_2, choice_3
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