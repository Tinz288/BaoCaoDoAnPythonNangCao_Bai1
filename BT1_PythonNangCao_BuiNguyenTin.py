import tkinter as tk
from tkinter import messagebox

history = []

def calculate(operation):
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())

        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 == 0:
                raise ZeroDivisionError("Không thể chia cho 0.")
            result = num1 / num2
        else:
            raise ValueError("Phép tính không hợp lệ.")

        label_result.config(text=f"Kết quả: {result}")

        history.append(f"{num1} {operation} {num2} = {result}")
    except ZeroDivisionError as e:
        messagebox.showerror("Lỗi", str(e))
    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập số hợp lệ.")

def show_history():
    """Hàm hiển thị lịch sử tính toán"""
    if not history:
        messagebox.showinfo("Lịch sử", "Chưa có phép tính nào được thực hiện.")
    else:
        history_str = "\n".join(history)
        messagebox.showinfo("Lịch sử", f"Lịch sử tính toán:\n{history_str}")


window = tk.Tk()
window.title("Máy tính")


tk.Label(window, text="Số thứ nhất:").grid(row=0, column=0, padx=10, pady=5)
entry_num1 = tk.Entry(window)
entry_num1.grid(row=0, column=1, padx=10, pady=5)

tk.Label(window, text="Số thứ hai:").grid(row=1, column=0, padx=10, pady=5)
entry_num2 = tk.Entry(window)
entry_num2.grid(row=1, column=1, padx=10, pady=5)

tk.Button(window, text="Cộng (+)", command=lambda: calculate("+")).grid(row=2, column=0, padx=10, pady=5)
tk.Button(window, text="Trừ (-)", command=lambda: calculate("-")).grid(row=2, column=1, padx=10, pady=5)
tk.Button(window, text="Nhân (*)", command=lambda: calculate("*")).grid(row=3, column=0, padx=10, pady=5)
tk.Button(window, text="Chia (/)", command=lambda: calculate("/")).grid(row=3, column=1, padx=10, pady=5)

tk.Button(window, text="Xem lịch sử", command=show_history).grid(row=4, column=0, columnspan=2, pady=10)

label_result = tk.Label(window, text="Kết quả: ")
label_result.grid(row=5, column=0, columnspan=2, pady=10)

window.mainloop()