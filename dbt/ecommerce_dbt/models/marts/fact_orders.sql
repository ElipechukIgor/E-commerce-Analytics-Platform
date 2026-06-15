select
    o.order_id,
    o.customer_id,
    o.order_date,
    o.status,
    o.marketing_channel
from {{ ref('stg_orders') }} o