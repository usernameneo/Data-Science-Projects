# Data Cleaning Project: Warehouse

## Overview
This project focuses on cleaning and standardizing warehouse inventory data to support accurate stock management and operational decision-making. The dataset contains product information, stock levels, pricing, and restocking dates that require standardization and missing value imputation to ensure data reliability for downstream analysis and reporting.

**Business Problem**: Inconsistent data formats and missing values in the warehouse management system are hindering accurate inventory tracking, stock level monitoring, and supplier performance analysis.

**Key Stakeholders**: 
- Warehouse Operations Team
- Inventory Management Department
- Supply Chain Analysts
- Business Intelligence Team

## Dataset Information
**Source**: GitHub - [https://github.com/eyowhite/Messy-dataset/tree/main]  
**Format**: CSV file  
**Original Size**: 1000 records × 10 columns  

**Key Variables/Columns**:
- **Product ID**: Unique identifier for each product
- **Product Name**: Nondescript name of the product
- **Category**: Product classification (Electronics, Clothing, etc.)
- **Warehouse**: Storage facility identifier
- **Location**: Specific storage location within warehouse
- **Quantity**: Current stock levels
- **Price**: Product pricing information
- **Supplier**: Supplier information
- **Status**: Product availability status
- **Last Restocked**: Date of most recent inventory replenishment

**Known Data Quality Issues**:
- Quantity values stored as text (including written numbers like "two hundred")
- Missing values across Quantity, Price, and Last Restocked columns
- Inappropriate date formats in Last Restocked column
- Redundant Product Name column when Product ID serves as unique identifier

## Data Quality Assessment
**Missing Values Analysis**:
- Quantity: 158 missing values
- Price: 207 missing values  
- Last Restocked: 200 missing values
- Other columns: Complete data

**Data Type Inconsistencies**:
- Quantity column stored as object instead of numeric
- Last Restocked stored as object instead of datetime
- Mixed text and numeric values in Quantity field

**Outliers and Anomalies**:
- Quantity values containing written numbers ("two hundred")
- Date format inconsistencies (DD/MM/YYYY strings)
- No duplicate records identified

## Cleaning Process Summary
**High-level Steps Taken**:
1. **Column Management**: Removed redundant Product Name column and renamed columns for clarity
2. **Data Type Conversion**: Converted quantity text values to numeric format using custom function
3. **Missing Value Imputation**: Applied category-based mean imputation for Quantity and Price
4. **Date Standardization**: Converted Last Restocked to proper datetime format
5. **Missing Date Handling**: Used median date imputation for missing restock dates

**Tools and Libraries Used**:
- **pandas**: Data manipulation and analysis
- **word2number**: Converting written numbers to digits

**Validation Methods Applied**:
- Data type verification after conversions
- Missing value count validation
- Date format consistency verification

## Results
**Before/After Comparison**:
- **Data Types**: 3 columns converted to appropriate types (Quantity → Int64, Last Restocked → datetime64)
- **Missing Values**: Eliminated all missing values through imputation
- **Data Consistency**: Standardized quantity formats and date representations
- **Column Count**: Reduced from 10 to 9 columns (removed redundant Product Name)

**Data Quality Improvements**:
- **100% data completeness** achieved across all columns
- **Standardized numeric formats** for all quantity values
- **Consistent datetime formatting** for restocking dates
- **Improved data usability** for analysis and reporting

**Final Dataset Characteristics**:
- **Size**: 1000 records × 9 columns
- **Data Types**: 2 int64, 5 object, 1 float64, 1 datetime64
- **Missing Values**: 0 across all columns
- **Quality Score**: High - ready for analysis and operational use

## Usage
**How to Run the Cleaning Pipeline**:
```bash
python warehouse_cleaning.py
```

**Dependencies and Requirements**:
```
pandas>=1.5.0
word2number>=2.0.0
```

**Installation**:
```bash
pip install pandas word2number
```

**Input Requirements**:
- CSV file with warehouse data
- Update `input_path` variable in `main()` function with your file location

**Output File Locations**:
- **Cleaned Dataset**: `/workspaces/Data-Science-Projects/EDA/Warehouse/data/warehouse_clean_data.csv`
- **Processing Log**: Console output with cleaning summary and dataset dimensions

**Configuration**:
- Modify file paths in the `main()` function as needed
- Adjust imputation methods in `clean_warehouse_data()` function if different strategies are required

**Expected Runtime**: < 1 minute for datasets up to 10,000 records