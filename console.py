#!/usr/bin/python3
"""
contains the entry point of the command interpreter
"""
import cmd
import os
import models
from models import BaseModel, User, Amenity, Review, City, Place, State

storage = models.storage


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
                args = s.split()
                new = eval("{}()".format(args[0]))
                new.save()
                print(new.id)
            except Exception:
                print("** class doesn't exist **")

    def do_show(self, s):
        """ Prints the string representation of an instance
            based on the class name and id
        """
        arg = s.split()
        if len(arg) == 0:
            print('** class name missing **')
        else:
            try:
                eval(s[0])
            except Exception:
                print("** class doesn't exist **")
        if len(arg) == 1:
            print('** instance id missing **')
        models.storage.reload()
        for key, val in models.storage.all().items():
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
        if len(arg) == 0:
            print('** class name missing **')
        else:
            try:
                eval(s[0])
            except Exception:
                print("** class doesn't exist **")
        if len(arg) == 1:
            print('** instance id missing **')
            return
        class_name, class_id = (arg[0], arg[1])
        query_key = class_name + '.' + class_id
        if query_key not in models.storage.all().keys():
            print("** no instance found **")
            return
        del models.storage.all()[query_key]
        models.storage.save()

    def do_all(self, s):
        """ Prints all string representation of all instances """
        storage.reload()
        arg = s.split()
        lists = []
        cont = storage.all()
        if len(arg) == 0:
            for arg_id in cont.keys():
                obj = cont[arg_id]
                lists.append(str(obj))
            print(lists)
            return
        if len(arg) == 1:
            try:
                eval(arg[0])
                for arg_id in cont.keys():
                    if type(cont[arg_id] is eval(arg[0])):
                        obj = cont[arg_id]
                        lists.append(str(obj))
                print(lists)
            except Exception:
                print("** class doesn't exist **")
                return

    def do_update(self, s):
        """
        Update command Updates an instance based on the class name and id
        by adding or updating attribute
        (save the change into the JSON file).
        """
        storage.reload()
        args = s.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if len(args) >= 1:
            try:
                eval(args[0])
                if len(args) == 1:
                    print("** instance id missing **")
                    return
                try:
                    key_id = args[0] + "." + args[1]
                    container_obj = storage.all()
                    container_obj[key_id]
                except Exception:
                    print("** no instance found **")
                    return
            except Exception:
                print("** class doesn't exist **")
                return
        if len(args) >= 2:
            try:
                eval(args[0])
                if len(args) == 2:
                    print("** attribute name missing **")
                    return
            except Exception:
                print("** class doesn't exist **")
                return

        if len(args) >= 3:
            try:
                eval(args[0])
                if len(args) == 3:
                    print("** value missing **")
                    return
            except Exception:
                print("** class doesn't exist **")
                return
        if len(args) >= 4:
            args = " ".join(str(arg).split(maxsplit=3)).split(maxsplit=3)

            class_name = args[0]
            obj_id = args[1]
            obj_attr = args[2].strip("\"\'")
            obj_new_val = args[3]
            try:
                eval(class_name)
                key_id = class_name + "." + obj_id
                container_obj = storage.all()
                if key_id in container_obj:
                    obj = container_obj[key_id]
                    try:
                        type_attr = type(getattr(obj, obj_attr))
                        obj_new_val = self.same_type_as_attr(obj_new_val,
                                                             type_attr)
                        if obj_new_val is False:
                            return
                    except Exception:
                        obj_new_val = self.convert_new_val(obj_new_val)
                    setattr(obj, obj_attr, obj_new_val)
                    storage.save()
                else:
                    print("** no instance found **")
                    return
            except Exception as ex:
                print("** class doesn't exist **") 


if __name__ == '__main__':
    HBNBCommand().cmdloop()
