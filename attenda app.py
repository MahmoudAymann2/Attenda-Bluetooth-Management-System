import tkinter
from tkinter.font import BOLD, Font
from tkinter import ttk
import time
from PIL import ImageTk, Image
import bluetooth
import customtkinter
import csv

customtkinter.set_appearance_mode("dark")

window = tkinter.Tk()
window.title("Attenda | Login")
window.geometry("450x250")
WelcomeText1 = tkinter.Frame()
WelcomeText2 = tkinter.Frame()
LoadingBar = ttk.Progressbar(window,
                             orient="horizontal",
                             length=200,
                             mode="determinate")

label_a = tkinter.Label(master=WelcomeText1,
                        text="Welcome to Attenda",
                        font=("Arial", 30, BOLD))
label_a.pack()

label_b = tkinter.Label(master=WelcomeText2,
                        text="The ultimate Bluetooth Management System",
                        font=("Arial", 10))
label_b.pack()

username_label = tkinter.Label(text="Username:")
username_entry = tkinter.Entry()
password_label = tkinter.Label(text="Password:")
password_entry = tkinter.Entry(show="*")


def login():
    username = username_entry.get()
    password = password_entry.get()
    if username == "test" and password == "test":
        tkinter.Label(text="Login successful!", fg="green").pack()
        tkinter.Button(window, text="Open Attendance System",
                       command=open_win).pack()
    else:
        tkinter.Label(text="Invalid username or password", fg="red").pack()


login_button = customtkinter.CTkButton(master=window,
                                       text="Login",
                                       command=login,
                                       anchor="center")

def open_win():
    device_scans = {}
    LogSucessPage = tkinter.Toplevel(window)
    tree = ttk.Treeview(LogSucessPage, columns=("name", "address", "scan_count"))
    tree.heading("name", text="Name")
    tree.heading("address", text="Address")
    tree.heading("scan_count", text="Scan Count")
    tree.column("name", width=400)
    tree.column("address", width=400)
    tree.column("scan_count", width=400)

    tree.pack()

    def update_devices():
        # Clear existing items from the treeview
        for row in tree.get_children():
            tree.delete(row)

        devices = bluetooth.discover_devices()
        for device in devices:
            name = bluetooth.lookup_name(device)
            # Increment the scan count for this device
            scan_count = device_scans.setdefault(device, 0) + 1
            device_scans[device] = scan_count
            tree.insert("", "end", text=name, values=(name, device, scan_count))

        # Refresh the treeview
        tree.update()

        # Schedule the next update in 5 seconds
        tree.after(5000, update_devices)

        

    # Call the update function to start the device rescanning and update process
    update_devices()

    def export_to_csv():
        # Open the CSV file for writing
        with open("devices.csv", "w", newline="") as csvfile:
            writer = csv.writer(csvfile)

            # Write the column headings
            writer.writerow(["Name", "Address", "Scan Count"])

            # Write the data for each row
            for row in tree.get_children():
                name = tree.item(row)["text"]
                address = tree.item(row)["values"][0]
                scan_count = tree.item(row)["values"][1]
                if scan_count >= 3:
                    writer.writerow([name, address, scan_count])

    export_button = tkinter.Button(LogSucessPage,
                                   text="Export to CSV",
                                   command=export_to_csv)
    export_button.pack()




  

WelcomeText1.pack()
WelcomeText2.pack()
username_label.pack()
username_entry.pack()
password_label.pack()
password_entry.pack()
login_button.pack()

window.mainloop()