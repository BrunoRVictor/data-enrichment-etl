# Data Enrichment ETL Pipeline (Python + Pandas)

## 📌 Descrição

Este projeto implementa um pipeline de ETL (Extract, Transform, Load) capaz de processar dados a partir de arquivos CSV ou JSON, enriquecendo os registros com identificadores únicos e aplicando transformações de limpeza e padronização.

O sistema funciona como uma ferramenta de linha de comando (CLI), permitindo ao usuário fornecer arquivos de entrada e escolher o formato de saída. Leia abaixo para saber como executar.

OBS: Para arquivos novos, eles precisam estar padronizados com as mesmas colunas (e os nomes) dos arquivos padrões que estão no projeto.

---

## ⚙️ Tecnologias utilizadas

* Python
* pandas

---

## 🔄 Funcionalidades

* Leitura de arquivos CSV e JSON
* Geração automática de IDs (`user_id`)
* Limpeza de dados (remoção de nulos)
* Conversão de tipos
* Padronização de texto
* Criação de novas colunas (`bonus`)
* Exportação para JSON ou CSV

---

## 🚀 Como executar (3 passos)

### ▶️ 1. Escreva a entrada padrão

```bash
python main.py
```

### ▶️ 2. Passe o nome dos arquivos manualmente 

```bash
python main.py users.csv
python main.py users.json
```

### ▶️ 3. Escolha o formato de saída

```bash
python main.py users.csv json
python main.py users.csv csv
```

Pronto. Só executar e ter o seu arquivo formatado com os IDs adicionados.

---

## 📂 Estrutura do projeto

```id="projtree"
project/
│
├── data/
│   └── users.csv
│
├── output/
│
├── main.py
└── README.md
```

---

## 📊 Exemplo de saída

```json
[
    {
        "user_id": 1,
        "user_name": "Bruno",
        "user_age": 23,
        "user_wage": 2000.0,
        "bonus": 200.0
    }
]
```

---

## 🧠 Observações

* O `user_id` é gerado automaticamente com base na ordem dos registros
* O sistema assume entrada tabular (CSV ou JSON em formato de lista de objetos)
* O projeto demonstra um fluxo simplificado de ETL

---

## 📈 Possíveis melhorias

* Validação de schema (colunas obrigatórias)
* Suporte a JSON aninhado
* Integração com banco de dados
* Interface CLI mais robusta (argparse)
