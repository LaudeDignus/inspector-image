from stegano import lsb


def stegano(image_path):
    with open(image_path, "rb") as img:
        lines = img.read().decode(errors="ignore").splitlines()

    pgp_key = []
    inside_key = False

    for line in lines:
        if "-----BEGIN PGP PUBLIC KEY BLOCK-----" in line:
            line=" ".join(line.split()[1:])
            inside_key=True

        if "-----END PGP PUBLIC KEY BLOCK-----" in line:
            line=" ".join(line.split()[:5])
            pgp_key.append(line)
            inside_key=False  

        if inside_key:
            pgp_key.append(line)


    print("\n".join(pgp_key) if pgp_key else "❌ Clé PGP non trouvée.")
