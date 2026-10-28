"""Lesson 3.1: import code from a module in the same folder."""

import sweet_crumbs.pricing as pricing
from sweet_crumbs.pricing import FREE_DELIVERY_FROM, order_total
from sweet_crumbs.pricing import delivery_fee as fee


if __name__ == "__main__":
    print(pricing.delivery_fee(1000))  # 200
    print(order_total(1500, 2))        # 3000
    print(fee(5000))                   # 0
    print(f"Free delivery from {FREE_DELIVERY_FROM:,} PKR")
