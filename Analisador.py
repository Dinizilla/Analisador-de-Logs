import re
from collections import Counter
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

# Compila o padrão de IP logo no início (boa prática, fica mais rápido)
ip_padrao = re.compile(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b')

def analisar_requisicoes(caminho_arquivo, limite_requisicoes):
    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
            # Lê todas as linhas do arquivo de log 
            linhas = arquivo.readlines()

            # Lista para armazenar os endereços IP encontrados
            todos_ips = []  

            for linha in linhas:
                # Encontra todos os endereços IP na linha usando regex
                ips_encontrados = ip_padrao.findall(linha)
                # Adiciona os endereços IP encontrados à lista todos_ips
                todos_ips.extend(ips_encontrados)

        # Conta a frequência de cada endereço IP usando Counter
        contagem_ips = Counter(todos_ips)

        # Filtra os endereços IP que excedem o limite de requisições
        ips_excedentes = {ip: count for ip, count in contagem_ips.items() if count > limite_requisicoes}

        # Ordena os endereços IP excedentes pelo número de requisições em ordem decrescente
        ips_ordenados = sorted(ips_excedentes.items(), key=lambda x: x[1], reverse=True)

        return ips_ordenados, None #indica que não houve erro

    except FileNotFoundError:
        # CORREÇÃO: Retorna None e a mensagem de erro para a interface poder tratar
        return None, f"Erro: O arquivo '{caminho_arquivo}' não foi encontrado."
    except Exception as e:
        # CORREÇÃO: Retorna None e a mensagem de erro
        return None, f"Ocorreu um erro: {e}"


class LogAnalyzerApp:
    # CORREÇÃO: Adicionada a indentação correta para os métodos da classe
    def __init__(self, root):
        self.root = root
        self.root.title("Analisador de Logs - IPs Suspeitos")
        self.root.geometry("500x450")
        self.root.configure(padx=20, pady=20)

        # --- Frame Superior (Seleção de Arquivo e Limite) ---
        frame_topo = tk.Frame(root)
        frame_topo.pack(fill="x", pady=(0, 15))

        # Botão e Label para o caminho do arquivo
        self.btn_selecionar = tk.Button(frame_topo, text="Selecionar Arquivo...", command=self.selecionar_arquivo)
        self.btn_selecionar.pack(side="left", padx=(0, 10))

        self.lbl_caminho = tk.Label(frame_topo, text="Nenhum arquivo selecionado", fg="gray")
        self.lbl_caminho.pack(side="left", fill="x", expand=True)

        # Label e Entry para o limite de requisições
        frame_limite = tk.Frame(root)
        frame_limite.pack(fill="x", pady=(0, 15))

        self.lbl_limite = tk.Label(frame_limite, text="Limite de requisições:")
        self.lbl_limite.pack(side="left", padx=(0, 5))

        # StringVar permite pegar o valor digitado no input facilmente. Por padrão: 5
        self.limite_var = tk.StringVar(value="5")
        self.entry_limite = tk.Entry(frame_limite, textvariable=self.limite_var, width=5)
        self.entry_limite.pack(side="left")

        # --- Botão de Analisar ---
        self.btn_analisar = tk.Button(root, text="Analisar IPs", bg="#4CAF50", fg="white", font=("Arial", 10, "bold"), command=self.executar_analise)
        self.btn_analisar.pack(pady=(0, 15))

        # --- Tabela de Resultados (Treeview) ---
        # style configura as cores das linhas alternadas da tabela
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview", rowheight=25)

        self.tree = ttk.Treeview(root, columns=("IP", "Requisicoes"), show="headings")
        self.tree.heading("IP", text="Endereço IP")
        self.tree.heading("Requisicoes", text="Qtd. Requisições")
        
        # Configura a largura das colunas
        self.tree.column("IP", width=250, anchor="w")
        self.tree.column("Requisicoes", width=150, anchor="center")
        
        self.tree.pack(fill="both", expand=True)

        # Variável para guardar o caminho do arquivo selecionado
        self.caminho_arquivo_selecionado = None
    
    # CORREÇÃO: Removida a indentação extra que estava colocando esta função dentro do __init__
    def selecionar_arquivo(self):
        """Abre a janela do Windows/Mac/Linux para escolher o arquivo .txt"""
        caminho = filedialog.askopenfilename(
            title="Selecione o arquivo de log",
            filetypes=[("Arquivos de Texto", "*.txt"), ("Todos os Arquivos", "*.*")]
        )
        
        if caminho: # Se o usuário não cancelou
            self.caminho_arquivo_selecionado = caminho
            # Pega apenas o nome do arquivo para não ficar grande demais na tela
            nome_arquivo = caminho.split("/")[-1]
            self.lbl_caminho.config(text=nome_arquivo, fg="black")

    def executar_analise(self):
        """Valida as entradas e chama a função de processamento"""
        # Verifica se o arquivo foi selecionado
        if not self.caminho_arquivo_selecionado:
            messagebox.showwarning("Aviso", "Por favor, selecione um arquivo de log primeiro.")
            return

        # Verifica se o limite digitado é um número válido
        try:
            limite = int(self.limite_var.get())
            if limite < 1:
                raise ValueError
        except ValueError:
            messagebox.showerror("Erro", "O limite de requisições deve ser um número inteiro maior que zero.")
            return

        # Limpa a tabela antes de inserir novos resultados
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Chama a função que processa o arquivo
        resultados, erro = analisar_requisicoes(self.caminho_arquivo_selecionado, limite)

        if erro:
            messagebox.showerror("Erro no processamento", erro)
        elif not resultados:
            messagebox.showinfo("Informação", "Nenhum IP excedeu o limite de requisições.")
        else:
            # Preenche a tabela com os resultados
            for ip, count in resultados:
                self.tree.insert("", "end", values=(ip, count))

# Este bloco inicia a aplicação
if __name__ == "__main__":
    # Cria a janela principal
    root = tk.Tk()
    # CORREÇÃO: Atualizado o nome da classe para o que você definiu acima
    app = LogAnalyzerApp(root)
    # Mantém a janela rodando
    root.mainloop()