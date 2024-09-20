from confluent_kafka import Consumer, KafkaError
import json
from collections import defaultdict
import math

# Function 1: Calculate Total Revenue
def calculate_total_revenue(orders):
    return sum(order['price'] * order['quantity'] for order in orders)

# Function 2: Find the Product with Max Revenue
def product_with_max_revenue(orders):
    product_revenue = defaultdict(float)
    for order in orders:
        revenue = order['price'] * order['quantity']
        product_revenue[order['product_name']] += revenue
    # Find the product with the maximum revenue
    max_product = max(product_revenue.items(), key=lambda x: x[1])
    return max_product

# Function 3: Calculate Average Price for Electronics Category
def average_price_of_electronics(orders):
    electronics_prices = [order['price'] for order in orders if order['category'] == 'Electronics']
    if electronics_prices:
        return sum(electronics_prices) / len(electronics_prices)
    return 0

# Function 4: Count Products in Personal Care Category
def count_personal_care_products(orders):
    return len([order for order in orders if order['category'] == 'Personal Care'])

# Function 5: Calculate Price Standard Deviation
def calculate_price_standard_deviation(orders):
    prices = [order['price'] for order in orders]
    if not prices:
        return 0
    avg_price = sum(prices) / len(prices)
    variance = sum((price - avg_price) ** 2 for price in prices) / len(prices)
    return math.sqrt(variance)

# Function 6: Calculate Total Quantity of Wireless Mouse Products
def total_quantity_wireless_mouse(orders):
    return sum(order['quantity'] for order in orders if order['product_name'] == 'Wireless Mouse')

# Function 7: Find the Product with Minimum Price
def product_with_min_price(orders):
    min_order = min(orders, key=lambda x: x['price'])
    return min_order

# Main consumer function to consume messages from Kafka and process the dataset
def consume_orders(topic='order_topic'):
    consumer = Consumer({
        'bootstrap.servers': 'localhost:9092',
        'group.id': 'order_group',
        'auto.offset.reset': 'earliest'
    })

    consumer.subscribe([topic])

    orders = []
    try:
        while True:
            msg = consumer.poll(1.0)
            if msg is None:
                continue
            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    continue
                else:
                    print(msg.error())
                    break

            # Deserialize the message from Kafka
            order = json.loads(msg.value().decode('utf-8'))
            orders.append(order)
            print(f"Order received: {order}")

            # After processing 30 orders, perform the complex calculations
            if len(orders) >= 30:
                print("Processing orders...")

                # Function 1: Calculate total revenue
                total_revenue = calculate_total_revenue(orders)
                print(f"Total Revenue: {total_revenue}")

                # Function 2: Product with max revenue
                max_revenue_product, max_revenue_value = product_with_max_revenue(orders)
                print(f"Product with Max Revenue: {max_revenue_product} (Revenue: {max_revenue_value})")

                # Function 3: Average price of electronics
                avg_price_electronics = average_price_of_electronics(orders)
                print(f"Average Price of Electronics: {avg_price_electronics}")

                # Function 4: Count products in personal care
                personal_care_count = count_personal_care_products(orders)
                print(f"Number of Products in Personal Care: {personal_care_count}")

                # Function 5: Price standard deviation
                price_std_dev = calculate_price_standard_deviation(orders)
                print(f"Price Standard Deviation: {price_std_dev}")

                # Function 6: Total quantity of Wireless Mouse
                wireless_mouse_quantity = total_quantity_wireless_mouse(orders)
                print(f"Total Quantity of Wireless Mouse: {wireless_mouse_quantity}")

                # Function 7: Product with min price
                min_price_product = product_with_min_price(orders)
                # Print only the product name for the product with the minimum price
                print(f"Product with Minimum Price: {min_price_product['product_name']}")

                break
    except KeyboardInterrupt:
        pass
    finally:
        consumer.close()

if __name__ == "__main__":
    consume_orders()
