import argparse

parser = argparse.ArgumentParser(description='argparse demo')
parser.add_argument('file', help='target file')
parser.add_argument('-n', '--number', action='store_true', help='show line number')
args = parser.parse_args()

# python counter.py big.log -n
with open(args.file) as f:
    for idx, line in enumerate(f, 1):
        print(f'{idx}: {line}' if args.number else line, end='')
