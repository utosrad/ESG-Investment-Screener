import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
import numpy as np
import os
import kagglehub


path = kagglehub.dataset_download("andrewmvd/sp-500-stocks")

companies = pd.read_csv(os.path.join(path, "sp500_companies.csv"))


df = pd.read_csv("esg_dataset/SP 500 ESG Risk Ratings.csv")

# Standardize casing
df["Name_upper"] = df["Name"].str.strip().str.upper()
companies["Shortname_upper"] = companies["Shortname"].str.strip().str.upper()
companies["Longname_upper"] = companies["Longname"].str.strip().str.upper()

# Standardize names
df["Name_upper"] = df["Name"].str.strip().str.upper()
companies["Longname_upper"] = companies["Longname"].str.strip().str.upper()

# Merge ESG + financials
merged = pd.merge(df, companies, left_on="Name_upper", right_on="Longname_upper", how="inner")

# list of columns to keep
cols_to_keep = [
    "Name", "Sector", "Industry", "Environment Risk Score",
    "Governance Risk Score", "Social Risk Score", "Total ESG Risk score", "ESG Risk Level"
]
df = df[cols_to_keep]

# Getting rid of rows that are empty in these 4 columns
df = df.dropna(subset=[
    "Environment Risk Score", "Governance Risk Score", "Social Risk Score", "Total ESG Risk score"
])



# visualization tools

# plt.figure(figsize=(12, 6))
# sns.boxplot(data=df, x="Sector", y="Total ESG Risk score")
# plt.xticks(rotation=45)
# plt.title("ESG Risk Score Distribution by Sector")
# plt.show()


X = df[["Environment Risk Score", "Governance Risk Score", "Social Risk Score"]]
y = df["Total ESG Risk score"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestRegressor()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("R²:", r2_score(y_test, y_pred))
print("RMSE:", np.sqrt(mean_squared_error(y_test, y_pred)))
print("MAE:", mean_absolute_error(y_test, y_pred))


final = merged[[
    "Name", "Sector_x", "Total ESG Risk score", "ESG Risk Level",
    "Marketcap", "Ebitda", "Revenuegrowth", "Currentprice", "Fulltimeemployees"
]].rename(columns={"Sector_x": "Sector"})

final.to_csv("esg_screener_data.csv", index=False)