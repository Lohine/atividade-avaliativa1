def sao_anagramas(string1, string2):
    normalizada1 = "".join(char.lower() for char in string1 if char != " ")
    normalizada2 = "".join(char.lower() for char in string2 if char != " ")

    if not normalizada1 or not normalizada2:
        return False

    return sorted(normalizada1) == sorted(normalizada2)

def cifra_de_cesar(texto, deslocamento):
    # TODO: Implementar a lógica
    pass

def encontrar_maior_palavra(frase):
    # TODO: Implementar a lógica
    pass
