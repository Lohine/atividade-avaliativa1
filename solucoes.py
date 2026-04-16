def sao_anagramas(string1, string2):
    normalizada1 = "".join(char.lower() for char in string1 if not char.isspace())
    normalizada2 = "".join(char.lower() for char in string2 if not char.isspace())

    return sorted(normalizada1) == sorted(normalizada2)

def cifra_de_cesar(texto, deslocamento):
    # TODO: Implementar a lógica
    pass

def encontrar_maior_palavra(frase):
    # TODO: Implementar a lógica
    pass
