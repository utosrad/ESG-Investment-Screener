https://esg-investment-screener.streamlit.app/


ESG Investment Screener

This Streamlit app allows users to screen S&P 500 companies based on ESG (Environmental, Social, and Governance) risk levels, sectors, and key financial metrics like market cap, revenue growth, and EBITDA. It combines ESG rating data with company-level financial information to help investors identify companies aligned with their ethical or sustainability priorities.

Users can:
- Filter companies by ESG Risk Level and Sector
- Set a custom Market Cap range
- View ESG score distributions
- See sector-level averages
- Export filtered company lists for further research

The app is intended for ESG-conscious investors and finance students interested in responsible investing.


--

Project Development Note

This project's primary technical challenge was integrating disparate ESG and financial datasets. The initial ESG data had significant gaps in key columns, while the S&P 500 financial data lacked standardized identifiers and had inconsistent company naming conventions.

With no reliable key to join the tables, I had to programmatically test various name fields to find the best match and minimize data loss during the merge. This required extensive data cleaning and normalization.

Setting up the Streamlit application also presented obstacles, including resolving FileNotFoundError issues caused by incorrect relative file paths and troubleshooting initial runtime command errors. Furthermore, I pivoted from using kagglehub due to documentation and workflow issues, opting instead for the more stable kaggle CLI for data acquisition.

Ultimately, what began as a straightforward dashboard became an in-depth exercise in data wrangling and environment configuration with real-world, imperfect data.
