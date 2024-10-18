import tkinter as tk

def on_click(key):
    current = display_var.get()
    if key == "=":
        try:
            result = eval(current)
            display_var.set(result)
        except Exception as e:
            display_var.set("Error")
    elif key == "C":
        display_var.set("")
    else:
        display_var.set(current + key)

def create_button(root, text, row, column, width=7, height=3):
    button = tk.Button(root, text=text, command=lambda: on_click(text), bg="blue", fg="white", font=("Arial", 16),
                       width=width, height=height, bd=4)
    button.grid(row=row, column=column, padx=5, pady=5)
    return button

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Teclado")
    root.geometry("400x600")

    display_var = tk.StringVar()
    display_var.set("")

    display = tk.Entry(root, textvariable=display_var, font=("Arial", 20), bd=10, relief="ridge", bg="black", fg="white",
                       justify="right")
    display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

    # Crear botones numéricos
    for i in range(10):
        create_button(root, str(i), 1 + i // 3, i % 3)

    # Crear botones de operaciones
    create_button(root, "/", 4, 3)
    create_button(root, "*", 3, 3)
    create_button(root, "-", 2, 3)
    create_button(root, "+", 1, 3)
    create_button(root, ".", 4, 1)

    # Botones de letras
    letters = ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P",
               "A", "S", "D", "F", "G", "H", "J", "K", "L",
               "Z", "X", "C", "V", "B", "N", "M"]
    row = 2
    column = 0
    for letter in letters:
        create_button(root, letter, row, column)
        column += 1
        if column > 8:
            column = 0
            row += 1

    create_button(root, "=", 5, 2, 15, 2)
    create_button(root, "C", 5, 0, 15, 2)

    root.mainloop()
