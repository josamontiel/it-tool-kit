#!/usr/bin/env python3

import string
import secrets
import tkinter as tk
from tkinter import ttk

def generate_password(length, include_uppercase, include_lowercase,
                      include_numbers, include_special_characters):
    """Generate a random password.

    Args:
        length (int): The length of the password.
        include_uppercase (bool): Whether to include uppercase letters.
        include_lowercase (bool): Whether to include lowercase letters.
        include_numbers (bool): Whether to include digits.
        include_special_characters (bool): Whether to include special characters.

    Returns:
        str: The generated password.
    """
    alphabet = ""
    if include_uppercase:
        alphabet += string.ascii_uppercase
    if include_lowercase:
        alphabet += string.ascii_lowercase
    if include_numbers:
        alphabet += string.digits
    if include_special_characters:
        alphabet += string.punctuation

    password = "".join(secrets.choice(alphabet) for _ in range(length))
    return password


def main():
    root = tk.Tk()
    root.title("Password Generator")

    length_label = ttk.Label(root, text="Length:")
    length_label.pack(padx=10, pady=10)

    length_spinbox = tk.Spinbox(root, from_=4, to=32, width=5)
    length_spinbox.pack(padx=10, pady=10)
    length_spinbox.delete(0, tk.END)
    length_spinbox.insert(0, "12")

    uppercase_var = tk.BooleanVar(value=True)
    uppercase_checkbutton = ttk.Checkbutton(
        root, text="Uppercase", variable=uppercase_var
    )
    uppercase_checkbutton.pack(padx=10, pady=5)

    lowercase_var = tk.BooleanVar(value=True)
    lowercase_checkbutton = ttk.Checkbutton(
        root, text="Lowercase", variable=lowercase_var
    )
    lowercase_checkbutton.pack(padx=10, pady=5)

    numbers_var = tk.BooleanVar(value=True)
    numbers_checkbutton = ttk.Checkbutton(
        root, text="Numbers", variable=numbers_var
    )
    numbers_checkbutton.pack(padx=10, pady=5)

    special_characters_var = tk.BooleanVar(value=False)
    special_characters_checkbutton = ttk.Checkbutton(
        root, text="Special Characters", variable=special_characters_var
    )
    special_characters_checkbutton.pack(padx=10, pady=5)

    generate_button = ttk.Button(root, text="Generate Password")
    generate_button.pack(padx=10, pady=10)

    password_label = ttk.Label(root, text="Click the button to generate a password.")
    password_label.pack(padx=10, pady=10)

    def generate_password_handler():
        """Generate a password and display it in a new window."""
        length = int(length_spinbox.get())
        include_uppercase = uppercase_var.get()
        include_lowercase = lowercase_var.get()
        include_numbers = numbers_var.get()
        include_special_characters = special_characters_var.get()

        password = generate_password(
        length,
        include_uppercase,
        include_lowercase,
        include_numbers,
        include_special_characters,
        )

        # Create a new window to display the generated password
        password_window = tk.Toplevel(root)
        password_window.title("Generated Password")

        # Create a label to display the generated password
        password_label = ttk.Label(password_window, text=password)
        password_label.pack(padx=10, pady=10)

        # Create a "Copy Password" button
        def copy_password():
            root.clipboard_clear()
            root.clipboard_append(password)

        copy_button = ttk.Button(password_window, text="Copy Password", command=copy_password)
        copy_button.pack(padx=10, pady=10)


    generate_button.config(command=generate_password_handler)

    root.mainloop()


if __name__ == "__main__":
    main()
