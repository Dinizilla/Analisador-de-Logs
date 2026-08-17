# 🔎 Analisador de Logs

Aplicação simples desktop desenvolvida em **Python** para análise de arquivos de log, identificação de endereços IP e detecção de IPs que ultrapassam um limite configurável de requisições.

O projeto foi desenvolvido como uma prática de programação e como forma de explorar conceitos relacionados à **análise de logs e Segurança da Informação**.

---

## 📌 Sobre o projeto

O Analisador de Logs permite selecionar um arquivo de texto contendo registros de log e definir um limite de requisições.

A aplicação identifica os endereços IPv4 presentes no arquivo, contabiliza suas ocorrências e apresenta os IPs que ultrapassaram o limite definido pelo usuário.

A ideia é facilitar uma análise inicial dos registros e destacar endereços que apresentam uma quantidade elevada de ocorrências, podendo servir como ponto de partida para uma investigação mais detalhada.

> **Importante:** o projeto não determina se um endereço IP é malicioso. Ele apenas identifica IPs que ultrapassam o limite de ocorrências configurado pelo usuário.

---

## 🖥️ Funcionalidades

- 📂 Seleção de arquivos de log através de uma interface gráfica.
- 🔍 Identificação de endereços IPv4 utilizando Expressões Regulares (Regex).
- 📊 Contagem das ocorrências de cada endereço IP.
- ⚙️ Definição de um limite de ocorrências pelo usuário.
- 🚨 Identificação de IPs que ultrapassam o limite configurado.
- 📋 Exibição dos resultados em uma tabela.
- 📈 Ordenação dos IPs pelo número de ocorrências.
- ⚠️ Validação das entradas fornecidas pelo usuário.
- 🛠️ Tratamento de erros durante a leitura e processamento do arquivo.

---

## 🛠️ Tecnologias utilizadas

- **Python**
- **Tkinter** — interface gráfica
- **Regular Expressions (Regex)** — identificação de endereços IP
- **collections.Counter** — contagem das ocorrências

O projeto utiliza apenas módulos da biblioteca padrão do Python, não necessitando da instalação de bibliotecas externas.

---

## ⚙️ Como funciona

O processamento realizado pela aplicação segue, de forma simplificada, estas etapas:

```text
Arquivo de Log
      │
      ▼
Leitura do arquivo
      │
      ▼
Identificação dos endereços IP
      │
      ▼
Contagem das ocorrências
      │
      ▼
Aplicação do limite definido
      │
      ▼
Ordenação dos resultados
      │
      ▼
Exibição na interface
