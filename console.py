#!/usr/bin/python3
"""module for a class that inherits from cmd"""
import cmd
import sys
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models import storage

classes = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}


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

    def do_create(self, line):
        """Creates a new instance of BaseModel"""
        args = line.split()
        # splits the string into a list
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in classes:
            print("** class doesn't exist **")
            return
        new_obj = getattr(sys.modules[__name__], args[0])()
        # sys.modules: dictionary containing all imported modules
        new_obj.save()
        print(new_obj.id)

    def do_show(self, line):
        """Prints the string representation of an instance"""
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        key = args[0] + "." + args[1]
        if key not in storage.all():
            print("** no instance found **")
            return
        print(storage.all()[key])

    def do_destroy(self, line):
        """ Deletes an instance based on the class name and id"""
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        key = args[0] + "." + args[1]
        if key not in storage.all():
            print("** no instance found **")
            return
        storage.all().pop(key)
        storage.save()

    def do_all(self, line):
        """Prints all string representation of all instances"""
        args = line.split()
        objs_list = []
        if len(args) == 0:
            for value in storage.all().values():
                objs_list.append(str(value))
            print(objs_list)
            return
        if args[0] not in classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            for key in storage.all().keys():
                if args[0] in key:
                    objs_list.append(str(storage.all()[key]))
            print(objs_list)
            return

    def do_update(self, line):
        """Updates an instance based on the class name and id"""
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        key = args[0] + "." + args[1]
        if key not in storage.all():
            print("** no instance found **")
            return
        if len(args) == 2:
            print("** attribute name missing **")
            return
        if len(args) == 3:
            print("** value missing **")
            return
        if type(args[3]) == str:
            args[3] = args[3].strip('"').replace('"', '')
        setattr(storage.all()[key], args[2], args[3])
        storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
