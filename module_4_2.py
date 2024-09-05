# Домашнее задание по уроку "Пространство имен"
def test_function():
    # inner_function()  # Если вызвать функцию inner_function() сразу. Выдаст ошибку: локальная переменная 'inner_function' не обнаружена
    def inner_function():
        print("Я в области видимости функции test_function")

    inner_function()  # Если Вызовать функцию inner_function внутри функции test_function в результате выведет "Я в области видимости функции test_function"


# inner_function()
# не работает. Ошибка NameError: name 'inner_function' is not defined. Did you mean: 'test_function'?
# Разное пространство имен
# Мы не можем вызывать функцию из глобального пространства обращаясь к локальному в нутри объемлющего

test_function()
