import tkinter as tk
from tkinter import ttk

def convert_units():
    try:
        value = float(entry_value.get())
        from_unit = combo_from.get()
        to_unit = combo_to.get()
        
        conversions = {
            ("Fahrenheit", "Celsius"): lambda x: (x - 32) * 5.0/9.0,
            ("Celsius", "Fahrenheit"): lambda x: (x * 9.0/5.0) + 32,
            ("Miles", "Kilometers"): lambda x: x * 1.60934,
            ("Kilometers", "Miles"): lambda x: x / 1.60934,
            ("Pounds", "Kilograms"): lambda x: x * 0.453592,
            ("Kilograms", "Pounds"): lambda x: x / 0.453592,
            ("Inches", "Centimeters"): lambda x: x * 2.54,
            ("Centimeters", "Inches"): lambda x: x / 2.54,
            ("Gallons", "Liters"): lambda x: x * 3.78541,
            ("Liters", "Gallons"): lambda x: x / 3.78541,
            # Add more conversions here
        }
        
        result = conversions.get((from_unit, to_unit), lambda x: "Invalid conversion")(value)
        label_result.config(text=f"Result: {result}")
    except ValueError:
        label_result.config(text="Invalid input")

def update_to_units(event):
    from_unit = combo_from.get()
    unit_options = {
        "Fahrenheit": ["Celsius"],
        "Celsius": ["Fahrenheit"],
        "Miles": ["Kilometers"],
        "Kilometers": ["Miles"],
        "Pounds": ["Kilograms"],
        "Kilograms": ["Pounds"],
        "Inches": ["Centimeters"],
        "Centimeters": ["Inches"],
        "Gallons": ["Liters"],
        "Liters": ["Gallons"],
        # Add more unit options here
    }
    combo_to.config(values=unit_options.get(from_unit, []))
    combo_to.current(0)

# Create the main window
root = tk.Tk()
root.title("Unit Converter")

# Create and place the widgets
label_value = ttk.Label(root, text="Value:")
label_value.grid(column=0, row=0, padx=10, pady=10)

entry_value = ttk.Entry(root)
entry_value.grid(column=1, row=0, padx=10, pady=10)

label_from = ttk.Label(root, text="From:")
label_from.grid(column=0, row=1, padx=10, pady=10)

combo_from = ttk.Combobox(root, values=["Fahrenheit", "Celsius", "Miles", "Kilometers", "Pounds", "Kilograms", "Inches", "Centimeters", "Gallons", "Liters"])
combo_from.grid(column=1, row=1, padx=10, pady=10)
combo_from.current(0)
combo_from.bind("<<ComboboxSelected>>", update_to_units)

label_to = ttk.Label(root, text="To:")
label_to.grid(column=0, row=2, padx=10, pady=10)

combo_to = ttk.Combobox(root, values=["Celsius", "Fahrenheit", "Kilometers", "Miles", "Kilograms", "Pounds", "Centimeters", "Inches", "Liters", "Gallons"])
combo_to.grid(column=1, row=2, padx=10, pady=10)
combo_to.current(0)

button_convert = ttk.Button(root, text="Convert", command=convert_units)
button_convert.grid(column=0, row=3, columnspan=2, padx=10, pady=10)

label_result = ttk.Label(root, text="Result:")
label_result.grid(column=0, row=4, columnspan=2, padx=10, pady=10)

# Run the application
root.mainloop()
