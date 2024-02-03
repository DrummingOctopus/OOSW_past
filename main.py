# Assignment CA3.
# This is the main program. Below all the relevant classes are imported and then some tickets are created.
# Finally, the program initiates running the Menu class
from helpdesk import Helpdesk
from fileservice import FileService
from ticket import Ticket
from menu import Menu


h1 = Helpdesk()
file1 = FileService()
menu = Menu(h1, file1)

# The database initializes here before everything else starts.
h1.start_database()

# The following lines create 8 tickets. Of those only 7 are shown in the list and one is added straight into the
# database as the ticket status is already set to resolved.
ticket1 = Ticket((file1.set_ticket_id()), (menu.current_time()), 'Bill Clinton', 'bill@usa.com', 'Press', '089765432',
                 'Stained Clothes', 9, 'Ticket opened')
ticket2 = Ticket((file1.set_ticket_id()), (menu.current_time()), 'Hillary Clinton', 'hillary@usa.com', 'Cloak & Dagger',
                 '089556662', 'Confused professional with personal mobile device and caused a data leak', 8, 'Ticket opened')
ticket3 = Ticket((file1.set_ticket_id()), (menu.current_time()), 'Barrack Obama', 'barrack@usa.com', 'Manager', '082345267',
                 'Too competent', 2, 'Ticket opened')
ticket4 = Ticket((file1.set_ticket_id()), (menu.current_time()), 'Dick Tracy', 'd.tracy@dicks.com', 'Research',
                 '2125558016', 'Wrong place at the wrong time', 10, 'Ticket opened')
ticket5 = Ticket((file1.set_ticket_id()), (menu.current_time()), 'Donald Duck', 'duck@usa.com', 'Comic', '089564321',
                 'Rich stingy uncle', 5, 'Ticket opened')
ticket6 = Ticket((file1.set_ticket_id()), (menu.current_time()), 'Mickey Mouse', 'mouse@usa.com', 'Disney', '089338321',
                 'Goofy friends', 10, 'Ticket opened')
ticket7 = Ticket((file1.set_ticket_id()), (menu.current_time()), 'Tobias Overton', 'toverton0@psu.edu',
                 'Product Management', '7456502842', 'Suspendisse accumsan tortor quis turpis. Sed ante.', 1, 'In Progess')
ticket8 = Ticket((file1.set_ticket_id()), (menu.current_time()), 'Dena Grigaut', 'dgrigautb@upenn.edu', 'Services',
                 '8674923369','Vestibulum sed magna at nunc commodo placerat. Praesent blandit.', 2, 'Resolved')


h1.log_issue(ticket3, ticket3.priority)
h1.log_issue(ticket1, ticket1.priority)
h1.log_issue(ticket4, ticket4.priority)
h1.log_issue(ticket2, ticket2.priority)
h1.log_issue(ticket5, ticket5.priority)
h1.log_issue(ticket6, ticket6.priority)
h1.log_issue(ticket7, ticket7.priority)
h1.log_issue(ticket8, ticket8.priority)
print("The node list size is ", h1.list.size)


while True:
    menu.print_console()
    option = input("Please make a choice > ")

    try:
        if option == "1": # Work on a ticket. View the first ticket in detail
            # h1.list.view_head_node()
            menu.view_first_ticket(h1,1)

        elif option == "2": # Log a new ticket
            temp_obj = menu.create_ticket(file1)
            h1.log_issue(temp_obj, temp_obj.priority)
        elif option == "3": # View whole ticket list
            # h1.list.view_list()
            menu.helpdesk.view_sll()
        elif option == "4": # Review or update a ticket
            menu.update_ticket(h1)
        elif option == "5": # Exit Console Menu
            menu.exit_program()

        else:
            raise Exception('Exception: Input should be between 1 and 5. The input value was: {}'.format(option))
    except Exception as e:
        print(e)
        menu.errorlog.error_to_txt(e)
    print("\n")
    input("Press any key to continue.....")
