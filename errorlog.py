# The class ErrorLog is responsible for handling error messages in the main program and passing them into the
# 'error_log.txt' file. If the file doesn't exist the class creates it when the program runs.

class ErrorLog:
    def error_to_txt(self, error_msg):
        with open('error_log.txt', 'a+') as f:
            f.write(str(error_msg) + '\n')
