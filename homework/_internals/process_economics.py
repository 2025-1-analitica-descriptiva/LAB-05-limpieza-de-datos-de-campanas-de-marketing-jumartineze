from .save_output import save_output


def process_economics(data):
    economics = data[["client_id", "cons_price_idx", "euribor_three_months"]].copy()
    save_output(economics, "files/output", "economics.csv")