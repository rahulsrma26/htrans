"""
libri [Convert-LibriSpeech]
===========================
Converts the LibriSpeech text from english to hindi using htrans.
"""

import os
import shutil
from argparse import ArgumentParser, RawTextHelpFormatter

from cmu2dev import CMU2DEV
from eng2cmu import wordbreak


def _convert(trans_file):
    backup = trans_file + '.old'
    if not os.path.isfile(backup):
        shutil.copyfile(trans_file, backup)
    with open(trans_file, 'w') as out_file, open(backup, 'r') as in_file:
    # with open(backup, 'r') as in_file:
        for line in in_file:
            line = line.strip()
            # print(f'line: "{line}"')
            words = line.split(' ')
            cmu = [wordbreak(word)[0] for word in words[1:]]
            # print(f'cmu: "{cmu}"')
            converted = [CMU2DEV.convert(word) for word in cmu]
            # print(f'converted: "{converted}"')
            out_file.write(f"{words[0]} {' '.join(converted)}\n")


def _args():
    prog_name = os.path.basename(__file__)
    parser = ArgumentParser(
        prog=prog_name, description=__doc__, formatter_class=RawTextHelpFormatter)
    parser.add_argument(
        'dir', type=str, help='directory path of the content like ./dev-clean')
    args = parser.parse_args()
    if not os.path.isdir(args.dir):
        print('Invalid dir', args.dir)
        exit(1)
    return args


def _main():
    args = _args()
    for book in os.listdir(args.dir):
        book_path = os.path.join(args.dir, book)
        if os.path.isdir(book_path):
            print('Processing book', book)
            for chapter in os.listdir(book_path):
                chapter_path = os.path.join(book_path, chapter)
                print('\tProcessing chapter', chapter)
                trans_file = os.path.join(chapter_path, f"{book}-{chapter}.trans.txt")
                if not os.path.isfile(trans_file):
                    print('\tError file not found', trans_file)
                    continue
                _convert(trans_file)


if __name__ == "__main__":
    _main()
