import tkinter as tk
import bluetooth
import time

def open_window():
    # Create a new window
    new_window = tk.Toplevel(window)
    new_window.title("Bluetooth Devices")

    # Create a label to display the output
    output_label = tk.Label(new_window, text="", font=("Arial", 12))
    output_label.pack()

    # Create a counter to track the number of updates
    update_count = 5

    def update_output():
        global update_count
        # Discover nearby devices
        nearby_devices = bluetooth.discover_devices(lookup_names=True, flush_cache=True)
        output = "Update #{}\nFound {} devices:\n".format(5 - update_count + 1, len(nearby_devices))
        for addr, name in nearby_devices:
            output += "  {} - {}\n".format(addr, name)
        # Update the label with the output
        output_label.config(text=output)
        # Decrement the update counter
        update_count -= 1
        # Schedule the next update if there are more updates remaining
        if update_count > 0:
            new_window.after(30000, update_output)

    # Schedule the first update
    new_window.after(0,update_output)

# Create the main window
window = tk.Tk()
window.title("Main Window")

# Create a button to open the new window
open_button = tk.Button(window, text="Open Bluetooth Window", command=open_window)
open_button.pack()

# Run the main loop
window.mainloop()