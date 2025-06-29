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

Personal Note: Building This Was Not Easy...

This project turned out to be significantly more challenging than I initially anticipated, both technically and logistically. The first major hurdle was acquiring clean, usable datasets. The ESG dataset I found had substantial gaps and inconsistencies, particularly in the key score columns that were essential to the analysis. At the same time, most available financial datasets for S&P 500 companies were either outdated, lacked standardized identifiers like tickers, or contained inconsistent naming formats across companies. This made any sort of data integration extremely difficult.

Attempting to merge the ESG data with the financials was a painstaking, iterative process. There was no single reliable key to join them. I had to experiment with multiple columns like Name, Shortname, and Longname, all of which were plagued with mismatches due to inconsistent formatting, whitespace issues, casing differences, and special characters. Even after cleaning and normalizing everything, I still lost a significant number of companies in the merge. I had to write logic just to calculate which field provided the highest match coverage and ensure I wasn’t discarding important data.

Then came the Streamlit layer. I made the classic mistake of trying to run the app with python instead of streamlit run, which threw an avalanche of cryptic ScriptRunContext warnings that took time to research and understand. When I finally got past that, I hit another wall. The app couldn’t find the merged dataset CSV, triggering repeated FileNotFoundErrors because of relative path confusion between my script and app environment. Debugging that required carefully inspecting file paths, working directories, and restructuring the project layout.

On top of it all, I originally attempted to pull datasets using kagglehub, which sounded simple but had its own quirks. It had outdated documentation, unclear behavior with certain datasets, and poor support for standard workflows like merging with financial data. I eventually scrapped it in favor of the more reliable kaggle CLI, which required setting up credentials, handling API keys, and downloading files manually before processing.

What seemed like a basic dashboard idea evolved into a multi-day debugging session involving API configuration, data cleaning at scale, painful column-by-column matching, and framework-specific runtime problems. But in the end, every piece came together. I learned far more than I expected, not just about ESG data, but about building robust, user-facing data applications from real-world, imperfect inputs.
