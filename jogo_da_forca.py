import random

def exibir_palavra(palavra, letras_corretas):
    """Exibe a palavra com as letras corretas reveladas e o resto com underscores."""
    palavra_atual = ""
    for letra in palavra:
        if letra in letras_corretas:
            palavra_atual += letra + " "
        else:
            palavra_atual += "_ "
    print(palavra_atual.strip())

def jogar_forca():

    lista_de_palavras = ["python", "desenvolvedor", "forca", "computador", "programacao", "algoritmo"]
 
    palavra_secreta = random.choice(lista_de_palavras).lower()

    tentativas_maximas = 6
    tentativas = 0
    
    letras_corretas = []

    letras_erradas = []
    

    print("Bem-vindo ao Jogo da Forca!")
    
    while tentativas < tentativas_maximas:

        exibir_palavra(palavra_secreta, letras_corretas)

        print(f"Letras erradas: {', '.join(letras_erradas)}")
        print(f"Tentativas restantes: {tentativas_maximas - tentativas}")

        letra = input("Digite uma letra: ").lower()

        if not letra.isalpha() or len(letra) != 1:
            print("Por favor, digite uma única letra válida.")
            continue
        
        if letra in letras_corretas or letra in letras_erradas:
            print("Você já tentou essa letra.")
            continue
        
        if letra in palavra_secreta:
            letras_corretas.append(letra)
            print(f"Boa! A letra {letra} está na palavra.")
        else:
            letras_erradas.append(letra)
            tentativas += 1
            print(f"A letra {letra} não está na palavra.")
        
        if all(letra in letras_corretas for letra in palavra_secreta):
            print(f"Parabéns! Você adivinhou a palavra: {palavra_secreta}")
            break
    

    if tentativas == tentativas_maximas:
        print(f"Você perdeu! A palavra era: {palavra_secreta}")

if __name__ == "__main__":
    jogar_forca()

#:V