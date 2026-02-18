# Data Dictionary - Supermarket Sales Project

This document describes the structure and content of the cleaned supermarket sales dataset.

| Column Name | Data Type | Description | Values / Examples |
| :--- | :--- | :--- | :--- |
| **Invoice ID** | Object (String) | Unique identification number of the sales invoice. | e.g., 386-10-2852 |
| **Branch** | Category | Branch of the supermarket. | Alex, Cairo, Giza |
| **City** | Category | Location of the supermarket branch. | Yangon, Naypyitaw, Mandalay |
| **Customer type** | Category | Type of customer. | M (Member), N (Normal) |
| **Gender** | Category | Gender of the customer. | M (Male), F (Female) |
| **Product line** | Category | General item category groups. | Health and beauty, Electronic accessories, etc. |
| **Unit price** | Float | Price of each product unit in USD. | e.g., 74.69 |
| **Quantity** | Integer | Number of units purchased by the customer. | 1 to 10 |
| **Tax 5%** | Float | 5% tax fee on the purchase. | Calculated field |
| **Sales** | Float | Total price including tax and COGS. | Calculated field (Tax + COGS) |
| **Full_Date** | Datetime64 | Combined date and time of the transaction. | YYYY-MM-DD HH:MM:SS |
| **Payment** | Category | Payment method used for the transaction. | Cash, Credit card, Ewallet |
| **cogs** | Float | Cost of Goods Sold. | e.g., 522.83 |
| **gross margin %** | Float | Gross margin percentage. | Standardized at 4.76% |
| **gross income** | Float | Gross income from the sale. | e.g., 26.14 |
| **Rating** | Float | Customer stratification rating on their overall shopping experience. | 4.0 to 10.0 |

**Note:** Categorical types were optimized to reduce memory usage by ~70% compared to standard strings.