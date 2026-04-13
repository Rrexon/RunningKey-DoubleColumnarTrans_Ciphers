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



def running_key_decryption_alg(key, ciphertext):

    plaintext = ""

    ciphertext = ciphertext.lower().replace(" ", "")
    key = key.lower().replace(" ", "")

    for i in range(len(ciphertext)):

        c_value = ord(ciphertext[i]) - ord('a')
        k_value = ord(key[i]) - ord('a')

        p_value = (c_value - k_value) % 26
        plaintext += chr(p_value + ord('a'))

    return plaintext
