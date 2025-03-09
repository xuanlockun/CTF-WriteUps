import base64

def xor_decrypt(enc_msg):
    try:
        decoded = bytearray(base64.b85decode(enc_msg))
        for i in range(len(decoded)):
            decoded[i] ^= (i % 256)  # Reverse XOR operation
        return decoded.decode(errors="ignore")
    except Exception as e:
        return f"[Error]: {e}"  # Handle any decoding errors

# Read encrypted messages from output.txt
with open('chall.txt', 'r') as f:
    encrypted_msgs = [line.strip() for line in f.readlines() if line.strip()]

# Decrypt all messages
for enc in encrypted_msgs:
    decrypted_msg = xor_decrypt(enc)
    if "VishwaCTF{" in decrypted_msg:  # Check if it's the flag
        print("[FLAG FOUND]:", decrypted_msg)
    else:
        print("[DECRYPTED]:", decrypted_msg)