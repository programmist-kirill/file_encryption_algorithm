import sys

def check_and_write(characters):
    if 'д' in characters:
        a0 = 'э'
        sys.path.append('/home/kirill/file_encryption_algorithms/')
        import write_string

        write_string.write(a0)
        