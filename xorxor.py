# k1=3c3f0193af37d2ebbc50cc6b91d27cf61197
# k21=ff76edcad455b6881b92f726987cbf30c68c
# k23=611568312c102d4d921f26199d39fe973118
# k1234=91ec5a6fa8a12f908f161850c591459c3887
# f45=0269dd12fe3435ea63f63aef17f8362cdba8

# k1=KEY1 
# k21=KEY2 ^ KEY1 
# k23=KEY2 ^ KEY3 
# k1234=KEY4 ^ KEY1 ^ KEY3 ^ KEY2 
# f45=FLAG ^KEY4^KEY5

# Data dari soal (hex string)
k1_hex = "3c3f0193af37d2ebbc50cc6b91d27cf61197"
k21_hex = "ff76edcad455b6881b92f726987cbf30c68c"
k23_hex = "611568312c102d4d921f26199d39fe973118"
k1234_hex = "91ec5a6fa8a12f908f161850c591459c3887"
f45_hex = "0269dd12fe3435ea63f63aef17f8362cdba8"

# Ubah ke bytes
k1 = bytes.fromhex(k1_hex)
k21 = bytes.fromhex(k21_hex)
k23 = bytes.fromhex(k23_hex)
k1234 = bytes.fromhex(k1234_hex)
f45 = bytes.fromhex(f45_hex)

# Fungsi bantu XOR
def xor_bytes(a, b):
    return bytes(x ^ y for x, y in zip(a, b))

# Dari relasi:
# k21 = KEY2 ^ KEY1  →  KEY2 = k21 ^ KEY1
# k23 = KEY2 ^ KEY3  →  KEY3 = k23 ^ KEY2 = k23 ^ k21 ^ KEY1
# k1234 = KEY4 ^ KEY1 ^ KEY3 ^ KEY2 → KEY4 = k1234 ^ KEY1 ^ KEY3 ^ KEY2
# f45 = FLAG ^ KEY4 ^ KEY5 → FLAG = f45 ^ KEY4 ^ KEY5

# Karena KEY5 adalah 4-byte rahasia (tidak diketahui), kita brute-force
# misalnya, kita asumsikan flag diawali dengan "cry{".

prefix = b"cry{"
for k5_int in range(0, 2**32):
    KEY5 = k5_int.to_bytes(4, 'big')
    KEY2 = xor_bytes(k21, k1)
    KEY3 = xor_bytes(k23, KEY2)
    KEY4 = xor_bytes(k1234, xor_bytes(xor_bytes(KEY1 := k1, KEY2), KEY3))
    FLAG = xor_bytes(f45, xor_bytes(KEY4, KEY5))
    if FLAG.startswith(prefix):
        print("Possible KEY5:", KEY5.hex())
        print("FLAG:", FLAG)
        break
