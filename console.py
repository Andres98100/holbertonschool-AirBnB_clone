#!/usr/bin/python3

import cmd


class HBNBCommand(cmd.Cmd):
    
    prompt = "(hbnb) "

    def do_quit(self, line):
        return True
    
    def do_EOF(self, line):
        return True

    def emptyline(self):
        """empty line + ENTER is not executed"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
