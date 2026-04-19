# RunningKey-DoubleColumnarTrans_Ciphers



# 🔐 Running Key Cipher (Versioni i thjeshtuar - 1) - RunningKeyCipher.py

Ky projekt implementon një version më të thjeshtë të **Running Key Cipher**, ku key duhet të jetë të paktën po aq i gjatë sa mesazhi dhe nuk përdoret zgjatje automatike.

---

# ⚙️ Si funksionon algoritmi

Teksti dhe key konvertohen në numra:

- a = 0, b = 1, ..., z = 25

Hapësirat hiqen para procesit.

---

## 🔐 Encryption Formula
C = (P + K) mod 26

---

# 🧠 Karakteristikat

- ✔ Nuk përdor key extension
- ✔ Heq hapësirat nga inputi
- ✔ Encryption & Decryption të thjeshta
- ✔ Validim i gjatësisë së key-t
- ✔ Përdor vetëm shkronja (a–z)

---

# 📌 Shembuj

## 🔹 Shembulli 1

<img width="748" height="106" alt="image" src="https://github.com/user-attachments/assets/0fce46a8-4d8e-4d80-970a-e6736893363d" />



---

## 🔹 Shembulli 2

**Input:**
Plaintext: cryptography
Key: keykeykeykeyk

**Output:**
Encrypted: mrxvzcxktqht
Decrypted: cryptography

---

## 🔹 Shembulli 3

**Input:**
Plaintext: attackatdawn
Key: lemonlemonle

**Output:**
Encrypted: lxfopvefrnhr
Decrypted: attackatdawn
# 🚀 Si përdoret

1. Run programin në Python
2. Zgjidh:
   - `1` për encryption
   - `2` për decryption
3. Jep plaintext/ciphertext dhe key
4. Programi kthen rezultatin

---

# ⚠️ Rregulla

- Key duhet të jetë **≥ gjatësisë së mesazhit**
- Hapësirat hiqen automatikisht
- Vetëm shkronja lejohen (a–z)
- Nuk ka key extension

  ---




# 🔐 Running Key Cipher (Encryption & Decryption in Python) - VERZIONI 2 

Ky projekt implementon një **Running Key Cipher**, një metodë klasike e kriptografisë ku mesazhi enkriptohet duke përdorur një key që zgjatet automatikisht për të përputhur gjatësinë e tekstit.

---

---

# 🚀 Si përdoret

1. Run programin në Python
2. Zgjidh:
   - `1` Encrypt
   - `2` Decrypt
3. Jep tekstin dhe key
4. Merr rezultatin

---

# ⚠️ Rregulla

- Vetëm shkronja dhe hapësira lejohen
- Key nuk duhet të jetë bosh
- Hapësirat nuk ndryshohen gjatë encryption/decryption

---


# ⚙️ Si funksionon algoritmi

Algoritmi konverton shkronjat në numra:

- a = 0, b = 1, ..., z = 25

---

## 🔐 Encryption Formula
C = (P + K) mod 26

Ku:
- P = shkronja e plaintext-it
- K = shkronja e key-t
- C = ciphertext

---

## 🔓 Decryption Formula
P = (C - K) mod 26


---

# 🧠 Funksionalitetet

- ✔ Validim i tekstit (vetëm shkronja dhe hapësira)
- ✔ Validim i key-t
- ✔ Zgjatje automatike e key-t
- ✔ Encryption
- ✔ Decryption
- ✔ Ruajtje e hapësirave

---

# 📌 Shembuj

## 🔹 Shembulli 1

**Input:**
Plaintext: hello world
Key: secret

**Output:**
Encrypted: zevvj giqlk
Decrypted: hello world


---

## 🔹 Shembulli 2

**Input:**
Plaintext: cryptography
Key: key

**Output:**
Encrypted: mrxvzcxktqht
Decrypted: cryptography

---

## 🔹 Shembulli 3

**Input:**
Plaintext: attack at dawn
Key: lemon

**Output:**
Encrypted: lxfopv ef rnhr
Decrypted: attack at dawn



# Kriptografi - Double Columnar Transposition Cipher


## Si të ekzekutohet

### Kërkesat
- Python 3.x

### Ekzekutimi

```bash
python DoubleColumnarTranspositionCipher.py
```

Pas ekzekutimit, programi pyet nëse dëshironi të **enkriptoni (1)** apo **dekriptoni (2)** mesazhin, pastaj kërkon inputet e nevojshme.

---

## Përshkrimi i algoritmit

Columnar Transposition është një algoritëm që rirendit shkronjat e mesazhit bazuar në një çelës. Teksti vendoset në një matricë rresht pas rreshti, pastaj kolonat lexohen sipas rendit alfabetik të çelësit. **Double** Columnar Transposition e aplikon këtë proces dy herë me dy çelësa të ndryshëm, duke rritur ndjeshëm sigurinë.

> **Shënim:** Nëse teksti nuk e plotëson matricën, plotësohet me shkronjën `x`.

---

## Shembuj

### Double Columnar Transposition Cipher

**Enkriptim:**
```
Would you like to encrypt or decrypt? Press 1 for encryption or press 2 for decryption: 1
Please enter the plaintext: hello world
Please enter the first key: key
Please enter the second key: code

Old message: hello world
The encrypted message is: ehlrolxdxolw
```

**Dekriptim:**
```
Would you like to encrypt or decrypt? Press 1 for encryption or press 2 for decryption: 2
Please enter the ciphertext: ehlrolxdxolw
Please enter the second key: code
Please enter the first key: key

Old message: ehlrolxdxolw
The decrypted message is: helloworld
```


