#SH = щ
import sys

def check_and_write(characters):
    if 'щ' in characters:
        a0 = 'а'
        sys.path.append('/home/kirill/file_encryption_algorithms/')
        import write_string

        write_string.write(a0)
        