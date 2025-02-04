import tkinter as tk
import tkinter.messagebox
from studentrecords import StudentRecords

class MyGUI:
    
    sep = "TEAM "
        
    def __init__(self, root, path="smstest.csv", bg_clr="lightblue"):
        self.root = root
        self.root.title("Student Database")
        self.root.geometry("800x600")
        self.root.configure(bg=bg_clr)

        self.records = StudentRecords(path)  # Link to the StudentRecords instance

        self.arg_list1 = ["ID", "Name", "Final Grade", "Group Size"]
        self.lbl_dict = {}
        self.entry_dict = {}
        self.arg_list2 = ["ADD", "DELETE", "SEARCH", "GROUP"]
        self.cmd_list = [self.Add, self.Delete, self.Search, self.Group]
        self.btn_dict = {}
        self.radio_var = tk.IntVar(value=1)

        self.createFrame()
        self.createLblEnt()
        self.createButtons()
        self.createOutputBox()
        self.RadioButtons()

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)  # Handle window close event

    def createFrame(self):
        """
            Creates Frame for Widgets and RadioButton sections.  """
        
        self.frame = tk.Frame(self.root, height = 600, width = 600)
        self.frameOperation = tk.Frame(self.root,height = 200, width = 600)
        self.frameOperation.pack( padx=20, pady=20, fill="both", expand=True)
        self.frame.pack( padx=20, pady=20, fill="both", expand=True)
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
        self.sturec_box = tk.Listbox(self.frame, height=6, width=30, bg="light blue")
        self.sturec_box.grid(row=len(self.arg_list2) + 2, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")

            # Insert items into the Listbox
        self.sturec_box.insert(tk.END, " ".join(self.arg_list1[0:3]))

            # Create the Scrollbar
        self.scrollbar = tk.Scrollbar(self.frame, orient=tk.VERTICAL, command=self.sturec_box.yview)
        self.scrollbar.grid(row=len(self.arg_list2) + 2, column=3, sticky="ns")  # Use grid to align scrollbar

            # Link the Listbox to the Scrollbar
        self.sturec_box.config(yscrollcommand=self.scrollbar.set)
        
    def SMS_or_GROUP(self):
        if self.radio_var.get() == 0:
            
            self.btn_dict["GROUP"]["state"] = "disabled"
            self.btn_dict["ADD"]["state"] = "active"
            self.btn_dict["DELETE"]["state"] = "active"
            self.btn_dict["SEARCH"]["state"] = "active"
            self.entry_dict["ID"]["state"] = "normal"
            self.entry_dict["Name"]["state"] = "normal"
            self.entry_dict["Final Grade"]["state"] = "normal"
            self.entry_dict["Group Size"]["state"] = "disabled"
             
        elif self.radio_var.get() == 1:
            
            self.btn_dict["ADD"]["state"] = "disabled"
            self.entry_dict["ID"]["state"] = "disabled"
            self.btn_dict["DELETE"]["state"] = "disabled"
            self.entry_dict["Name"]["state"] = "disabled"
            self.btn_dict["SEARCH"]["state"] = "disabled"
            self.entry_dict["Final Grade"]["state"] = "disabled"
            self.btn_dict["GROUP"]["state"] = "active"
            self.entry_dict["Group Size"]["state"] = "normal"
            
    def RadioButtons(self):
        self.radio_var = tk.IntVar()  # Define an instance variable to track the selected radiobutton
        lst = ["Students Records Management", "Group Students"]

        for idx, value in enumerate(lst):
            self.rd_btn = tk.Radiobutton(
                self.frameOperation,
                text=value,
                variable=self.radio_var,  # Associate the variable with the radiobuttons
                font=("Arial", 18),
                value=idx,  # Value of the radiobutton
                command=self.SMS_or_GROUP,  # Call SMS_or_GROUP when a button is selected
            )
            self.rd_btn.pack(anchor = "w")  # Align radiobuttons to the left
            
        self.see_btn = tk.Button(self.frameOperation, text = "SEE", command = self.see, width =10)
        self.see_btn.pack(side="top", anchor="ne")

    def Add(self):
        record = [self.entry_dict["ID"].get(), self.entry_dict["Name"].get(), self.entry_dict["Final Grade"].get()]
        self.sturec_box.delete(0, tk.END)

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
        
        self.sturec_box.delete(0, tk.END)

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
        
        self.sturec_box.delete(0, tk.END)

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
            
    def Group(self):
       
        try:
            # Get the group size from input and convert it to an integer
            group_size = int(self.entry_dict["Group Size"].get())
        except ValueError:
            # Show a warning if the input is invalid
            tk.messagebox.showwarning("Warning", "Please enter a valid number for Group Size.")
            return  # Exit early if the input is invalid

        # Get the teams from the group_records method
        teams = self.records.group_records(group_size)

        if teams is None:  # No valid teams could be formed
            tk.messagebox.showwarning("Warning", "Invalid Group Size!")
            return
        
        self.sturec_box.delete(0, tk.END)
        
#         for i, group in enumerate(teams):
#             team_text = f"Team {i + 1}:\n "  # Format the team header
#             members_text = ", ".join(str(e) for e in group)  # Join members with commas
#             self.sturec_box.insert(tk.END, team_text + "\n" + members_text + " \n")  # Insert the team and members into the Listbox

        # Format the result string for display
        result = ""
        for i, group in enumerate(teams):
            self.sturec_box.insert(tk.END, f"{'-' * 7}{self.sep}{i + 1}{'-' * 7}\n" ) # Separator for the group
            for member in group:
                self.sturec_box.insert(tk.END, f" Member: {member}\n") # Format each group member
            self.sturec_box.insert(tk.END, "\n")
        self.sturec_box.insert(tk.END, f"{'-' * 7}{'-' * len(self.sep)}{'-' * len(str(i + 1))}{'-' * 7}\n") # End of the last group
        
        #print(result)
        # Insert the formatted result into the text box
        #self.sturec_box.insert(tk.END, result)
        
    def see(self):
        self.sturec_box.delete(0, tk.END)
        for row in self.records.cr:
            formatted_row = " ".join(map(str, row))  
            self.sturec_box.insert(tk.END, formatted_row)


    def on_closing(self):
        
        """Handle application closing."""
        self.records.close()  # Close the file to release resources
        self.root.destroy()


