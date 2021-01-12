import os, requests

class Customers:
    def __init__(self):
        self._customers_end_point = os.environ["CUSTOMERS_END_POINT"]
        self.customers = self._load_customers()

    def _load_customers(self):
        return requests.get(self._customers_end_point).json()

    def find_customer(self, id):
        return list(filter(lambda x: x["id"] == int(id), self.customers))[0]



if __name__ == "__main__":
    c = Customers()
    print(c.find_customer(id='01'))
    # import orders
    # o = Orders()
    # a = o.order_by_total())
    # b = o.biggest_purchase_by_year("2016")