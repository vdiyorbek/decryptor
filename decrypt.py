from Crypto.Cipher import AES

# Hexdan bytlarga o'tkazishgit
aes_key = bytes.fromhex("269d97273d0f2604887802b29d984aa66a534fcf57c44962068423374f148a95")
encrypted_data = bytes.fromhex("d3733572aaa3a577393909b9665da127bae8952f45f99c0bcc5c329ebbfc00e6eefdb0ba7efd6b99e498")

# IV va shifrlangan ma'lumotni ajratish
iv = encrypted_data[:12]  # AES-GCM uchun 12 bayt IV
ciphertext = encrypted_data[12:-16]  # Oxirgi 16 bayt tag emas
tag = encrypted_data[-16:]  # AES-GCM tag (16 bayt)

# AES-GCM bilan dekodlash
cipher = AES.new(aes_key, AES.MODE_GCM, nonce=iv)

try:
    plaintext = cipher.decrypt_and_verify(ciphertext, tag)  # To‘g‘ri funksiya
    print(f"Decrypted IP: {plaintext.decode('utf-8')}")
except ValueError as e:
    print(f"Decryption failed: {e}")