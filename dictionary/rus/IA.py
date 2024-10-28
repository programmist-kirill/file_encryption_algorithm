#IA = я

import sys

def check_and_write(characters):
    if 'я' in characters:
        a0 = 'ф'
        sys.path.append('/home/kirill/file_encryption_algorithms/')
        import write_string

        write_string.write(a0)
        