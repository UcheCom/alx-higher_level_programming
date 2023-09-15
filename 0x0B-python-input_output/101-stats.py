#!/usr/bin/python3
"""This script reads stdin line by line and computes metrics
After every ten lines or the input of a keyboard interruption (CTRL + C),
prints the following statistics:
    - Total file size up to that point.
    - Count of read status codes up to that point.
"""
import sys


class Stats:
    """Defines a Stats class to print stats info"""

    def __init__(self):
        """Initialize the dict that will hold informations
           and the size
        """
        self.dict = {}
        self.size = 0

    def init_info(self):
        """init info in the dic"""
        self.dict["200"] = 0
        self.dict["301"] = 0
        self.dict["400"] = 0
        self.dict["401"] = 0
        self.dict["403"] = 0
        self.dict["404"] = 0
        self.dict["405"] = 0
        self.dict["500"] = 0

    def inc_status(self, status):
        """Increment the number of status code"""
        if status in self.dict:
            self.dict[status] += 1

    def print_info(self):
        """Print info"""
        print("File size: {}".format(self.size))
        for key in sorted(self.dict.keys()):
            if self.dict[key] != 0:
                print("{}: {:d}".format(key, self.dict[key]))


if __name__ == "__main__":
    stat = Stats()
    stat.init_info()
    counter = 0

    try:
        for line in sys.stdin:
            if counter != 0 and counter % 10 == 0:
                stat.print_info()

            try:
                word_line = [x for x in line.split(" ")]
                stat.inc_status(word_line[-2])
                stat.size += int(word_line[-1].strip("\n"))
            except Exception:
                pass

            counter += 1
    except KeyboardInterrupt:
        stat.print_info()
        raise
