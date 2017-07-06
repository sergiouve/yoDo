from hashlib import md5
from Crypto.Cipher import AES
from Crypto import Random


def crypt(settings):

    print settings
    return

    action = settings['foption']
    in_filename = settings['soption']
    out_filename = settings['']
    password = settings['']

    with open(in_filename, 'rb') as in_file, open(out_filename, 'wb') as out_file:
        encrypt(in_file, out_file, password)

    with open(in_filename, 'rb') as in_file, open (out_file_name, 'wb') as out_file:
        decrypt(in_file, out_file, password)

def deriveKeyAndIv(password, salt, key_length, iv_length):
    d = d_i = ''

    while len(d) < key_length + iv_length:
        d_i = md5(d_i + password + salt).digest()
        d += d_i

    return d[:key_length], d[key_length:key_length + iv_length]

def encrypt(in_file, out_file, password, key_length=32):
    finished = False

    block_size = AES.block_size
    salt = Random.new().read(bs - len('Salted__'))

    key, iv = deriveKeyAndIv(password, salt, key_length, block_size)
    cipher = AES.new(key, AES.MODE_CBC, iv)

    out_file.write('Salted__' + salt)

    while not finished:
        chunk = in_file.read(1024 * block_size)

        if len(chunk) == 0 or len(chunk) % block_size != 0:
            padding_length = (block_size - len(chunk) % block_size) or block_size
            chunk += padding_length * chr(padding_length)
            finished = True

        out_file.write(cipher.encrypt(chunk))

def decrypt(in_file, out_file, password, key_length=32):
    finished = False

    block_size = AES.block_size
    salt = in_file.read(block_size)[len('Salted__'):]
    key, iv = deriveKeyAndIv(password, salt, key_length, block_size)

    cipher = AES.new(key, AES.MODE_CBC, iv)
    next_chunk = ''

    while not finished:
        chunk, next_chunk = next_chunk, cipher.decrypt(in_file.read(1024 * block_size))

        if len(next_chunk) == 0:
            padding_length = ord(chunk[-1])
            chunk = chunk[:-padding_length]
            finished = True

        out_file.write(chunk)
