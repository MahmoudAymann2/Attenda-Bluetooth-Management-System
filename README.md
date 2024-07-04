# Attenda-Bluetooth-Management-System
Welcome to Attenda, the ultimate Bluetooth Management System designed to simplify attendance tracking through seamless Bluetooth device discovery and management. This desktop application provides a user-friendly interface for logging in, scanning for Bluetooth devices, and exporting the collected data to a CSV file.

Features

User Authentication: A simple login screen for user authentication.
Bluetooth Device Scanning: Automatically discovers nearby Bluetooth devices and displays them in a structured treeview.
Real-time Updates: Continuously updates the list of discovered Bluetooth devices every 5 seconds.
Data Export: Allows users to export the list of discovered devices and their scan counts to a CSV file.
Customizable UI: Dark mode appearance using CustomTkinter.

Project Structure

main.py: The main script that initializes the application, handles user login, and opens the attendance system window.
Dependencies:
tkinter: For creating the GUI components.
ttk: For enhanced widget styling.
customtkinter: For custom-themed widgets.
bluetooth: For discovering Bluetooth devices.
csv: For exporting data to CSV files.

Usage

Login: Start the application and log in using the provided credentials (default: username: test, password: test).
Discover Devices: After a successful login, open the attendance system window to start discovering nearby Bluetooth devices.
Export Data: Click on the "Export to CSV" button to save the list of discovered devices with their scan counts to a CSV file.

Contributing
We welcome contributions to improve Attenda. If you'd like to contribute, please follow these steps:

1)Fork the repository.
2)Create a new branch (git checkout -b feature-branch).
3)Commit your changes (git commit -m 'Add some feature').
4)Push to the branch (git push origin feature-branch).
5)Open a pull request.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgements
Special thanks to the developers of the tkinter, customtkinter, and bluetooth libraries for making this project possible.


