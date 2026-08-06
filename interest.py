def basic_pay(hours, rate):
    return hours * rate


def add_hra(basic, percent):
    return basic + (basic * percent / 100.0)


def deduct_tax(salary, percent):
    return salary - (salary * percent / 100.0)

if __name__ == "__main__":
    hours = 160
    rate = 250
    basic = basic_pay(hours, rate)
    print(basic)


    hra_percent = 20  
    salary_with_hra = add_hra(basic, hra_percent)
    print(salary_with_hra)

    tax_percent = 10 
    salary_after_tax = deduct_tax(salary_with_hra, tax_percent)
    print(salary_after_tax)