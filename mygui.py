import tkinter as tk
import tkinter.messagebox
from studentrecords import StudentRecords  

class MyGUI:
    def __init__(self, root, path="smstest.csv", bg_clr="lightblue"):
        self.root = root
        self.root.title("Student Database")
        self.root.geometry("800x600")
        self.root.configure(bg=bg_clr)

        self.records = StudentRecords(path)  # Link to the StudentRecords instance

        self.arg_list1 = ["ID", "Name", "Final Grade"]
        self.lbl_dict = {}
        self.entry_dict = {}
        self.arg_list2 = ["ADD", "DELETE", "SEARCH"]
        self.cmd_list = [self.Add, self.Delete, self.Search]
        self.btn_dict = {}

        self.createFrame()
        self.createLblEnt()
        self.createButtons()
        self.createOutputBox()

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)  # Handle window close event

    def createFrame(self):
        self.frame = tk.Frame(self.root)
        self.frame.pack(padx=20, pady=20, fill="both", expand=True)
        for i in range(3):
            self.frame.columnconfigure(i, weight=1)
        for i in range(4):
            self.frame.rowconfigure(i, weight=1)

    def createLblEnt(self):
        for idx, lbl in enumerate(self.arg_list1):
            self.lbl_dict[lbl] = tk.Label(self.frame, text=lbl, relief="groove", width=10)
            self.lbl_dict[lbl].grid(row=idx, column=0, padx=10, pady=10, sticky="nsew")
            self.entry_dict[lbl] = tk.Entry(self.frame, width=20)
            self.entry_dict[lbl].grid(row=idx, column=1, padx=10, pady=10, sticky="nsew")

    def createButtons(self):
        for idx, btn in enumerate(self.arg_list2):
            self.btn_dict[btn] = tk.Button(self.frame, text=btn, command=self.cmd_list[idx], width=10)
            self.btn_dict[btn].grid(row=idx, column=2, padx=10, pady=10, sticky="nsew")

    def createOutputBox(self):
        self.sturec_box = tk.Listbox(self.frame, height=8, width=30, bg="light blue")
        self.sturec_box.grid(row=len(self.arg_list2) + 2, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")
        self.sturec_box.insert(tk.END, " ".join(self.arg_list1))

    def Add(self):
        record = [self.entry_dict["ID"].get(), self.entry_dict["Name"].get(), self.entry_dict["Final Grade"].get()]

        if not all(record):
            tk.messagebox.showerror("Error", "Error: All fields must be complete!")
            return

        if not record[0].isdigit():
            tk.messagebox.showerror("Error", "Error: ID field must be numeric!")
            return

        if not record[1].replace(" ", "").isalpha():
            tk.messagebox.showerror("Error", "Error: Name field must contain only alphabetic characters!")
            return

        if not record[2].isdigit():
            tk.messagebox.showerror("Error", "Error: Final Grade must be numeric!")
            return

        try:
            self.records.create_record(record)
            self.sturec_box.insert(tk.END, f"Record Added: {record}")
            self.sturec_box.update()
        except Exception as e:
            tk.messagebox.showerror("Error", f"Error: {e}")

    def Delete(self):
        record_id = self.entry_dict["ID"].get()

        if not record_id.isdigit():
            tk.messagebox.showerror("Error", "Error: ID field must be numeric!")
            return

        if not self.records.search_record(record_id):
            tk.messagebox.showerror("Error", f"Error: Record with ID {record_id} not found!")
            return

        try:
            self.records.delete_record(record_id)
            tk.messagebox.showinfo("Message", f"Record with ID {record_id} deleted.")
        except Exception as e:
            tk.messagebox.showerror("Error", f"Error: {e}")

    def Search(self):
        record_id = self.entry_dict["ID"].get()

        if not record_id:
            tk.messagebox.showerror("Error", "Error: ID field is required!")
            return

        try:
            record = self.records.search_record(record_id)
            if record:
                tk.messagebox.showinfo("Information", f"Record with ID {record_id} found.")
                self.sturec_box.insert(tk.END, " ".join(record))
            else:
                tk.messagebox.showinfo("Information", f"Record with ID {record_id} not found.")
        except Exception as e:
            tk.messagebox.showerror("Error", f"Error: {e}")

    def on_closing(self):
        """Handle application closing."""
        self.records.close()  # Close the file to release resources
        self.root.destroy()


