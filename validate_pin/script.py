def validate_pin(pin):
    """Validates the pin on ATM cards
    """
    if len(pin) not in [4, 6]: return False

    for digit in pin:
        try:
            int(digit)
        except ValueError:
            return False

    return True