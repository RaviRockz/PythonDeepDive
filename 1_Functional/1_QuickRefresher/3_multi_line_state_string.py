""""""

'''Python Program'''
'''
    --> Text Document
    --> Physical lines of code  # Ends with newline character
    --> Logical lines of code  # Ends with token
    --> Tokenized
    --> Conversion can be implicit and explicit
        -> Implicit (Support Inline Comments)
            * List Literals  [1,  # item 1
                              2,  # item 2
                              3]  # item 3
            * Tuple Literals
            * Dictionary Literals
            * Set Literals
            * Function args / params
        -> Explicit (Don't Support Inline Comments)
            * String Literals  'Hello' \
                               'World'
            * Condition Statements
'''

lst = [1,  # item 1
       2,  # item 2
       3]  # item 3

if 1 < 2 \
        and 2 > 1:
    print(True)

a = 'this is a string'
print(a)
a = 'this is a \nnewline string'
print(a)

a = 'this is a' \
    'continuation string'
print(a)

a = '''this is a
multiline string'''
print(a)
