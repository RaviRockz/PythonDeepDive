""""""

'''Case-Sensitive'''
'''
    --> my_var and my_Var are different
    --> ham and Ham are different
'''
'''Rules'''
'''
    --> Starts with underscore (_) or letters (a-z A-Z)
    --> Followed by any number of underscores (_), letters (a-z A-Z) or digits (0-9)
    --> Cannot be reserved words
        None    True    False
        and     or      not
        if      else    elif
        for     while   break   continue    pass
        def     lambda  global  nonlocal    yield
        del     in      is      assert      class
        try     except  finally raise
        import  from    with    as
'''
'''Conventions'''
'''
    --> _my_var
        |
        |_Single Underscore --> Private objects
    --> __my_var
        |
        |_Double Underscore --> More Private (useful in inheritance chains)
    --> __my_var__
        |       |
        |_______| Before and After Double Underscore --> System Defined names, 
                                                         that have a special meaning
'''
'''Other Naming Conventions PEP8 Style Guide'''
'''
    --> Packages
        -> short, all-lowercase names, preferably no underscores
    --> Modules
        -> short, all-lowercase names, can have underscores
    --> Classes
        -> CapWords (Upper camel case)
    --> Functions
        -> lowercase, words separated by underscores
    --> Variables
        -> lowercase, words separated by underscores
    --> Constants
        -> all-upercase, words separated by underscores
'''
