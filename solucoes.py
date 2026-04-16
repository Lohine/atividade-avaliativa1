import string


def sao_anagramas(string1, string2):
    normalizada1 = "".join(char.lower() for char in string1 if not char.isspace())
    normalizada2 = "".join(char.lower() for char in string2 if not char.isspace())

    return sorted(normalizada1) == sorted(normalizada2)

def cifra_de_cesar(texto, deslocamento):
    resultado = ""

    for caractere in texto:
        if "a" <= caractere <= "z":
            novo_codigo = (ord(caractere) - ord("a") + deslocamento) % 26
            resultado += chr(ord("a") + novo_codigo)
        elif "A" <= caractere <= "Z":
            novo_codigo = (ord(caractere) - ord("A") + deslocamento) % 26
            resultado += chr(ord("A") + novo_codigo)
        else:
            resultado += caractere

    return resultado

def encontrar_maior_palavra(frase):
    maior_palavra = ""

    for palavra in frase.split():
        palavra_limpa = palavra.strip(string.punctuation)

        if len(palavra_limpa) > len(maior_palavra):
            maior_palavra = palavra_limpa

    return maior_palavra
