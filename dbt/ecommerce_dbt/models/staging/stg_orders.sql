select
    order_id,
    customer_id,
    order_date,
    status,
    marketing_channel
from read_csv_auto('../../data/raw/orders.csv', header=true)