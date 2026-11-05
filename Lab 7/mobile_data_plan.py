import math

def parse_plan(text):
    """
    Parses a plan string in the format 'plan:data_in_gb' (e.g. 'standard:5').
    Returns a tuple (plan_name.title(), float(gb)) or None if input is invalid.
    """
    if not isinstance(text, str):
        return None
    parts = text.split(':')
    if len(parts) != 2:
        return None
    plan, gb = parts
    plan_clean = plan.strip()
    if not plan_clean:
        return None
    try:
        gb_val = float(gb.strip())
        if math.isnan(gb_val) or math.isinf(gb_val) or gb_val < 0:
            return None
        return plan_clean.title(), gb_val
    except (ValueError, OverflowError):
        return None

def usage_average(usage_csv):
    """
    Calculates the integer average of daily usage given as a comma-separated string.
    Returns the average in MB or None if input is invalid or empty.
    """
    if not isinstance(usage_csv, str):
        return None
    cleaned = usage_csv.strip()
    if not cleaned:
        return None
    parts = cleaned.split(',')
    values = []
    for r in parts:
        r_str = r.strip()
        if not r_str:
            return None
        try:
            val = int(r_str)
            if val < 0:
                return None
            values.append(val)
        except (ValueError, OverflowError):
            return None
    if not values:
        return None
    return sum(values) // len(values)

def payable_bill(text):
    """
    Computes total payable bill after 18% tax and discount from 'bill|discount'.
    Returns max(total, 0.0) rounded to 2 decimal places or None if input is invalid.
    """
    if not isinstance(text, str):
        return None
    parts = text.split('|')
    if len(parts) != 2:
        return None
    bill_str, discount_str = parts
    try:
        bill = float(bill_str.strip())
        discount = float(discount_str.strip())
        if math.isnan(bill) or math.isnan(discount) or math.isinf(bill) or math.isinf(discount):
            return None
        if bill < 0 or discount < 0:
            return None
        total = bill * 1.18 - discount
        return round(max(total, 0.0), 2)
    except (ValueError, OverflowError):
        return None

def main():
    print("==== Running parse_plan ====")
    user_input = input("Enter plan:data in GB (e.g. standard:5): ")
    result = parse_plan(user_input)
    print("Plan and Data:", result)

    print("\n==== Running usage_average ====")
    user_input = input("Enter daily usage in MB as CSV (e.g. 300,450,800): ")
    result = usage_average(user_input)
    print("Average Usage:", result)

    print("\n==== Running payable_bill ====")
    user_input = input("Enter bill|discount (e.g. 399|50): ")
    result = payable_bill(user_input)
    print("Payable Bill:", result)

if __name__ == "__main__":
    main()
