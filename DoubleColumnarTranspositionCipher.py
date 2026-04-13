import math

def columnar_transposition_encryption_alg(key, plaintext):

    ciphertext = ""

    plaintext = plaintext.lower().replace(" ", "")
    key = key.lower().replace(" ", "")

    numri_i_rreshtave = math.ceil(len(plaintext) / len(key))
    numri_i_kolonave = len(key)

    while len(plaintext) < (numri_i_rreshtave * numri_i_kolonave):
        plaintext += "x"

    matrica = [[0 for _ in range(numri_i_kolonave)] for _ in range(numri_i_rreshtave)]

    index = 0
    for i in range(numri_i_rreshtave):
        for j in range(numri_i_kolonave):
            matrica[i][j] = plaintext[index]
            index +=1

    ciftet = []
    for i in range(len(key)):
        ciftet.append([key[i], i])

    ciftet.sort()

    for cifti in ciftet:
        for j in range(numri_i_rreshtave):
            ciphertext += matrica[j][cifti[1]]

    return ciphertext


def double_columnar_transposition_encryption_alg(key1, key2, plaintext):

    ciphertext = columnar_transposition_encryption_alg(key1, plaintext)
    ciphertext2 = columnar_transposition_encryption_alg(key2, ciphertext)
    return ciphertext2


def columnar_transposition_decryption_alg(key, ciphertext):
    plaintext = ""

    key = key.lower().replace(" ", "")
    ciphertext = ciphertext.lower().replace(" ", "")

    numri_i_rreshtave = len(ciphertext) // len(key)
    numri_i_kolonave = len(key)

    matrica = [[0 for _ in range(numri_i_kolonave)] for _ in range(numri_i_rreshtave)]

    ciftet = []
    for i in range(numri_i_kolonave):
        ciftet.append([key[i], i])

    ciftet.sort()

    index = 0

    for cifti in ciftet:
        for i in range(numri_i_rreshtave):

            matrica[i][cifti[1]] = ciphertext[index]
            index +=1

    for i in range(numri_i_rreshtave):
        for j in range(numri_i_kolonave):

            plaintext += matrica[i][j]

    return plaintext


def double_columnar_transposition_decryption_alg(key1, key2, ciphertext):

    plaintext = columnar_transposition_decryption_alg(key2, ciphertext)
    plaintext2 = columnar_transposition_decryption_alg(key1, plaintext)

    return plaintext2


# The decryption algorithms are not implemented yet, but they will be added in the future.
if "__main__" == __name__:

    answer = input("Would you like to encrypt ? Press 1 for encryption : ")
    if answer == "1":

        plaintext = input("Please enter the plaintext: ")
        key1 = input("Please enter the first key: ")
        key2 = input("Please enter the second key: ")
        
        print(f"Old message: {plaintext}")
        print(f"The encrypted message is {double_columnar_transposition_encryption_alg(key1, key2, plaintext)}")

