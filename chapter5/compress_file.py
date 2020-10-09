gz_file = 'test_file.gz'
bz_file = 'test_file.bz2'

# gzip compression
import gzip
with gzip.open(gz_file, 'rt') as f:
    text = f.read()

# bz2 compression
import bz2
with bz2.open(bz_file, 'rt') as f:
    text = f.read()


# gzip compression
import gzip
with gzip.open(gz_file, 'wt') as f:
    f.write(text)

# bz2 compression
import bz2
with bz2.open(bz_file, 'wt') as f:
    f.write(text)


with gzip.open(gz_file, 'wt', compresslevel=3) as f:
    f.write(text)


import gzip
f = open(gz_file, 'rb')
with gzip.open(f, 'rt') as g:
    text = g.read()
