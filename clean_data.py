import pandas as pd
import numpy as np
import os

def load_data(file_path):
    """
    Loads the raw CSV dataset and creates a deep copy for processing.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} was not found.")
    
    print(f"--- Loading data from: {file_path} ---")
    raw_data = pd.read_csv(file_path)
    print(f"Initial shape: {raw_data.shape}")

    # Returns a deep copy to ensure the processed DataFrame is independent 
    # and avoid SettingWithCopy warnings in the pipeline.
    return raw_data.copy(deep=True)

def clean_strings(df):
    """
    Standardizes categorical strings: removes whitespaces and simplifies labels.
    """
    print("Standardizing strings and labels...")
    
    # Identify categorical columns (object type)
    categorical_cols = df.select_dtypes(include=['object']).columns
    
    # Strip leading/trailing whitespaces
    df[categorical_cols] = df[categorical_cols].apply(lambda x: x.str.strip())
    
    # Map Gender and Customer Type to shorthand for efficiency
    df["Gender"] = df["Gender"].replace({"Male": "M", "Female": "F"})
    df["Customer type"] = df["Customer type"].replace({"Member": "M", "Normal": "N"})
    
    return df

def optimize_types(df):
    """
    Converts columns to appropriate data types to save memory and improve performance.
    """
    print("Optimizing data types...")
    
    # Convert to categorical type
    to_category = ["Branch", "City", "Customer type", "Gender", "Product line", "Payment"]
    for col in to_category:
        df[col] = df[col].astype("category")
        
    # Handle Date and Time

    # Format for parsing: 
    # %m/%d/%Y for date (e.g., 01/05/2021) and
    # %I:%M:%S %p for time with format like 12:30:45 PM
    date_format = "%m/%d/%Y %I:%M:%S %p"

    df["Full_Date"] = pd.to_datetime(df["Date"] + " " + df["Time"], format=date_format)
    df = df.drop(columns=["Date", "Time"])
    
    return df

def validate_financial_integrity(df):
    """
    Validates that Sales = Tax 5% + COGS using numerical tolerance.
    """
    print("Verifying financial integrity...")
    
    expected_sales = df['cogs'] + df['Tax 5%']
    # Check if values are close enough to account for floating point rounding
    integrity_check = np.allclose(df['Sales'], expected_sales, atol=0.01)
    
    if integrity_check:
        print("✅ Success: Financial totals are consistent.")
    else:
        # Identify rows with discrepancies if the check fails
        discrepancies = df[~np.isclose(df['Sales'], expected_sales, atol=0.01)]
        print(f"⚠️ Warning: Found {len(discrepancies)} rows with inconsistent totals.")
        
    return df

def generate_quality_summary(df):
    """
    Creates a summary of the dataset's final state.
    """
    summary = pd.DataFrame({
        "Dtype": df.dtypes,
        "Total Rows": len(df),
        "Non-Null Count": df.count(),
        "Missing (%)": (df.isna().mean() * 100).round(2),
        "Unique Values": df.nunique(),
        "Zero Values": (df == 0).sum(),
        "Negatives": df.select_dtypes(include=['number']).lt(0).sum()
    })
    
    # Basic statistics only for numeric columns
    desc = df.describe().T[['min', 'mean', 'max']].round(2)
    summary = summary.join(desc, how='left')
    
    return summary


def save_output(df, summary, base_filename):
    """
    Exports the cleaned data to Excel (multi-sheet) and Parquet formats.
    """
    # 1. Save to Excel
    excel_file = f"{base_filename}.xlsx"
    with pd.ExcelWriter(excel_file, engine='xlsxwriter') as writer:
        df.to_excel(writer, sheet_name='Cleaned Data', index=False)
        summary.to_excel(writer, sheet_name='Quality Report')
    
    # 2. Save to Parquet (Optimized for Data Science portfolios)
    parquet_file = f"{base_filename}.parquet"
    df.to_parquet(parquet_file, index=False)
    
    print(f"--- Process completed successfully ---")
    print(f"Files generated: {excel_file}, {parquet_file}")

def main():
    """
    Main execution pipeline.
    """
    # Configuration
    INPUT_CSV = "SuperMarketAnalysis.csv"
    OUTPUT_BASE = "SupermarketSales_Cleaned"
    
    try:
        # Step-by-step pipeline execution
        df = load_data(INPUT_CSV)
        df = clean_strings(df)
        df = optimize_types(df)
        df = validate_financial_integrity(df)
        
        # Final reporting and export
        quality_report = generate_quality_summary(df)
        save_output(df, quality_report, OUTPUT_BASE)
        
    except Exception as e:
        print(f"❌ An error occurred during processing: {e}")

if __name__ == "__main__":
    main()