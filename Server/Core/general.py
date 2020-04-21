from colorama import Back, Fore, Style
import colorama

colorama.init()

class General:
    
    # public 
    ## public property
    cmdMode = False

    # init
    def __init__(self):
        pass
    
    #static method
    @staticmethod
    def outputMsg(message, msgType):

        if msgType == 1:
            
            print(Fore.YELLOW + message)
            # to do, change the console output size/color
            pass
        elif msgType == 2:
            print ("[ERROR] " + message)
            pass
        else:
            print(message)
            pass

        pass

    @staticmethod
    def processParameter(command, compCommand):
        
        result = command.find(compCommand)
        if result == -1:
            return (False, command)
        else:
            length = len(compCommand)
            tmp = command[:result - 1] + command[result + length:]
            return (True, tmp)
        pass