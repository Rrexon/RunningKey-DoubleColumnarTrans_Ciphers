# RunningKey-DoubleColumnarTrans_Ciphers



# 🔐 Running Key Cipher (Versioni i thjeshtuar - 1) - RunningKeyCipher.py

Ky projekt implementon një version më të thjeshtë të **Running Key Cipher**, ku key duhet të jetë të paktën po aq i gjatë sa mesazhi dhe nuk përdoret zgjatje automatike.
## Si të ekzekutohet

### Kërkesat
- Python 3.x
### Ekzekutimi

```bash
python RunningKeyCipher.py
```
Pas ekzekutimit, programi pyet nëse dëshironi të enkriptoni (1) apo dekriptoni (2) mesazhin, pastaj kërkon inputet e nevojshme.
---

# ⚙️ Si funksionon algoritmi

Teksti dhe key konvertohen në numra:

- a = 0, b = 1, ..., z = 25

Hapësirat hiqen para procesit.

---

## 🔐 Encryption Formula
C = (P + K) mod 26
Ku:
- P = shkronja e plaintext-it
- K = shkronja e key-t
- C = ciphertext
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

<img width="743" height="89" alt="image" src="https://github.com/user-attachments/assets/86400926-604b-41e7-9ece-bc3fc8c882bc" />


---

## 🔹 Shembulli 3
<img width="751" height="91" alt="image" src="https://github.com/user-attachments/assets/c7da81ce-c8a5-4577-943c-d77206253c87" />

## Shembulli 4
<img width="689" height="76" alt="image" src="https://github.com/user-attachments/assets/4ce57aa0-0101-4d34-a2d1-a73665e368dd" />


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
## Si të ekzekutohet

### Kërkesat
- Python 3.x
### Ekzekutimi

```bash
python verzioni2.py
```
Pas ekzekutimit, programi pyet nëse dëshironi të enkriptoni (1) apo dekriptoni (2) mesazhin, pastaj kërkon inputet e nevojshme.

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

<img width="193" height="154" alt="image" src="https://github.com/user-attachments/assets/e54f9fc0-766f-42b7-b666-635e56a66043" />



---

## 🔹 Shembulli 2

<img width="550" height="158" alt="image" src="https://github.com/user-attachments/assets/2e2d7c7e-e49d-48f2-8cb6-13294cd5ef34" />

---

## 🔹 Shembulli 3

<img width="242" height="148" alt="image" src="https://github.com/user-attachments/assets/1d4899c9-b9a1-441c-ab2c-54d8044a3725" />




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


