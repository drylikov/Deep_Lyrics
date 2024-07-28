#!/usr/bin/env python
__author__ = 'Tony Beltramelli www.tonybeltramelli.com - 19/08/2016'

import argparse
import codecs
from modules.Vocabulary import *


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_file', type=str, required=True)
    input_file = parser.parse_args().input_file

    vocabulary = Vocabulary()
    vocabulary.generate(input_file)

    output_file_name = "{}.vocab".format(input_file[:input_file.index('.')])
    output_file = open(output_file_name, 'w')
    output_file.write(vocabulary.get_serialized_binary_representation())
    output_file.close()

    print "Vocabulary saved in {}".format(output_file_name)

if __name__ == "__main__":
    main()
