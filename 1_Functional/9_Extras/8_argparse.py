""""""

'''argparse'''
'''
    --> ArgumentParser
        -> description -> base
    --> add_argument method
        -> short -> -s
        -> long -> --square
        -> help -> description for argument
        -> type -> int
        -> default -> default value if user not pass it uses defaults
        -> const -> constant value for arg
        -> required -> if arg is required or not
        -> dest -> store value to parser attribute
        -> action -> default 'store'
            * store_const -> if passed take const else default if default mentioned else None
            * store_false -> if not passed takes True else False
                                (action=store_const, const=False, default=True)
            * store_true -> if not passed takes False else True
                                (action=store_const, const=True, default=False)
    --> access args via dest if dest is set else short/long
        -> parser.a
        -> parser.b
    --> add_mutually_exclusive_group()
        -> pass any one option only
'''