""""""

'''Integer Representation'''
'''
    --> Represented internally base-2(binary) digits not decimal
        
                               1     0     0     1     1 
            ----  ----  ----  ----  ----  ----  ----  ----   
            2**7  2**6  2**5  2**4  2**3  2**2  2**1  2**0
            
                              1x16 + 0x8 + 0x4 + 1x2 + 1x1 = 16+2+1 = 19
                                          (10011)2 = (19)10
                                     5 bits represent 19 decimal value
                                     
        --> So, 8 bit represent = 256 = (2**8)
                        0-255 = 256
                         0-7  =  8
        --> Range Split by (2**7) - 1 = 128 - 1 = 127
        --> 8bits represent range            [-128, 127]                        (2**7) - 1
        --> 16bits represent range           [-32,768, 32,767]                  (2**15) - 1
        --> 32bits represent range           [-2,147,483,648, 2,147,483,647]    (2**31) - 1
'''

import sys
import time

print(type(100))
print(sys.getsizeof(0))
print(sys.getsizeof(1))
print(sys.getsizeof(2**1000))


def cal(a):
    star_time = time.perf_counter()
    for i in range(10000000):
        a * 2
    end_time = time.perf_counter()
    return end_time - star_time


print('10000000 times, 10 * 2:', cal(10))
print('10000000 times, 2 ** 100:', cal(2**100))
print('10000000 times, 2 ** 10000:', cal(2**10000))
