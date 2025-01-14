import csv

class StudentRecords:
    def __init__(self, path, mode="a+"):
        self.path = path
        self.mode = mode
        self.file = open(path, mode, newline="")
        self.cw = csv.writer(self.file)
        self.file.seek(0)
        self.cr = csv.reader(self.file)
        
        # Write header if file is empty
        if not self.file.read(1):  # Check if the file is empty
            self.file.seek(0)
            self.cw.writerow(["ID", "Name", "Final Grade"])
            self.file.flush()
        else:
            self.file.seek(0)  # Ensure the file pointer is at the start

    def create_record(self, record):
        """
        Writes student data into csv file.
        
        Parameters:
        record: list parameter that has student data, so the writer can write it
        into the file.
        
        Returns:
        True if data written succesfully, else False.
        """
        try:
            self.cw.writerow(record)
            self.file.flush()
            return True
        except Exception as e:
            print(f"{e}")
            return False
        
        

    def delete_record(self, record_id):
        """
        Deletes student data in a CSV file by checking ID (primary key).
        
        Parameters:
        record_id: str parameter that is the ID of the student record used to check data.
        
        Returns:
        True if rows are written without exception, else False.
        """
        try:
            self.file.seek(0)
            
            rows = list(self.cr)  # Read all rows into memory
            self.file.seek(0)
            
            self.file.truncate() # Clear the file
            
            found = False
            
            for row in rows:
                if row and row[0] != record_id: # Skip empty rows and matching IDs
                    self.cw.writerow(row)
                else:
                    found = True
            self.file.flush()
            return found
        except Exception as e:
            print(f"{e}")
            return False

    def search_record(self, record_id):
        """
        Searches student data in a CSV file by checking ID (primary key).
        
        Parameters:
        record_id: str parameter that is the ID of the student record used to check data.
        
        Returns:
        Returns the student row (list) if the ID matches; else returns an empty list ([]).
        """
        self.file.seek(0)  # Ensure the file pointer is at the start
        for row in self.cr:
            if row and row[0] == record_id:  # Check row is not empty and matches
                return row
        return []
    
    def group_records(self, group_size):
        """
            Groups students based on group size required.
            
            Parameters:
            group_size: size of each student group.
            
            Returns:
            Grouped list if conditions valid, else nothing."""
        
        self.file.seek(0)
        
        Students = list(self.cr)
        print(Students)
        
        if len(Students) <= 1:  # No data rows
            return None  # Return None if there's no data to group
    
        Students = Students[1:]  # Skip the header row
        
        if group_size <= 0:  # Invalid group size
            return None
        
        total_team_size = len(Students)
        whole_team_size = total_team_size // group_size
        rem_team_size = total_team_size % group_size
        
        whole_list = [tuple(Students[i * group_size : (i + 1) * group_size]) for i in range(whole_team_size)]
    
        if rem_team_size != 0:
            whole_list.append(tuple(Students[whole_team_size * group_size:]))
        
        return whole_list
    
#     def see_records(self):
#         data = "\n".join(str(row) for row in self.cr)
#         
#         return data
        
        

    def close(self):
        """Closes the file to ensure resources are properly released."""
        self.file.close()
