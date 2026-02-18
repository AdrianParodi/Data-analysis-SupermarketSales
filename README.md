# 🛒 Supermarket Sales: Professional Data Cleaning Pipeline

## 📋 Project Overview
This project transforms a raw retail dataset of 1,000 transactions into a high-quality, production-ready format. It's not just a cleaning script; it's a modular data pipeline designed with memory efficiency and data integrity as top priorities.

## 🛠️ Key Features & Engineering Decisions
**1. Memory Optimization (The "Category" Hack)**  
Instead of storing repetitive strings like "Member" or "Normal" as heavy objects, I converted categorical columns to the `category` data type.  
- **Impact:** Reduced memory usage for targeted columns by ~80%.
- **Outcome:** A leaner DataFrame that loads faster and scales better.

**2. Financial Integrity Validation**  
I implemented a cross-field validation check to ensure that:

$$\text{Sales} = \text{COGS} + \text{Tax (5\\%)}$$

Using `numpy.allclose`, the pipeline verifies mathematical consistency while accounting for floating-point rounding errors.  

**3. Temporal Consolidation**  
Separate `Date` and `Time` columns were merged into a single `Full_Date` (datetime64) object with explicit format parsing `(%m/%d/%Y %I:%M:%S %p)` to avoid regional ambiguity and enable time-series analysis.

**4. String Normalization**
- Removed inconsistent whitespaces.
- Mapped long strings to shorthand codes (e.g., `Member` → `M`, `Female` → `F`) to improve storage and readability.

## 🚀 How to Run
**Prerequisites**  
Install the required engines for Parquet and Excel support:

```Bash
pip install pandas numpy pyarrow xlsxwriter
```

**Execution**  
Simply run the automated cleaning script:
```Bash
python clean_data.py
```

## 📁 Repository Structure
| File |Description |
|:------|:-------------|
| `cleaning.ipynb` | Interactive exploratory cleaning process and prototyping. |
| `clean_data.py` | Automated Pipeline: Modular script for production-ready cleaning. |
| `DATA_DICTIONARY.md` | Detailed explanation of every column and data type. |
| `SuperMarketAnalysis.csv` | Original raw dataset. |
| `SupermarketSales_Cleaned.parquet` | Final output in high-performance columnar storage format. |
| `SupermarketSales_Cleaned.xlsx` | Final output in xlsx (Excel) format. |