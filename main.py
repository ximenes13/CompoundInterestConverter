import tkinter as tk
from tkinter import ttk, messagebox

def Calculate():
    try:
        principal = float(entry_investment.get())
        rate = float(entry_rate.get()) / 100
        years = float(entry_years.get())
        freq = freq_options[compound_var.get()]

        amount = principal * (1 + rate / freq) ** (freq * years)
        result_var.set(f"{currency_var.get()} {amount:.2f}")
    except ValueError:
        messagebox.showerror(title="Error", message="Please enter a number.")

def clear_fields():
    entry_investment.delete(0, tk.END)
    entry_rate.delete(0, tk.END)
    entry_years.delete(0, tk.END)
    result_var.set("")

# App setup
app = tk.Tk()
app.title("💰 Compound Interest Calculator")
app.geometry("500x450")
app.columnconfigure(0, weight=1)

# Main frame
main_frame = ttk.Frame(app, padding=10)
main_frame.grid(sticky="nsew")
main_frame.columnconfigure(0, weight=1)

# Title
ttk.Label(main_frame, text="Compound Interest", font=("Calibre", 16, "bold")).grid(row=0, column=0, pady=10)

# Currency selection
currency_var = tk.StringVar(value="$")
currency_frame = ttk.Frame(main_frame)
currency_frame.grid(row=1, column=0, pady=5, sticky="w")
ttk.Label(currency_frame, text="Currency:").grid(row=0, column=0, sticky="w")
for i, cur in enumerate(["$", "€", "£"], start=1):
    ttk.Radiobutton(currency_frame, text=cur, variable=currency_var, value=cur).grid(row=0, column=i, padx=2)

# Investment details
details_frame = ttk.LabelFrame(main_frame, text="Investment Details", padding=10)
details_frame.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")
details_frame.columnconfigure(1, weight=1)

ttk.Label(details_frame, text="Initial Investment:").grid(row=0, column=0, sticky="w")
entry_investment = ttk.Entry(details_frame)
entry_investment.grid(row=0, column=1, sticky="ew", pady=2)

ttk.Label(details_frame, text="Interest Rate (%):").grid(row=1, column=0, sticky="w")
entry_rate = ttk.Entry(details_frame)
entry_rate.grid(row=1, column=1, sticky="ew", pady=2)

ttk.Label(details_frame, text="Time (Years):").grid(row=2, column=0, sticky="w")
entry_years = ttk.Entry(details_frame)
entry_years.grid(row=2, column=1, sticky="ew", pady=2)

ttk.Label(details_frame, text="Compound Frequency:").grid(row=3, column=0, sticky="w")
compound_var = tk.StringVar(value="Monthly")
freq_options = {"Daily": 365, "Monthly": 12, "Annually": 1}

freq_frame = ttk.Frame(details_frame)
freq_frame.grid(row=3, column=1, sticky="w")
for i, freq in enumerate(freq_options):
    ttk.Radiobutton(freq_frame, text=freq, variable=compound_var, value=freq).grid(row=0, column=i, padx=2)

# Buttons frame
buttons_frame = ttk.Frame(main_frame)
buttons_frame.grid(row=3, column=0, pady=10)
ttk.Button(buttons_frame, text="Calculate", command=Calculate).grid(row=0, column=0, padx=5)
ttk.Button(buttons_frame, text="Clear", command=clear_fields).grid(row=0, column=1, padx=5)

# Result label
result_var = tk.StringVar()
ttk.Label(main_frame, text="Result:").grid(row=4, column=0, sticky="w", pady=(10, 0))
ttk.Label(main_frame, textvariable=result_var, font=("Arial", 14)).grid(row=5, column=0, sticky="w")

app.mainloop()
