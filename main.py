import tkinter as tk
from tkinter import ttk, messagebox

# ------------------------------
# Core Calculation Logic
# ------------------------------
def compound_interest(principal, rate, years, freq, contribution=0):
    """Calculate compound interest with optional contributions."""
    amount = principal * (1 + rate / freq) ** (freq * years)
    if contribution > 0:
        amount += contribution * (((1 + rate / freq) ** (freq * years) - 1) / (rate / freq))
    return amount

# ------------------------------
# UI Functions
# ------------------------------
def calculate():
    try:
        principal = float(entry_investment.get())
        rate = float(entry_rate.get()) / 100
        years = float(entry_years.get())
        contribution = float(entry_contribution.get() or 0)
        freq = freq_options[compound_var.get()]

        # Final amount
        amount = compound_interest(principal, rate, years, freq, contribution)
        interest = amount - (principal + contribution * years * freq)

        # Update result label
        result_var.set(
            f"Final Balance: {currency_var.get()} {amount:,.2f}\n"
            f"Principal + Contributions: {currency_var.get()} {principal + contribution * years * freq:,.2f}\n"
            f"Interest Earned: {currency_var.get()} {interest:,.2f}"
        )

        # Update chart
        draw_chart(principal, rate, years, freq, contribution)

    except ValueError:
        messagebox.showerror(title="Error", message="Please enter valid numbers.")

def clear_fields():
    entry_investment.delete(0, tk.END)
    entry_rate.delete(0, tk.END)
    entry_years.delete(0, tk.END)
    entry_contribution.delete(0, tk.END)
    result_var.set("")
    chart_canvas.delete("all")

# ------------------------------
# Canvas Chart Functions
# ------------------------------
def draw_chart(principal, rate, years, freq, contribution):
    chart_canvas.delete("all")

    width = int(chart_canvas['width'])
    height = int(chart_canvas['height'])
    margin = 40

    # Prepare data points
    points = []
    max_value = 0
    for year in range(1, int(years)+1):
        value = compound_interest(principal, rate, year, freq, contribution)
        points.append((year, value))
        if value > max_value:
            max_value = value

    # Scaling functions
    def x_coord(year): return margin + (year / years) * (width - 2*margin)
    def y_coord(value): return height - margin - (value / max_value) * (height - 2*margin)

    # Draw axes
    chart_canvas.create_line(margin, margin, margin, height-margin, width=2)  # y-axis
    chart_canvas.create_line(margin, height-margin, width-margin, height-margin, width=2)  # x-axis
    chart_canvas.create_text(margin/2, margin, text="Balance", anchor="w")
    chart_canvas.create_text(width-margin, height-margin+15, text="Years", anchor="n")

    # Draw line
    for i in range(len(points)-1):
        x1, y1 = x_coord(points[i][0]), y_coord(points[i][1])
        x2, y2 = x_coord(points[i+1][0]), y_coord(points[i+1][1])
        chart_canvas.create_line(x1, y1, x2, y2, fill="blue", width=2)

    # Draw points
    for x, y_val in points:
        cx, cy = x_coord(x), y_coord(y_val)
        chart_canvas.create_oval(cx-3, cy-3, cx+3, cy+3, fill="red")

# ------------------------------
# Tkinter App Setup
# ------------------------------
app = tk.Tk()
app.title("💰 Compound Interest Calculator")
app.geometry("900x800")
app.columnconfigure(0, weight=1)

main_frame = ttk.Frame(app, padding=10)
main_frame.grid(sticky="nsew")
main_frame.columnconfigure(0, weight=1)

# Title
ttk.Label(main_frame, text="Compound Interest Calculator", font=("Calibre", 16, "bold")).grid(row=0, column=0, pady=10)

# Currency
currency_var = tk.StringVar(value="$")
currency_frame = ttk.Frame(main_frame)
currency_frame.grid(row=1, column=0, pady=5, sticky="w")
ttk.Label(currency_frame, text="Currency:").grid(row=0, column=0, sticky="w")
for i, cur in enumerate(["$", "€", "£"], start=1):
    ttk.Radiobutton(currency_frame, text=cur, variable=currency_var, value=cur).grid(row=0, column=i, padx=2)

# Investment Details
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

ttk.Label(details_frame, text="Monthly Contribution (optional):").grid(row=3, column=0, sticky="w")
entry_contribution = ttk.Entry(details_frame)
entry_contribution.grid(row=3, column=1, sticky="ew", pady=2)

# Compound Frequency
ttk.Label(details_frame, text="Compound Frequency:").grid(row=4, column=0, sticky="w")
compound_var = tk.StringVar(value="Monthly")
freq_options = {
    "Daily": 365,
    "Weekly": 52,
    "Monthly": 12,
    "Quarterly": 4,
    "Semi-Annually": 2,
    "Annually": 1
}
freq_frame = ttk.Frame(details_frame)
freq_frame.grid(row=4, column=1, sticky="w")
for i, freq in enumerate(freq_options):
    ttk.Radiobutton(freq_frame, text=freq, variable=compound_var, value=freq).grid(row=0, column=i, padx=2)

# Buttons
buttons_frame = ttk.Frame(main_frame)
buttons_frame.grid(row=3, column=0, pady=10)
ttk.Button(buttons_frame, text="Calculate", command=calculate).grid(row=0, column=0, padx=5)
ttk.Button(buttons_frame, text="Clear", command=clear_fields).grid(row=0, column=1, padx=5)

# Result
result_var = tk.StringVar()
result_frame = ttk.LabelFrame(main_frame, text="Result", padding=10)
result_frame.grid(row=4, column=0, sticky="ew", padx=10, pady=10)
ttk.Label(result_frame, textvariable=result_var, font=("Arial", 12), justify="left").grid(row=0, column=0, sticky="w")

# Chart Canvas
chart_frame = ttk.LabelFrame(main_frame, text="Growth Chart", padding=10)
chart_frame.grid(row=5, column=0, sticky="nsew", padx=10, pady=10)
chart_canvas = tk.Canvas(chart_frame, width=550, height=300, bg="white")
chart_canvas.pack(fill="both", expand=True)

app.mainloop()
