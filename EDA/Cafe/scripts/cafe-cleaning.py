import pandas as pd
import numpy as np
from random import choice


def data_type_convert(dataframe: pd.DataFrame) -> pd.DataFrame:
    """
    Convert data types and clean initial data inconsistencies.
    
    Parameters:
    -----------
    dataframe : pd.DataFrame
        Raw cafe sales data with columns: Txn_ID, Item, Quantity, Unit_Price, 
        Total, Payment, Location, Date
    
    Returns:
    --------
    pd.DataFrame
        DataFrame with corrected data types and cleaned values
    """
    
    # Create a copy to avoid modifying the original dataframe
    dataframe = dataframe.copy()
    
    # Replace placeholder error values with proper NA values for Item column
    dataframe.loc[dataframe.Item.isin(["UNKNOWN", "ERROR"]), "Item"] = pd.NA
    
    # Convert numeric columns to nullable integer/float types to handle missing values
    dataframe.Quantity = pd.to_numeric(dataframe.Quantity, errors="coerce").astype("Int64")
    dataframe.Unit_Price = pd.to_numeric(dataframe.Unit_Price, errors="coerce").astype("Float64")
    dataframe.Total = pd.to_numeric(dataframe.Total, errors="coerce").astype("Float64")
    
    # Replace placeholder error values with proper NA values for Location column
    dataframe.loc[dataframe.Location.isin(["UNKNOWN", "ERROR"]), "Location"] = pd.NA
    
    # Convert date strings to datetime objects
    dataframe.Date = pd.to_datetime(dataframe.Date, errors="coerce")

    return dataframe


def data_pruning(dataframe: pd.DataFrame) -> pd.DataFrame:
    """
    Remove rows with insufficient data for meaningful analysis.
    
    This function identifies and removes transactions that lack essential information
    needed for sales analysis. It removes rows where critical combinations of
    fields are missing, making the transaction unusable.
    
    Removal criteria:
    - Missing Item, Quantity, and Unit_Price 
    - Missing Quantity, Unit_Price, and Total 
    - Missing Item, Unit_Price, and Total 
    - Missing Item, Quantity, and Total
    - Missing Quantity and Total 
    - Missing Date 
    
    Parameters:
    -----------
    dataframe : pd.DataFrame
        DataFrame after data type conversion
    
    Returns:
    --------
    pd.DataFrame
        DataFrame with incomplete/invalid rows removed
    """
    dataframe = dataframe.copy()
    
    # Remove rows missing core product information (Item, Quantity, Unit_Price)
    mask = dataframe.Item.isna() & dataframe.Quantity.isna() & dataframe.Unit_Price.isna()
    dataframe = dataframe.drop(dataframe[mask].index)

    # Remove rows missing all financial information (Quantity, Unit_Price, Total)
    mask = dataframe.Quantity.isna() & dataframe.Unit_Price.isna() & dataframe.Total.isna()
    dataframe = dataframe.drop(dataframe[mask].index)

    # Remove rows missing item and all value information (Item, Unit_Price, Total)
    mask = dataframe.Item.isna() & dataframe.Unit_Price.isna() & dataframe.Total.isna()
    dataframe = dataframe.drop(dataframe[mask].index)

    # Remove rows missing item and quantity information (Item, Quantity, Total)
    mask = dataframe.Item.isna() & dataframe.Quantity.isna() & dataframe.Total.isna()
    dataframe = dataframe.drop(dataframe[mask].index)

    # Remove rows missing sufficient information for mathematical recovery
    mask = dataframe.Quantity.isna() & dataframe.Total.isna()
    dataframe = dataframe.drop(dataframe[mask].index)

    # Remove rows with missing dates
    dataframe = dataframe.dropna(subset=["Date"])

    return dataframe


def impute_unit_price(dataframe: pd.DataFrame, menu_dict: dict) -> pd.DataFrame:
    """
    Impute missing Unit_Price values using Item names and a menu dictionary. Only imputes prices for known menu items
    to maintain data integrity.
    
    For rows where:
    - Item is present (not NaN)
    - Unit_Price is missing (NaN)  
    - Item exists as a key in the menu dictionary
    
    The missing Unit_Price will be filled with the corresponding price from the menu.
    
    Parameters:
    -----------
    dataframe : pd.DataFrame
        DataFrame containing 'Item' and 'Unit_Price' columns
    menu_dict : dict
        Dictionary mapping item names to their standard prices
    
    Returns:
    --------
    pd.DataFrame
        DataFrame with imputed Unit_Price values where possible
    """
    dataframe = dataframe.copy() 
    
    # Create boolean mask for rows that meet imputation criteria
    mask = (dataframe['Item'].notna() & 
        dataframe['Unit_Price'].isna() & 
        dataframe['Item'].isin(menu_dict.keys()))
    
    # Impute Unit_Price for matching rows
    dataframe.loc[mask, 'Unit_Price'] = dataframe.loc[mask, 'Item'].map(menu_dict)
    
    return dataframe


def impute_item(dataframe: pd.DataFrame, price_item_dict: dict) -> pd.DataFrame:
    """
    Impute missing Item values using Unit_Price and a price-to-items mapping dictionary.
    
    For rows where Unit_Price is present, Item is missing, and the Unit_Price exists 
    in the price_item_dict, randomly selects an item from the available options to preserve price consistency while maintaining data diversity.
    
    Parameters:
    -----------
    dataframe : pd.DataFrame
        DataFrame containing 'Item' and 'Unit_Price' columns
    price_item_dict : dict
        Dictionary mapping prices to lists of items with that price
        
    Returns:
    --------
    pd.DataFrame
        DataFrame with imputed Item values where possible
    """
    dataframe = dataframe.copy()
    
    # Create boolean mask for rows that meet imputation criteria
    mask = (dataframe['Unit_Price'].notna() & 
        dataframe['Item'].isna() & 
        dataframe['Unit_Price'].isin(price_item_dict.keys()))
    
    # Define function to randomly select item for a given price
    def select_random_item(price):
        return choice(price_item_dict[price])
    
    # Impute Item for matching rows using random selection from valid options
    dataframe.loc[mask, 'Item'] = dataframe.loc[mask, 'Unit_Price'].map(select_random_item)
    
    return dataframe


def calculate_missing_values(dataframe: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate missing values for Quantity, Unit_Price, and Total based on available data.
    
    Uses the relationship: Total = Quantity * Unit_Price
    - If Quantity is missing but Unit_Price and Total exist: Quantity = Total / Unit_Price
    - If Unit_Price is missing but Quantity and Total exist: Unit_Price = Total / Quantity  
    - If Total is missing but Quantity and Unit_Price exist: Total = Quantity * Unit_Price
    
    Parameters:
    -----------
    dataframe : pd.DataFrame
        DataFrame containing Quantity, Unit_Price, and Total columns
    
    Returns:
    --------
    pd.DataFrame
        DataFrame with calculated missing values where mathematically possible
    """
    dataframe = dataframe.copy()
    
    # Calculate missing Quantity values 
    dataframe.Quantity = np.where(dataframe.Unit_Price.notna() & dataframe.Total.notna(), 
        dataframe.Total / dataframe.Unit_Price, 
        dataframe.Quantity)
    
    # Calculate missing Unit_Price values
    dataframe.Unit_Price = np.where(dataframe.Quantity.notna() & dataframe.Total.notna(), 
        dataframe.Total / dataframe.Quantity, 
        dataframe.Unit_Price)
    
    # Calculate missing Total values 
    dataframe.Total = np.where(dataframe.Quantity.notna() & dataframe.Unit_Price.notna(), 
        dataframe.Quantity * dataframe.Unit_Price, 
        dataframe.Total)
    
    return dataframe


def clean_cafe_data(input_path: str, output_path: str) -> pd.DataFrame:
    """
    Complete data cleaning pipeline for cafe sales data.
    
    Pipeline steps:
    1. Load raw data and rename columns
    2. Convert data types and handle erroneous values
    3. Remove incomplete/invalid records
    4. Impute missing prices using menu dictionary
    5. Calculate missing values using mathematical relationships
    6. Impute missing items using price-to-item dictionary
    7. Fill remaining missing categorical values using mode by Item group
    8. Save cleaned data to specified output path
    
    Parameters:
    -----------
    input_path : str
        File path to the raw CSV data file
    output_path : str
        File path where cleaned data should be saved
    
    Returns:
    --------
    pd.DataFrame
        Cleaned dataframe ready for analysis
    """
    
    # Define cafe menu with standard pricing
    menu = {
        "Cookie": 1.0, "Tea": 1.5, "Coffee": 2.0, "Cake": 3.0,
        "Juice": 3.0, "Sandwich": 4.0, "Smoothie": 4.0, "Salad": 5.0,
    }

    # Create reverse mapping for item imputation. This allows us to impute missing item names when we know the price
    price_item_dict = {}
    for item, price in menu.items():
        price_item_dict.setdefault(price, []).append(item)
    
    # Load raw data from CSV file
    df = pd.read_csv(input_path)
    
    # Rename columns for efficiency
    df.columns = ['Txn_ID', 'Item', 'Quantity', 'Unit_Price', 'Total',
                  'Payment', 'Location', 'Date']
    
    # Apply cleaning pipeline in sequence
    df = data_type_convert(df)
    df = data_pruning(df)
    df = impute_unit_price(df, menu)
    df = calculate_missing_values(df)
    df = impute_item(df, price_item_dict)

    # Define mode function that handles empty categorical rows
    mode = lambda x: x.fillna(x.mode().iloc[0]) if not x.mode().empty else x

    # Fill missing Payment methods using mode within each Item group
    df.Payment = df.groupby('Item').Payment.transform(mode)
    
    # Fill missing Locations using mode within each Item group
    df.Location = df.groupby('Item').Location.transform(mode)

    # Save cleaned dataset
    df = df.reset_index()
    df.to_csv(output_path, index=False)

    return df


def main():
    """
    Main function to execute the data cleaning pipeline.
    """

    # Define file paths for input and output data
    input_path = ("/workspaces/Data-Science-Projects/EDA/Cafe/data/"
                  "dirty_cafe_sales.csv")
    output_path = ("/workspaces/Data-Science-Projects/EDA/Cafe/data/"
                   "cafe_clean_data.csv")
    
    # Execute the complete data cleaning pipeline
    cleaned_df = clean_cafe_data(input_path, output_path)
    
    # Provide summary information about the cleaning results
    print(f"\n{'='*50}")
    print(f"DATA CLEANING SUMMARY")
    print(f"{'='*50}")
    print(f"✓ Data cleaning completed successfully!")
    print(f"✓ Cleaned data saved to: {output_path}")
    print(f"✓ Final dataset shape: {cleaned_df.shape}\n")
    

# Execute the main function when script is run directly
if __name__ == "__main__":
    main()