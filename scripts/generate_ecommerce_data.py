import pandas as pd
import random
from faker import Faker
from datetime import datetime, timedelta
from pathlib import Path

fake = Faker("pt_BR")

BASE_PATH = Path("data/raw")
BASE_PATH.mkdir(parents=True, exist_ok=True)

random.seed(42)

# Clientes
clientes = []
for i in range(1, 501):
    clientes.append({
        "customer_id": i,
        "customer_name": fake.name(),
        "email": fake.email(),
        "city": fake.city(),
        "state": fake.estado_sigla(),
        "created_at": fake.date_between(start_date="-2y", end_date="today")
    })

clientes_df = pd.DataFrame(clientes)

# Categorias
categorias = [
    "Eletrônicos",
    "Moda",
    "Casa",
    "Beleza",
    "Esporte",
    "Livros",
    "Brinquedos"
]

# Produtos
produtos = []
for i in range(1, 101):
    categoria = random.choice(categorias)
    produtos.append({
        "product_id": i,
        "product_name": f"{categoria} Produto {i}",
        "category": categoria,
        "price": round(random.uniform(20, 2500), 2)
    })

produtos_df = pd.DataFrame(produtos)

# Pedidos
orders = []
order_items = []
payments = []
deliveries = []

for order_id in range(1, 2001):
    customer = random.choice(clientes)
    order_date = fake.date_time_between(start_date="-12M", end_date="now")
    status = random.choice(["completed", "completed", "completed", "cancelled", "returned"])
    marketing_channel = random.choice(["organic", "paid_search", "social", "email", "affiliate"])

    orders.append({
        "order_id": order_id,
        "customer_id": customer["customer_id"],
        "order_date": order_date,
        "status": status,
        "marketing_channel": marketing_channel
    })

    qtd_items = random.randint(1, 4)
    selected_products = random.sample(produtos, qtd_items)

    order_total = 0

    for item_id, product in enumerate(selected_products, start=1):
        quantity = random.randint(1, 3)
        unit_price = product["price"]
        total_amount = round(quantity * unit_price, 2)
        order_total += total_amount

        order_items.append({
            "order_item_id": f"{order_id}_{item_id}",
            "order_id": order_id,
            "product_id": product["product_id"],
            "quantity": quantity,
            "unit_price": unit_price,
            "total_amount": total_amount
        })

    payments.append({
        "payment_id": order_id,
        "order_id": order_id,
        "payment_method": random.choice(["credit_card", "pix", "boleto", "debit_card"]),
        "payment_status": "paid" if status == "completed" else random.choice(["refunded", "failed"]),
        "amount": round(order_total, 2)
    })

    expected_delivery = order_date + timedelta(days=random.randint(2, 10))
    actual_delivery = expected_delivery + timedelta(days=random.randint(-2, 5))

    deliveries.append({
        "delivery_id": order_id,
        "order_id": order_id,
        "expected_delivery_date": expected_delivery.date(),
        "actual_delivery_date": actual_delivery.date(),
        "delivery_status": "delivered" if status == "completed" else "not_delivered"
    })

orders_df = pd.DataFrame(orders)
order_items_df = pd.DataFrame(order_items)
payments_df = pd.DataFrame(payments)
deliveries_df = pd.DataFrame(deliveries)

clientes_df.to_csv(BASE_PATH / "customers.csv", index=False)
produtos_df.to_csv(BASE_PATH / "products.csv", index=False)
orders_df.to_csv(BASE_PATH / "orders.csv", index=False)
order_items_df.to_csv(BASE_PATH / "order_items.csv", index=False)
payments_df.to_csv(BASE_PATH / "payments.csv", index=False)
deliveries_df.to_csv(BASE_PATH / "deliveries.csv", index=False)

print("Arquivos CSV gerados com sucesso em data/raw/")