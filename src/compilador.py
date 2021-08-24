import os, argparse

parser = argparse.ArgumentParser(description="Compiler")
parser.add_argument('script', metavar='S',help='A path to a script to be compiled')
args = parser.parse_args()

def main():
    with open (args.script) as f:
        content = f.readlines()
        op_queue = []
        content_splite = splitter(content)

def splitter(ob):
    symbol_queue = [x.split(' ') for x in ob]
    return symbol_queue

def identifier(ob, q):
    for el in ob:
        if(isinstance(el, list)):
            identifier(ob,q)
        else:
            pass#logic for identifying elements in the code


if __name__ == '__main__':
    main()