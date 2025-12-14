import sys
import os


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

    print("stringa rimappata secondo la tabella adfgvx:", stringa_rimappata)
    print("keyword riordinata:", keyword_riordinata)

    string_encrypted = ""
    for idx in keyword_riordinata:
        string_encrypted += "".join(char for char in lista_prov[idx])

    return string_encrypted


def main():
    stringa = "lorem"

    print("stringa da crittografare: ", stringa)

    print("matrice adfgvx: ")
    print(" ", symbol)
    for idx, lista in enumerate(matrice_adfgvx):
        print(symbol[idx], lista)

    print("parola chiave: ", key_word)

    testo_crittografato = algoritmo_adfgvx(stringa)

    print("stringa crittografata: ", testo_crittografato)
    return 0


if __name__ == "__main__":
    result = main()
    sys.exit(result)

