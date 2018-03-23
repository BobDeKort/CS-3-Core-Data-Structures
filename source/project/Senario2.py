#!python

from binarytree import BinarySearchTree

class MatchNode(object):
    def __init__(self, route, cost):
        """Initialize this binary tree node with the given data."""
        self.route = route
        self.cost = cost

    # Required to compare based on route
    def __eq__(self, other):
        return self.route == other.route

    def __lt__(self, other):
        return self.route < other.route

    def __gt__(self, other):
        return self.route > other.route

def get_routes_data(path):
    '''Reads the file at the given path and store the routes data in a binary tree'''
    binary_tree = BinarySearchTree()
    for line in open(path, 'r'):                # Open file and read each line
        route, cost = line.split(',')           # Split each line in route and cost for that route
                                                # We need strings because the routes should be ordered alphabetically, not on numerical value
        match_node = MatchNode(route, cost)     # Store the route and cost as a pair
        binary_tree.insert(match_node)          # Insert route, cost pair into tree
    return binary_tree

def get_phone_number_list(path):
    '''Reads the file at the given path an stores the phone numbers in a list'''
    phone_numbers = []
    with open(path, 'r') as l:                  # open file and read each line
        phone_numbers = l.read().splitlines()   # Splits line on new line character
    return phone_numbers

def get_call_cost(tree, phone_numbers):
    '''Prints out the cost for the given phone numbers based on the data in the given routes cost tree'''
    for number in phone_numbers:
        determined_cost = 0
        number = number.strip()                         # Removes any whitespace
        for prefix_length in range(1, len(number)+1):   # Loop over each possible prefix_length
            route = number[0:prefix_length]             # Slice the number to get the prefix based on the prefix length
            node = tree.search(route)
            if node != 0:
                determined_cost = node
        print(node)
        print("The number: " + number +" costs " + determined_cost)

def main():
    cost_path = 'data/route-costs-4.txt'
    cost_tree = get_routes_data(cost_path)
    number_path= 'data/phone-numbers-3.txt'
    phone_numbers = get_phone_number_list(number_path)
    get_call_cost(cost_tree, phone_numbers)


if __name__ == '__main__':
    main()
