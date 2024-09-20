import unittest
from test.TestUtils import TestUtils
from producer import *
from consumer import (
    calculate_total_revenue,
    product_with_max_revenue,
    average_price_of_electronics,
    count_personal_care_products,
    calculate_price_standard_deviation,
    total_quantity_wireless_mouse,
    product_with_min_price
)

# Sample data for testing
orders = [
    { "order_id": "1", "product_name": "Laptop", "quantity": 1, "price": 1200.50, "category": "Electronics" },
    { "order_id": "2", "product_name": "Smartphone", "quantity": 2, "price": 799.99, "category": "Electronics" },
    { "order_id": "3", "product_name": "Headphones", "quantity": 5, "price": 50.75, "category": "Accessories" },
    { "order_id": "4", "product_name": "Refrigerator", "quantity": 1, "price": 450.75, "category": "Appliances" },
    { "order_id": "5", "product_name": "Television", "quantity": 3, "price": 550.00, "category": "Electronics" },
    { "order_id": "6", "product_name": "Microwave", "quantity": 1, "price": 120.75, "category": "Appliances" },
    { "order_id": "7", "product_name": "Blender", "quantity": 2, "price": 45.99, "category": "Appliances" },
    { "order_id": "8", "product_name": "Toaster", "quantity": 1, "price": 35.50, "category": "Appliances" },
    { "order_id": "9", "product_name": "Washing Machine", "quantity": 1, "price": 750.00, "category": "Appliances" },
    { "order_id": "10", "product_name": "Smartwatch", "quantity": 4, "price": 199.99, "category": "Wearables" },
    { "order_id": "11", "product_name": "Fitness Tracker", "quantity": 3, "price": 99.99, "category": "Wearables" },
    { "order_id": "12", "product_name": "Air Conditioner", "quantity": 1, "price": 600.00, "category": "Appliances" },
    { "order_id": "13", "product_name": "Digital Camera", "quantity": 2, "price": 400.00, "category": "Electronics" },
    { "order_id": "14", "product_name": "Coffee Maker", "quantity": 1, "price": 75.00, "category": "Appliances" },
    { "order_id": "15", "product_name": "Gaming Console", "quantity": 1, "price": 500.00, "category": "Electronics" },
    { "order_id": "16", "product_name": "Wireless Mouse", "quantity": 10, "price": 25.00, "category": "Accessories" },
    { "order_id": "17", "product_name": "External Hard Drive", "quantity": 2, "price": 120.00, "category": "Electronics" },
    { "order_id": "18", "product_name": "Tablet", "quantity": 1, "price": 250.00, "category": "Electronics" },
    { "order_id": "19", "product_name": "Desktop Computer", "quantity": 1, "price": 1500.00, "category": "Electronics" },
    { "order_id": "20", "product_name": "Portable Speaker", "quantity": 5, "price": 60.00, "category": "Accessories" },
    { "order_id": "21", "product_name": "Action Camera", "quantity": 1, "price": 300.00, "category": "Electronics" },
    { "order_id": "22", "product_name": "Smart Home Hub", "quantity": 3, "price": 150.00, "category": "Smart Devices" },
    { "order_id": "23", "product_name": "Bluetooth Headset", "quantity": 6, "price": 40.00, "category": "Accessories" },
    { "order_id": "24", "product_name": "Smart Doorbell", "quantity": 1, "price": 200.00, "category": "Smart Devices" },
    { "order_id": "25", "product_name": "Vacuum Cleaner", "quantity": 1, "price": 350.00, "category": "Appliances" },
    { "order_id": "26", "product_name": "Drone", "quantity": 2, "price": 1000.00, "category": "Electronics" },
    { "order_id": "27", "product_name": "Electric Shaver", "quantity": 4, "price": 55.00, "category": "Personal Care" },
    { "order_id": "28", "product_name": "Hair Dryer", "quantity": 2, "price": 40.00, "category": "Personal Care" },
    { "order_id": "29", "product_name": "Steam Iron", "quantity": 1, "price": 75.00, "category": "Appliances" },
    { "order_id": "30", "product_name": "Smart Thermostat", "quantity": 1, "price": 250.00, "category": "Smart Devices" }
]


class ConsumerTest(unittest.TestCase):
    def test_produce_30_messages(self):
        # Load real data from the dataset.json file (ensure 'dataset.json' has at least 30 records)
        data = load_data_from_json('dataset.json')
        test_obj = TestUtils()

        # If data is None, fail the test using YakshaAssert
        if data is None:
            test_obj.yakshaAssert("TestProduce30Messages", False, "Functional")
            print("Test Produce 30 Messages Failed: Dataset could not be loaded or is empty.")
        else:
            # Ensure the dataset has at least 30 entries
            if len(data) >= 30:
                produce_orders(data)  # Call the produce_orders function with real data
                test_obj.yakshaAssert("TestProduce30Messages", True, "Functional")
                print(f"Test Produce 30 Messages Passed: {len(data)} messages processed.")
            else:
                test_obj.yakshaAssert("TestProduce30Messages", False, "Functional")
                print(f"Test Produce 30 Messages Failed: Dataset has only {len(data)} messages instead of 30.")

    def test_calculate_total_revenue(self):
        expected_revenue = 15933.14
        actual_revenue = calculate_total_revenue(orders)
        test_obj = TestUtils()
        if actual_revenue == expected_revenue:
            test_obj.yakshaAssert("TestCalculateTotalRevenue", True, "Functional")
            print(f"Total Revenue Test Passed: {actual_revenue} == {expected_revenue}")
        else:
            test_obj.yakshaAssert("TestCalculateTotalRevenue", False, "Functional")
            print(f"Total Revenue Test Failed: {actual_revenue} != {expected_revenue}")

    def test_product_with_max_revenue(self):
        expected_product = ("Drone", 2000.0)
        actual_product = product_with_max_revenue(orders)
        if actual_product is None:
            actual_product = (None, None)
        test_obj = TestUtils()
        if actual_product == expected_product:
            test_obj.yakshaAssert("TestProductWithMaxRevenue", True, "Functional")
            print(f"Product with Max Revenue Test Passed: {actual_product} == {expected_product}")
        else:
            test_obj.yakshaAssert("TestProductWithMaxRevenue", False, "Functional")
            print(f"Product with Max Revenue Test Failed: {actual_product} != {expected_product}")

    def test_average_price_of_electronics(self):
        expected_avg_price = 662.049
        actual_avg_price = average_price_of_electronics(orders)
        test_obj = TestUtils()
        if actual_avg_price is not None and round(actual_avg_price, 3) == expected_avg_price:
            test_obj.yakshaAssert("TestAveragePriceOfElectronics", True, "Functional")
            print(f"Average Price of Electronics Test Passed: {round(actual_avg_price, 3)} == {expected_avg_price}")
        else:
            test_obj.yakshaAssert("TestAveragePriceOfElectronics", False, "Functional")
            print(f"Average Price of Electronics Test Failed: {actual_avg_price} != {expected_avg_price}")

    def test_count_personal_care_products(self):
        expected_count = 2
        actual_count = count_personal_care_products(orders)
        test_obj = TestUtils()
        if actual_count == expected_count:
            test_obj.yakshaAssert("TestCountPersonalCareProducts", True, "Functional")
            print(f"Count Personal Care Products Test Passed: {actual_count} == {expected_count}")
        else:
            test_obj.yakshaAssert("TestCountPersonalCareProducts", False, "Functional")
            print(f"Count Personal Care Products Test Failed: {actual_count} != {expected_count}")

    def test_calculate_price_standard_deviation(self):
        expected_std_dev = 371.6461855536197
        actual_std_dev = calculate_price_standard_deviation(orders)
        test_obj = TestUtils()
        if actual_std_dev is not None and round(actual_std_dev, 3) == round(expected_std_dev, 3):
            test_obj.yakshaAssert("TestPriceStandardDeviation", True, "Functional")
            print(f"Price Standard Deviation Test Passed: {round(actual_std_dev, 3)} == {round(expected_std_dev, 3)}")
        else:
            test_obj.yakshaAssert("TestPriceStandardDeviation", False, "Functional")
            print(f"Price Standard Deviation Test Failed: {actual_std_dev} != {expected_std_dev}")

    def test_total_quantity_wireless_mouse(self):
        expected_quantity = 10
        actual_quantity = total_quantity_wireless_mouse(orders)
        test_obj = TestUtils()
        if actual_quantity == expected_quantity:
            test_obj.yakshaAssert("TestTotalQuantityWirelessMouse", True, "Functional")
            print(f"Total Quantity of Wireless Mouse Test Passed: {actual_quantity} == {expected_quantity}")
        else:
            test_obj.yakshaAssert("TestTotalQuantityWirelessMouse", False, "Functional")
            print(f"Total Quantity of Wireless Mouse Test Failed: {actual_quantity} != {expected_quantity}")

    def test_product_with_min_price(self):
        expected_product = "Wireless Mouse"
        actual_product = product_with_min_price(orders)
        if actual_product is None:
            actual_product = {"product_name": None}
        test_obj = TestUtils()
        if actual_product["product_name"] == expected_product:
            test_obj.yakshaAssert("TestProductWithMinPrice", True, "Functional")
            print(f"Product with Minimum Price Test Passed: {actual_product['product_name']} == {expected_product}")
        else:
            test_obj.yakshaAssert("TestProductWithMinPrice", False, "Functional")
            print(f"Product with Minimum Price Test Failed: {actual_product['product_name']} != {expected_product}")

if __name__ == "__main__":
    unittest.main()
