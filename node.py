# This class takes ticket objects and turns them into node objects, so they can be incorporated into  the SLL.
# The Node class is only called in the SLL class. It is only comprised of getters and setters. The names of the
# functions are self-explanatory.


class Node:
    def __init__(self, data, priority):
        self.data = data
        self.next = None
        self.priority = priority

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data

    def get_next(self):
        return self.next

    def set_next(self, next_node):
        self.next = next_node

    def get_priority(self):
        return self.priority

    def set_priority(self, new_priority):
        self.priority = new_priority
