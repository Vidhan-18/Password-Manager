import tkinter as tk
from tkinter import messagebox
from cryptography.fernet import Fernet

# Load the encryption key from the 'key.key' file
def load_key():
    """Load the encryption key."""
    return open("key.key", "rb").read()

# Encrypt the password
def encrypt_password(password, key):
    """Encrypt a password."""
    f = Fernet(key)
    encrypted_password = f.encrypt(password.encode())
    return encrypted_password

# Decrypt the password
def decrypt_password(encrypted_password, key):
    """Decrypt an encrypted password."""
    f = Fernet(key)
    decrypted_password = f.decrypt(encrypted_password).decode()
    return decrypted_password

# Add a password to the storage file
def add_password(service, password, key):
    """Add a new password to the password manager."""
    encrypted_password = encrypt_password(password, key)
    
    with open("passwords.txt", "a") as f:
        f.write(f"{service}|{encrypted_password.decode()}\n")
    
    messagebox.showinfo("Success", f"Password for {service} added successfully!")

# View a password for a given service
def view_password(service, key):
    """View a password for a given service."""
    with open("passwords.txt", "r") as f:
        lines = f.readlines()
        
        for line in lines:
            stored_service, stored_password = line.strip().split("|")
            if stored_service == service:
                decrypted_password = decrypt_password(stored_password.encode(), key)
                return decrypted_password

    messagebox.showwarning("Not Found", f"Service '{service}' not found.")
    return None

# Delete a password for a given service
def delete_password(service):
    """Delete a password for a given service."""
    with open("passwords.txt", "r") as f:
        lines = f.readlines()
    
    # Rewrite the file excluding the service to be deleted
    with open("passwords.txt", "w") as f:
        found = False
        for line in lines:
            stored_service, _ = line.strip().split("|")
            if stored_service != service:
                f.write(line)
            else:
                found = True

    if found:
        messagebox.showinfo("Success", f"Password for {service} deleted successfully!")
    else:
        messagebox.showwarning("Not Found", f"Service '{service}' not found.")

# GUI Functionality
def gui_main():
    # Create the main window
    root = tk.Tk()
    root.title("Password Manager")

    # Load encryption key
    key = load_key()

    # Function to handle adding a password
    def add_password_gui():
        service = service_entry.get()
        password = password_entry.get()
        if service and password:
            add_password(service, password, key)
        else:
            messagebox.showwarning("Input Error", "Please enter both service name and password.")

    # Function to handle viewing a password
    def view_password_gui():
        service = service_entry.get()
        if service:
            password = view_password(service, key)
            if password:
                messagebox.showinfo("Password", f"Password for {service}: {password}")
        else:
            messagebox.showwarning("Input Error", "Please enter the service name.")

    # Function to handle deleting a password
    def delete_password_gui():
        service = service_entry.get()
        if service:
            delete_password(service)
        else:
            messagebox.showwarning("Input Error", "Please enter the service name.")

    # Function to toggle password visibility
    def toggle_password():
        if show_password_var.get():
            password_entry.config(show="")  # Show password
        else:
            password_entry.config(show="*")  # Hide password

    # Create labels and entry widgets
    service_label = tk.Label(root, text="Service Name:")
    service_label.pack(pady=5)
    
    service_entry = tk.Entry(root, width=30)
    service_entry.pack(pady=5)

    password_label = tk.Label(root, text="Password:")
    password_label.pack(pady=5)
    
    password_entry = tk.Entry(root, width=30, show="*")
    password_entry.pack(pady=5)

    # Checkbox to toggle password visibility
    show_password_var = tk.BooleanVar()
    show_password_checkbox = tk.Checkbutton(root, text="Show Password", variable=show_password_var, command=toggle_password)
    show_password_checkbox.pack(pady=5)

    # Create buttons for actions
    add_button = tk.Button(root, text="Add Password", command=add_password_gui)
    add_button.pack(pady=10)

    view_button = tk.Button(root, text="View Password", command=view_password_gui)
    view_button.pack(pady=10)

    # Add Delete Password button
    delete_button = tk.Button(root, text="Delete Password", command=delete_password_gui)
    delete_button.pack(pady=10)

    # Start the GUI event loop
    root.mainloop()

# Start the GUI
if __name__ == "__main__":
    gui_main()
