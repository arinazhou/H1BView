# H1BView: H1B Job Title Insight Dashboard

Currently, this is a lightweight, interactive dashboard that helps international students explore job sponsorship trends by job title, using FY2025 Q2 LCA Disclosure Data.

Built with `Streamlit`, `Pandas`, `Plotly`, and SQL, this project serves as both a career research tool and a data-driven résumé booster.

---

## Purpose

**Why this project?**

Many international students struggle to understand which jobs, companies, and roles have higher H1B sponsorship potential. This dashboard provides a first step toward exploring this question using real U.S. government labor condition application (LCA) disclosure data.

> Note:  
> Although the project originally planned to **compare LCA filings with USCIS H-1B approval data**, this feature is temporarily postponed for the following reasons:
>
> - **USCIS 2025 data not fully released**  
> - **FY2024 and FY2025 use different selection rules**: a new lottery mechanism effective March 2024 significantly alters approval logic, which causes recent datasets to just represent a transitional trend
> - To ensure accurate, meaningful cross-source comparisons, deeper restructuring will be needed (planned for future phases)

---

## Features

1. Search job titles using keyword  
2. Display matched cases by employer, title, state, estimated salary, and case status 
3. Visualize:
- Top 10 employers by median certified salary
- Approval vs Denial rate for searched keyword


| Dashboard Search | Salary & Approval Charts |
|------------------|--------------------------|
| *(Add Screenshot Here)* | *(Add Screenshot Here)* |


