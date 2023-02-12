#!/usr/bin/python3
"""A module that contains the entry point of the command interpreter"""
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """Defines an interpreter"""

    prompt = '(hbnb) '

    def emptyline(self):
        """Doesn't execute an empty line + ENTER"""
        pass

    def do_quit(self, line):
        """exit the program"""
        return True

    def help_quit(self):
        """A handler that provides information for the command quit"""
        print('Quit command to exit the program')

    def do_EOF(self, line):
        """exit the program"""
        return True

    def help_EOF(self):
        """A handler that provides information for the command EOF"""
        print('Quit command to exit the program')

    def do_create(self, args):
        """ Creates a new instance of BaseModel, saves it
            (to the JSON file) and prints the id
        """
        cls_name = args.strip()
        if not cls_name:
            print("** class name missing **")
            return
        try:
            new_instance = eval(cls_name + "()")
        except NameError:
            print("** class doesn't exist **")
            return
        new_instance.save()
        print(new_instance.id)

    def help_create(self):
        """provides an information how to use the command"""
        print("Creates a new instance of BaseModel, saves it "
              "(to the JSON file) and prints the id.")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
