k1  = bytes.fromhex("c94133d85deeb56c7d7693863708cacc95bda79a5561a48f8cfdd64c119f4242263ba7")
k21 = bytes.fromhex("a33ce5d8c29f99dcd7c997901d9f1cef62fea5b338318c43099896d8b99b384fa1424f")  # KEY2 ^ KEY1
k23 = bytes.fromhex("130e347ddc61b9e934130643f69c7b7eb2c2a548078ec70d59f35cb08b642620145a54")  # KEY2 ^ KEY3
f123= bytes.fromhex("b32174d1e8fb79f16911f0aeaffbdddd401622a1379f16eea066aa92f58b010f500481")  # FLAG ^ KEY1 ^ KEY3 ^ KEY2

bxor = lambda a,b: bytes(x ^ y for x,y in zip(a,b))

k2 = bxor(k1, k21)            # KEY2 = (KEY2 ^ KEY1) ^ KEY1
k3 = bxor(k23, k2) # KEY3 = (KEY2^KEY1) ^ (KEY2^KEY3) ^ KEY1
flag = bxor(bxor(bxor(f123, k1), k3), k2)

print(flag.decode()) 

