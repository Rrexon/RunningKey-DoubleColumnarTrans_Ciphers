def running_key_encryption_alg(key, plaintext):
    ciphertext = ""

    plaintext = plaintext.lower().replace(" ", "")
    key = key.lower().replace(" ", "")

    for i in range(len(plaintext)):

        p_value = ord(plaintext[i]) - ord('a')
        k_value = ord(key[i]) - ord('a')

        c_value = (p_value + k_value) % 26
        ciphertext += chr(c_value + ord('a'))

    return ciphertext
