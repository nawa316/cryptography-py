def xor_bytes(*args: bytes) -> bytes:
    """XOR multiple byte strings. If lengths differ, shorter ones repeat cyclically."""
    if not args:
        return b''
    max_len = max(len(a) for a in args)
    # Repeat each arg to match max length
    repeated = [bytes(a[i % len(a)] for i in range(max_len)) for a in args]
    # XOR all
    result = bytearray(max_len)
    for a in repeated:
        for i, b in enumerate(a):
            result[i] ^= b
    return bytes(result)


def repeat_key(key: bytes, length: int) -> bytes:
    """Repeat a key cyclically to the desired length."""
    return bytes(key[i % len(key)] for i in range(length))


def fix_hex(s: str) -> str:
    """Ensure hex string has even length."""
    return s if len(s) % 2 == 0 else "0" + s


# --- Given data (hex) ---
hex_values = {
    "k1":    "3c3f0193af37d2ebbc50cc6b91d27cf61197",
    "k21":   "ff76edcad455b6881b92f726987cbf30c68c",
    "k23":   "611568312c102d4d921f26199d39fe973118",
    "k1234": "91ec5a6fa8a12f908f161850c591459c3887",
    "f45":   "0269dd12fe3435ea63f63aef17f8362cdba8",
}

# --- Convert hex to bytes ---
for key in hex_values:
    hex_values[key] = bytes.fromhex(fix_hex(hex_values[key]))

k1, k21, k23, k1234, f45 = (
    hex_values["k1"],
    hex_values["k21"],
    hex_values["k23"],
    hex_values["k1234"],
    hex_values["f45"],
)

# --- Step 1: Reconstruct all keys ---
KEY1 = k1
KEY2 = xor_bytes(k21, KEY1)
KEY3 = xor_bytes(KEY2, k23)
KEY4 = xor_bytes(k1234, KEY1, KEY3, KEY2)

# --- Step 2: Derive KEY5 (4-byte) using known prefix 'cry{' ---
flag_prefix = b"cry{"
KEY5 = xor_bytes(flag_prefix, KEY4[:4], f45[:4])

# --- Step 3: Recover full FLAG ---
KEY5_full = repeat_key(KEY5, len(f45))
FLAG = xor_bytes(f45, KEY4, KEY5_full)

# --- Step 4: Display results ---
print(f"{FLAG.decode('utf-8')}")
