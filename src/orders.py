import requests, os
from src import utils

class Orders:
    def __init__(self):
        self._orders_end_point = os.environ["ORDERS_END_POINT"]
        self.orders = self._load_orders()

    def _load_orders(self):
        return requests.get(self._orders_end_point).json()

    def _calculate_total(self, cliente):
        return round(sum([x["valorTotal"] for x in list(filter(lambda x: x["cliente"] == cliente, self.orders))]),2)

    def order_by_total(self):
        filtered_dict = {i["cliente"].split(".")[-1]: self._calculate_total(i["cliente"]) for i in self.orders}
        return sorted(filtered_dict.items(), key=lambda kv: kv[1], reverse=True)

    def biggest_purchase_by_year(self, year:str):
        filtered_dict = self._filter_by_year(year)
        biggest_purchase = {"error": f"No purchase found in year {year}", "valorTotal": 0}
        for order in filtered_dict:
            if order["valorTotal"] > biggest_purchase["valorTotal"]:
                biggest_purchase = order
        return biggest_purchase

    def _filter_by_year(self, year:str):
        return list(filter(lambda x: str(utils.parse_date(x["data"]).year) == year, self.orders))

if __name__ == "__main__":
    o = Orders()
    print(o.order_by_total())
    print(o.biggest_purchase_by_year("2018"))