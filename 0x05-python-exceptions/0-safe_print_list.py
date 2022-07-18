#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        n = 0
        for i in my_list[:x]:
            print(i, end='')
            n += 1
        print()
        return (n)
    except (IndexError):
        print('Index does not exist')
