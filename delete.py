import hashlib, hmac, os, stat, sys

def file_hash(name):
    f = open(name)
    h = hashlib.sha256()
    while True:
        buf = f.read(16384)
        if len(buf) == 0: break
        h.update(buf)
    f.close()
    return h.hexdigest()

def traverse(h, path):
    rs = os.lstat(path)
    quoted_name = repr(path)
    if stat.S_ISDIR(rs.st_mode):
        h.update('dir ' + quoted_name + '\n')
        for entry in sorted(os.listdir(path)):
            traverse(h, os.path.join(path, entry))
    elif stat.S_ISREG(rs.st_mode):
        h.update('reg ' + quoted_name + ' ')
        h.update(str(rs.st_size) + ' ')
        h.update(file_hash(path) + '\n')

h = hashlib.sha256()
for root in sys.argv[1:]:
    traverse(h, 'D\\test')
    h.update('end\n')
print (h.hexdigest())
