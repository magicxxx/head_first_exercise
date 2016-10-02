#!/usr/bin/env python


def print_lol(the_list):
    '''
    print elements of list no matter that is single element or a list.
    '''
    for each_item in the_list:
        if isinstance(each_item, list):
            print_lol(each_item)
        else:
            print each_item

