import random

def rolar_dado():
    return random.randint(1, 6)

def exibir_resultado():
    print("Bem-vindo ao simulador de rolagem de dado!")
    input("Pressione Enter para rolar o dado...")
    
    resultado = rolar_dado()
    print(f"O resultado do dado foi: {resultado}")

def jogo():
    while True:
        exibir_resultado()
        
        resposta = input("Deseja rolar o dado novamente? (s/n): ").lower()
        if resposta != 's':
            print("Obrigado por jogar!")
            break

if __name__ == "__main__":
    jogo()

#:V