import tkinter as tk
from tkinter import ttk, messagebox, simpledialog

class ContactBook:
    def __init__(self, master):
        self.master = master
        self.master.title("Contact Book")

        self.contacts = []

        # Labels
        ttk.Label(master, text="Name:").grid(row=0, column=0, padx=10, pady=5, sticky="E")
        ttk.Label(master, text="Phone:").grid(row=1, column=0, padx=10, pady=5, sticky="E")
        ttk.Label(master, text="Email:").grid(row=2, column=0, padx=10, pady=5, sticky="E")
        ttk.Label(master, text="Address:").grid(row=3, column=0, padx=10, pady=5, sticky="E")

        # Entry widgets
        self.name_entry = ttk.Entry(master, width=30)
        self.name_entry.grid(row=0, column=1, padx=10, pady=5)

        self.phone_entry = ttk.Entry(master, width=30)
        self.phone_entry.grid(row=1, column=1, padx=10, pady=5)

        self.email_entry = ttk.Entry(master, width=30)
        self.email_entry.grid(row=2, column=1, padx=10, pady=5)

        self.address_entry = ttk.Entry(master, width=30)
        self.address_entry.grid(row=3, column=1, padx=10, pady=5)

        # Buttons
        ttk.Button(master, text="Add Contact", command=self.add_contact).grid(row=4, column=0, columnspan=2, pady=10)
        ttk.Button(master, text="View Contacts", command=self.view_contacts).grid(row=5, column=0, columnspan=2, pady=10)
        ttk.Button(master, text="Search Contact", command=self.search_contact).grid(row=6, column=0, columnspan=2, pady=10)
        ttk.Button(master, text="Update Contact", command=self.update_contact).grid(row=7, column=0, columnspan=2, pady=10)
        ttk.Button(master, text="Delete Contact", command=self.delete_contact).grid(row=8, column=0, columnspan=2, pady=10)

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()

        if name and phone:
            contact = {"Name": name, "Phone": phone, "Email": email, "Address": address}
            self.contacts.append(contact)
            messagebox.showinfo("Success", "Contact added successfully!")
            self.clear_entries()
        else:
            messagebox.showerror("Error", "Name and Phone are required fields.")

    def view_contacts(self):
        if not self.contacts:
            messagebox.showinfo("Info", "No contacts found.")
            return

        contact_list = "\n".join([f"{contact['Name']}: {contact['Phone']}" for contact in self.contacts])
        messagebox.showinfo("Contact List", contact_list)

    def search_contact(self):
        name_to_search = simpledialog.askstring("Search Contact", "Enter name to search:")

        if name_to_search:
            found_contacts = [contact for contact in self.contacts if name_to_search.lower() in contact["Name"].lower()]
            if found_contacts:
                contact_list = "\n".join([f"{contact['Name']}: {contact['Phone']}" for contact in found_contacts])
                messagebox.showinfo("Search Results", contact_list)
            else:
                messagebox.showinfo("Info", "No matching contacts found.")
        else:
            messagebox.showinfo("Info", "Search canceled.")

    def update_contact(self):
        name_to_update = simpledialog.askstring("Update Contact", "Enter name to update:")

        if name_to_update:
            found_contacts = [contact for contact in self.contacts if name_to_update.lower() in contact["Name"].lower()]
            if found_contacts:
                selected_contact = found_contacts[0]

                # Ask user for updated details
                updated_name = simpledialog.askstring("Update Contact", "Enter updated name:", initialvalue=selected_contact["Name"])
                updated_phone = simpledialog.askstring("Update Contact", "Enter updated phone:", initialvalue=selected_contact["Phone"])
                updated_email = simpledialog.askstring("Update Contact", "Enter updated email:", initialvalue=selected_contact["Email"])
                updated_address = simpledialog.askstring("Update Contact", "Enter updated address:", initialvalue=selected_contact["Address"])

                # Update contact details
                selected_contact["Name"] = updated_name if updated_name else selected_contact["Name"]
                selected_contact["Phone"] = updated_phone if updated_phone else selected_contact["Phone"]
                selected_contact["Email"] = updated_email if updated_email else selected_contact["Email"]
                selected_contact["Address"] = updated_address if updated_address else selected_contact["Address"]

                messagebox.showinfo("Success", "Contact updated successfully!")
            else:
                messagebox.showinfo("Info", "No matching contacts found.")
        else:
            messagebox.showinfo("Info", "Update canceled.")

    def delete_contact(self):
        name_to_delete = simpledialog.askstring("Delete Contact", "Enter name to delete:")

        if name_to_delete:
            found_contacts = [contact for contact in self.contacts if name_to_delete.lower() in contact["Name"].lower()]
            if found_contacts:
                self.contacts.remove(found_contacts[0])
                messagebox.showinfo("Success", "Contact deleted successfully!")
            else:
                messagebox.showinfo("Info", "No matching contacts found.")
        else:
            messagebox.showinfo("Info", "Deletion canceled.")

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBook(root)
    root.mainloop()
