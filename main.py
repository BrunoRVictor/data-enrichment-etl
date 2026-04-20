import pandas as pd
def extract():
    ids = pd.read_csv("ids.csv")
    users = pd.read_csv("users.csv")
    ids = ids.rename(columns = {"UserID": "user_id"})
    return ids, users

print(extract())