# The FileService  class is responsible for automatically generating a ticket_id number for every ticket
# registered through the ticketing system. The class reads and updates the 'ticket_id.txt' file that should
# be included in the program folder. The class is programmed to read the file find the last id number used and increment
# forward. If the user deletes the number form the file it restarts from 1.


class FileService:

    def set_ticket_id(self): # this method generates, reads and writes the id number for tickets in and out of txt file
        with open('ticket_id.txt', 'r+') as ticket_id:
            current_id_number = ticket_id.readline()

            if not current_id_number:
                current_id_number = ticket_id.write("1")
                return current_id_number
            elif current_id_number:
                with open('ticket_id.txt', 'w') as ticket_id:
                    id_number = int(current_id_number) + 1
                    ticket_id.write(str(id_number))
                return id_number
