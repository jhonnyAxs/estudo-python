# Sabor Express 🍽️

Sistema de gerenciamento de restaurante via linha de comando (CLI), desenvolvido como projeto prático durante meus estudos de Python.

## 📋 Sobre o projeto

O Sabor Express é um sistema CLI para gerenciamento de restaurantes parceiros, construído para praticar lógica de programação, estruturas de dados (listas e dicionários) e tratamento de erros em Python.

## ⚙️ Funcionalidades

- Cadastro de restaurante (nome, categoria, CNPJ, endereço, telefone, email, senha)
- Listagem de todos os restaurantes cadastrados, com situação (ativo/inativo)
- Ativação/desativação de um restaurante pelo nome
- Menu interativo via terminal com validação de opção inválida
- Tratamento de erros de entrada (try/except)

> Os dados são mantidos apenas em memória durante a execução — ao fechar o programa, as informações são perdidas (veja "Próximos passos" abaixo).

## 🛠️ Tecnologias

- Python 3
- Estruturas de dados nativas (listas e dicionários)

## ▶️ Como executar

```bash
git clone https://github.com/seu-usuario/sabor-express.git
cd sabor-express
python sabor_express.py
```

*(ajuste o nome do arquivo se necessário)*

## ⚠️ Limitações conhecidas

- Senhas dos restaurantes são armazenadas e exibidas em texto puro, sem hash ou criptografia (escolha consciente para focar na lógica do CLI durante o aprendizado)
- Limpeza de tela (`os.system('cls')`) funciona apenas no Windows

## 🚧 Próximos passos

Este é um projeto em evolução conforme avanço nos estudos. Melhorias planejadas:

- [ ] Persistência de dados (salvar em arquivo JSON ou banco de dados)
- [ ] Validação de CNPJ, telefone e email
- [ ] Ocultar senha na digitação/exibição
- [ ] Busca de restaurante por CNPJ (não só por nome)

## 📚 Contexto

Projeto desenvolvido durante a trilha de Backend Python da Alura, como prática dos conceitos de funções, dicionários, listas e tratamento de exceções.
