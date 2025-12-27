import tkinter as tk

# ===== Window =====
window = tk.Tk()
window.title("Currency Converter")
window.geometry("700x500")  # Increased window size
window.configure(bg="skyblue")  # Window background color

# ===== Currency Rates (base: USD) =====
rates = {
    "USD": 1.0,     # United States Dollar
    "BDT": 110.0,   # Bangladeshi Taka
    "INR": 83.0,    # Indian Rupee
    "EUR": 0.92,    # Euro (used in France, Germany, Portugal, etc.)
    "GBP": 0.79,    # British Pound Sterling
    "JPY": 144.0,   # Japanese Yen
    "CAD": 1.36,    # Canadian Dollar
    "AUD": 1.52,    # Australian Dollar
    "PKR": 285.0,   # Pakistani Rupee
    "LKR": 365.0,   # Sri Lankan Rupee
    "CNY": 7.2,     # Chinese Yuan
    "NPR": 133.0,   # Nepalese Rupee
    "BRL": 5.2,     # Brazilian Real
    "ARS": 360.0,   # Argentine Peso
    "KRW": 1420.0,  # South Korean Won
    "RUB": 92.0,    # Russian Ruble
    "UAH": 37.0     # Ukrainian Hryvnia
}

# ===== Functions =====
def convert():
    try:
        amount = float(e1.get())
        from_cur = e2.get().upper()
        to_cur = e3.get().upper()

        if from_cur not in rates or to_cur not in rates:
            result_label.config(text="Sorry, Your Currency Convertion is not possible", fg="red")
            return

        usd_amount = amount / rates[from_cur]
        result = usd_amount * rates[to_cur]

        result_label.config(
            text=f"Your Currency Convertion has Completed\nConverted Currency: {round(result, 2)} {to_cur}\nThank You",
            fg="red"
        )

    except:
        result_label.config(text="Sorry, Your Currency Convertion is not possible", fg="red")

def reset_data():
    e1.delete(0, tk.END)
    e2.delete(0, tk.END)
    e3.delete(0, tk.END)
    result_label.config(text="")

def quit_app():
    window.destroy()

# ===== Labels =====
tk.Label(window, text="Universal Currency Converter", font=("Times New Roman", 28, "bold"), bg="skyblue", fg="red").place(x=30, y=20)
tk.Label(window, text="Amount:", font=("Times New Roman", 20, "bold"), bg="skyblue", fg="red").place(x=60, y=100)
tk.Label(window, text="From Currency:", font=("Times New Roman", 20, "bold"), bg="skyblue", fg="red").place(x=60, y=160)
tk.Label(window, text="To Currency:", font=("Times New Roman", 20, "bold"), bg="skyblue", fg="red").place(x=60, y=220)

# ===== Entries =====
e1 = tk.Entry(window, font=("Arial", 18, "bold"), fg="red")  # Amount
e2 = tk.Entry(window, font=("Arial", 18, "bold"), fg="red")  # From Currency
e3 = tk.Entry(window, font=("Arial", 18, "bold"), fg="red")  # To Currency

e1.place(x=300, y=105, width=220)
e2.place(x=300, y=165, width=220)
e3.place(x=300, y=225, width=220)

# ===== Buttons =====
tk.Button(window, text="Convert", font=("Arial", 18, "bold"), bg="lightgreen", fg="red", bd=5, relief="raised", command=convert).place(x=80, y=290, width=140, height=55)
tk.Button(window, text="Reset", font=("Arial", 18, "bold"), bg="orange", fg="red", bd=5, relief="raised", command=reset_data).place(x=250, y=290, width=140, height=55)
tk.Button(window, text="Quit", font=("Arial", 18, "bold"), bg="red", fg="white", bd=5, relief="raised", command=quit_app).place(x=420, y=290, width=140, height=55)

# ===== Result =====
result_label = tk.Label(window, text="", font=("Times New Roman", 22, "bold"), bg="skyblue", fg="red")
result_label.place(x=60, y=370)

window.mainloop()

"""
USD – United States
BDT – Bangladesh
INR – India
EUR – Eurozone (France, Germany, Portugal, etc.)
GBP – United Kingdom
JPY – Japan
CAD – Canada
AUD – Australia
PKR – Pakistan
LKR – Sri Lanka
CNY – China
NPR – Nepal
BRL – Brazil
ARS – Argentina
KRW – South Korea
RUB – Russia
UAH – Ukraine
"""
