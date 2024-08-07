import typing as t


class FoodDeliverySystem:
    order_id: int = 0
    orders_log: t.Dict[int, t.Dict[str, t.Any]] = {}

    def __init__(self) -> None:
        self.menu: t.Dict[str, int] = {
            "Burger": 150,
            "Pizza": 250,
            "Pasta": 200,
            "Salad": 120,
            "Beverages": 130,
            "Noodles": 150,
            "Sushi": 270,
            "Bakery": 350,
        }

    def display_menu(self) -> t.Dict[str, int]:
        return self.menu

    def place_order(self, customer_name: str, order_items: t.Dict[str, int]) -> t.Union[str, t.Dict[int, t.Dict[str, t.Any]]]:
        for item in order_items.keys():
            if item not in self.menu:
                return "order placement failed"

        self.__class__.order_id += 1

        self.orders_log[self.__class__.order_id] = {
            "customer_name": customer_name,
            "order_items": order_items,
            "status": "Placed",
        }
        return {self.__class__.order_id: self.orders_log[self.__class__.order_id]}

    def generate_bill(self, order_id: int) -> t.Optional[float]:
        if order_id in self.orders_log:
            order_items = self.orders_log[order_id]["order_items"]
            total_sum = sum(self.menu[item] * quantity for item, quantity in order_items.items())
            if total_sum > 1000:
                total_bill_amount = total_sum * 1.10
            else:
                total_bill_amount = total_sum * 1.05
            return total_bill_amount
        return None

    def pickup_order(self, order_id: int) -> t.Optional[str]:
        if order_id in self.orders_log:
            self.orders_log[order_id]["status"] = "Picked Up"
            return "Picked Up"
        return None

    def deliver_order(self, order_id: int) -> t.Optional[str]:
        if order_id in self.orders_log:
            self.orders_log[order_id]["status"] = "Delivered"
            return "Delivered"
        return None

    def modify_order(self, order_id: int, new_items: t.Dict[str, int]) -> t.Union[str, t.Optional[t.Dict[int, t.Dict[str, t.Any]]]]:
        if order_id in self.orders_log and self.orders_log[order_id]["status"] == "Placed":
            for item in new_items.keys():
                if item not in self.menu:
                    return "order modification failed"
            self.orders_log[order_id]["order_items"] = new_items
            return {order_id: self.orders_log[order_id]}
        return None

    def cancel_order(self, order_id: int) -> t.Optional[t.Dict[int, t.Dict[str, t.Any]]]:
        if order_id in self.orders_log and self.orders_log[order_id]["status"] == "Placed":
            del self.orders_log[order_id]
            return self.orders_log
        return None
