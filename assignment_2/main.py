

def get_percentage(part: int | float, whole: int | float):
    """Finds, rounds and returns the percentage of a number.

    Args:
        part (int): percentage that needs to be calculated.
        whole (int): number from which a percentage was taken.

    Returns:
        int: found percentage.
    """

    return round(float(whole) / 100 * float(part))


def calculate_time_format(months: int):
    """This function makes sure that the time is outputed in a correct format.

    Args:
        months (int): the number of months it takes tot complete the purchase.
    """

    number_of_years = months // 12
    number_of_months = months % 12

# gtext
    match number_of_years:
        case 0:
            return f'{number_of_months} місяців'
        case 1:
            return f'{number_of_years} рік та {number_of_months} місяців'
        case 2 | 3 | 4:
            return f'{number_of_years} роки та {number_of_months} місяці'
        case _:
            return f'{number_of_years} років та {number_of_months} місяців'


# Перший етап
salary = int(input('Яка у вас заробітня платня?: '))
saving_percent = int(input(
    'Який відсоток вашої зарплати ви готові зберігати?: '))
investment_return_rate = int(input(
    'Який ваш річний відсоток дохідності від інвестицій?: '))
real_estate_price = int(input('Яка ціна нерухомості, яка вас цікавить?: '))
down_payment_percentage = int(input(
    'Який відсоток від ціни потрібно віддати на стартовий внесок?: '))


month_saving_amount = get_percentage(saving_percent, salary)
required_price = get_percentage(
    down_payment_percentage, real_estate_price)

months = 0
current_savings = 0

while current_savings < required_price:
    current_savings += month_saving_amount

    current_savings += get_percentage(investment_return_rate /
                                      12, current_savings)
    months += 1


purchase_time = calculate_time_format(months)

print(f'Квартира коштує ${real_estate_price}. Стартовий внесок - {down_payment_percentage}%, вам потрібно зібрати ${required_price}. Відкладаючи по {saving_percent}% щомісяця, це можна зробити за {purchase_time}.')

# Другий етап
with_loan = input('Чи хочете ви порахувати і тіло кредиту? (Y/N): ').lower()

if with_loan == 'y':
    loan_term = int(input('Скільки років кредитування ви бажаете?: '))
    annual_interest_rate = int(
        input('Який річний відсоток кредитування ви бажаете?: '))

    formatted_loan_term = calculate_time_format(loan_term)
    loan_amount = get_percentage(
        annual_interest_rate, real_estate_price) * loan_term
    monthly_payment = loan_amount / 12
    total_amount = real_estate_price + loan_amount

    if monthly_payment > salary:
        print('Нажаль ми не можемо видати вам кредит.')

    else:
        print(f'Та ж квартира коштує ${real_estate_price}, відсотки по кредиту - {annual_interest_rate}% річних. Якщо ви берете кредит на {loan_term} років, то маєте сумарно виплатити ${loan_amount}. Загальна сума стає ${total_amount}, без стартового внеску ${down_payment_percentage} або ${monthly_payment:.2f} щомісяця за {formatted_loan_term}.')
