import pandas as pd
import sys

def extract(caminho):
    if (caminho.endswith(".csv")):
     users = pd.read_csv(caminho)    
    elif (caminho.endswith("json")):
     users = pd.read_json(caminho)
    else:
     raise ValueError(f"Formato de arquivo '{caminho}' não suportado. Use um arquivo CSV ou JSON.")
    return users

def transform(users):
    users = users.copy()
    users["user_id"] = range(1, len(users) + 1)
    cols = ["user_id"] + [col for col in users.columns if col != "user_id"]
    users = users[cols]
    users = users.dropna(subset=["user_age"])
    users["user_age"] = users["user_age"].astype(int)
    users["user_wage"] = users["user_wage"].astype(float)
    users["user_name"] = users["user_name"].str.strip().str.title()
    users["bonus"] = users["user_wage"] * 0.1
    return users

def load(df, formato="json"):
    if formato.lower() == "json":
     caminho_saida = "output/processed_users.json"
     df.to_json(caminho_saida, orient="records", indent=4)
     print(f"{len(df)} registros salvos com sucesso.\nArquivo JSON gerado na pasta Output em {caminho_saida}.")
    elif formato.lower() == "csv":
     caminho_saida = "output/processed_users.csv"
     df.to_csv(caminho_saida, index=False)
     print(f"{len(df)} registros salvos com sucesso.\nArquivo CSV gerado na pasta Output em {caminho_saida}.")
    else:
     raise ValueError(f"Formato de saída '{formato}' não suportado. Use 'json' ou 'csv'.")

def main():
 try:
    print("Iniciando o processo de ETL...\n(Se nenhum argumento for fornecido, o programa usará 'data/users.csv' como entrada e 'json' como formato de saída por padrão.)")
    caminho = (f"data/{sys.argv[1]}") if len(sys.argv) > 1 else "data/users.csv"
    print(f"Arquivo de entrada: {caminho}")
    formato = sys.argv[2] if len(sys.argv) > 2 else "json"
    print(f"Formato de saída: {formato}")
    users = extract(caminho)
    print("Extração concluída.")
    df = transform(users)
    print("Transformação concluída.")
    load(df, formato)
    print("Carregamento concluído. Processo de ETL finalizado.")
 except Exception as e:
    print(f"Ocorreu um erro durante o processo de ETL: {e}")

if __name__ == "__main__":
    main()