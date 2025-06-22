# Data Dictionary - Cafe Dataset

## Active Columns (Final Dataset)

| Column | Original Name | Type | Description | Cleaning Notes | Status |
|--------|---------------|------|-------------|----------------|--------|
| Txn_ID | Transaction ID | object | Unique transaction identifier | Renamed from 'Transaction ID' | Active |
| Item | Item | object | Menu item purchased (Cookie, Tea, etc.) | Replaced 'ERROR' and 'UNKNOWN' with `pd.NA`; imputed missing values using price-to-item mapping with random selection | Active |
| Quantity | Quantity | Int64 | Quantity of items purchased in transaction | Converted to nullable Int64; calculated missing values using Total ÷ Unit_Price when possible | Active |
| Unit_Price | Price Per Unit | Float64 | Price per individual item unit | Renamed from 'Price Per Unit'; converted to nullable Float64; imputed missing values using menu dictionary; calculated using Total ÷ Quantity when possible | Active |
| Total | Total Spent | Float64 | Total transaction amount | Renamed from 'Total Spent'; converted to nullable Float64; calculated missing values using Quantity × Unit_Price when possible | Active |
| Payment | Payment Method | object | Payment method used for transaction | Renamed from 'Payment Method'; replaced 'UNKNOWN' and 'ERROR' with `pd.NA`; imputed missing values using mode within each Item group | Active |
| Location | Location | object | Point of transaction (In-store, Takeaway) | Replaced 'UNKNOWN' and 'ERROR' with `pd.NA`; imputed missing values using mode within each Item group | Active |
| Date | Transaction Date | datetime64[ns] | Date and time of transaction | Renamed from 'Transaction Date'; converted from string to datetime format; removed records with invalid/missing dates | Active |

## Cleaning Process Details

### Data Type Conversions
- **Quantity**: object → Int64 (nullable integer to handle missing values)
- **Unit_Price**: object → Float64 (nullable float to handle missing values)
- **Total**: object → Float64 (nullable float to handle missing values)
- **Date**: object → datetime64[ns] (proper datetime format for temporal analysis)

### Missing Value Imputation Strategy
- **Unit_Price**: Menu-based imputation using domain knowledge of cafe pricing
- **Item**: Price-based imputation with random selection from items matching the price point
- **Quantity & Total**: Mathematical calculation using relationship Total = Quantity × Unit_Price
- **Payment & Location**: Mode imputation within Item groups (items tend to have consistent payment/location patterns)

### Data Pruning Criteria
Records removed if missing:
- Item, Quantity, AND Unit_Price (no product information)
- Quantity, Unit_Price, AND Total (no financial information)
- Item, Unit_Price, AND Total (no item or value information)
- Item, Quantity, AND Total (no item or transaction information)
- Quantity AND Total (insufficient for mathematical recovery)
- Date (no temporal context for analysis)

### Menu Dictionary Used for Imputation
```
Cookie: $1.00    |    Juice: $3.00
Tea: $1.50       |    Sandwich: $4.00
Coffee: $2.00    |    Smoothie: $4.00
Cake: $3.00      |    Salad: $5.00
```

## Data Quality Summary
- **Original columns**: 8
- **Final columns**: 8
- **Columns cleaned**: 8 (all columns processed)
- **Columns renamed**: 5 (Transaction ID → Txn_ID, Price Per Unit → Unit_Price, Total Spent → Total, Payment Method → Payment, Transaction Date → Date)
- **Columns dropped**: 0 (all original columns retained)
- **Data type conversions**: 4 (Quantity, Unit_Price, Total, Date)
- **Records with missing dates removed**: Variable (depends on input data quality)
- **Missing values imputed**: Variable across all columns using domain knowledge and statistical methods
- **Mathematical relationships preserved**: Total = Quantity × Unit_Price maintained throughout dataset

## Validation Checks Applied
- **Data type consistency**: All columns converted to appropriate nullable types
- **Mathematical relationship validation**: Total = Quantity × Unit_Price verified
- **Menu pricing consistency**: Unit prices align with established menu pricing
- **Date format standardisation**: All dates converted to datetime64[ns] format
- **Missing value minimisation**: Comprehensive imputation strategy applied
- **Transaction completeness**: Only records with sufficient data retained

## Business Rules Implemented
- **Menu Consistency**: Prices must match established cafe menu items
- **Transaction Validity**: Records must contain sufficient information for financial analysis
- **Date Integrity**: All transactions must have valid dates for time-series analysis
- **Category Coherence**: Payment methods and locations grouped by item type for realistic imputation