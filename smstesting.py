import os
import unittest
from studentrecords import *


class TestSMS(unittest.TestCase):
    
    
    @classmethod
    def setUpClass(cls):
        path = "testingcasescsv"
        filetest = StudentRecords(path)

    @classmethod
    def tearDownClass(cls):
        path = "testingcasescsv"
        if ospathexists(path):
            osremove(path)
            print("File deleted successfully")
        else:
            print("File not found")
    
    
    def test_del_search_empty(self):
        assertEqual(filetestdelete_record("1"), False)
        actual_result = filetestsearch_record("1", [])
        
        
    def test_search_del_empty(self):
        assertEqual(filetestsearch_record("1"), [])
        assertEqual(filetestdelete_record("1"), False)
        
    def test_del_search_notempty(self):
        filetestcreate_record(["1","Ritvik Sharma", "92"])
        
        assertEqual(filetestdelete_record("1"), True)
        actual_result = filetestsearch_record("1")
        assertEqual(actual_result , ["1","Ritvik Sharma","92"] )
        
    def test_search_del_notempty(self):
        filetestcreate_record(["1","Ritvik Sharma", "92"])
        
        assertEqual(filetestsearch_record("1"), ["1","Ritvik Sharma", "92"])
        assertEqual(filetestdelete_record("1"), True)
        
    def test_add_search_del_mul(self):
            filetestcreate_record(["1","Ritvik Sharma", "92"]) 
            filetestcreate_record(["2","Ryan Sharma", "92"])
            filetestcreate_record(["5","Bob Sharma", "92"])
            
            assertEqual(filetestsearch_record("1"), ["1","Ritvik Sharma", "92"])
            assertEqual(filetestsearch_record("2"), ["2","Ryan Sharma", "92"])
            assertEqual(filetestsearch_record("13"),[])
            assertEqual(filetestsearch_record("5"), ["5","Bob Sharma", "92"])
            
            assertEqual(filetestdelete_record("1"), True)
            assertEqual(filetestdelete_record("2"), True)
            assertEqual(filetestdelete_record("13"), False)
            assertEqual(filetestdelete_record("5"), True)
            
            
    def test_del_search_multiple(self):
        assertEqual(filetestdelete_record("1"),False)
        assertEqual(filetestdelete_record("2",False))
        
        filetestsearch_record()
        
        
        
        
        
        
if __name__ == "__main__":
    unittest.main()