import os
import unittest
import tempfile
from studentrecords import StudentRecords

class TestStudentRecords(unittest.TestCase):
    
    def setUp(self):
        self.temp_file = tempfile.NamedTemporaryFile(delete=False)
        self.f1 = StudentRecords(self.temp_file.name)
    
    def tearDown(self):
        self.f1.close()
        self.temp_file.close()
        os.remove(self.temp_file.name)
        
    def test_add_del(self):
        rec = ["1","Ritvik Sharma", "92"]
        self.assertEqual(self.f1.create_record(rec),True)
        self.assertEqual(self.f1.delete_record(rec[0]),True)
        
    def test_add_search(self):
        rec = ["1","Ritvik Sharma", "92"]
        self.assertEqual(self.f1.create_record(rec),True)
        self.assertEqual(self.f1.search_record(rec[0]),rec)
        
    def test_add_del_search(self):
        rec = ["1","Ritvik Sharma", "92"]
        self.assertEqual(self.f1.create_record(rec),True)
        self.assertEqual(self.f1.delete_record(rec[0]),True)
        self.assertEqual(self.f1.search_record(rec[0]),[])
        
    def test_add_search_del(self):
        rec = ["1","Ritvik Sharma", "92"]
        self.assertEqual(self.f1.create_record(rec),True)
        self.assertEqual(self.f1.search_record(rec[0]),rec)
        self.assertEqual(self.f1.delete_record(rec[0]),True)
        
    def test_all_breaks(self):
        
        rec1 = ["1","Ritvik Sharma", "92"]
        rec2 = ["2", "Ryan Sharma", "90"]
        
        self.assertEqual(self.f1.create_record(rec1),True)
        self.assertEqual(self.f1.create_record(rec2),True)
        
        self.assertEqual(self.f1.search_record(rec1[0]),rec1)
        self.assertEqual(self.f1.search_record(rec2[0]),rec2)
        self.assertEqual(self.f1.search_record("3"), [])
        
        self.assertEqual(self.f1.delete_record(rec1[0]),True)
        self.assertEqual(self.f1.delete_record(rec2[0]),True)
        self.assertEqual(self.f1.delete_record("3"),False)
        
if __name__ == "__main__":
    unittest.main()
        
        