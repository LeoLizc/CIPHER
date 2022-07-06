from codifier import *
import argparse

def read_file(file):
    '''
    Reads a file and returns the content as a string.
    '''
    with open(file, 'r') as f:
        return f.read()
# ----------------------------------------------------------------------------------------------------------------------

_examples = """
examples:
    ...
"""

# ----------------------------------------------------------------------------------------------------------------------

def main():

    parser = argparse.ArgumentParser(
        description='''Cipher encripter.\n
        
        Run python %(prog)s -h for more information.''',
        epilog=_examples,
    )

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-m', '--message', help='Message to cipher', dest='message')
    group.add_argument('-f', '--file', help='File with the message to cipher', dest='message', type=read_file)

    parser.add_argument('-o', '--output', help='Output file', metavar='FILE')

    # ENCRYPTION TYPES TIPELINE
    parser.add_argument('-c', '--caesar',
        help='''Use caesar cipher. 
        The key is the number of letters to shift. 
        can be negative. (default: %(const)s)''',
        metavar='KEY',
        action='append',
        dest='ciphers',
        nargs='?',
        const='3',
        type = lambda x: (caesarCipher, int(x)),
    )
    parser.add_argument(
        '-k', '--keyword',
        help='''Use keyword substitution cipher. 
        The key is the keyword. 
        (the key must be a string with no duplicate characters)''', 
        metavar='KEY',
        action='append',
        dest='ciphers',
        type=lambda x: (keywordCipher, x),
    )
    
    args = parser.parse_args()
    if not args.ciphers:
        args.ciphers = [(caesarCipher, 3)]

    # print(args.ciphers)
    # print('message:', args.message)

    # APPLY CIPHERS
    message = args.message
    for cipher, key in args.ciphers:
        message = cipher(message, key)
    
    # WRITE THE MESSAGE
    if args.output:
        with open(args.output, 'w') as f:
            f.write(message)
    else:
        print(message)



if __name__ == '__main__':
    # print(caesarCipher('Hello, World!', 3))
    main()