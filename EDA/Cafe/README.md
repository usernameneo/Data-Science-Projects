# Data Cleaning Project: Cafe Sales

## Overview
This project focuses on cleaning and standardising cafe sales transaction data to support accurate financial reporting, customer behavior analysis, and business performance monitoring. The dataset contains transaction records with product information, quantities, pricing, payment methods, and timestamps that require comprehensive cleaning and missing value imputation to ensure data reliability for downstream analysis and business intelligence reporting.

**Business Problem**: Incomplete transaction records and inconsistent data formats in the cafe's point-of-sale system are hindering accurate sales analysis, inventory management, and customer behavior insights. Missing values in critical fields like item names, quantities, and prices prevent reliable revenue calculations and business performance tracking.

**Key Stakeholders**: 
- Cafe Management Team
- Financial Reporting Department
- Marketing & Customer Analytics Team
- Inventory Management Staff
- Business Intelligence Analysts

## Dataset Information
**Source**: [Kaggle](https://www.kaggle.com/datasets/ahmedmohamed2003/cafe-sales-dirty-data-for-cleaning-training)  
**Format**: CSV file  
**Original Size**: 10 000 × 8 columns  

**Key Variables/Columns**:
- **Txn_ID**: Unique transaction identifier
- **Item**: Product/menu item purchased
- **Quantity**: Number of items purchased
- **Unit_Price**: Price per individual item
- **Total**: Total transaction amount
- **Payment**: Payment method used
- **Location**: Point of transaction (In-Store, Takeaway)
- **Date**: Transaction timestamp

**Known Data Quality Issues**:
- Missing values across Item, Quantity, Unit_Price, Total, Payment, and Location columns
- "UNKNOWN" and "ERROR" placeholder values requiring standardisation
- Inconsistent data types (numeric fields stored as text)
- Invalid date formats requiring conversion
- Incomplete transaction records missing essential financial information

## Data Quality Assessment
**Missing Values Analysis**:
- Item: Variable missing values (replaced with domain knowledge)
- Quantity: Variable missing values (calculated using mathematical relationships)
- Unit_Price: Variable missing values (imputed using menu pricing)
- Total: Variable missing values (calculated using Quantity × Unit_Price)
- Payment: Variable missing values (imputed using mode by item category)
- Location: Variable missing values (imputed using mode by item category)
- Date: Variable missing values (records removed if date unavailable)

**Data Type Inconsistencies**:
- Numeric columns stored as object/text instead of proper numeric types
- Date column stored as string instead of datetime
- Placeholder error values ("UNKNOWN", "ERROR") requiring standardisation

**Outliers and Anomalies**:
- Transactions with impossible combinations (e.g., missing all financial data)
- Invalid date entries requiring conversion or removal

## Cleaning Process Summary
**High-level Steps Taken**:
1. **Data Type Conversion**: Standardised all columns to appropriate data types (Int64, Float64, datetime64)
2. **Error Value Standardisation**: Converted "UNKNOWN" and "ERROR" placeholders to proper NA values
3. **Data Pruning**: Removed transactions with insufficient data for meaningful analysis
4. **Menu-Based Price Imputation**: Used domain knowledge of cafe menu to impute missing unit prices
5. **Mathematical Value Recovery**: Calculated missing quantities and totals using relationship: Total = Quantity × Unit_Price
6. **Price-Based Item Imputation**: Imputed missing item names using price-to-item mapping
7. **Categorical Imputation**: Used mode imputation within item groups for Payment and Location

**Tools and Libraries Used**:
- **pandas**: Data manipulation, type conversion, and analysis
- **numpy**: Mathematical operations and vectorised calculations
- **random**: Random selection for item imputation when multiple options available

**Domain Knowledge Applied**:
- **Cafe Menu Dictionary**: Standard pricing for all menu items
- **Price-to-Item Mapping**: Reverse lookup for item imputation
- **Business Logic**: Mathematical relationships between quantity, price, and total

**Validation Methods Applied**:
- Data type verification after conversions
- Missing value elimination confirmation
- Mathematical relationship validation (Total = Quantity × Unit_Price)
- Date format consistency verification

## Results
**Before/After Comparison**:
- **Data Types**: 5 columns converted to appropriate types (Quantity → Int64, Unit_Price/Total → Float64, Date → datetime64)
- **Missing Values**: Systematic elimination of missing values through imputation and calculation
- **Data Consistency**: Standardised pricing using menu knowledge and mathematical relationships
- **Transaction Completeness**: Retained only transactions with sufficient data for analysis

**Data Quality Improvements**:
- **Maximized data completeness** through intelligent imputation strategies
- **Consistent pricing structure** aligned with actual cafe menu
- **Reliable financial calculations** using mathematical relationships
- **Enhanced categorical data** through group-based mode imputation
- **Improved temporal consistency** with proper datetime formatting

**Final Dataset Characteristics**:
- **Size**: 9514 × 8 columns (after pruning incomplete transactions)
- **Data Types**: 1 Int64 (Quantity), 2 Float64 (Unit_Price, Total), 4 object (Item, Payment, Location), 1 datetime64 (Date)
- **Missing Values**: Minimised through comprehensive imputation strategy
- **Quality Score**: High - ready for financial analysis, customer behavior studies, and business intelligence

## Usage
**How to Run the Cleaning Pipeline**:
```bash
python cafe-cleaning.py
```

**Dependencies and Requirements**:
```
pandas>=1.5.0
numpy>=1.20.0
```

**Installation**:
```bash
pip install pandas numpy
```

**Input Requirements**:
- CSV file with cafe sales transaction data
- Expected columns: Transaction ID,Item,Quantity,Price Per Unit,Total Spent,Payment Method,Location,Transaction Date
- Update `input_path` variable in `main()` function with