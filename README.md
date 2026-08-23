## 🎯 Objetivo do Projeto

Desenvolver um módulo em Python reutilizável, modular e orientado a objetos, capaz de processar dados em lote em formato CSV **sem o uso de bibliotecas de terceiros** (como `pandas`, `numpy` ou `matplotlib`), garantindo alta qualidade técnica, legibilidade e manutenibilidade.

## 🚀 Repositório github
https://github.com/ricardobs23/Programacao_para_Dados

🚀 Como Executar o Projeto

Pré-requisitos
Python 3.8 ou superior instalado.

## 🚀 Para processar os dados completos da Steam e visualizar os discursos analíticos gerados no console:

python main.py

## 📁 Estrutura do Repositório

Programacao_para_Dados/
│
├── dados/
│   ├── dataset_completo.csv      # Base completa com +70.000 jogos da Steam (maio/2023)[cite: 6]
│   └── amostra_20_jogos.csv      # Amostra aleatória de 20 jogos para validação de testes
│
├── steam_analyzer/               # Pacote Python para análise de dados
│   ├── __init__.py               # Torna a pasta um pacote importável
│   ├── exceptions.py             # Tratamento e exceções personalizadas de dados
│   ├── models.py                 # Modelo Orientado a Objetos (Classe Jogo)
│   ├── repository.py             # Leitura e carregamento via leitor nativo `csv`
│   └── analyzer.py               # Lógica de processamento das 3 consultas analíticas
│
├── tests/
│   └── test_analyzer.py          # Testes automatizados na amostra com asserções
│
├── main.py                       # Execução do pipeline principal de análise
└── README.md                     # Documentação e instruções do projeto

