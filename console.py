#!/usr/bin/python3
"""module for a class that inherits from cmd"""
import cmd


class HBNBCommand(cmd.Cmd):
    """A custom command line class for the AirBnB
    project based on the base class cmd"""
    
    prompt = "(hbnb) "

    def do_quit(self, line):
        """to exit the program"""
        return True
    
    def do_EOF(self, line):
        """to exit the program"""
        return True

    def emptyline(self):
        """empty line + ENTER is not executed"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
