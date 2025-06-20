import pandas as pd
from word2number import w2n

def convert_to_digits(value):
    """Convert string numbers and words to digits, handling NaN values."""

    # Ignore null values
    if pd.isna(value):
        return value
    
    # Convert value to string, remove whitespace, and make lowercase
    str_value = str(value).strip().lower()
    
    # Try to convert directly to a number
    try:
        return int(float(str_value))
    except ValueError:
        # If direct convertion fails, try word-to_num convertion
        try:
            return w2n.word_to_num(str_value)
        except ValueError:
            # If word-to-num convertion fails, return Null value
            return pd.NA

def clean_warehouse_data(input_path, output_path) -> pd.DataFrame:
    """
    Clean warehouse data by handling missing values and converting formats.
    
    Args:
        input_path (str): Path to input CSV file
        output_path (str): Path to save cleaned CSV file
    
    Returns:
        pd.DataFrame: Cleaned dataframe object
    """
    
    # Load data
    df = pd.read_csv(input_path)
    
    # Drop unnecessary column and rename
    df = df.drop(["Product Name"], axis=1)
    df = df.rename(columns={"Product ID": "ID", "Last Restocked": "Restocked"})
    
    # Convert worded quantity values to digits
    df.Quantity = df["Quantity"].apply(convert_to_digits)
    
    # Fill missing quantities with category averages
    category_quantity_ave = round(df.groupby("Category")["Quantity"].mean())
    df.Quantity = df.Quantity.fillna(df["Category"].map(category_quantity_ave)).astype("Int64")
    
    # Fill missing prices with category averages
    category_price_ave = round(df.groupby("Category")["Price"].mean())
    df.Price = df.Price.fillna(df["Category"].map(category_price_ave))
    
    # Convert Restocked column to datetime format
    df.Restocked = pd.to_datetime(df.Restocked, errors="coerce")

    # Fill missing restock dates with median date
    median_date = df.Restocked.median()
    df.Restocked = df.Restocked.fillna(median_date)
    
    # Save cleaned data
    df.to_csv(output_path, index=False)
    
    return df

def main():
    """Main function to execute the data cleaning pipeline."""

    input_path = ("/workspaces/Data-Science-Projects/EDA/Warehouse/data/"
                  "warehouse_messy_data.csv")
    output_path = ("/workspaces/Data-Science-Projects/EDA/Warehouse/data/"
                   "warehouse_clean_data.csv")
    
    # Clean the data
    cleaned_df = clean_warehouse_data(input_path, output_path)
    
    print(f"Data cleaning completed successfully!")
    print(f"Cleaned data saved to: {output_path}")
    print(f"Final dataset shape: {cleaned_df.shape}")

if __name__ == "__main__":
    main()