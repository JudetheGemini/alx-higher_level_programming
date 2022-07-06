#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    ol = list(a_dictionary.keys())
    ol.sort()
    for i in ol:
        print("{}: {}".format(i, a_dictionary.get(i)))
