def basic_pay(hours, rate):
    return hours * rate

def add_hra(basic, percent):
    return basic + (basic * percent / 100.0)

def deduct_tax(salary, percent):
    return salary - (salary * percent / 100.0)

if __name__ == "__main__":
    hours = 160
    rate = 250
    print(basic_pay(hours, rate))