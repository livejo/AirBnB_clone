#!/usr/bin/python3
"""
contains the entry point of the command interpreter
"""
import cmd
import shlex
import os
import models
from models import BaseModel, User, Amenity, Review, City, Place, State

storage = models.storage
classes_dict = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
                "Place": Place, "Review": Review, "State": State, "User": User}


class HBNBCommand(cmd.Cmd):
    """ a command line interpreter """
    prompt = '(hbnb) '
    keyss = classes_dict.keys()

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

    def do_show(self, arg):
        """
        Show command to Prints the string representation of an instance based
        on
        the class name and id
        Usage: show <Class_Name> <obj_id>
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        try:
            eval(args[0])
        except Exception:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
        else:
            storage.reload()
            container_obj = storage.all()
            key_id = args[0] + "." + args[1]
            if key_id in container_obj:
                value = container_obj[key_id]
                print(value)
            else:
                print("** no instance found **")

    def do_destroy(self, s):
        """ deletes an instance
            based on the class name and id
        """
        args = s.split()
        obj = []
        if len(args) == 0:
            print("** class name missing **")
            return
        try:
            eval(args[0])
        except Exception:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
        else:
            storage.reload()
            obj = storage.all()
            key_id = args[0] + "." + args[1]
            if key_id in obj:
                del obj[key_id]
                storage.save()
            else:
                print("** no instance found **")

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

    def do_update(self, _input):
        """Updates an instance based on the class name and id by adding
           or updating attribute (save the change into the JSON file)
        """
        _input = shlex.split(_input)
        query_key = ''

        if len(_input) == 0:
            print("** class name missing **")
            return
        if _input[0] not in self.keyss:
            print("** class doesn't exist **")
            return
        if len(_input) == 1:
            print("** instance id missing **")
            return
        if len(_input) > 1:
            query_key = _input[0] + '.' + _input[1]
        if query_key not in models.storage.all().keys():
            print("** no instance found **")
            return
        if len(_input) == 2:
            print('** attribute name missing **')
            return
        if len(_input) == 3:
            print('** value missing **')
            return
        key_name = _input[2]
        input_value = _input[3]
        setattr(models.storage.all()[query_key], key_name, input_value)

        models.storage.all()[query_key].save()
        
        @staticmethod
    def check_for_braces(command, open_brace, close_brace):
        try:
            first_brace = command.index(open_brace)
            second_brace = command.index(close_brace)
            if command[second_brace + 1] == ")":
                return first_brace, second_brace
            else:
                return False, False
        except ValueError:
            return False, False

    def get_list_of_args(self, command):
        obj_id = ""
        attr = ""
        new_val = ""
        className = ""
        functionName = ""
        try:
            core_args = command.split("(")[0].split(".")  # User.update
            all_args = command.split("(")[1][:-1]  # *args + **kwargs
            className = core_args[0]
            functionName = core_args[1]
            if all_args != "":
                first_brace, second_brace = self.check_for_braces(all_args,
                                                                  "{", "}")
                if first_brace is not False:
                    arguments = all_args[:first_brace - 2]
                else:
                    arguments = all_args
                # eliminate any white space
                arguments = ' '.join(arguments.split())
                arguments = arguments.split(maxsplit=2, sep=",")
                obj_id = arguments[0].strip("\" ")
                attr = arguments[1].strip("\" ")
                try:
                    index_brace = arguments[2].index("]")  # if we found "["
                    new_val = arguments[2][:index_brace + 1].strip("\" ")
                except Exception:
                    new_val = arguments[2]  # if we didn't found "["
            return className, functionName, obj_id, attr, new_val
        except Exception as ex:
            # print(ex)
            return className, functionName, obj_id, attr, new_val

    def default(self, line):
        """
            Change Default console action:
            Usage:
                <class name>.count()
                <class name>.all()
                <class name>.show(<id>)
                <class name>.destroy(<id>)
                <class name>.update(<id>, <attribute name>, <attribute value>)
        """
        first_brace, second_brace = self.check_for_braces(line, "{", "}")
        if first_brace is not False:
            core_string = line[:first_brace]
            str_dict = line[first_brace: second_brace + 1]
            dict_args = eval(str_dict)
            for key, val in dict_args.items():
                command = core_string + repr(key) + ', ' + repr(val) + ')'
                self.default(command)
            return
        try:
            args = self.get_list_of_args(line)

            if len(args) > 1:
                className, functionName, obj_id, attr, new_val = args
                if inspect.isclass(eval(className)) is True:
                    arg = className + ' ' + obj_id
                    if functionName == "all":
                        return self.do_all(className)
                    elif functionName == "show":
                        return self.do_show(arg)
                    elif functionName == "destroy":
                        return self.do_destroy(arg)
                    elif functionName == "update":
                        return self.do_update(arg + ' ' + attr + ' ' + new_val)
                    elif functionName == "count":
                        i = 0
                        object_container = storage.all()
                        for obj_id, obj in object_container.items():
                            if type(obj) is eval(className):
                                i += 1
                        print(i)
            else:
                print("*** Unknown syntax: {}".format(line))
                return False
        except Exception:
            pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
