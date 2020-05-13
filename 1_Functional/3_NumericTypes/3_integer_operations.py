""""""

'''Integer Operations'''
'''
    Operations      Symbol    input     Return type
    addition          +      int, int       int
    subtraction       -      int, int       int
    multiplication    *      int, int       int
    division          /      int, int      float
    floor division    //     int, int       int
    modulo            %      int, int       int
    exponent          **     int, int       int
    
    input sign                           operation    output  sign
    [(+, +), (-, -), (+, -), (-, +)]         +        [+, +, -, -]
    [(+, +), (-, -), (+, -), (-, +)]         -        [+, +, -, -]
    [(+, +), (-, -), (+, -), (-, +)]         *        [+, +, -, -]
    [(+, +), (-, -), (+, -), (-, +)]         /        [+, +, -, -]
    [(+, +), (-, -), (+, -), (-, +)]         //       [+, +, -, -]
    [(+, +), (-, -), (+, -), (-, +)]         %        [+, -, -, +]
    [(+, +), (-, -), (+, -), (-, +)]         **       [+, +, -, -]
'''

print(135 % 4)
print(-135 % -4)
print(135 % -4)
print(-135 % 4)

