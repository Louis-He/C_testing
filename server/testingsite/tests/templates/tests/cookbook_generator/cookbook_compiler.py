import argparse
import re

parser = argparse.ArgumentParser(
    description='Convert hello C file to html.')
parser.add_argument('--hcfile', type=str,
                    help='specify the hello C file you need', required=True)
args = parser.parse_args()


def classify_line(line):
    x = re.findall("\[.*\]", line)
    print(x)
    for tag in x:
        


def main():
    with open(args.hcfile, 'r') as hc_file:
        content = hc_file.readlines()
        for line in content:
            classify_line(line)


if __name__ == "__main__":

    main()
