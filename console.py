#!/usr/bin/python3
"""
Define the command interpreter class
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """
    Represents the command interpreter the project
    """
    prompt = "(hbnb)"

    def do_quit(self, *args):
        return True

    def help_quit(self):
        print("Quit command to exit the program")

    def do_EOF(self, line):
        return True

    def help_EOF(self):
        print("End of the line")

    def emptyline(self):
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
