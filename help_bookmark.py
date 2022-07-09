#!/usr/bin/env python3

from misc import COMMANDS, \
                 exit_if, \
                 HELP_USAGE, INVALID_COMMAND

from sys import argv


def main():
    if len(argv) == 1:
        print(COMMANDS)
        exit(0)
        
    if len(argv) == 2:
        command = argv[1]
        
        if command == 'bm':
            print('\t----bm----\n\n\
Prints the bookmarks from the current directory.\n\n\
Has the following flags:\n\
\t-a or --all == Prints all the books which have been bookmarked and their respective directory.')
        elif command == 'initbm':
            print('\t----initbm----\n\n\
Creates a bookmark file in the current directory.')
        elif command == 'delbm':
            print('\t----delbm----\n\n\
Deletes the bookmark file from the current directory.')
        elif command == 'addbm':
            print('\t----addbm----\n\n\
Adds a bookmark and a short description to the current bookmark file.')
        elif command == 'gotobm':
            print('\t----gotobm----\n\n\
Given a title of a book (the title is the one found when using bm -a) goes to its respective directory.')
        elif command == 'helpbm':
            print('\t----helptodo----\n\n\
Takes zero or one argument:\n\
For 0 arguments lists all possible commands.\n\
For 1 argument prints the description of the command given as an argument.')
        else:
            exit_if(True, INVALID_COMMAND)
            
        exit(0)
        

    exit_if(True, HELP_USAGE)


if __name__ == '__main__':
    main()
    