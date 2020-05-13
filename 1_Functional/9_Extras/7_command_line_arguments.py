import sys

print(sys.argv)

keys = sys.argv[1::2]
values = sys.argv[2::2]

args = {k: v for k, v in zip(keys, values)}

fname = args.get('--fname', None)
lname = args.get('--lname', None)
age = args.get('--age', None)
print(fname, lname, age)
