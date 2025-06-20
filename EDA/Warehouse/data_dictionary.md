# Data Dictionary - Warehouse Dataset

## Active Columns (Final Dataset)
| Column | Original Name | Type | Description | Cleaning Notes | Status |
|--------|---------------|------|-------------|----------------|---------|
| ID | Product ID | int64 | Unique product identifier | Renamed from 'Product ID' | Active |
| Category | Category | object | Product category (Electronics, Clothing, etc.) | No changes applied | Active |
| Warehouse | Warehouse | object | Warehouse facility identifier | No changes applied | Active |
| Location | Location | object | Storage location within warehouse | No changes applied | Active |
| Quantity | Quantity | Int64 | Stock quantity available | Converted words to numbers, converted from object to Int64, filled missing with category mean | Active |
| Price | Price | float64 | Product price | Filled missing with category mean | Active |
| Supplier | Supplier | object | Product supplier identifier | No changes applied | Active |
| Status | Status | object | Product status (In Stock, Low Stock or Out of Stock) | No changes applied | Active |
| Restocked | Last Restocked | datetime64 | Last restock date | Renamed, converted from object to datetime, filled missing with median | Active |

## Dropped Columns
| Column | Original Type | Description | Reason for Removal |
|--------|---------------|-------------|-------------------|
| Product Name | object | Name/title of the product | **DROPPED** - Redundant with Product ID, not needed for analysis |

## Data Quality Summary
- **Original columns**: 10
- **Final columns**: 9
- **Columns cleaned**: 3 (Quantity, Price, Last Restocked)
- **Columns renamed**: 2 (Product ID → ID, Last Restocked → Restocked)
- **Columns dropped**: 1 (Product Name)
- **Total missing values handled**: 565
