# File Manipulation

# Modes:
# r for read (default)
# r+ for read and write (keeps existing file)
# w for write (overwrites)
# a for append

# we can add `b` to open in binary mode (default is text mode)

f = open('file.data', 'w', encoding='utf-8')
f.readline()
f.close()

f.closed # True

# Better way
with open('file.data', encoding='utf-8') as f:
    data = f.read()

f.closed # True


# === Reading ===

f.read() # reads all content

f.read(1) # read 1 byte
f.read(1024) # read 1024 bytes

f.readline() # read until \n (included)

# Looping throughout the lines
for line in f:
    print(line)


# === Writing ===
f.write('A linhe\n')

# writes string as binary
f.write(b'0123456789abcdef')

my_tuple = ('answer', 42)
f.write(str(my_tuple))


# === Navigating ===

# returns the current position (# bytes when binary mode and text position when text mode)
current_position f.tell()

offset = 10
offset = -1 # rewinding
# 0 -> beginning of the file; 1 -> current position; 2 -> end of the file
f.seek(offset, 0)


# === JSON ===
# To facilitate the read/write complex values we can use json module
import json
json.dumps([1, 2]) # '[1, 2]'
json.dumps([1, 2, 3, 4, 5], f) # writes to file

my_value = json.load(f)

# === Pickle module ===
# We can use pickle to read/write complex values as binaries
import pickle
pickle.dumps([1, 2]) # b'\x80\x03]q\x00(K\x01K\x02e.'
pickle.dumps([1, 2], f) # writes to file

# we can wrap a file with an instance of Pickle
pickler = pickle.Pickler(f)
pickler.dumps([1, 2])

pickle.load(f)