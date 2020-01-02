#!/usr/bin/env python3

from decimal import Decimal
from decimal import ROUND_HALF_UP
import locale as lc

# display a title
print("The Invoice program")
print()

choice = "y"
while choice == "y":
    
    # get user entry
    order_total = Decimal(input("Enter order total:    "))
    order_total = order_total.quantize(Decimal("1.00"), ROUND_HALF_UP)
    print()               

    # determine discount percent
    if order_total > 0 and order_total < 100:
        discount_percent = Decimal("0")
    elif order_total >= 100 and order_total < 250:
        discount_percent = Decimal(".1")
    elif order_total >= 250:
        discount_percent = Decimal(".2")

    # calculate results
    discount = order_total * discount_percent
    discount = discount.quantize(Decimal("1.00"), ROUND_HALF_UP)                                
    subtotal = order_total - discount
    shipping_percent = Decimal(".085")
    shipping_cost = subtotal * shipping_percent
    shipping_cost = shipping_cost.quantize(Decimal("1.00"), ROUND_HALF_UP)                                 
    tax_percent = Decimal(".05")
    sales_tax = subtotal * tax_percent
    sales_tax = sales_tax.quantize(Decimal("1.00"), ROUND_HALF_UP)                                 
    invoice_total = subtotal + shipping_cost + sales_tax

    # display the results
    lc.setlocale(lc.LC_ALL, "us")     # for Windows
    #lc.setlocale(lc.LC_ALL, "en_US")  # for Mac OS X
    print("Order total:      {:>11}".format(
        lc.currency(order_total, grouping=True)))
    print("Discount amount:  {:11,}".format(discount))
    print("Subtotal:         {:11,}".format(subtotal))
    print("Shipping cost:    {:11,}".format(shipping_cost))
    print("Sales tax:        {:11,}".format(sales_tax))
    print("Invoice total:    {:>11}".format(
        lc.currency(invoice_total, grouping=True)))
    print()

    choice = input("Continue? (y/n): ")    
    print()
    
print("Bye")
