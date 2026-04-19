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

