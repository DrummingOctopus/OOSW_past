# The Helpdesk class is the one that is managing the processes of the whole program. It calls most of the other classes
# and runs the main methods of the menu.

from sll import SLL
from fileservice import  FileService
from dbservice import DBService


class Helpdesk:

    def __init__(self):
        self.list = SLL()
        self.log = FileService()
        self.db = DBService('database')

    # This method adds tickets into the SLL and checks the status of the ticket to be added unto the list.
    # If the status is already set to 'Resolved' then it only gets added to the database.
    def log_issue(self, issue, priority):
        if issue.ticket_status.upper() == 'RESOLVED':
            self.add_to_db(issue)
        else:
            self.list.push(issue, priority)

    def remove_issue(self, pos):
        self.list.pop(pos)

    def get_ticket(self, pos):
        return self.list.get_node(pos)

    # THIS METHOD WORKS FOR PRINTING THE WHOLE SLL. IT CALLS THE RELEVANT METHOD FROM THE SLL CLASS
    def view_sll(self):
        return self.list.view_list()

    # def update_issue(self, identifier):  # This is not fully developed yet. Other methods are currently used to
    #     return ValueError                # update a ticket. It is for future reference

    def start_database(self):  # This method initiates the database for storing the resolved tickets
        self.db.create_table()

    def add_to_db(self, obj):
        self.db.db_add(obj)


