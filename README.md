# Kriptografi - Running Key & Columnar Transposition

Ky projekt implementon dy algoritme kriptografike: **Running Key Cipher** dhe **Double Columnar Transposition Cipher**.

---

## Si të ekzekutohet

### Kërkesat
- Python 3.x

### Ekzekutimi

**Running Key Cipher:**
```bash
python running_key.py
```

**Double Columnar Transposition Cipher:**
```bash
python columnar_transposition.py
```

Pas ekzekutimit, programi pyet nëse dëshironi të **enkriptoni (1)** apo **dekriptoni (2)** mesazhin, pastaj kërkon inputet e nevojshme.

---

## Përshkrimi i algoritmeve



### 2. Double Columnar Transposition Cipher

Columnar Transposition është një algoritëm që rirendit shkronjat e mesazhit bazuar në një çelës. Teksti vendoset në një matricë rresht pas rreshti, pastaj kolonat lexohen sipas rendit alfabetik të çelësit. **Double** Columnar Transposition e aplikon këtë proces dy herë radhazi me dy çelësa të ndryshëm, duke rritur ndjeshëm sigurinë.

---