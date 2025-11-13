# 💰 Compound Interest Calculator App with Python + Tkinter

This project is a simple desktop application built using Python and Tkinter. It allows users to calculate compound interest over a period of time based on initial investment, interest rate, duration, and compounding frequency. The interface is intuitive and styled with modern ttk widgets.

---

## 🚀 Features

📥 Input fields for:  
- Initial investment  
- Interest rate (%)  
- Time in years  

🔘 Radio buttons to choose compounding frequency: Daily, Monthly, Annually  
💱 Currency selector to toggle between $, €, and £ — **only affects how the final result is displayed; calculation logic remains the same**  
🎯 "Calculate" button to compute the final balance  
🧹 "Clear" button to reset all inputs and output  
❌ Error handling for invalid (non-numeric) inputs  
🪟 Clean and responsive layout with ttk-styled widgets and grid manager  
🔧 Pure Python implementation compatible with Python 3.x  

---

## 🖥️ Technologies Used

- Python 3.x  
- Tkinter (ttk) for the graphical user interface  
- Built-in math operations (no external libraries required)  
- PyCharm (recommended IDE)  

---

## 📂 Project Structure

- **main.py**: Core script that handles both UI layout and calculation logic. Key responsibilities: <br>
  🖼️ Creates the GUI with modern ttk widgets: Label, Entry, Button, Frame, etc. <br>
  🧠 Calculates compound interest using the formula: <br>
  
      - A = P × (1 + r/n)^(nt) where: 
          - A = final amount 
          - P = principal (initial investment) 
          - r = annual interest rate (decimal)
          - n = compounding frequency per year 
          - t = time in years
          
  💱 Supports multiple currencies via radio buttons — **only changes the displayed symbol, does not affect the calculation** <br>
  🔁 Dynamically updates the result using `StringVar()` <br>
  🧹 Implements a Clear function to reset the form <br>
  ❌ Catches invalid input using `try/except` and displays user-friendly error messages 

---

## 🛠️ Setup

### Step 1: Clone the Repository

To get started, clone this repository to your local machine using the following command:

`git clone https://github.com/your-username/CompoundInterestConverter.git`

### Step 2: Dependencies

Make sure you have Python 3.x installed. You can check your version with:

`python3 --version`

### Step 3: Run the project

Once you've installed the dependencies, you can run the main Python script to generate and interact with the calculator app.

`python3 main.py`

--- 

## 🤝 Contributing

Contributions are welcome! If you'd like to improve the project, feel free to:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-name`).
3. Make your changes and commit them (`git commit -m 'Add new feature'`).
4. Push to your branch (`git push origin feature-name`).
5. Submit a pull request.

If you find bugs or have feature requests, please [open an issue](https://github.com/ximenes13/CompoundInterestConverter/issues).

