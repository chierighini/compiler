import os, argparse, json

parser = argparse.ArgumentParser(description="Compiler")
parser.add_argument('script', metavar='S',help='A path to a script to be compiled')
args = parser.parse_args()

def main():
    with open (args.script) as f:
        raw_content = f.readlines()
    with open('reserved.json') as res:
        reserved = json.load(res)
    op_queue = []
    content = splitter(raw_content)
    identifier(content, op_queue,reserved)

def splitter(ob):
    '''
    splits every line into smaller elements of an array, separated by the spaces
    '''
    symbol_queue = [x.split(' ') for x in ob]
    return symbol_queue

def identifier(ob, q, reserved):
    '''
    identifies if the elements of a list are not lists, 
    and recursively gets to the strings for identification
    '''
    for el in ob:
        if(isinstance(el, list)):
            identifier(el,q,reserved)
        else:
            if(el.find('\n')!= -1):
                pass


if __name__ == '__main__':
    main()