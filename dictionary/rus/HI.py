#HI = ь

import sys

def check_and_write(characters):
    if 'ь' in characters:
        a0 = 'о'
        sys.path.append('/home/kirill/file_encryption_algorithms/')
        import write_string

        write_string.write(a0)
        