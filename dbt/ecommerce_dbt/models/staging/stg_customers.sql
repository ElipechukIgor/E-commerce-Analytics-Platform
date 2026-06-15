select
    customer_id,
    customer_name,
    email,
    city,
    state,
    created_at
from read_csv_auto('../../data/raw/customers.csv', header=true)
