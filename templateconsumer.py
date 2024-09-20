from confluent_kafka import Consumer, KafkaError
import json
from collections import defaultdict
import math

# Function 1: Calculate Total Revenue
def calculate_total_revenue(orders):
    if not orders:  # If the orders list is empty or None
        return None
    # TODO: Add logic to calculate total revenue
    pass

# Function 2: Find the Product with Max Revenue
def product_with_max_revenue(orders):
    if not orders:  # If the orders list is empty or None
        return None, None
    # TODO: Add logic to find product with max revenue
    pass

# Function 3: Calculate Average Price for Electronics Category
def average_price_of_electronics(orders):
    if not orders:  # If the orders list is empty or None
        return None
    # TODO: Add logic to calculate the average price of electronics
    pass

# Function 4: Count Products in Personal Care Category
def count_personal_care_products(orders):
    if not orders:  # If the orders list is empty or None
        return None
    # TODO: Add logic to count products in Personal Care category
    pass

# Function 5: Calculate Price Standard Deviation
def calculate_price_standard_deviation(orders):
    if not orders:  # If the orders list is empty or None
        return None
    # TODO: Add logic to calculate price standard deviation
    pass

# Function 6: Calculate Total Quantity of Wireless Mouse Products
def total_quantity_wireless_mouse(orders):
    if not orders:  # If the orders list is empty or None
        return None
    # TODO: Add logic to calculate total quantity of Wireless Mouse products
    pass

# Function 7: Find the Product with Minimum Price
def product_with_min_price(orders):
    if not orders:  # If the orders list is empty or None
        return None
    # TODO: Add logic to find the product with the minimum price
    pass

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
                try:
                    total_revenue = calculate_total_revenue(orders)
                    if total_revenue is None:
                        print("Total Revenue: None")
                    else:
                        print(f"Total Revenue: {total_revenue}")
                except Exception:
                    print("Total Revenue: None")

                # Function 2: Product with max revenue
                try:
                    max_revenue_product, max_revenue_value = product_with_max_revenue(orders)
                    if max_revenue_product is None:
                        print("Product with Max Revenue: None")
                    else:
                        print(f"Product with Max Revenue: {max_revenue_product} (Revenue: {max_revenue_value})")
                except Exception:
                    print("Product with Max Revenue: None")

                # Function 3: Average price of electronics
                try:
                    avg_price_electronics = average_price_of_electronics(orders)
                    if avg_price_electronics is None:
                        print("Average Price of Electronics: None")
                    else:
                        print(f"Average Price of Electronics: {avg_price_electronics}")
                except Exception:
                    print("Average Price of Electronics: None")

                # Function 4: Count products in personal care
                try:
                    personal_care_count = count_personal_care_products(orders)
                    if personal_care_count is None:
                        print("Number of Products in Personal Care: None")
                    else:
                        print(f"Number of Products in Personal Care: {personal_care_count}")
                except Exception:
                    print("Number of Products in Personal Care: None")

                # Function 5: Price standard deviation
                try:
                    price_std_dev = calculate_price_standard_deviation(orders)
                    if price_std_dev is None:
                        print("Price Standard Deviation: None")
                    else:
                        print(f"Price Standard Deviation: {price_std_dev}")
                except Exception:
                    print("Price Standard Deviation: None")

                # Function 6: Total quantity of Wireless Mouse
                try:
                    wireless_mouse_quantity = total_quantity_wireless_mouse(orders)
                    if wireless_mouse_quantity is None:
                        print("Total Quantity of Wireless Mouse: None")
                    else:
                        print(f"Total Quantity of Wireless Mouse: {wireless_mouse_quantity}")
                except Exception:
                    print("Total Quantity of Wireless Mouse: None")

                # Function 7: Product with min price
                try:
                    min_price_product = product_with_min_price(orders)
                    if min_price_product is None:
                        print("Product with Minimum Price: None")
                    else:
                        print(f"Product with Minimum Price: {min_price_product['product_name']}")
                except Exception:
                    print("Product with Minimum Price: None")

                break
    except KeyboardInterrupt:
        pass
    finally:
        consumer.close()

if __name__ == "__main__":
    consume_orders()
