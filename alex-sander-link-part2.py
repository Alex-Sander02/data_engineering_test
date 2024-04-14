import pandas as pd
from datetime import date

saturday_df = pd.read_csv("data_2023-02-11.csv", encoding="UTF-8")
sunday_df = pd.read_csv("data_2023-02-12.csv", encoding="UTF-8")

saturday_df["generation_date"] = date.today()
sunday_df["generation_date"] = date.today()

weekend_df = pd.concat([saturday_df, sunday_df], ignore_index = True)

weekend_df.to_csv("weekend.csv", index=False, encoding="UTF-8")