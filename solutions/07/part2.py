################################################################################
# part2.py
################################################################################

import logging

logging.basicConfig()
log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)

# Read in the contents of our INPUT

with open('input.txt') as input_file:
    input_data = input_file.readlines()

# Process each input line. Determine what entry type it is; cd, ls, dir or file
# and take the appropriate action.

current_path = ''
directories = {}

for input_line_raw in input_data:
    input_line = input_line_raw.strip()

    # Change directory.  Parse out the 'where' and calculate our current
    # path...

    if input_line.startswith('$ cd'):
        cd_to = input_line[5:]

        log.debug('cd: %s', cd_to)

        # move UP on level
        if cd_to == '..':

            # Split into directory names while dropping the first entry, as
            # it is the left of root ('/') and always ''. When moving up,
            # make sure you deal with the special case of '.. back to /', as
            # our path segments will be empty...

            path_segments = current_path.split('/')[1:]

            if len(path_segments) == 0:
                current_path = '/'
            else:
                current_path = '/' + '/'.join(path_segments[:-1])

        # move DOWN into directory...
        else:

            # Move to the specified subdir. Make sure CD to / returns you to
            # root. Also, if current path is '/', don't prefix with another '/'!

            if cd_to == '/':
                current_path = '/'
            else:
                if current_path == '/':
                    current_path += cd_to
                else:
                    current_path += '/' + cd_to

    # List Files... We don't care about this, so move to next line.

    elif input_line.startswith('$ ls'):
        continue

    # Directory Item... We don't care about this, so move to next line.

    elif input_line.startswith('dir'):
        continue

    # Everything else, should just be File items.

    else:

        # Split the file item into 2 pieces; size and name. Also break up
        # our path so we can use it to figure out what entries to update.

        file_info = input_line.split(' ')
        path_segments = current_path.split('/')

        # For each segment of the path, add file size to EACH ONE.

        update_path = ''
        for dir_name in path_segments:
            
            if dir_name == '':
                update_path = '/'
            else:
                if update_path == '/':
                    update_path += dir_name
                else:
                    update_path += '/' + dir_name

            # If directories doesn't contain this path, seed it 0.

            if update_path not in directories:
                directories[update_path] = 0

            # Add the file size to the path.

            log.debug('adding %s to %s', file_info[0], update_path)
            directories[update_path] += int(file_info[0])

# Review each directory entry size looking for anything over what we need to
# fre up. If it meets the critera and is SMALLER than what we've already found,
# use it instead!

# root will always be the largest, so start with that...
result = directories['/']

for entry in directories:

    if directories[entry] >= (30000000 - 21618835):
        if directories[entry] < result:
            result = directories[entry]

print(result)

################################################################################
# END
################################################################################
