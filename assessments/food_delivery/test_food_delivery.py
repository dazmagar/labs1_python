import unittest

from food_delivery_system import FoodDeliverySystem


class Test(unittest.TestCase):
    def test_01_check_menu(self) -> None:
        f = FoodDeliverySystem()
        self.assertEqual(
            f.display_menu(),
            {
                "Burger": 150,
                "Pizza": 250,
                "Pasta": 200,
                "Salad": 120,
                "Beverages": 130,
                "Noodles": 150,
                "Sushi": 270,
                "Bakery": 350,
            },
        )

    def test_02_place_order(self) -> None:
        f = FoodDeliverySystem()
        self.assertEqual(
            f.place_order("Mary Smith", {"Burger": 1, "Pasta": 2}),
            {
                1: {
                    "customer_name": "Mary Smith",
                    "order_items": {"Burger": 1, "Pasta": 2},
                    "status": "Placed",
                }
            },
        )

    def test_03_generate_bill(self) -> None:
        f = FoodDeliverySystem()
        self.assertEqual(f.generate_bill(1), 577.5)

    def test_04_pickup_order(self) -> None:
        f = FoodDeliverySystem()
        self.assertEqual(f.pickup_order(1), "Picked Up")

    def test_05_deliver_order(self) -> None:
        f = FoodDeliverySystem()
        self.assertEqual(f.deliver_order(1), "Delivered")

    def test_06_modify_order(self) -> None:
        f = FoodDeliverySystem()
        f.place_order("Boby Smith", {"Noodles": 1, "Salad": 1})
        self.assertEqual(
            f.modify_order(2, {"Pizza": 2, "Salad": 1}),
            {
                2: {
                    "customer_name": "Boby Smith",
                    "order_items": {"Pizza": 2, "Salad": 1},
                    "status": "Placed",
                }
            },
        )

    def test_07_cancel_order(self) -> None:
        f = FoodDeliverySystem()
        f.cancel_order(2)
        self.assertNotIn(2, f.orders_log)


if __name__ == "__main__":
    unittest.main()
