import pandas as pd
def extract():
    ids = pd.read_csv("data/ids.csv")
    users = pd.read_csv("data/users.csv")
    return ids, users

def transform(ids, users):
    if len(ids) != len(users):
     raise ValueError("Invalid data: mismatch in number of IDs and users.")
    users = users.copy()
    users["user_id"] = ids["UserID"].values
    cols = ["user_id"] + [col for col in users.columns if col != "user_id"]
    users = users[cols]
    users = users.dropna(subset=["user_age"])
    users = users[users["user_age"] >= 18].copy()
    users["user_age"] = users["user_age"].astype(int)
    users["user_wage"] = users["user_wage"].astype(float)
    users["user_name"] = users["user_name"].str.strip().str.title()
    users["bonus"] = users["user_wage"] * 0.1
    return users

def load(df):
    df.to_json("output/processed_users.json", orient="records", indent=4)
    print(f"{len(df)} registros salvos com sucesso.")

def main():
 try:
    print("Iniciando o processo de ETL...")
    ids, users = extract()
    print("Extração concluída.")
    df = transform(ids, users)
    print("Transformação concluída.")
    load(df)
    print("Carregamento concluído. Processo de ETL finalizado.\nArquivo JSON gerado na pasta Output.")
 except Exception as e:
    print(f"Ocorreu um erro durante o processo de ETL: {e}")

if __name__ == "__main__":
    main()