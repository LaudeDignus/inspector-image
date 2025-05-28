# 🕵️ Inspector Image

## 🔐 Concepts clés

### 🧠 1. Stéganographie

La **stéganographie** est l’art de **cacher un message dans un support numérique** (image, audio, vidéo, etc.).

Contrairement à la cryptographie (qui protège le contenu), la stéganographie **cache l’existence même du message**.

📦 Dans ce projet, le message est caché dans les **pixels de l’image**, via le bit le moins significatif (**LSB**).

---

### 🔒 2. Cryptographie

La **cryptographie** permet de chiffrer un message pour le rendre illisible sans la bonne clé.

- **Symétrique** : même clé pour chiffrer et déchiffrer
- **Asymétrique (PGP)** : clé publique (chiffrer), clé privée (déchiffrer)

---

### 🔏 3. Clé PGP

**PGP (Pretty Good Privacy)** est un système de chiffrement **asymétrique**.

Une clé publique PGP ressemble à ceci :

```
-----BEGIN PGP PUBLIC KEY BLOCK-----
...
-----END PGP PUBLIC KEY BLOCK-----
```
Dans ce projet, la clé est **dissimulée dans l’image** via stéganographie et peut être révélée par notre outil.

---

### 🖼️ 4. Métadonnées

Les **métadonnées** d’une image sont des données invisibles contenues dans le fichier, comme :

- 📅 Date de prise de vue
- 📷 Modèle de l'appareil photo
- 📍 Localisation GPS (si activée)

---

### 🧾 5. Format EXIF

**EXIF (Exchangeable Image File Format)** est le format utilisé pour stocker les métadonnées dans une image.

Exemples de données EXIF utiles :

- `GPS GPSLatitude` et `GPSLatitudeRef`
- `GPS GPSLongitude` et `GPSLongitudeRef`

Ces données sont accessibles grâce à la bibliothèque Python `exifread`.

---


## 📁 Structure du projet

```bash
.
├── image.py                 # Script principal CLI
├── .gitignore                # Fichiers ignorés par Git
├── requirement.txt           # Dépendances à installer
├── model/                    # Contient la logique de données
│   ├── gui_map.py
|   ├── image_info.py
|   ├── map_info.py
│   └── steg_info.py
├── image.jpeg
└── style.py

```

---

## 🛠️ Installation

### 1. Cloner le projet

```bash
https://learn.zone01dakar.sn/git/mouwade/inspector-image.git
cd inspector-image
```

### 2. Installe les dépendances avec pip :

```bash
pip install -r requirement.txt
```

---

## ⚙️ Utilisation et Fonctionnalités

| Commande                        | Description |
|----------------------------------|-------------|
| `python3 image.py -map image.jpeg`| Affiche les coordonnées GPS depuis EXIF |
| `python3 image.py -steg image.jpeg`| Extrait une clé PGP cachée dans l’image |
| `python3 image.py --gui`         | Lance l’interface graphique Tkinter |
| `python3 image.py --info image.jpeg`      | Ouvrir l'image avec open-cv |

---

## 📦 Bibliothèques utilisées

- [`exifread`](https://github.com/ianare/exif-py) – Lecture des métadonnées EXIF
- [`stegano`](https://github.com/cedricbonhomme/Stegano) – Cacher/révéler des messages dans les images
- `tkinter` – Interface graphique utilisateur
- `Pillow` – Affichage et manipulation d’images

---

## 📊 Comparatif : Métadonnées vs Stéganographie vs Cryptographie

| Caractéristique        | Métadonnées          | Stéganographie           | Cryptographie           |
|------------------------|----------------------|---------------------------|--------------------------|
| But principal          | Stocker des infos     | Cacher un message        | Sécuriser un message     |
| Visibles facilement ?  | ✅ Oui (`exiftool`)   | ❌ Non                    | ❌ Non                   |
| Standardisé ?          | ✅ Oui (EXIF, XMP)    | ❌ Non (bits cachés)      | ✅ Oui (PGP, AES, etc.)  |
| Supprimable ?          | ✅ Facilement         | ❌ Plus complexe          | ❌ Non (nécessite clé)   |
| Utilisation légitime ? | ✅ Métadonnées utiles | ✅ Éducation, secrets     | ✅ Sécurité numérique     |

---

## Author
### @MOUWADE

---
### 🔗 Voir la vidéo sur YouTube
[![Voir la vidéo sur YouTube](https://img.youtube.com/vi/uGmQcJAI0g0/maxresdefault.jpg)](https://youtu.be/uGmQcJAI0g0?si=SDokrxgkYjPjhMsU)
---

## ⚠️ Avertissement

> Ce projet est fourni à des fins **éducatives uniquement**.  
> Toute utilisation sur des fichiers ne vous appartenant pas, sans autorisation explicite, pourrait violer la loi.

---

