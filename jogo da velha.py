import tkinter as tk
from tkinter import messagebox


def verificar_vitoria():

    for i in range(3):
        if tabuleiro[i][0] == tabuleiro[i][1] == tabuleiro[i][2] and tabuleiro[i][0] != "":
            return tabuleiro[i][0]
        if tabuleiro[0][i] == tabuleiro[1][i] == tabuleiro[2][i] and tabuleiro[0][i] != "":
            return tabuleiro[0][i]

    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] and tabuleiro[0][0] != "":
        return tabuleiro[0][0]
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] and tabuleiro[0][2] != "":
        return tabuleiro[0][2]

 
    for i in range(3):
        for j in range(3):
            if tabuleiro[i][j] == "":
                return None
    return "Empate"

def clique(i, j):
    global turno
    if tabuleiro[i][j] == "":
        tabuleiro[i][j] = "X" if turno % 2 == 0 else "O"
        botoes[i][j].config(text=tabuleiro[i][j], state="disabled")
        turno += 1
        vencedor = verificar_vitoria()

        if vencedor:
            if vencedor == "Empate":
                messagebox.showinfo("Fim de Jogo", "Empate!")
            else:
                messagebox.showinfo("Fim de Jogo", f"O Jogador {vencedor} venceu!")
            reiniciar_jogo()
        elif turno == 9:
            messagebox.showinfo("Fim de Jogo", "Empate!")
            reiniciar_jogo()

def reiniciar_jogo():
    global turno, tabuleiro
    turno = 0
    tabuleiro = [["" for _ in range(3)] for _ in range(3)]
    for i in range(3):
        for j in range(3):
            botoes[i][j].config(text="", state="normal")

root = tk.Tk()
root.title("Jogo da Velha")

tabuleiro = [["" for _ in range(3)] for _ in range(3)]
turno = 0

botoes = [[None for _ in range(3)] for _ in range(3)]
for i in range(3):
    for j in range(3):
        botoes[i][j] = tk.Button(root, text="", width=10, height=3,
                                 font=("Arial", 24), command=lambda i=i, j=j: clique(i, j))
        botoes[i][j].grid(row=i, column=j)

btn_reiniciar = tk.Button(root, text="Reiniciar", width=10, height=2, font=("Arial", 14), command=reiniciar_jogo)
btn_reiniciar.grid(row=3, column=0, columnspan=3)

root.mainloop()

#:V