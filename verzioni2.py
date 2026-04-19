import re


# VALIDIM I TEKSTIT

def validate_text(text):
    """
    Kontrollon nëse teksti përmban vetëm shkronja dhe hapësira.
    Përdoret për plaintext dhe ciphertext.
    """
    return all(ch.isalpha() or ch == " " for ch in text)



# VALIDIM I KEY-T

def validate_key(key):
    """
    Key duhet të përmbajë vetëm shkronja.
    Hapësirat hiqen automatikisht për validim.
    """
    return key.replace(" ", "").isalpha()



# ZGJATJA AUTOMATIKE E KEY-T

def extend_key(key, length):
    """
    E zgjat key-in deri në gjatësinë e tekstit.
    Kjo është baza e Running Key cipher.
    """
    key = key.replace(" ", "").lower()

    # Mbrojtje nga crash nëse key është bosh
    if len(key) == 0:
        return ""

    return (key * (length // len(key) + 1))[:length]


#
# ENCRYPTION FUNKSIONI
#
def running_key_encryption_alg(key, plaintext):

    ciphertext = ""

    # e standardizojmë plaintext
    plaintext = plaintext.lower()

    # marrim vetëm shkronjat për llogaritje të key
    plaintext_letters_only = plaintext.replace(" ", "").lower()

    # zgjasim key-in sipas gjatësisë së shkronjave
    key_extended = extend_key(key, len(plaintext_letters_only))

    j = 0  # index për key

    for ch in plaintext:

        # ruajmë hapësirat pa ndryshim
        if ch == " ":
            ciphertext += " "
            continue

        # konvertim shkronjash në numra (a=0 ... z=25)
        p_value = ord(ch) - ord('a')
        k_value = ord(key_extended[j]) - ord('a')

        # formula e encryption (mod 26)
        c_value = (p_value + k_value) % 26

        ciphertext += chr(c_value + ord('a'))

        j += 1

    return ciphertext

