#!python

from hashtable import HashTable

class HashSet(object):

    def __init__(self, elements=None):
        """Initialize set with the given initial size."""
        self.size = 0
        self.hashTable = HashTable()

        if elements is not None:
            for element in elements:
                if element is not None:
                    self.add(element)

    def contains(self, element):
        """Returns a Boolean to indicate if an element is present in the set."""
        return self.hashTable.contains(element)

    def add(self, element):
        """Adds an element to the set."""
        if self.contains(element) == False:
            self.size += 1
            self.hashTable.set(element, 0)
        # Raise error?

    def remove(self, element):
        """Removes an element from the set."""
        if self.contains(element) == True:
            self.size -= 1
            self.hashTable.delete(element)
        else:  # Not found
            raise ValueError('Element not found: {}'.format(element))

    def union(self, other_set):
        """Returns a new set containing all values from given set and self"""
        #TODO: Find better solution
        new_set = HashSet()

        # Add every item in self to new_set
        for element in self.hashTable.items(): # use .keys() instead of .items()
            new_set.add(element[0])

        # Loop over other_set, check if self contains element then add
        # (More natural) Add every element in other_set if it doesn't exist
        for element in other_set.hashTable.items():
            if self.contains(element[0]) == False:
                new_set.add(element[0])

        return new_set

    def intersection(self, other_set):
        """Returns a new set containing the values present in the given set and self"""
        new_set = HashSet()

        #TODO: Do I need to check which lenght is greater?

        # Adds items shared by both sets
        for element in self.hashTable.keys(): # don't use self.hashTable.items()
            if other_set.contains(element):
                new_set.add(element)

        return new_set

    def difference(self, other_set):
        """Returns a new set that is the difference between self and the given set"""
        new_set = HashSet()
        #TODO: Find better solution
        for element in self.hashTable.items():
            if other_set.contains(element[0]) == False:
                new_set.add(element[0])

        for element in other_set.hashTable.items():
            if self.contains(element[0]) == False:
                new_set.add(element[0])

        return new_set

    def is_subset(self, other_set):
        """Returns a Boolean indicating if whether other_set is a sub set of this set"""
        intersection = self.intersection(other_set)

        if intersection.size == other_set.size:
            return True

        return False
