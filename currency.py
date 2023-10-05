def round_rate(rate):
    return round(rate, 4)

def reverse_rate(rate):
    if rate != 0:
        return round(1 / rate, 4)
    else:
        return 0.0000  # Return 0.0000 for zero rate

def format_output(date, from_currency, to_currency, rate, amount, converted_amount, inverse_rate):
    formatted_text = (
        f"{amount:.2f} {from_currency} = {rate:.4f} {to_currency}\n"
        f"\nThe conversion rate on {date} from {from_currency} to {to_currency} was {rate:.4f}. "
        f"So {amount} in {from_currency} corresponds to {rate:.4f} in {to_currency}. "
        f"The inverse rate was {inverse_rate:.4f}."
    )

    return formatted_text


