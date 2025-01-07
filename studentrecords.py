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
        if not any(self.cr):
            self.cw.writerow(["ID", "Name", "Final Grade"])
            
            
    
    """
    create_record: Writes student data into csv file.

    @param record: list paramter that has student data, so the writer can write it
    into the file.

    """
    def create_record(self, record):
        self.cw.writerow(record)
        self.file.flush()
        
    """
    delete_record: deletes student data in a csv file by checking ID(primary key).

    @param record_d: int paramter that is the ID of the student record used to check data.
    

    """


    def delete_record(self, record_id):
        # Move to the start of the file
        self.file.seek(0)

        # Read all rows into memory
        rows = list(self.cr)

        # Truncate the file to start fresh
        self.file.seek(0)
        self.file.truncate()

        # Write back rows that don't match the record_id
        for row in rows:
            if row[0] != record_id:
                self.cw.writerow(row)

        # Ensure data is written to the file
        self.file.flush()

        
    """
    search_record: searches student data in a csv file by checking ID(primary key).

    @param record_d: int paramter that is the ID of the student record used to check data.
    
    @return: return the student row(list) if the ID is matched else returns and empty list([]).

    """
        
    def search_record(self, record_id):
    # Ensure the file pointer is at the start
        self.file.seek(0)
    
    # Iterate through the CSV reader directly
        for row in self.cr:
            if row and row[0] == record_id:  # Check row is not empty and matches
                return row
        
        return []
