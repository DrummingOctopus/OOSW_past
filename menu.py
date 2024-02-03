# This is a class for handling the menu options and running the program interface. All methods in this class
# are about calling methods from the SLL and Helpdesk classes. What is more, the error handling (try-catch)
# happens here too and uses the ErrorLog class.
from ticket import Ticket
from datetime import datetime
from errorlog import ErrorLog


class Menu:
    def __init__(self, helpdesk, fileservice):
        self.helpdesk = helpdesk
        self.fileservice = fileservice
        self.errorlog = ErrorLog()

    def print_console(self):  # This function prints the main menu
        print(f"""        ****************************************** 
                            MAIN MENU
            [The list contains {self.helpdesk.list.size} tickets for processing] \n
            Select an option below:
            ------------------------------------------
            1. Work on a ticket (Tickets with the highest priority appear first)
            2. Create a new ticket
            3. View all tickets  
            4. Review or update a ticket
            5. Exit Console Menu
            ------------------------------------------""")

    def view_first_ticket(self, helpdesk, pos):  # Shows the first ticket in the SLL with the highest priority.
        string = ''
        self.helpdesk.list.detail_view(pos)

        while True:
            print("\n")
            print("What would you like to do with this ticket?")
            print("Select an option below:")
            print(f'{string:-^45}')
            print("1. View the ticket description.")
            print("2. Update the ticket status.")
            print("3. Go back to the main menu.")
            print(f'{string:-^45}')
            choice = input("Please enter your choice here: ")

            try:
                if choice == "1":
                    self.helpdesk.list.detail_view(1)
                    continue
                elif choice == "2":
                    print("Set status for this ticket")
                    print(f'{string:-^45}')
                    print("1. Open")
                    print("2. Under Review")
                    print("3. Resolved")
                    print(f'{string:-^45}')
                    tmp = input("> ")
                    try: # Try catch errors and write them in the error_log.txt file
                        if tmp == '1':
                            self.helpdesk.list.get_ticket_object(pos).ticket_status = 'Ticket Opened'
                        elif tmp == '2':
                            self.helpdesk.list.get_ticket_object(pos).ticket_status = 'Under Review'
                        elif tmp == '3':
                            self.helpdesk.list.get_ticket_object(pos).ticket_status = 'Resolved'
                            input("Press any key to continue")
                            print("NOW SHOWING NEXT TICKET")
                            self.helpdesk.add_to_db(helpdesk.list.get_ticket_object(pos))
                            self.helpdesk.list.detail_view(pos+1)
                            self.helpdesk.list.pop(pos)
                        else:
                            raise Exception('Exception: Input should be between 1 and 3. The input value was: {}'.format(tmp))
                    except Exception as e:
                        print(e)
                        self.errorlog.error_to_txt(e)  # adds the error to the fileservice txt file

                elif choice == '3':
                    break
                else:
                    raise Exception('Exception: Input should be between 1 and 3. The input value was: {}'.format(choice))
            except Exception as e:
                print(e)
                self.errorlog.error_to_txt(e)

    def update_ticket(self, helpdesk):  # Offers functionality on updating the ticket attributes
        string = ''
        print(f'{string:-^45}')
        self.helpdesk.list.view_list()
        print(f'{string:-^45}')
        pos_choice = int(input("Choose a ticket to update > "))

        try:
            if self.helpdesk.list.isEmpty() is True:
                print("List is Empty!")
            elif pos_choice > self.helpdesk.list.get_size():
                raise Exception(f'Exception: Input should be between 1 and {self.helpdesk.list.get_size()}. '
                                f'The input value was: {pos_choice}')
        except Exception as e:
            print(e)
            self.errorlog.error_to_txt(e)

        self.helpdesk.list.detail_view(pos_choice)
        print(f'{string:-^45}')

        while True:
            print("What would you like to do with this ticket?")
            print("Select an option below:")
            print(f'{string:-^45}')
            print("1. Update the NAME.")
            print("2. Update the EMAIL.")
            print("3. Update the DEPARTMENT.")
            print("4. Update the CONTACT NO.")
            print("5. Update the DESCRIPTION.")
            print("6. Update the PRIORITY.")
            print("7. Update the STATUS.")
            print("8. Go back")
            print(f'{string:-^45}')
            choice = input("Please enter your choice here: > ")

            try:
                if choice == "1":
                    new_name = input("Set new name: > ")
                    self.helpdesk.list.get_ticket_object(pos_choice).user_name = new_name
                    self.helpdesk.list.detail_view(pos_choice)
                    continue
                elif choice == '2':
                    new_email = input("Set new email: > ")
                    self.helpdesk.list.get_ticket_object(pos_choice).email = new_email
                    self.helpdesk.list.detail_view(pos_choice)
                    continue
                elif choice == '3':
                    new_department = input("Set new department: > ")
                    self.helpdesk.list.get_ticket_object(pos_choice).department = new_department
                    self.helpdesk.list.detail_view(pos_choice)
                    continue
                elif choice == '4':
                    new_contact_no = input("Set new contact no: > ")
                    self.helpdesk.list.get_ticket_object(pos_choice).department = new_contact_no
                    self.helpdesk.list.detail_view(pos_choice)
                    continue
                elif choice == '5':
                    new_description = input("Set new issue description: > ")
                    self.helpdesk.list.get_ticket_object(pos_choice).department = new_description
                    self.helpdesk.list.detail_view(pos_choice)
                    continue
                elif choice == '6':
                    new_priority = int(input("Set new priority: > "))
                    tmp_node = self.helpdesk.list.get_ticket_object(pos_choice)
                    upd_node = tmp_node
                    upd_node.set_priority(new_priority)

                    # This loop is to prevent the function from keeping the same ticket more than once if there is
                    # no update made in its priority
                    while True:
                        if upd_node == tmp_node:
                            break
                        else:
                            return False

                    self.helpdesk.log_issue(upd_node, upd_node.priority)
                    self.helpdesk.remove_issue(pos_choice)
                    self.helpdesk.view_sll()
                    break
                elif choice == "7":
                    print("Set status for this ticket")
                    print(f'{string:-^45}')
                    print("1. Open")
                    print("2. Under Review")
                    print("3. Resolved")
                    print(f'{string:-^45}')
                    tmp = input("> ")
                    try:
                        if tmp == '1':
                            self.helpdesk.list.get_ticket_object(pos_choice).ticket_status = 'Ticket Opened'
                        elif tmp == '2':
                            self.helpdesk.list.get_ticket_object(pos_choice).ticket_status = 'Under Review'
                        elif tmp == '3':
                            self.helpdesk.list.get_ticket_object(pos_choice).ticket_status = 'Resolved'
                            self.helpdesk.add_to_db(helpdesk.list.get_ticket_object(pos_choice))
                            self.helpdesk.remove_issue(pos_choice)
                            break
                        else:
                            raise ValueError
                    except ValueError as e:
                        print("Not a valid option. Please choose either option 1, 2 or 3")
                        self.errorlog.error_to_txt(e)                # adds the error to the fileservice txt file

                elif choice == '8':
                    break

                else:
                    raise Exception('Exception: Input should be between 1 and 8. The input value was: {}'.format(choice))
            except Exception as e:
                print(e)
                self.errorlog.error_to_txt(e)

    def current_time(self):  # This function generates the timestamp required for each ticket
        return datetime.now().strftime('%d-%m-%Y %H:%M:%S')

    # MAIN MENU OPTION 2
    def create_ticket(self, fileservice):  # This method takes the user's input for creating a ticket.
                                           # The ticket_id and the timestamp are generated automatically.

        # CREATE A TICKET
        ticket_id = self.fileservice.set_ticket_id()  # this calls the method from fileservice
        timestamp = self.current_time()
        tmp_name = input("Who reports the issue? Please insert the user's name: ")
        tmp_email = input("Please fill in the user's email: ")
        tmp_department = input("Please fill in the user's department: ")
        tmp_contact_no = input("Please fill in in the user's contact number: ")
        tmp_description = input("Please fill in a description of the issue: ")
        tmp_priority = int(input("Please indicate a level of priority for this issue between 1 and 10: "))

        if tmp_priority > 10 or ValueError:
            e = 'Exception: Priority value should be between 1 and 10. The input value was: {}'.format(tmp_priority)
            print(e)
            self.errorlog.error_to_txt(e)
            tmp_priority = int(input("Please indicate a level of priority for this issue between 1 and 10: "))

        tmp_status = "Ticket opened"

        new_ticket = Ticket(ticket_id, timestamp, tmp_name, tmp_email, tmp_department, tmp_contact_no, tmp_description,
                            tmp_priority, tmp_status)

        return new_ticket

    def exit_program(self):  # this function exits the program
        print("Have a nice day! Don't be a stranger now.")
        exit()
