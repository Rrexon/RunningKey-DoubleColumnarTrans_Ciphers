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

**Input:**
Plaintext: hello world
Key: secretkeyyy

**Output:**
Encrypted: zfyyfvlxqk
Decrypted: helloworld

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

