import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class ToolTip:
    def __init__(self, widget, text):
        self.widget = widget
        self.text = text
        self.tooltip = None
        widget.bind("<Enter>", self.show_tooltip)
        widget.bind("<Leave>", self.hide_tooltip)

    def show_tooltip(self, event):
        x, y, _, _ = self.widget.bbox("insert")
        x += self.widget.winfo_rootx() + 25
        y += self.widget.winfo_rooty() + 25
        self.tooltip = tk.Toplevel(self.widget)
        self.tooltip.wm_overrideredirect(True)
        self.tooltip.wm_geometry(f"+{x}+{y}")
        label = tk.Label(self.tooltip, text=self.text, background="yellow", relief="solid", borderwidth=1, font=("Arial", 10, "normal"))
        label.pack()

    def hide_tooltip(self, event):
        if self.tooltip:
            self.tooltip.destroy()
            self.tooltip = None

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
        label_result.config(text=f"Result: {result} {to_unit}")
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter a valid number")

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
        # Add more options here
    }
    combo_to['values'] = unit_options.get(from_unit, [])

def clear_fields():
    entry_value.delete(0, tk.END)
    combo_from.set('')
    combo_to.set('')
    label_result.config(text="")

root = tk.Tk()
root.title("Unit Converter")

# Main Frame
main_frame = tk.Frame(root, padx=20, pady=20)
main_frame.grid(row=0, column=0, padx=10, pady=10)

# Title Label
title_label = tk.Label(main_frame, text="Unit Converter", font=("Arial", 16, "bold"))
title_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))

# Labels
label_value = tk.Label(main_frame, text="Value:")
label_value.grid(row=1, column=0, padx=10, pady=10, sticky="e")
ToolTip(label_value, "Enter the value to convert")

label_from = tk.Label(main_frame, text="From:")
label_from.grid(row=2, column=0, padx=10, pady=10, sticky="e")
ToolTip(label_from, "Select the unit to convert from")

label_to = tk.Label(main_frame, text="To:")
label_to.grid(row=3, column=0, padx=10, pady=10, sticky="e")
ToolTip(label_to, "Select the unit to convert to")

# Entry
entry_value = tk.Entry(main_frame)
entry_value.grid(row=1, column=1, padx=10, pady=10)
ToolTip(entry_value, "Enter the value here")

# Comboboxes
combo_from = ttk.Combobox(main_frame, values=["Fahrenheit", "Celsius", "Miles", "Kilometers", "Pounds", "Kilograms", "Inches", "Centimeters", "Gallons", "Liters"])
combo_from.grid(row=2, column=1, padx=10, pady=10)
combo_from.bind("<<ComboboxSelected>>", update_to_units)
ToolTip(combo_from, "Select the unit to convert from")

combo_to = ttk.Combobox(main_frame)
combo_to.grid(row=3, column=1, padx=10, pady=10)
ToolTip(combo_to, "Select the unit to convert to")

# Result Label
label_result = tk.Label(main_frame, text="Result: ", font=("Arial", 12, "bold"))
label_result.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Buttons
button_convert = tk.Button(main_frame, text="Convert", command=convert_units, bg="lightblue", font=("Arial", 10, "bold"))
button_convert.grid(row=5, column=0, padx=10, pady=10, sticky="w")
ToolTip(button_convert, "Click to convert the value")

button_clear = tk.Button(main_frame, text="Clear", command=clear_fields, bg="lightblue", font=("Arial", 10, "bold"))
button_clear.grid(row=5, column=1, padx=10, pady=10, sticky="e")
ToolTip(button_clear, "Click to clear the fields")

root.mainloop()