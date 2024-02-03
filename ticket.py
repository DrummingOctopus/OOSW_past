# Here we have the class for creating Ticket Objects.
# The various methods implemented are used by other classes and methods for updating ticket objects

class Ticket:
    def __init__(self, ticket_id, timestamp, user_name, user_email, user_department,
                 contact_no, issue_description, priority, status):
        self.timestamp = timestamp
        self.user_name = user_name
        self.email = user_email
        self.department = user_department
        self.contact_no = contact_no
        self.description = issue_description
        self.ticket_status = status  # This will have 3 possible options: (open ticket, under review, resolved)
        self.__ticket_id = ticket_id
        self.priority = priority

    def view_ticket(self):
        return f"{self.__ticket_id}, {self.timestamp}, {self.user_name}, {self.email}, " \
               f"{self.department}, {self.contact_no}, {self.description}, {self.ticket_status}, " \
               f"{self.priority}"

    def get_ticketid(self):
        return self.__ticket_id

    def get_ticket_priority(self):
        return self.priority

    # This method was initially intended to be used to create tickets,
    # but it turned out simpler to not use it in the end.
    # Still it is good to have it for future uses.
    def create_ticket(self, __ticket_id, timestamp, user_name, email, department,
                      contact_no, description, ticket_status, priority):

        new_ticket = Ticket(__ticket_id, timestamp, user_name, email, department,
                            contact_no, description, ticket_status, priority)
        return new_ticket

    def set_priority(self, new_priority):
        self.priority = new_priority

    def view_priority(self):
        return self.priority

