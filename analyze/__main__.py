# A file not connected to Flask, in which you can debug
from analyze.analyzer import analyze_file
from pprint import pprint
import argparse


def get_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description='Performs the shmdoc analyze on the passed files',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('files', nargs='+', type=str, action='store', help='files to analyze', )
    parser.add_argument('-t', '--type', type=str, default=None, action='store', help='type of file-anaylsis to use', )
    return parser


def main():
    parser = get_arg_parser()
    args = parser.parse_args()
    vargs = vars(args)
    files = vargs['files']
    type = vargs['type']
    for fname in files:
        result = analyze_file(fname, type)
        print("*** Result for file %s" % fname)
        pprint(result)


if __name__ == '__main__':
    main()
