import tkinter as tk
from tkinter import messagebox

def verificar_login(): 
    usuario = entrada_usuario.get()
    senha = entrada_senha.get()
    
    if usuario == "Maria" and senha == "2025":
        messagebox.showinfo ("Sucesso", "Login realizado com sucesso!")
        janela.destroy() 
    else: 
        messagebox.showerror("Erro", "Usuario ou senha incorretor. ")
        
# Cria a janela principal
janela = tk.Tk()
janela.title("Tela de Login")
janela.configure(bg="pink")
janela.iconbitmap("meu_icone.ico")
janela.geometry("600x400")

janela.grid_columnconfigure(0, weight=1) 
janela.grid_columnconfigure(1, weight=3)  
janela.grid_rowconfigure(0, weight=1)  
janela.grid_rowconfigure(1, weight=1)  
janela.grid_rowconfigure(2, weight=1)  

# Rótulo para o nome de usuário
rotulo_usuario = tk.Label(janela, text="Usuario: ", 
                          fg="black",
                          bg="pink",
                          font=("Times New Roman", 12, "bold"))
rotulo_usuario.grid(row=0, column=0, padx=10, pady=10, sticky="w")

# Campo de entrada para o nome de usuário
entrada_usuario = tk.Entry(janela)
entrada_usuario.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

# Rótulo para a senha
rotulo_senha = tk.Label(janela, text="Senha: ",
                        fg="black",
                        bg="pink",
                        font=("Times New Roman", 12, "bold"))
rotulo_senha.grid(row=1, column=0, padx=10, pady=10, sticky="w")

# Campo de entrada para a senha 
entrada_senha = tk.Entry(janela, show="*") 
entrada_senha.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

#Botão de Login
botao_login = tk.Button(janela, text="Login", command=verificar_login, 
                        bg="#FF007F",
                        fg="white",
                        activebackground="#45a049",
                        font=("Times New Roman", 12, "bold"))
botao_login.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

janela.grid_columnconfigure(1, weight=1)

janela.mainloop()