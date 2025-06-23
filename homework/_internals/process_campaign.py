from .save_output import save_output


import pandas as pd


def process_campaign(data):
    campaign = data[["client_id", "number_contacts", "contact_duration", "previous_campaign_contacts",
                     "previous_outcome", "campaign_outcome"]].copy()
    campaign["previous_outcome"] = (campaign["previous_outcome"] == "success").astype(int)
    campaign["campaign_outcome"] = (campaign["campaign_outcome"] == "yes").astype(int)
    campaign["last_contact_date"] = pd.to_datetime(
        "2022-" + data["month"] + "-" + data["day"].astype(str),
        format="%Y-%b-%d"
    )
    save_output(campaign, "files/output", "campaign.csv")