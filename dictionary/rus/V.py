import sys

def check_and_write(characters):
    if 'в' in characters:
        a0 = 'г'
        sys.path.append('/home/kirill/file_encryption_algorithms/')
        import write_string

        write_string.write(a0)
        