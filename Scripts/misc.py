### LOCATIONS ###
BOOKS_FILE = '/mnt/e/Programming/BOOKMARK-CLI/Scripts/books.bm'
BOOKMARKS_FILE = 'bookmarks.bm'

### ERRORS ###
NO_FILES            = '[ERROR]: Please write the path to BOOKS_FILE and BOOKMARKS_FILE in the misc.py file.'
INVALID_FLAG        = '[ERROR]: Invalid flag: '
BOOKMARKS_NOT_FOUND = '[ERROR]: No bookmarks.bm file found here.'
BOOKMARKS_FOUND     = '[ERROR]: bookmarks.bm file already present here.'
PAGE_INT            = '[ERROR]: <PAGE> must be a natural number.'

### USAGES ###
TITLE_USAGE         = '[USAGE]: initbm <TITILE>.'
DESCRIPTION_USAGE   = '[USAGE]: addbm <PAGE> <DESCRIPTION>.'


### HELPERS ###
def exit_if(condition, message):
    if condition:
        print(message)
        exit(2)

def flag_message(flag):
    return INVALID_FLAG + flag + '.'

### FLAGS ###
FLAGS_PRINT = ['-a', '--all']

exit_if(BOOKS_FILE == '' or BOOKMARKS_FILE == '', NO_FILES)