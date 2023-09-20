#!/usr/bin/python3
"""This package defines a base model class.
"""
import json
import os
import csv


class Base:
    """This is the base class for all other classes of this project.

    Attributes:
        __nb_objects: The number of instantiated Bases.

    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new base.
        Args:
            id: This is the identity of the new bases

        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ This returns the JSON string representation"""
        if list_dictionaries is None or list_dictionaries == "[]":
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, _listobjs):
        """ Save object in a file """
        filename = "{}.json".format(cls.__name__)
        _listdic = []

        if not _listobjs:
            pass
        else:
            for i in range(len(_listobjs)):
                _listdic.append(_listobjs[i].to_dictionary())

        lists = cls.to_json_string(_listdic)

        with open(filename, 'w') as m:
            m.write(lists)

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of JSON string representation"""
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ This creates an instance """
        if cls.__name__ == "Rectangle":
            new = cls(1, 1)
        else:
            new = cls(1)
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        """ Returns a list of instances """
        filename = "{}.json".format(cls.__name__)

        if os.path.exists(filename) is False:
            return []

        with open(filename, 'r') as m:
            list_str = m.read()

        _listcls = cls.from_json_string(list_str)
        _listobj = []

        for index in range(len(_listcls)):
            _listobj.append(cls.create(**_listcls[index]))

        return _listobj

    @classmethod
    def save_to_file_csv(cls, _listobjs):
        """This writes the CSV serialization of a list of objects to a file.
        Args:
            _listobjs (list):  This lists inherited Base instances.

        """
        filename = "{}.csv".format(cls.__name__)
        if cls.__name__ == "Rectangle":
            _listdic = [0, 0, 0, 0, 0]
            _listkeys = ['id', 'width', 'height', 'x', 'y']
        else:
            _listdic = [0, 0, 0, 0]
            _listkeys = ['id', 'size', 'x', 'y']

        jos = []
        if _listobjs:
            for obj in _listobjs:
                for i in range(len(_listkeys)):
                    _listdic[i] = obj.to_dictionary()[_listkeys[i]]
                jos.append(_listdic[:])

        with open(filename, 'w') as m:
            writer = csv.writer(m)
            writer.writerows(jos)

    @classmethod
    def load_from_file_csv(cls):
        """This deserialises the CSV file"""
        filename = "{}.csv".format(cls.__name__)

        if os.path.exists(filename) is False:
            return []

        with open(filename, 'r') as m:
            reader = csv.reader(m)
            _listrows = list(reader)

        if cls.__name__ == "Rectangle":
            _listkeys = ['id', 'width', 'height', 'x', 'y']
        else:
            _listkeys = ['id', 'size', 'x', 'y']

        jos = []
        for row in _listrows:
            _dicrow = {}
            for elt in enumerate(row):
                _dicrow[_listkeys[elt[0]]] = int(elt[1])
            jos.append(_dicrow)

        _listobjs = []
        for i in range(len(jos)):
            _listobjs.append(cls.create(**jos[i]))

        return _listobjs
