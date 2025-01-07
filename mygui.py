import tkinter as tk
import tkinter.messagebox
from studentrecords import StudentRecords  

class MyGUI:
    def __init__(self, root, path = "smstest.csv", bg_clr="lightblue"):
        self.root = root
        self.root.title("Student Database")
        self.root.geometry("800x600")
        self.root.configure(bg=bg_clr)

        self.records = StudentRecords(path) # Link to the StudentRecords instance

        # Initialize instance variables
        self.arg_list1 = ["ID", "Name", "Final Grade"]
        self.lbl_dict = {}
        self.entry_dict = {}
        self.arg_list2 = ["ADD", "DELETE","SEARCH"]
        self.cmd_list = [self.Add, self.Delete,self.Search]
        self.btn_dict = {}

        self.createFrame()
        self.createLblEnt()
        self.createButtons()
        self.createOutputBox()
        
        
    """
    createFrame : creates frame for widgets to be placed on.

    """

    def createFrame(self):
        self.frame = tk.Frame(self.root)
        self.frame.pack(padx=20, pady=20, fill="both", expand=True)
        for i in range(3):
            self.frame.columnconfigure(i, weight=1)
        for i in range(4):
            self.frame.rowconfigure(i, weight=1)
            
    """
    createLblEnt : creates labels and corresponding entries linked to the fields required for a student in the database.

    """

    def createLblEnt(self):
        for idx, lbl in enumerate(self.arg_list1):
            self.lbl_dict[lbl] = tk.Label(self.frame, text=lbl, relief="groove", width=10)
            self.lbl_dict[lbl].grid(row=idx, column=0, padx=10, pady=10, sticky="nsew")

            self.entry_dict[lbl] = tk.Entry(self.frame, width=20)
            self.entry_dict[lbl].grid(row=idx, column=1, padx=10, pady=10, sticky="nsew")
            
    """
    createButtons: creates buttons for operations to be executed.

    """

    def createButtons(self):
        for idx, btn in enumerate(self.arg_list2):
            self.btn_dict[btn] = tk.Button(self.frame, text=btn, command=self.cmd_list[idx], width=10)
            self.btn_dict[btn].grid(row=idx, column=2, padx=10, pady=10, sticky="nsew")
            
    """
    createOutputBox: creates Output Box for data to be shown when specfic operations are executed.

    """


    def createOutputBox(self):
        self.sturec_box = tk.Listbox(self.frame, height=8, width=30, bg = "light blue")
        self.sturec_box.grid(row=len(self.arg_list2) + 2, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")
        self.sturec_box.insert(tk.END, " ".join(self.arg_list1))
        
    """
    Add: gets student record as a list from field entries and writes them into the csv file using the create_record function in studentrecords class .

    """

    def Add(self):
        # Get input values
        record = [self.entry_dict["ID"].get(), self.entry_dict["Name"].get(), self.entry_dict["Final Grade"].get()]

        # Validate inputs
        if not all(record):
            tk.messagebox.showerror("Error","Error: All fields must be complete!")
            return
        
        if not str(self.entry_dict["ID"].get()).isdigit():
            tk.messagebox.showerror("Error","Error: ID field must be numeric!")
            return
        
        if not str(self.entry_dict["Name"].get()).replace(" ", "").isalpha():
            tk.messagebox.showerror("Error","Error: Name field must be alpha numeric!")
            return
        
        if not str(self.entry_dict["Final Grade"].get()).isdigit():
            tk.messagebox.showerror("Error","Final Grade must be numeric!")
            return

        # Add record to file
        try:
            self.records.create_record(record)
            self.sturec_box.insert(tk.END, f"Record Added: {record}")
        except Exception as e:
            self.sturec_box.insert(tk.END, f"Error: {e}")
            
    """
    Delete: Deletes student record by using primary key--Student ID.

    """

    def Delete(self):
        record_id = self.entry_dict["ID"].get()

        # Validate input
        if not self.records.search_record(record_id):
            tk.messagebox.showerror("Error","Error: ID field is not found!")
            return

        # Delete record from file
        try:
            self.records.delete_record(record_id)
            tk.messagebox.showinfo("Message",f"Record with ID {record_id} deleted.")
        except Exception as e:
            tk.messagebox.showerror("Error", f"Error: {e}")
            
            
    """
    Search: searches record by primary key--Student ID and displays the record if a match is found
    else it will show an error if not found.

    """
            
    def Search(self):
     
        record_id = self.entry_dict["ID"].get()

        # Validate input
        if not record_id:
            tk.messagebox.showerror("Error","Error: ID field is required!")
            return
        
        x = self.records.search_record(record_id)
        
        
        # Search for the record
        try:
            if x:
                tk.messagebox.showinfo("Information",f"Record with ID: {record_id} exists.")
                self.sturec_box.insert(tk.END, " ".join(x))
            else:
                tk.messagebox.showinfo("Information",f"Record with ID: {record_id} doesn't exist.")
        except Exception as e:
            tk.messagebox.showerror("Error",f"Error: {e}")

        



