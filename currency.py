def format_conversion_text(date, from_currency, to_currency, rate, amount, converted_amount, inverse_rate):
    # Create the bold and centered text
    bold_centered_text = f"<p style='text-align:center; font-weight:bold; font-size:24px;'>" \
                         f" {amount:.2f} {from_currency} = {converted_amount:.2f} {to_currency}" \
                         f"</p>"
    
    # Create the description text with formatting
    description = f"<p style='text-align:center;'>" \
                 f"The conversion rate on {date} from {from_currency} to {to_currency} was {converted_amount:.4f}. " \
                 f"So 1.00 in {from_currency} corresponds to {converted_amount:.4f} in {to_currency}. " \
                 f"The inverse rate was {inverse_rate:.4f}." \
                 f"</p>"

    # Combine the description and bold centered text using HTML
    formatted_text = f"{bold_centered_text}<br><br>{description}"

    return formatted_text
