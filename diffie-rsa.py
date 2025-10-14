from Crypto.util.number import getPrime, bytes_to_long, long_to_bytes
import gmpy2

p = getPrime(1024)
q = getPrime(1024)
p_dh = getPrime(2048)
g = getPrime(512)
a = getPrime(512)
b = getPrime(512)

def generate_public_int(g, a, p):
    return g ^ a % p

def generate_shared_secret(A, b, p):
    return A ^ b % p

n = p * q
e = 3
flag = SECRET
flag_int = bytes_to_long(flag)
A = generate_public_int(g,a,p_dh)
B = generate_public_int(g,b,p_dh)
shared_int = generate_shared_secret(A, b, p_dh)
flag2 = flag_int ^ shared_int
c = pow(flag2, e, n)

print(f"e = {e}")
print(f"n = {n}")
print(f"c = {c}")
print(f"p_dh = {p_dh}")
print(f"g = {g}")
print(f"A = {A}")
print(f"B = {B}")