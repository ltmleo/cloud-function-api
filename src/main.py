from src import  customers, orders
import os

customers = customers.Customers()
orders = orders.Orders()

def list_customers_by_total_handler(event, context):
    ordered_by_total = orders.order_by_total()
    return {
        "statusCode": 200,
        "body": [{"id": x[0], "total": x[1], **customers.find_customer(id=x[0])} for x in ordered_by_total]
    }

def biggest_purchase_customer_handler(event, context):
    try:
        year = event["year"]
    except:
        year = "2016"
    biggest_purchase = orders.biggest_purchase_by_year(year)
    try:
        id = biggest_purchase["cliente"].split(".")[-1]
        return {
            "statusCode": 200,
            "body": {**customers.find_customer(id=id), "year": year, "purchase": biggest_purchase }
        }
    except:
        return {
            "statusCode": 404,
            "body": biggest_purchase
        }

