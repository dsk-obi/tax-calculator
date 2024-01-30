PERSONAL_ALLOWANCE = 12500
PERSONAL_ALLOWANCE_OFF = 100000
ADDITIONAL_RATE_MIN = 125141
HIGHER_RATE_MAX = 125140
BASIC_RATE_MAX = 50200
BASIC_RATE_MIN = 17500
PENSION_CONTRIBUTION_RATE = 0.05
BASIC_RATE = 0.2
HIGHER_RATE = 0.4
ADDITIONAL_RATE = 0.45
NI_LOW_RATE = 72.5
NI_HI_RATE = 0.02


def calculate_ni(gross_pay):
    # nothing on the first £242.0
    # 10% (£72.50) on your earnings between £242.01 and £967
    # 2% (£0.66) on the remaining earnings above £967

    if gross_pay/52 <= 242:
        return 0
        
    elif gross_pay/52 <= 967:
        hi_deduct = 52 * (0.1 * ((gross_pay/52)-242))
        return hi_deduct

    elif gross_pay/52 > 967:
        hi_deduct = 52 * (0.02 * ((gross_pay/52)-967))
        return NI_LOW_RATE + hi_deduct
        

def calculate_tax(gross_pay):
    pen_deduct = gross_pay * PENSION_CONTRIBUTION_RATE

    if gross_pay < BASIC_RATE_MIN:
        return gross_pay - (calculate_ni(gross_pay) + pen_deduct)

    elif gross_pay <= BASIC_RATE_MAX:
        tax_deduct = BASIC_RATE * (gross_pay - PERSONAL_ALLOWANCE)
        return gross_pay - (calculate_ni(gross_pay) + tax_deduct + pen_deduct)
    
    elif gross_pay <= PERSONAL_ALLOWANCE_OFF:
        hi_tax = HIGHER_RATE * (gross_pay - BASIC_RATE_MAX)
        ba_tax = BASIC_RATE * BASIC_RATE_MAX
        return gross_pay - (calculate_ni(gross_pay) + pen_deduct +
                            hi_tax + ba_tax)
    
    elif gross_pay >= ADDITIONAL_RATE_MIN:
        hi_tax = HIGHER_RATE * (HIGHER_RATE_MAX - PERSONAL_ALLOWANCE_OFF)
        ad_tax = ADDITIONAL_RATE * (gross_pay - ADDITIONAL_RATE_MIN)
        ba_tax = BASIC_RATE * BASIC_RATE_MAX
        return gross_pay - (calculate_ni(gross_pay) + pen_deduct + hi_tax +
                            ad_tax + ba_tax)


while True:
    try:
        # Input from the user
        gross_pay = int(input("What is your Annual gross_pay? "))
    except ValueError:
        ("Please enter a valid number greater than zero")
    else:
        # Output the result
        net_pay = calculate_tax(gross_pay)
        print(f"Your yearly Netpay is £{net_pay}")
        break
