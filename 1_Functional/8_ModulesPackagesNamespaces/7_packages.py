""""""

'''Packages'''
'''
    --> Packages are modules but not vice-versa
    --> it contains modules, sub-packages..,
    --> . indicates the path hierarchy
    --> everything is File Based Packages
        -> directories repr packages -> dir_name -> package_name
        -> code in a directory then it is a module
        -> __init__.py tells this directory is a package
    --> app.zip/
            package1/
                __init__.py
                module1.py
                module2.py
        import package1 --> code in __init__.py (loaded in sys.modules with package1)
    --> absolute path -> __path__, __file__
    --> Nested packages
        app.zip/
            package1/
                __init__.py
                module1.py      --> module inside package1              package1.module1
                module2.py
            package2/
                __init__.py     --> package inside package1             package1.package2
                module1.py      --> module inside package1.package2     package1.package2.module1
                module2.py
    --> modules have
        -> __file__, __package__ and __path__
    --> why packages?
        -> api.py                           -> api\
            * connect                              api.py
            * execute_no_result                    dbutilities.py
            * User                                 jsonutilities.py
            * Users                                typeconversions.py
            * UserProfile                          validations.py
            * authenticate ...,                    authorization.py
                                                   users.py ...,
                                                   
        -> api/
           |----utilities/
           |    |    __init__.py
           |    |----database/
           |    |    |  __init__.py
           |    |    |  connections.py
           |    |    |  queries.py
           |    |----json/
           |    |    |  __init__.py
           |    |    |  encoders.py
           |    |    |  decoders.py
           |----models/
           |    |    __init__.py
           |    |----Users/
           |    |       __init__.py
           |    |       user.py
           |    |       userprofile.py
           
    --> Easier to write
    --> Easier to test and debug
    --> Easier to read/understand
    --> Easier to document
'''