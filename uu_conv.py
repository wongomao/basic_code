import sys
from codecs import encode
import uu
import os

def do_k(filename):
    CHUNK_SIZE = 102400
    write_filename_base = os.path.splitext(filename)[0] + 'UU'
    write_filename_counter = 1
    with open(filename, 'rb') as f:
        data = f.read(CHUNK_SIZE)
        while data:
            encoded = encode(data, 'uu')
            write_filename = '{0}{1}.txt'.format(write_filename_base, write_filename_counter)
            with open(write_filename, 'wt') as f2:
                f2.write(str(encoded, 'utf-8'))
                write_filename_counter += 1
            data = f.read(CHUNK_SIZE)


def main():
    if len(sys.argv) < 2:
        print("File not specified.")
        raise
    do_k(sys.argv[1])


if __name__ == '__main__':
    main()
