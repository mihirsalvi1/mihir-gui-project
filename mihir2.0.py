import tkinter as tk
from tkinter import messagebox


class CustomerDetailsWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Customer Details")
        self.customer_name = tk.StringVar()
        self.customer_contact = tk.StringVar()
        self.create_gui()

    def create_gui(self):
        details_frame = tk.LabelFrame(self.root, text="Customer Details")
        details_frame.pack(fill="both", expand=True, padx=10, pady=10)

        name_label = tk.Label(details_frame, text="Name:")
        name_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")
        name_entry = tk.Entry(details_frame, textvariable=self.customer_name)
        name_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")

        contact_label = tk.Label(details_frame, text="Contact:")
        contact_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")
        contact_entry = tk.Entry(details_frame, textvariable=self.customer_contact)
        contact_entry.grid(row=1, column=1, padx=5, pady=5, sticky="w")
        contact_entry.configure(validate="key")
        contact_entry.configure(validatecommand=(contact_entry.register(self.validate_contact), "%P"))

        next_button = tk.Button(self.root, text="Next", command=self.open_menu_window)
        next_button.pack(pady=10)

    def open_menu_window(self):
        if not self.customer_name.get().strip() or not self.customer_contact.get().strip():
            messagebox.showwarning("Warning", "Please enter customer name and contact.")
            return
        self.root.destroy()  # Close current window
        menu_window = tk.Tk()
        restaurant_system = MenuWindow(menu_window)
        menu_window.mainloop()

    def validate_contact(self, value):
        return value.isdigit() or value == ""

class MenuWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Menu")
        self.items = {
            "Burger": 100,
            "Pizza": 200,
            "Pasta": 150,
            "Sandwich": 80,
            "Frankie":80,
            "Nuggets":100,
            "Salad": 90,
            "Pepsi": 40,
            "Sprite": 40,
            "Icecream": 50,
            
        }
        self.selection = {}  # To store selected items
        self.create_gui()

    def create_gui(self):
        menu_frame = tk.LabelFrame(self.root, text="Menu")
        menu_frame.pack(fill="both", expand=True, padx=10, pady=10)

        # Create checkboxes for each menu item
        for item, price in self.items.items():
            var = tk.IntVar()
            checkbox = tk.Checkbutton(menu_frame, text=f"{item} - ₹{price}", variable=var)
            checkbox.var = var  # Save variable reference to checkbox
            checkbox.grid(sticky="w")
            self.selection[item] = {"var": var, "price": price}

        confirm_button = tk.Button(self.root, text="Confirm", command=self.show_selected_items)
        confirm_button.pack(pady=10)

    def show_selected_items(self):
        selected_items = [item for item, info in self.selection.items() if info["var"].get() == 1]
        if not selected_items:
            messagebox.showwarning("Warning", "Please select at least one item.")
            return

        total_price = sum(self.selection[item]["price"] for item in selected_items)
        bill = f"Selected Items:\n"
        for item in selected_items:
            bill += f"{item} - ₹{self.selection[item]['price']}\n"
        bill += f"\nTotal Price: ₹{total_price}"
        messagebox.showinfo("Selected Items", bill)

def main():
    customer_details_window = tk.Tk()
    customer_details_system = CustomerDetailsWindow(customer_details_window)
    customer_details_window.mainloop()

if __name__ == "__main__":
    main()
