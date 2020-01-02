#!/usr/bin/env python3

from datetime import date, datetime, timedelta

def get_invoice_date():
    while True:
        invoice_date_str = input("Enter invoice date (MM/DD/YYYY): ")    
        try:
            dt = datetime.strptime(invoice_date_str, "%m/%d/%Y")
        except ValueError:
            print("Invalid date format! Try again.")
            continue

        # create date object from datetime object
        invoice_date = date(dt.year, dt.month, dt.day)

        # check if date object is today or earlier
        if invoice_date > date.today():
            print("Invoice date must be today or earlier. Try again.")
            continue
        else:
            return invoice_date

def main():
    print("The Invoice Due Date program")
    print()

    while True:
        invoice_date = get_invoice_date()
        print()

        # calculate due date and days overdue
        due_date = invoice_date + timedelta(days=30)
        current_date = date.today()
        days_overdue = (current_date - due_date).days

        # display results
        print("Invoice Date: " + invoice_date.strftime("%B %d, %Y"))
        print("Due Date:     " + due_date.strftime("%B %d, %Y"))
        print("Current Date: " + current_date.strftime("%B %d, %Y"))
        if days_overdue > 0:
            print("This invoice is", days_overdue, "day(s) overdue.")
        else:
            days_due = days_overdue * -1
            print("This invoice is due in", days_due, "day(s).")
        print()

        # ask if user wants to continue
        result = input("Continue? (y/n): ")
        print()
        if result.lower() != "y":
            print("Bye!")
            break
        
if __name__ == "__main__":
    main()
