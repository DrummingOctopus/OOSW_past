# This is the class that creates a singly linked list. All the methods developed here
# focus on creating, updating and handling the SLL.
from node import Node
from ticket import Ticket


class SLL:
    def __init__(self):
        self.head = None
        self.size = 0

    def isEmpty(self):
        return True if self.head is None else False

    def get_size(self):
        return self.size

    def get_node(self, pos):  # This method returns the node in position 'pos'
        counter = 1
        tmp_node = None

        while counter <= pos:
            if counter == 1:
                tmp_node = self.head
            else:
                tmp_node = tmp_node.get_next()
            counter += 1
        # print(counter)
        return tmp_node

    def get_ticket_object(self, pos):  # This method returns the ticket(data) of the node in position 'pos'
        counter = 1
        tmp_node = None

        while counter <= pos:
            if counter == 1:
                tmp_node = self.head
            else:
                tmp_node = tmp_node.get_next()
            counter += 1
        return tmp_node.get_data()

    # This is the heart of the SLL class. It creates the list by turning the ticket objects into nodes and then
    # sorts them by priority in descending order.
    def push(self, data, priority):

        # Condition check for checking if SLL is empty or not
        if self.isEmpty() is True:
            # Creating a new node and assigning
            # it as head of list in an empty list
            self.head = Node(data, priority)

            # Returning 1 for successful execution
            self.size += 1
            return 1

        else:
            # The second node to be added goes through this special condition check to see whether its priority is
            # higher than the existing first node (head) of the queue.
            if self.head.priority <= int(priority):

                # Creating a new node
                new_node = Node(data, priority)
                new_node.next = self.head

                # Assigning it to self.head
                self.head = new_node

                # Returning 1 for successful execution
                self.size += 1
                return 1

            else:
                # If the new node hasn't a higher priority than the head of the list, it traverses through the list
                # until it finds the next smaller priority node
                temp = self.head

                while temp.next:
                    # If same priority node found then current
                    # node will come after the previous node
                    if int(priority) >= temp.next.priority:
                        break

                    temp = temp.next

                new_node = Node(data, priority)
                new_node.next = temp.next
                temp.next = new_node
                self.size += 1
                # Returning 1 for successful execution
                return 1

    # This method removes nodes from the SLL from a given position 'pos'
    def pop(self, pos):
        if pos == 1:
            tmp_node = self.get_node(1)
            self.head = tmp_node.get_next()
        elif pos == self.size and self.size > 1:
            tmp_node = self.get_node(pos-1)
            tmp_node.set_next(None)
        else:
            current = self.get_node(pos)
            previous = self.get_node(pos-1)
            previous.set_next(current.get_next())

        self.size -= 1

    # This method provides the head node of the SLL or returns a message saying the list is empty.
    def view_head_node(self):
        if self.isEmpty() is True:
            return "List is Empty!"

        else:
            temp = self.head
            print(f"{temp.data.view_ticket()}", end = "\n")

    # This method provides a detailed view of the node in the selected positon 'pos'
    def detail_view(self, pos):
        if self.isEmpty() is True:
            return "Queue is Empty!"

        else:
            temp_node = self.get_ticket_object(pos)
            print(f'TICKET ID: {temp_node.get_ticketid()}')
            print(f'PRIORITY: {temp_node.priority}')
            print(f'LOG TIME:  {temp_node.timestamp}')
            print(f'USER NAME: {temp_node.user_name}')
            print(f'EMAIL: {temp_node.email}')
            print(f'DEPARTMENT: {temp_node.department}')
            print(f'CONTACT NUMBER: {temp_node.contact_no}')
            print('\n')
            print(f'ISSUE DESCRIPTION: {temp_node.description}')
            print('\n')
            print(f'Ticket STATUS: {temp_node.ticket_status}')

    # This is the method responsible for printing the whole linked list sorted by priority.
    def view_list(self):
        if self.isEmpty() is True:
            return "Queue is Empty!"
        else:
            count = 1
            temp = self.head
            while temp:
                print(f"{count} - {temp.data.view_ticket()}", end = "\n")
                temp = temp.next
                count += 1
