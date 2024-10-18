import tkinter as tk

def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                encrypted_text += chr((ord(char) - 65 + shift) % 26 + 65)
            else:
                encrypted_text += chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            encrypted_text += char
    return encrypted_text

def on_encrypt():
    text = entry_text.get()
    shift = int(entry_shift.get())
    encrypted_text = encrypt(text, shift)
    result_var.set(encrypted_text)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Encriptador de Palabras")

    label_text = tk.Label(root, text="Texto:")
    label_text.grid(row=0, column=0, padx=5, pady=5)

    entry_text = tk.Entry(root)
    entry_text.grid(row=0, column=1, padx=5, pady=5)

    label_shift = tk.Label(root, text="Desplazamiento:")
    label_shift.grid(row=1, column=0, padx=5, pady=5)

    entry_shift = tk.Entry(root)
    entry_shift.grid(row=1, column=1, padx=5, pady=5)

    encrypt_button = tk.Button(root, text="Encriptar", command=on_encrypt)
    encrypt_button.grid(row=2, column=0, columnspan=2, padx=5, pady=10)

    result_var = tk.StringVar()
    result_label = tk.Label(root, textvariable=result_var, wraplength=250, justify="left", font=("Arial", 12))
    result_label.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

    root.mainloop()
