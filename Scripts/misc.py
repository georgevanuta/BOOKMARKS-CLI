### LOCATIONS ###
BOOKS_FILE     = ''
BOOKMARKS_FILE = 'bookmarks.bm'


### ERRORS ###
NO_FILES            = '[ERROR]: Please write the path to BOOKS_FILE and BOOKMARKS_FILE in the misc.py file.'
INVALID_FLAG        = '[ERROR]: Invalid flag: '
BOOKMARKS_NOT_FOUND = '[ERROR]: No bookmarks.bm file found here.'
TITLE_NOT_FOUND     = '[ERROR]: Title not found in the books table.'
BOOKMARKS_FOUND     = '[ERROR]: bookmarks.bm file already present here.'
PAGE_INT            = '[ERROR]: <PAGE> must be a natural number.'
INVALID_COMMAND     = '[ERROR]: Command not found.'

### USAGES ###
TITLE_USAGE         = '[USAGE]: initbm <TITILE>.'
DESCRIPTION_USAGE   = '[USAGE]: addbm <PAGE> <DESCRIPTION>.'
GOTO_USAGE          = '[USAGE]: gotobm <TITLE>.'
HELP_USAGE          = '[USAGE]: helpbm | helpbm <BOOKMARK_COMMAND>.'

### HELPERS ###
def exit_if(condition, message):
    if condition:
        print(message)
        exit(2)


### FORMAT ###
def flag_message(flag):
    return INVALID_FLAG + flag + '.'


### FLAGS ###
FLAGS_PRINT = ['-a', '--all']


### CHECK IF COMPLETED PATH ###
exit_if(BOOKS_FILE == '' or BOOKMARKS_FILE == '', NO_FILES)


### FORMATING TABLE ###
HEADER_ALL_BOOKS        = '|PATH' + '\t' * 7 + '|BOOK' + '\t' * 7 + '|'
HEADER_LEN_SPACES       = 55
LINE_TABLE              = '+' + '-' * HEADER_LEN_SPACES + '+' + '-' * HEADER_LEN_SPACES + '+'

HEADER_CURRENT_SPACES   = 31
HEADER_CURRENT_BOOKS    = '|PAGE' + '\t' * 4 + '|DESCRIPTION' + 3 * '\t' + '|DATE' + '\t' * 4 + '|'
LINE_CURRENT_TABLE      = '+' + HEADER_CURRENT_SPACES * '-' + '+' + HEADER_CURRENT_SPACES * '-' + '+' + HEADER_CURRENT_SPACES * '-' + '+'

### ALL COMMANDS ###
COMMANDS = \
'\t----BOOKMARK Commands----\n\n\
-bm\n\
-initbm\n\
-delbm\n\
-addbm\n\
-gotobm\n\
-helpbm'