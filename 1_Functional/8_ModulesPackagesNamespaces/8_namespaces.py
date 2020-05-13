""""""

'''Namespace Packages'''
'''
    --> like package but doesn't contain __init__.py
    --> PEP 420
    --> utils/
            validators/
                boolean.py
                date.py
                json/
                    __init__.py
                    serializers.py
                    validators.py
    --> Regular Package                             Namespace Package
        type            -> module                   type         -> module
        __init.__py     -> yes                      __init__.py  -> no
        __file__        -> package __init__         __file__     -> not set
        paths           -> path not dynamically     paths        -> dynamic path
                           computed                                 computation
'''