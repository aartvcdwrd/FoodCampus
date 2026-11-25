"""Test Driver для DiscountModule (FoodCampus).

Имитирует работу пользователя и проверяет корректность расчёта льготы.
Сценарии: Happy Path, Edge Case, негативное тестирование, стресс-тест.
"""
from discount_service import DiscountModule

def run_tests():
    module = DiscountModule()
    results = []  

    def check(name, expected, actual):
        status = "PASS" if expected == actual else "FAIL"
        results.append((name, status, expected, actual))
        print(f"{name}: ожидание={expected}, факт={actual} -> {status}")
    res1 = module.apply_student_discount("12345678")
    check("Тест 1 (скидка 15%)", 0.15, res1)

    res2 = module.apply_student_discount("123")
    check("Тест 2 (скидка 0%)", 0.0, res2)

    res3 = module.apply_student_discount("ABC-1234")
    check("Тест 3 (скидка 0%)", 0.0, res3)

    try:
        res4 = module.apply_student_discount(None)
        check("Тест 4 (скидка 0%)", 0.0, res4)
    except TypeError as e:
        results.append(("Тест 4 (None)", "FAIL", 0.0, f"Крах: TypeError"))
        print("Тест 4 (None): программа упала с ошибкой TypeError -> FAIL")

    res5 = module.apply_student_discount("12345678" * 100)
    check("Тест 5 (скидка 0%)", 0.0, res5)

    res6 = module.apply_student_discount("")
    check("Тест 6 (скидка 0%)", 0.0, res6)

    print()
    print(f"Итого: {sum(1 for r in results if r[1] == 'PASS')} PASS, "
          f"{sum(1 for r in results if r[1] == 'FAIL')} FAIL")

run_tests()
