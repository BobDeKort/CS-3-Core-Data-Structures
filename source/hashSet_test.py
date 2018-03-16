#!python

from hashSet import HashSet
import unittest
# Python 2 and 3 compatibility: unittest module renamed this assertion method
if not hasattr(unittest.TestCase, 'assertCountEqual'):
    unittest.TestCase.assertCountEqual = unittest.TestCase.assertItemsEqual

class HashSetTest(unittest.TestCase):

    def test_empty_init(self):
        hs = HashSet()
        assert hs.size == 0

    def test_filled_init(self):
        hs = HashSet(["Shane", "Alan"])
        assert hs.size == 2
        assert hs.contains("Alan") == True
        assert hs.contains("Bob") == False

    def test_init_edge_cases(self):
        hs = HashSet(["", 1, None])
        assert hs.size == 2
        assert hs.contains("") == True

    def test_add(self):
        hs = HashSet()
        assert hs.size == 0
        hs.add("Shane")
        assert hs.size == 1
        assert hs.contains("Shane") == True
        assert hs.contains("Alan") == False
        assert hs.contains("Bob") == False
        hs.add("Alan")
        assert hs.size == 2
        assert hs.contains("Shane") == True
        assert hs.contains("Alan") == True
        assert hs.contains("Bob") == False

    def test_remove(self):
        hs = HashSet(["Shane", "Alan", "Laurel"])
        assert hs.size == 3
        assert hs.contains("Shane") == True
        assert hs.contains("Alan") == True
        assert hs.contains("Laurel") == True

        hs.remove("Alan")
        assert hs.size == 2
        assert hs.contains("Alan") == False
        assert hs.contains("Shane") == True
        assert hs.contains("Laurel") == True

        hs.remove("Shane")
        assert hs.size == 1
        assert hs.contains("Alan") == False
        assert hs.contains("Shane") == False
        assert hs.contains("Laurel") == True

        hs.remove("Laurel")
        assert hs.size == 0
        assert hs.contains("Alan") == False
        assert hs.contains("Shane") == False
        assert hs.contains("Laurel") == False

    def test_union(self):
        hs1 = HashSet(["Melody","Erik", "Jake"])
        hs2 = HashSet(["Jake", "Alan", "Shane"])
        union = hs1.union(hs2)
        assert union.size == 5
        assert union.contains("Melody") == True
        assert union.contains("Erik") == True
        assert union.contains("Jake") == True
        assert union.contains("Alan") == True
        assert union.contains("Shane") == True
        assert union.contains("Bob") == False

    def test_intersection(self):
        hs1 = HashSet(["Melody","Erik", "Jake", "Shane"])
        hs2 = HashSet(["Jake", "Alan", "Shane"])
        intersection = hs1.intersection(hs2)
        assert intersection.size == 2
        assert intersection.contains("Jake") == True
        assert intersection.contains("Shane") == True
        assert intersection.contains("Melody") == False
        assert intersection.contains("Erik") == False
        assert intersection.contains("Alan") == False

    def test_intersection2(self):
        hs1 = HashSet(["Jake", "Jeff", "Shane", "Fre"])
        hs2 = HashSet(["Melody","Erik", "Shane", "Alan", "Bob", "Kaichi", "Jake"])
        intersection = hs1.intersection(hs2)
        assert intersection.size == 2
        assert intersection.contains("Jake") == True
        assert intersection.contains("Shane") == True
        assert intersection.contains("Alan") == False
        assert intersection.contains("Melody") == False
        assert intersection.contains("Erik") == False

    def test_difference(self):
        hs1 = HashSet(["Melody","Erik", "Jake", "Shane"])
        hs2 = HashSet(["Jake", "Alan", "Shane"])
        difference = hs1.difference(hs2)
        assert difference.size == 3
        assert difference.contains("Melody") == True
        assert difference.contains("Erik") == True
        assert difference.contains("Alan") == True
        assert difference.contains("Jake") == False
        assert difference.contains("Shane") == False
        assert difference.contains("Bob") == False

    def test_difference2(self):
        hs1 = HashSet(["Jake", "Jeff", "Shane", "Fre"])
        hs2 = HashSet(["Melody","Erik", "Shane", "Alan", "Bob", "Kaichi", "Jake"])
        difference = hs1.difference(hs2)
        assert difference.size == 7
        assert difference.contains("Jake") == False
        assert difference.contains("Shane") == False
        assert difference.contains("Jeff") == True
        assert difference.contains("Alan") == True


    def test_is_subset(self):
        hs1 = HashSet(["Jake", "Jeff", "Shane", "Fre"])
        hs2 = HashSet(["Jeff", "Shane"])
        is_subset = hs1.is_subset(hs2)
        assert is_subset == True
        hs3 = HashSet(["Jeff", "Shane", "Alec"])
        is_subset2 = hs1.is_subset(hs3)
        assert is_subset2 == False
