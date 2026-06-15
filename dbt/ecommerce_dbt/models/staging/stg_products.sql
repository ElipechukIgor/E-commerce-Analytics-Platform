select
    product_id,
    product_name,
    category,
    price
from read_csv_auto('../../data/raw/products.csv', header=true)