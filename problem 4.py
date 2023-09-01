def validate_credit_card(number):
    # Reverse the credit card number and convert it to a list of integers
    digits = [int(x) for x in str(number)][::-1]

    # Step 1: Multiply every other digit by 2, starting from the second-to-last digit
    doubled_digits = [2 * digit if i % 2 != 0 else digit for i, digit in enumerate(digits)]

    # Step 2: Sum the individual digits of the doubled products and non-doubled digits
    summed_digits = [digit // 10 + digit % 10 for digit in doubled_digits]

    # Step 3: Calculate the total sum of all digits
    total_sum = sum(summed_digits)

    # Step 4: Check if the total sum modulo 10 is congruent to 0
    if total_sum % 10 == 0:
        return True
    else:
        return False

def identify_card_type(number):
    # Check the card type based on the provided rules
    if len(number) == 15 and (number[:2] == "34" or number[:2] == "37"):
        return "American Express"
    elif len(number) == 16 and (number[:2] == "51" or number[:2] == "52" or number[:2] == "53" or number[:2] == "54" or number[:2] == "55"):
        return "MasterCard"
    elif (len(number) == 13 or len(number) == 16) and number[0] == "4":
        return "Visa"
    else:
        return "Unknown"

# Example usage
credit_card_number = input("Enter the credit card number: ")

if validate_credit_card(credit_card_number):
    card_type = identify_card_type(credit_card_number)
    print("Valid", card_type, "card number.")
else:
    print("Invalid credit card number.")
