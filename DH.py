import tkinter as tk
from tkinter import ttk, messagebox
import time


def calculate_dh():
    try:
        g = int(entry_g.get())
        p = int(entry_p.get())
        a = int(entry_a.get())
        b = int(entry_b.get())

        if g <= 1 or p <= 1 or a < 1 or b < 1:
            messagebox.showerror("Ошибка", "Все числа должны быть больше 1!")
            return

        status_label.config(text="🔄 Вычисление...", foreground="orange")
        root.update()
        time.sleep(0.6)

        # Вычисления
        A = pow(g, a, p)
        B = pow(g, b, p)
        Ka = pow(B, a, p)
        Kb = pow(A, b, p)

        # Анимация появления результатов
        label_A.config(text=f"A (от Алисы) = {A}")
        root.update()
        time.sleep(0.3)

        label_B.config(text=f"B (от Боба) = {B}")
        root.update()
        time.sleep(0.3)

        if Ka == Kb:
            label_K.config(text=f"🔑 Общий секретный ключ K = {Ka}", foreground="#2ecc71")
            status_label.config(text="✅ Ключи успешно совпали!", foreground="#2ecc71")
        else:
            label_K.config(text="❌ Ключи не совпали!", foreground="red")
            status_label.config(text="Ошибка", foreground="red")

    except ValueError:
        messagebox.showerror("Ошибка", "Введите корректные целые числа!")
    except Exception as e:
        messagebox.showerror("Ошибка", f"Произошла ошибка: {e}")


# ====================== ИНТЕРФЕЙС ======================
root = tk.Tk()
root.title("🔑 Протокол Диффи-Хеллмана")
root.geometry("560x680")
root.configure(bg="#2c3e50")

style = ttk.Style()
style.theme_use('clam')

# Заголовок
tk.Label(root, text="🔑 Диффи-Хеллман",
         font=("Helvetica", 20, "bold"), fg="#ecf0f1", bg="#2c3e50").pack(pady=20)

main_frame = ttk.Frame(root, padding=20)
main_frame.pack(fill="both", expand=True)

# Публичные параметры
param_frame = ttk.LabelFrame(main_frame, text=" Публичные параметры ", padding=15)
param_frame.pack(fill="x", pady=10)

ttk.Label(param_frame, text="g (основание):").grid(row=0, column=0, sticky="w", pady=8)
entry_g = ttk.Entry(param_frame, width=25)
entry_g.grid(row=0, column=1, pady=8, padx=10)
entry_g.insert(0, "5")

ttk.Label(param_frame, text="p (простое число):").grid(row=1, column=0, sticky="w", pady=8)
entry_p = ttk.Entry(param_frame, width=25)
entry_p.grid(row=1, column=1, pady=8, padx=10)
entry_p.insert(0, "23")

# Секретные числа
secret_frame = ttk.LabelFrame(main_frame, text=" Секретные числа ", padding=15)
secret_frame.pack(fill="x", pady=10)

ttk.Label(secret_frame, text="a (секрет Алисы):").grid(row=0, column=0, sticky="w", pady=8)
entry_a = ttk.Entry(secret_frame, width=25)
entry_a.grid(row=0, column=1, pady=8, padx=10)
entry_a.insert(0, "6")

ttk.Label(secret_frame, text="b (секрет Боба):").grid(row=1, column=0, sticky="w", pady=8)
entry_b = ttk.Entry(secret_frame, width=25)
entry_b.grid(row=1, column=1, pady=8, padx=10)
entry_b.insert(0, "15")

# Кнопка
ttk.Button(main_frame, text="🔑 Вычислить общий ключ", command=calculate_dh).pack(pady=20)

# Статус
status_label = tk.Label(main_frame, text="Готов к работе",
                        font=("Helvetica", 11), fg="#2ecc71", bg="#2c3e50")
status_label.pack(pady=10)

# Результаты
result_frame = ttk.LabelFrame(main_frame, text=" Результат обмена ", padding=15)
result_frame.pack(fill="x", pady=10)

label_A = tk.Label(result_frame, text="A = ", font=("Courier", 12), bg="#34495e", fg="white", width=50)
label_A.pack(pady=8)

label_B = tk.Label(result_frame, text="B = ", font=("Courier", 12), bg="#34495e", fg="white", width=50)
label_B.pack(pady=8)

label_K = tk.Label(result_frame, text="Общий ключ K = ",
                   font=("Helvetica", 14, "bold"), bg="#2c3e50", fg="#f1c40f")
label_K.pack(pady=15)

# Подсказка
tk.Label(main_frame, text="💡 Пример: g=5, p=23, a=6, b=15",
         font=("Helvetica", 10), fg="#95a5a6", bg="#2c3e50").pack(pady=10)

root.mainloop()