#!/usr/bin/python3
"""A module that contains the entry point of the command interpreter"""
import cmd


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


if __name__ == "__main__":
    HBNBCommand().cmdloop()
