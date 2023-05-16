#!/usr/bin/python3
"""
Define the command interpreter class
"""
import re
import cmd
from shlex import split
from models import storage
from models.base_model import BaseModel
from models.user import User

def parse(arg):
    curly_braces = re.search(r"\{(.*?)\}", arg)
    brackets = re.search(r"\[(.*?)\]", arg)
    if curly_braces is None:
        if brackets is None:
            return [i.strip(",") for i in split(arg)]
        else:
            lexer = split(arg[:brackets.span()[0]])
            retl = [i.strip(",") for i in lexer]
            retl.append(brackets.group())
            return retl
    else:
        lexer = split(arg[:curly_braces.span()[0]])
        retl = [i.strip(",") for i in lexer]
        retl.append(curly_braces.group())
        return retl

class HBNBCommand(cmd.Cmd):
    """
    Represents the command interpreter the project
    """
    prompt = "(hbnb)"
    __classes = {
            "BaseModel",
            "User",
    }
    def do_create(self, arg):
        arg_list = parse(arg)
        if arg:
            if arg_list[0] not in HBNBCommand.__classes:
                print("** class doesn't exist **")
            else:
                print(eval(arg_list[0])().id)
                storage.save()
        else:
            print("** class name missing **")

    def do_show(self, arg):
        arg_list = parse(arg)
        objects = storage.all()
        if arg:
            if arg_list[0] not in HBNBCommand.__classes:
                print("** class doesn't exist **")
            elif len(arg_list) == 1:
                print("** instance id missing **")
            elif "{}.{}".format(arg_list[0], arg_list[1]) not in objects:
                print("** no instance found **")
            else:
                print(objects["{}.{}".format(arg_list[0], arg_list[1])])
        else:
            print("** class name missing **")

    def do_destroy(self, arg):
        arg_list = parse(arg)
        objects = storage.all()
        if arg:
            if arg_list[0] not in HBNBCommand.__classes:
                print("** class doesn't exist **")
            elif len(arg_list) == 1:
                print("** instance id missing **")
            elif "{}.{}".format(arg_list[0], arg_list[1]) not in objects:
                print("** no instance found **")
            else:
                del objects["{}.{}".format(arg_list[0], arg_list[1])]
                storage.save()
        else:
            print("** class name missing **")

    def do_all(self, arg):
        arg_list = parse(arg)
        if len(arg_list) > 0 and arg_list[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            res = []
            for obj in storage.all().values():
                if len(arg_list) > 0 and arg_list[0] == obj.__class__.__name__:
                    res.append(obj.__str__())
                else:
                    res.append(obj.__str__())
            print(res)

    def do_update(self, arg):
        arg_list = parse(arg)
        objects = storage.all()
        if arg:
            if arg_list[0] not in HBNBCommand.__classes:
                print("** class doesn't exist **")
                return False
            elif len(arg_list) == 1:
                print("** instance id missing **")
                return False
            elif "{}.{}".format(arg_list[0], arg_list[1]) not in objects:
                print("** no instance found **")
                return False
            elif len(arg_list) == 2:
                print("** attribute name missing **")
                return False
            elif len(arg_list) == 3:
                print("** value missing **")
                return False
            elif arg_list[2] in ["id","created_at", "updated_at"]:
                return False
            elif len(arg_list) >= 4:
                obj = objects["{}.{}".format(arg_list[0], arg_list[1])]
                obj.__dict__[arg_list[2]] = arg_list[3]
        else:
            print("** class name missing **")
            return False
        storage.save()

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
