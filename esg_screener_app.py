import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv("esg_screener_data.csv")

st.set_page_config(page_title="ESG Investment Screener", layout="wide")
st.title("ESG Investment Screener")

# Sidebar filters
sector = st.sidebar.selectbox("Filter by Sector", ["All"] + sorted(df["Sector"].dropna().unique()))
risk = st.sidebar.selectbox("Filter by ESG Risk Level", ["All"] + sorted(df["ESG Risk Level"].dropna().unique()))
marketcap = st.sidebar.slider("Market Cap Range (Billions)", 
                              float(df["Marketcap"].min()/1e9), 
                              float(df["Marketcap"].max()/1e9), 
                              (float(df["Marketcap"].min()/1e9), float(df["Marketcap"].max()/1e9)))

# Apply filters
filtered = df.copy()
if sector != "All":
    filtered = filtered[filtered["Sector"] == sector]
if risk != "All":
    filtered = filtered[filtered["ESG Risk Level"] == risk]
filtered = filtered[(filtered["Marketcap"]/1e9 >= marketcap[0]) & (filtered["Marketcap"]/1e9 <= marketcap[1])]

# Main table
st.subheader("Filtered Companies")
st.dataframe(filtered[[
    "Name", "Sector", "Total ESG Risk score", "ESG Risk Level", 
    "Marketcap", "Revenuegrowth", "Ebitda", "Currentprice"
]])

# Sector average ESG
if sector != "All":
    st.markdown("### Sector Average Metrics")
    st.write(filtered[["Total ESG Risk score", "Marketcap", "Revenuegrowth"]].mean())

# ESG Risk Distribution
st.markdown("### ESG Risk Score Distribution")
fig, ax = plt.subplots()
filtered["Total ESG Risk score"].hist(bins=20, ax=ax)
plt.xlabel("ESG Risk Score")
plt.ylabel("Count")
st.pyplot(fig)

# Download button
st.download_button("Download Filtered Data", filtered.to_csv(index=False), "filtered_companies.csv")