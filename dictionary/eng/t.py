import sys

def check_and_write(characters):
    if 't' in characters:
        a0 = 'n'
        sys.path.append('/home/kirill/file_encryption_algorithms/')
        import write_string

        write_string.write(a0)
        