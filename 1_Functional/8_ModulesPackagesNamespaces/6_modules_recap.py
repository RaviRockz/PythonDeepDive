""""""

'''
    --> module imported using
        -> import and importlib.import_module
    --> when a module is imported
        -> sys cache first -> if found return reference from -> sys.modules
        -> sys.meta_path -> find builtins -> _frozen_importlib.BuiltinImporter
                         -> find frozen -> _frozen_importlib.FrozenImporter
        -> sys.path and package __path__ -> find file-based -> _frozen_importlib_external.PathFinder
        -> collections.__path__ -> ['/usr/lib/python3.6/collections']
    --> builtin -> import math
        -> math.__spec__
        -> math.__name__
        -> math.__package__
        -> __file__ -> builtins only not for math                  
'''