from .save_output import save_output


import pandas as pd


def process_client(data):
    client = data[["client_id", "age", "job", "marital", "education", "credit_default", "mortgage"]].copy()
    client["job"] = client["job"].str.replace(".", "").str.replace("-", "_")
    client["education"] = client["education"].str.replace(".", "_").replace("unknown", pd.NA)
    client["credit_default"] = (client["credit_default"] == "yes").astype(int)
    client["mortgage"] = (client["mortgage"] == "yes").astype(int)
    save_output(client, "files/output", "client.csv")