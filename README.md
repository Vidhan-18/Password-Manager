# Password Manager

A simple password manager built with Python, Tkinter, and Cryptography. This application allows users to securely store and manage their passwords. It supports encryption/decryption, password visibility toggle (show/hide), and the ability to delete saved passwords.

## Features
- **Secure Password Storage**: Passwords are encrypted using the `cryptography` library and saved in a text file.
- **Show/Hide Password**: Toggle between showing and hiding the password using the "Show Password" checkbox.
- **Delete Password**: Option to delete passwords associated with a specific service.
- **Cross-platform**: Works on Windows, macOS, and Linux (provided you have Python installed).

## Installation

### Prerequisites
- **Python 3.x**: Make sure you have Python installed. You can download Python from [here](https://www.python.org/downloads/).
- **Libraries**: This project requires the following Python libraries:
  - `tkinter` (comes pre-installed with Python).
  - `cryptography` (for password encryption).

### Steps to Install
1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/yourusername/password-manager.git
    cd password-manager
    ```

2. (Optional) Set up a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required Python libraries:

    ```bash
    pip install cryptography
    ```

4. **Create the `key.key` file**:
   - Run the script once to generate the encryption key file:
     ```bash
     python password_manager.py
     ```
   - This will generate the `key.key` file needed for encryption/decryption.
   - Keep the `key.key` file safe and **do not commit it to version control** (it contains your encryption key).

## Usage

1. **Run the application**:
   - Open a terminal or command prompt, navigate to the project directory, and run the script:

     ```bash
     python password_manager.py
     ```

2. **Add a Password**:
   - Enter a **service name** (e.g., "Gmail") and a **password**.
   - Click **Add Password** to save the encrypted password.

3. **View a Password**:
   - Enter the **service name** (e.g., "Gmail").
   - Click **View Password** to see the decrypted password.

4. **Delete a Password**:
   - Enter the **service name** and click **Delete Password** to remove that entry from the list.

5. **Show/Hide Password**:
   - You can toggle password visibility by checking the "Show Password" checkbox.

## How It Works

- **Encryption**: The passwords are encrypted using the `cryptography` library (Fernet symmetric encryption) before being saved in the `passwords.txt` file.
- **Password Storage**: Passwords are saved in `passwords.txt` in an encrypted format. The file contains lines with each service and its corresponding encrypted password.
- **Key Management**: The encryption key is stored in `key.key`. **Make sure to keep this key safe**. If the key is lost, you will not be able to decrypt the saved passwords.

## Security Considerations
- **Do not share your `key.key` file**. If someone gains access to this file, they can decrypt all stored passwords.
- The `passwords.txt` file contains **encrypted** passwords, but if someone gains access to both the `passwords.txt` and `key.key` files, they can decrypt the passwords.
