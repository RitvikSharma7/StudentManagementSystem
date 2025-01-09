import unittest
from groupteam import *

class TestGroupTeam(unittest.TestCase):
    
    def test_grouping(self):
        grp1 = GroupTeam([1,2,3,4], group_size = 2)
        grp2 = GroupTeam([1,2,3,4,5], group_size = 6)
        grp3 = GroupTeam([1,2,3], group_size = 0)
        self.assertEqual(grp1.groups, [(1,2), (3,4)])
        self.assertEqual(grp2.groups, None)
        self.assertEqual(grp3.groups, None)
        
        
        
        
        
if __name__ == "__main__":
    unittest.main()