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
        create_record: Writes student data into csv file.
        @param record: list parameter that has student data, so the writer can write it
        into the file.
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
        delete_record: Deletes student data in a CSV file by checking ID (primary key).
        @param record_id: str parameter that is the ID of the student record used to check data.
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
        search_record: Searches student data in a CSV file by checking ID (primary key).
        @param record_id: str parameter that is the ID of the student record used to check data.
        @return: Returns the student row (list) if the ID matches; else returns an empty list ([]).
        """
        self.file.seek(0)  # Ensure the file pointer is at the start
        for row in self.cr:
            if row and row[0] == record_id:  # Check row is not empty and matches
                return row
        return []

    def close(self):
        """Closes the file to ensure resources are properly released."""
        self.file.close()
