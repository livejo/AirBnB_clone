#!/usr/bin/python3
""" 
contains the entry point of the command interpreter
"""
import cmd
import os
import models
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """ a command line interpreter """
    prompt = '(hbnb)'

    def do_quit(self, s):
        """ exit operation """
        return True

    def do_EOF(self, s):
        """ exit operation """
        return True

    def emptyline(self):
        """ empty line + ENTER shouldn’t execute anything """
        return False

    def do_create(self, s):
        """ Creates a new instance of BaseModel
            saves it (to the JSON file) and prints the id
        """
        if len(s) == 0:
            print('** class name missing **')
        else:
            try:
                args = s.split
                new = eval("{}()".format(s[0]))
                new.save()
                print(new.id)
            except:
                print("** class doesn't exist **")

    def do_show(self, s):
        """ Prints the string representation of an instance
            based on the class name and id
        """
        arg = split.s
        if len(arg) == 0:
            print('** class name missing **')
        else:
            try:
                eval(s[0])
            except:
                print('** class doesn't exist **')
        if len(arg) == 1:
            print('** instance id missing **')
        models.storage.reload()
        for key, val in models.storage.all.items():
            if val.__class__.__name__ == arg[0] and val == arg[1]:
                print(val.__str__())
                return
        print('** no instance found **')

    def do_destroy(self, s):
        """ deletes an instance
            based on the class name and id
        """
        arg = s.split()
        cont = []
        if len(arg[0] == 0):
            print('** class name missing **')
        else:
            try:
                eval(s[0])
            except:
                print('** class doesn't exist **')
        if len(arg) == 1:
            print('** instance id missing **')
        else:
            storage.reload()
            cont = storage.all()
            key_id = arg[0] + "." + arg[1]
            if key_id in cont:
                del cont[key_id]
                storage.save()
            else:
                print('** no instance found **')
            
            


if __name__ == '__main__':
    HBNBCommand().cmdloop()
