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
    button = tk.Button(root, text=text, command=lambda: on_click(text), width=width, height=height)
    button.grid(row=row, column=column, padx=5, pady=5)
    return button

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Calculadora")

    display_var = tk.StringVar()
    display_var.set("")

    display = tk.Entry(root, textvariable=display_var, font=("Arial", 20), bd=10, relief="ridge", justify="right")
    display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

    create_button(root, "7", 1, 0)
    create_button(root, "8", 1, 1)
    create_button(root, "9", 1, 2)
    create_button(root, "/", 1, 3)

    create_button(root, "4", 2, 0)
    create_button(root, "5", 2, 1)
    create_button(root, "6", 2, 2)
    create_button(root, "*", 2, 3)

    create_button(root, "1", 3, 0)
    create_button(root, "2", 3, 1)
    create_button(root, "3", 3, 2)
    create_button(root, "-", 3, 3)

    create_button(root, "0", 4, 0)
    create_button(root, ".", 4, 1)
    create_button(root, "=", 4, 2)
    create_button(root, "+", 4, 3)

    create_button(root, "C", 5, 0, 15, 2)

    root.mainloop()
