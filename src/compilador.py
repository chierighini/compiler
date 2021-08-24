import os, argparse

parser = argparse.ArgumentParser(description="Compiler")
parser.add_argument('script', metavar='S',help='A path to a script to be compiled')
args = parser.parse_args()

with open (args.script) as f:
    for line in f:
        pass