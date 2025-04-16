from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter.ttk import Progressbar
from time import sleep

class UnitConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("Unit Converter")
        self.root.geometry("400x300")
        self.root.resizable(0, 0)
        
        self.input_value = tk.DoubleVar()
        self.output_value = tk.StringVar()
        self.input_unit = tk.StringVar()
        self.output_unit = tk.StringVar()
        
        self.conversions = {
            'Length': {
                'Meter': 1.0,
                'micrometer': 0.000001,
                'Nanometer': 0.000000001,
                'Kilometer': 1000.0,
                'Centimeter': 0.01,
                'Millimeter': 0.001,
                'Mile': 1609.34,
                'Yard': 0.9144,
                'Foot': 0.3048,
                'Inch': 0.0254
            },
            'Weight': {
                'Kilogram': 1.0,
                'Gram': 0.001,
                'Milligram': 0.000001,
                'Pound': 0.453592,
                'Ounce': 0.0283495,
                'Ton': 907.185
            },
            'Temperature': {
                'Celsius': 1.0,
                'Fahrenheit': 1.8,
                'Kelvin': 1.0    
            },
            'Volume': {
                'Liter': 1.0,
                'Milliliter': 0.001,
                'microliter': 0.000001,
                'Gallon': 3.78541,
                'Quart': 0.946353,
                'Pint': 0.473176,
                'Cup': 0.236588,
                'Fluid Ounce': 0.0295735,
                'Cubic Meter': 1000.0,
                'Cubic Centimeter': 0.001
            },
            'Time': {
                'Second': 1.0,
                'Millisecond': 0.001,
                'Microsecond': 0.000001,
                'Minute': 60.0,
                'Hour': 3600.0,
                'Day': 86400.0,
                'Week': 604800.0,
                'Month': 2628000.0,  
                'Year': 31536000.0   
            },
        }
        
        self.category_label = ttk.Label(root, text="Select Category:")
        self.category_label.grid(row=0, column=0, padx=5, pady=5, sticky='w')
        
        self.category_combobox = ttk.Combobox(root, values=list(self.conversions.keys()))
        self.category_combobox.grid(row=0, column=1, padx=5, pady=5)
        self.category_combobox.bind('<<ComboboxSelected>>', self.update_units)
        self.category_combobox.current(0) 
        
        self.input_label = ttk.Label(root, text="Input Value:")
        self.input_label.grid(row=1, column=0, padx=5, pady=5, sticky='w')
        
        self.input_entry = ttk.Entry(root, textvariable=self.input_value)
        self.input_entry.grid(row=1, column=1, padx=5, pady=5)
        
        self.input_unit_combobox = ttk.Combobox(root, textvariable=self.input_unit)
        self.input_unit_combobox.grid(row=1, column=2, padx=5, pady=5)

        self.output_label = ttk.Label(root, text="Result:")
        self.output_label.grid(row=2, column=0, padx=5, pady=5, sticky='w')
        
        self.output_entry = ttk.Entry(root, textvariable=self.output_value, state='readonly')
        self.output_entry.grid(row=2, column=1, padx=5, pady=5)
        
        self.output_unit_combobox = ttk.Combobox(root, textvariable=self.output_unit)
        self.output_unit_combobox.grid(row=2, column=2, padx=5, pady=5)

        self.convert_button = ttk.Button(root, text="Convert", command=self.convert)
        self.convert_button.grid(row=3, column=1, padx=5, pady=10)

        self.update_units()
        
    def update_units(self, event=None):
        category = self.category_combobox.get()
        units = list(self.conversions[category].keys())
        
        self.input_unit_combobox['values'] = units
        self.output_unit_combobox['values'] = units
        
        if len(units) > 0:
            self.input_unit.set(units[0])
            if len(units) > 1:
                self.output_unit.set(units[1])
            else:
                self.output_unit.set(units[0])
    
    def convert(self):
        try:
            value = self.input_value.get()
            input_unit = self.input_unit.get()
            output_unit = self.output_unit.get()
            category = self.category_combobox.get()
            
            if category == 'Temperature':
                result = self.convert_temperature(value, input_unit, output_unit)
            else:                
                base_value = value * self.conversions[category][input_unit]
               
                result = base_value / self.conversions[category][output_unit]
            
            self.output_value.set(f"{result:.6g}")  
        except ValueError:
            self.output_value.set("Invalid input")
        except Exception as e:
            self.output_value.set("Error in conversion")
    
    def convert_temperature(self, value, from_unit, to_unit):
    
        if from_unit == 'Celsius':
            celsius = value
        elif from_unit == 'Fahrenheit':
            celsius = (value - 32) * 5/9
        elif from_unit == 'Kelvin':
            celsius = value - 273.15
        else:
            raise ValueError("Unknown temperature unit")
        
    
        if to_unit == 'Celsius':
            return celsius
        elif to_unit == 'Fahrenheit':
            return (celsius * 9/5) + 32
        elif to_unit == 'Kelvin':
            return celsius + 273.15
        else:
            raise ValueError("Unknown temperature unit")

class IntroScreen:
    def __init__(self, root):
        self.root = root
        self.root.title("Unit Converter")
        self.root.configure(bg="#008080")
        self.root.resizable(0, 0)
        self.center_window(500, 230)
        
    
        self.entry = Label(root, bg="#008080", fg="white", 
                          text="Welcome to Unit Converter!", 
                          font=("Footlight MT Light", 15, "bold"))
        self.entry.place(x=50, y=30, width=410, height=30)
        
        
        self.load = Progressbar(root, orient=HORIZONTAL, length=250, mode='indeterminate')
        
        
        self.start = Button(root, bg="#f5f5f5", fg="black", text="START", command=self.loading)
        self.start.place(x=200, y=90, width=80, height=30)
    
    def center_window(self, width, height):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2
        self.root.geometry(f"{width}x{height}+{x}+{y}")
    
    def loading(self):
    
        self.start.place_forget()

        self.load.place(x=120, y=100)
        self.root.update()
   
        c = 0
        while c < 100:
            self.load['value'] += 5
            self.root.update()
            sleep(0.1)
            c += 5

        self.clear_intro()
        self.show_converter()
    
    def clear_intro(self):
        for widget in self.root.winfo_children():
            widget.destroy()
    
    def show_converter(self):
        
        self.root.geometry("400x300")
        self.center_window(400, 300)
        self.root.configure(bg='SystemButtonFace')
        
       
        UnitConverter(self.root)

if __name__ == "__main__":
    root = tk.Tk()
    app = IntroScreen(root)
    root.mainloop()