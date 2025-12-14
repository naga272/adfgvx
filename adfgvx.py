import sys


symbol = ["a", "d", "f", "g", "v", "x"]
key_word = "CIPHER"


# matrice 6x6
matrice_adfgvx = [
    ["a", "b", "c", "d", "e", "f"],
    ["g", "h", "i", "j", "k", "l"],
    ["m", "n", "o", "p", "q", "r"],
    ["s", "t", "u", "v", "w", "x"],
    ["y", "z", "0", "1", "2", "3"],
    ["4", "5", "6", "7", "8", "9"],
]


def re_map(string_to_remap: str) -> str:
    string_encrypted = ""
    for char in string_to_remap:
        for idx, row in enumerate(matrice_adfgvx):
            if char in row:
                char_asse_y = symbol[idx]
                for idx_row, element in enumerate(row):
                    if element == char:
                        char_asse_x = symbol[idx_row]
                        string_encrypted += char_asse_y + char_asse_x
                        break
                break
    return string_encrypted


def order(key: str) -> list:
    return sorted(range(len(key)), key=lambda i: key[i])


def algoritmo_adfgvx(to_encrypt: str) -> str:
    """
    *   algoritmo adfgvx step by step
    """
    # step 1: sostituzione
    stringa_rimappata = re_map(to_encrypt)

    # step 2: trasposizione colonne tramite keyword
    keyword_riordinata = order(key_word)

    lista_prov = []
    for i in range(len(key_word)):
        lista_prov.append([])

    for idx, c in enumerate(stringa_rimappata):
        lista_prov[idx % len(key_word)].append(c)

    # questo serve solo per l'output
    print(
        "stringa rimappata secondo la tabella adfgvx:\n",
        stringa_rimappata,
        end="\n\n"
    )
    print("keyword originale:")
    print("".join(char + "  " for char in key_word))
    print("".join(f"{ord(char)} " for char in key_word))

    print(keyword_riordinata)

    # ristampa la nuova matrice
    len_key = len(key_word)

    # la stringa viene formattata
    # [a, b, c, d, e]
    print("[", end="")
    for idx, char in enumerate(stringa_rimappata):
        chiusura = (idx + 1) % len_key != 0
        print(char, end=", " if chiusura else "")

        if not chiusura:
            print("]")
            if idx + 1 != len(stringa_rimappata):
                print("[", end="")

    string_encrypted = ""
    sections = []

    for i in range(len_key):
        sections.append("")

    for idx, char in enumerate(stringa_rimappata):
        sections[idx % len_key] += char

    for section in sections:
        print(section)

    sorted_indices = sorted(
        range(
            len(keyword_riordinata)
        ),
        key=lambda i: keyword_riordinata[i]
    )
    for num in sorted_indices:
        string_encrypted += sections[num] + " "

    return string_encrypted.upper()


def main():
    stringa = "MunitionierungbeschleunigenPunktSoweitnichteingesehenauchbeiTag".lower()

    print("stringa da crittografare:\n", stringa.upper())
    print("matrice adfgvx: ")
    print(" ", symbol)

    for idx, lista in enumerate(matrice_adfgvx):
        print(symbol[idx], lista)

    testo_crittografato = algoritmo_adfgvx(stringa)

    print("stringa crittografata:\n" + testo_crittografato)
    return 0


if __name__ == "__main__":
    result = main()
    sys.exit(result)
