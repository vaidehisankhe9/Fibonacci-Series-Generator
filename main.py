import tkinter as tk

def generate_fibonacci(n):
    fib_series = [0, 1]
    for i in range(2, n):
        fib_series.append(fib_series[-1] + fib_series[-2])
    return fib_series

def show_fibonacci():
    n = int(entry.get())
    result = generate_fibonacci(n)
    result_label.config(text=f"Fibonacci Series: {result}")


root = tk.Tk()
root.title("Fibonacci Generator")


label = tk.Label(root, text="Enter the number of terms:")
label.pack(pady=10)

entry = tk.Entry(root)
entry.pack(pady=10)

generate_button = tk.Button(root, text="Generate Fibonacci Series", command=show_fibonacci)
generate_button.pack(pady=10)

result_label = tk.Label(root, text="Fibonacci Series: ")
result_label.pack(pady=10)

root.mainloop()
