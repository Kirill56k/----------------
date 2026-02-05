# test_functions.py
# test_functions.py
import pytest
from functions import add, get_user_full_name
@pytest.mark.math
def test_add():
    """
    Проверяем, что функция add() правильно складывает два числа.
    """
    assert add(2, 3) == 5
    assert add(2, 2) == 4 # <-- Вот здесь мы намеренно ошиблись
    assert add(10, -5) == 5

@pytest.fixture
def sample_user_data():
    """Фикстура, которая возвращает словарь с данными пользователя."""
    return {
    "first_name": "Jane",
    "last_name": "Doe",
    "email": "jane.doe@example.com"
    }
# ШАГ 2: Используем фикстуру в тестах
@pytest.mark.user_profile
def test_get_user_full_name_with_fixture(sample_user_data):
    # Pytest автоматически вызовет фикстуру и передаст ее результат
# в аргумент sample_user_data
    assert get_user_full_name(sample_user_data) == "Jane Doe"
@pytest.mark.user_profile
def test_user_has_email_with_fixture(sample_user_data):
    assert "email" in sample_user_data
    
#Создаем список тестовых сценариев
# Каждый кортеж - это один набор данных: (аргумент_1, аргумент_2,ожидаемый_результат)
test_cases = [
    (1, 2, 3), # Обычное сложение
    (-1, -1, -2), # Сложение отрицательных чисел
    (5, 0, 5), # Сложение с нулем
    (-1, 1, 0), # Противоположные числа
    (3.5, 2.5, 6.0) # Сложение чисел с плавающей точкой
    ]
@pytest.mark.parametrize("a, b, expected", test_cases)
def test_add_parametrized(a, b, expected):
    """Проверяем функцию add() с разными наборами данных."""
    assert add(a, b) == expected
from functions import divide
def test_divide_by_zero_raises_error():
    """Проверяем, что деление на ноль вызывает ValueError."""
    with pytest.raises(ValueError):
        divide(10, 0)

@pytest.mark.skip(reason="Эта функция еще в разработке")
def test_new_feature():
    # Код теста для новой, еще не готовой функции
    assert False
  
@pytest.mark.xfail(reason="Известный баг с точностью float, тикет #123")
def test_float_precision_bug():
    assert (0.1 + 0.2) == 0.3 # Этот тест упадет из-за особенностей float

#задача1 
from functions import is_valid_password
assert is_valid_password("12345678") == True
assert is_valid_password("1234") == False
assert is_valid_password("12345679") == True


#задача2

import pytest
from functions import get_age_group
test_cases = [
    (12, "ребенок"),
    (13, "подросток"),
    (17, "подросток"),
    (18, "взрослый"),
]
@pytest.mark.parametrize("age, expected", test_cases)
def test_add_parametrized(age, expected):
    """Проверяем функцию add() с разными наборами данных."""
    assert get_age_group(age) == expected 

#задача3 
import pytest
from functions import calculate_cart_total

@pytest.fixture
def sample_cart():
    return [
    {"name": "Товар 1", "price": 10.0, "quantity": 2},
    {"name": "Товар 2", "price": 5.0, "quantity": 3},
    {"name": "Товар 3", "price": 20.0, "quantity": 1},
    ]

def test_calculate_total_correctness(sample_cart):
    expected_total = (
        10.0 * 2 +
        5.0 * 3 +
        20.0 * 1
    )
    total = calculate_cart_total(sample_cart)
    assert total == expected_total

def test_cart_contains_specific_item(sample_cart):
    item_names = [item["name"] for item in sample_cart]
    assert "Товар 2" in item_names
    assert "Товар 1" in item_names
    assert "Товар 3" in item_names

 #задача4
from functions import get_value_from_dict
def test_get_value():
    dict = {"name": "Товар 3", "quanity": 1}
    assert get_value_from_dict(dict, "name" ) == "Товар 3"
    assert get_value_from_dict(dict, "quanity" ) == 1

def test_get_value_raises_error():
    dict = {"name": "Товар 3", "quanity": 1}
    with pytest.raises(KeyError):
        get_value_from_dict(dict,"none")

#5
import pytest 
from functions import Wallet, InsufficientFundsError

@pytest.fixture
def wallet():
   return Wallet(initial_balance=20.0)

def test_wallet_deposit(wallet):
    wallet.deposit(30.0)
    assert wallet.balance == 50.0

def test_wallet_withdraw(wallet):
    wallet.withdraw(10.0)
    assert wallet.balance == 10.0

def test_wallet_insufficient_funds(wallet):
    with pytest.raises(InsufficientFundsError):
        wallet.withdraw(100.0)

wallet_test_cases = [
    ("__init__", -10.0),
    ("deposit", 0.0),
    ("withdraw", -5.0)
]

@pytest.mark.parametrize("method, amount", wallet_test_cases)
def test_wallet_value_error(method,amount):
    if method == "__init__" :
        with pytest.raises(ValueError):
            Wallet(initial_balance=amount)
    else:
        wallet = Wallet(initial_balance=20.0)
        if method == "deposit":
            with pytest.raises(ValueError):
                wallet.deposit(amount)
        elif method == "withdraw":
            with pytest.raises(ValueError):
                wallet.withdraw(amount)
