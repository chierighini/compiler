import os, argparse, json

#argument parser -> usage: python3 compilador.py path_to_script
parser = argparse.ArgumentParser(description="Compiler")
parser.add_argument('script', metavar='S',help='A path to a script to be compiled')
args = parser.parse_args()

def main():
    '''
    reads script from first argument path and reserved symbols json file,
    splits every line per space, calls out identification function and writes out
    the token list in a temporary file
    '''
    with open (args.script) as f:
        raw_content = f.readlines()
    with open('src/reserved.json') as res:
        reserved = json.load(res)
    op_queue = []
    content = splitter(raw_content)
    identifier(content, op_queue,reserved)    
    with open('tmp/tokens.txt','w') as t:
        for el in op_queue:
            t.write(str(el) + '\n')

def splitter(ob):
    '''
    splits every line into smaller elements of an array, separated by the spaces
    '''
    symbol_queue = [x.split(' ') for x in ob]
    #final_queue = [x.replace('\n','') for x in symbol_queue]
    return symbol_queue

def identifier(ob, op_q, reserved):
    '''
    identifies if the elements of a list are not lists, 
    and recursively gets to the strings for token identification and 
    stores them in per-line lists inside a larger list, 
    removing line breaks and tabs
    '''
    q= []
    for el in ob:
        if(isinstance(el, list)):
            identifier(el,op_q,reserved)
        else:
            if(el.find('\n')!= -1 or el.find('\t')!= -1):
                el = el.replace('\n','')
                el = el.replace('\t','')
            if(el in reserved['line_breaker']):
                q.append('LINE_END')
            elif(el in reserved["words"]):
                q.append('RES_WORD')
            elif(el in reserved["operators"]):
                q.append('OPERATOR')
            elif(el in reserved["delimitators"]):
                q.append('DELIM')
            elif(el in reserved["declarators"]):
                q.append('DECLAR')
            elif(el in reserved["separators"]):
                q.append('SEPRT')
            elif(el in reserved["comment"]):
                break
            else:
                try:
                    int(el)
                except ValueError:
                    if(el != ''):
                        q.append("VARIABLE")
                else:
                    q.append("VALUE")
    op_q.append(q)

            

if __name__ == '__main__':
    main()